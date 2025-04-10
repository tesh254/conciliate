import os
import dotenv

dotenv.load_dotenv()

network = "matic" # supported networks: vlx (VELAS), matic (POLYGON), bnb (BINANCE)
private_key = os.getenv("PRIVATE_KEY")
wallet_address = "0x89A96283f24BA0d6c8a68122857ebf5c48e7Ef7c"
trade_volume_limiter = 1
# This is the token that the arbitrage trade will start and end at
# I would suggest a stable coin
# Set to None to use default value in the const/addresses currency_address dictionary
base_token = "usdt"
infura_api_key=os.getenv("INFURA_API_KEY")
env = os.getenv("ENV")
