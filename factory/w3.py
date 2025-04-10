import os
from typing import Dict, Union, Set, List
import time
import random
import logging

from web3 import Web3
from dotenv import load_dotenv

from const.controlls import network
from const.config import private_key, wallet_address, env

load_dotenv()
polygon_rpc_url = os.getenv("POLYGON_RPC_URL")
if env == "test":
    polygon_rpc_url = os.getenv("POLYGON_TESTNET_RPC_URL")

# Set up logging
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('Web3Connection')

class W3:
    _instance = None
    velas_private_key = private_key
    velas_network_url = "https://evmexplorer.velas.com/rpc"
    velas_network_id = 106
    
    # Polygon configuration with multiple RPC endpoints
    matic_private_key = private_key
    matic_primary_url = polygon_rpc_url
    matic_backup_urls = [
        "https://rpc-mainnet.matic.network",
        "https://rpc-mainnet.maticvigil.com", 
        "https://polygon-mainnet.public.blastapi.io",
        "https://polygon.llamarpc.com",
        "https://polygon.rpc.blxrbdn.com"
    ]
    matic_network_id = 137
    
    bnb_private_key = private_key
    bnb_network_url = "https://bsc-dataseed.binance.org/"
    bnb_network_id = 56

    executor_wallet = wallet_address
    velasW3 = None
    maticW3 = None
    bnbW3 = None
    
    # Track failed endpoints to avoid immediately retrying them
    _failed_endpoints = {
        "matic": set()
    }
    
    # Track when we last tried failed endpoints (in seconds since epoch)
    _last_retry_time = {
        "matic": 0
    }
    
    # How long to wait before retrying failed endpoints (in seconds)
    _retry_interval = 300  # 5 minutes

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(W3, cls).__new__(
                                cls, *args, **kwargs)
        return cls._instance

    def velas(self):
        if self.velasW3 is None:
            self.velasW3 = Web3(Web3.HTTPProvider(self.velas_network_url))
            self.velasW3.eth.account.from_key(self.velas_private_key)
        return self.velasW3

    def matic(self):
        """
        Get a Web3 connection to the Polygon network with fallback mechanism.
        
        This method will try to connect using the primary URL first. If that fails,
        it will try each of the backup URLs until a successful connection is established.
        Failed endpoints are tracked and not immediately retried.
        """
        # If we already have a connection, check if it's still working
        if self.maticW3 is not None:
            try:
                # Simple check to see if connection is still alive
                self.maticW3.eth.block_number
                return self.maticW3
            except Exception as e:
                logger.warning(f"Existing Polygon connection failed: {str(e)}")
                self.maticW3 = None
        
        # Clear the failed endpoints list periodically to allow retrying
        current_time = time.time()
        if current_time - self._last_retry_time["matic"] > self._retry_interval:
            self._failed_endpoints["matic"].clear()
            self._last_retry_time["matic"] = current_time
        
        # Try the primary URL first if it's not in the failed list
        if self.matic_primary_url not in self._failed_endpoints["matic"]:
            try:
                logger.info(f"Attempting to connect to primary Polygon RPC: {self.matic_primary_url}")
                self.maticW3 = Web3(Web3.HTTPProvider(self.matic_primary_url))
                if self.maticW3.isConnected():
                    logger.info("Successfully connected to primary Polygon RPC")
                    self.maticW3.eth.account.from_key(self.matic_private_key)
                    return self.maticW3
            except Exception as e:
                logger.warning(f"Failed to connect to primary Polygon RPC: {str(e)}")
                self._failed_endpoints["matic"].add(self.matic_primary_url)
        
        # If primary URL fails, try the backup URLs
        # Shuffle the list to distribute load across backup endpoints
        backup_urls = list(self.matic_backup_urls)
        random.shuffle(backup_urls)
        
        for url in backup_urls:
            if url in self._failed_endpoints["matic"]:
                continue
                
            try:
                logger.info(f"Attempting to connect to backup Polygon RPC: {url}")
                self.maticW3 = Web3(Web3.HTTPProvider(url))
                if self.maticW3.isConnected():
                    logger.info(f"Successfully connected to backup Polygon RPC: {url}")
                    self.maticW3.eth.account.from_key(self.matic_private_key)
                    return self.maticW3
            except Exception as e:
                logger.warning(f"Failed to connect to backup Polygon RPC {url}: {str(e)}")
                self._failed_endpoints["matic"].add(url)
        
        # If we got here, all connection attempts failed
        error_msg = "Failed to connect to any Polygon RPC endpoint"
        logger.error(error_msg)
        raise ConnectionError(error_msg)

    def bnb(self):
        if self.bnbW3 is None:
            self.bnbW3 = Web3(Web3.HTTPProvider(self.bnb_network_url))
        return self.bnbW3

    def get_private_key(self):
        if network == "vlx":
            return self.velas_private_key
        if network == "matic":
            return self.matic_private_key
        if network == "bnb":
            return self.bnb_private_key  # Updated to return the BNB private key

    def getWeb3(self):
        if network == "vlx":
            return self.velas()
        if network == "matic":
            return self.matic()
        if network == "bnb":
            return self.bnb()

    def get_chain_id(self):
        if network == "vlx":
            return self.velas_network_id
        if network == "matic":
            return self.matic_network_id
        if network == "bnb":
            return self.bnb_network_id

    def get_tx_args(self) -> Dict[str, Union[int, str]]:  # Updated type annotation
        nonce = self.getWeb3().eth.get_transaction_count(self.executor_wallet)
        return {
            'chainId': self.get_chain_id(),
            'gas': 3000000,
            'gasPrice': self.getWeb3().toWei('5', 'gwei'),
            'nonce': nonce
        }

    def reset_connection(self):
        """
        Force the Web3 connections to be re-established on the next call.
        Useful when you want to ensure fresh connections.
        """
        if network == "vlx":
            self.velasW3 = None
        elif network == "matic":
            self.maticW3 = None
        elif network == "bnb":
            self.bnbW3 = None