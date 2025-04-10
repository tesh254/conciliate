from web3 import Web3

from const.config import base_token
from const.controlls import network

bnb = {
    "exchange_address": {
        "pancakeswap": Web3.toChecksumAddress("0x10ED43C718714eb63d5aA57B78B54704E256024E"),
        "knightswap": Web3.toChecksumAddress("0x05E61E0cDcD2170a76F9568a110CEe3AFdD6c46f"),
        "viking swap": Web3.toChecksumAddress("0x05fF2B0DB69458A0750badebc4f9e13aDd608C7F"),
        "apeswap": Web3.toChecksumAddress("0xcF0feBd3f17CEf5b47b0cD257aCf6025c5BFf3b7"),
        "bakeryswap": Web3.toChecksumAddress("0xCDe540d7eAFE93aC5fE6233Bee57E1270D3E330F"),
        "cafeswap": Web3.toChecksumAddress("0x933DAea3a5995Fb94b14A7696a5F3ffD7B1E385A"),
        "cheesecake swap": Web3.toChecksumAddress("0x10ED43C718714eb63d5aA57B78B54704E256024E")
    },
    "currency_address": {
        "base": Web3.toChecksumAddress("0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c"),  # wbnb
        "wag": Web3.toChecksumAddress("0x7fa7df4996ac59f398476892cfb195ed38543520"),
        "busd": Web3.toChecksumAddress("0xe9e7cea3dedca5984780bafc599bd69add087d56"),
        "eth": Web3.toChecksumAddress("0x2170ed0880ac9a755fd29b2688956bd959f933f8"),
        "cake": Web3.toChecksumAddress("0x0e09fabb73bd3ade0a17ecc321fd13a19e81ce82"),
        "mbox": Web3.toChecksumAddress("0x3203c9e46ca618c8c1ce5dc67e7e9d75f5da2377"),
        "btcb": Web3.toChecksumAddress("0x7130d2a12b9bcbfae4f2634d864a1ee1ce3ead9c"),
        "doge": Web3.toChecksumAddress("0xba2ae424d960c26247dd6c32edc70b295c744c43"),
        "cgar": Web3.toChecksumAddress("0x432c7cf1de2b97a013f1130f199ed9d1363215ba"),
        "hero": Web3.toChecksumAddress("0xd40bedb44c081d2935eeba6ef5a3c8a31a1bbe13"),
        "BabyDoge": Web3.toChecksumAddress("0xc748673057861a797275cd8a068abb95a902e8de"),
        "Kiba": Web3.toChecksumAddress("0x31d3778a7ac0d98c4aaa347d8b6eaf7977448341"),
        "sea": Web3.toChecksumAddress("0x26193c7fa4354ae49ec53ea2cebc513dc39a10aa"),
        "stack": Web3.toChecksumAddress("0x6855f7bb6287f94ddcc8915e37e73a3c9fee5cf3"),
        "axm": Web3.toChecksumAddress("0x3a8a6a9543fc810c73cb4521caab3fe4fa9350b2"),
        "spg": Web3.toChecksumAddress("0x0ecaf010fc192e2d5cbeb4dfb1fee20fbd733aa1"),
        "dogeKing": Web3.toChecksumAddress("0x641ec142e67ab213539815f67e4276975c2f8d50"),
        "bcoin": Web3.toChecksumAddress("0x00e1656e45f18ec6747f5a8496fd39b50b38396d"),
        "gmi": Web3.toChecksumAddress("0x93d8d25e3c9a847a5da79f79ecac89461feca846"),
        "gear": Web3.toChecksumAddress("0xb4404dab7c0ec48b428cf37dec7fb628bcc41b36"),
        "difx": Web3.toChecksumAddress("0x697bd938e7e572e787ecd7bc74a31f1814c21264"),
        "nfs": Web3.toChecksumAddress("0x64815277c6caf24c1c2b55b11c78ef393237455c"),
        "lus": Web3.toChecksumAddress("0xde301d6a2569aefcfe271b9d98f318baee1d30a4"),
        "usdt": Web3.toChecksumAddress("0x55d398326f99059ff775485246999027b3197955"),
        "usdc": Web3.toChecksumAddress("0x8ac76a51cc950d9822d68b83fe1ad97b32cd580d"),
        "bpad": Web3.toChecksumAddress("0x29132062319aa375e764ef8ef756f2b28c77a9c9")
    }
}
# The exchange_address are the addresses of the UniSwapV02 router
vlx = {
    "exchange_address": {
        "wagyuswap": Web3.toChecksumAddress("0x3D1c58B6d4501E34DF37Cf0f664A58059a188F00"),
        "astroswap": Web3.toChecksumAddress("0x3328cd3a9A295cd00fBb1d71Bf097e002B4614ad"),
        "jungleSwap": Web3.toChecksumAddress("0x72E9064e0d0e85a50d058cCED3dE1957B1dCAc19")
    },
    "currency_address": {
        "base": Web3.toChecksumAddress("0xc579d1f3cf86749e05cd06f7ade17856c2ce3126"),  # wvlx
        "vinu": Web3.toChecksumAddress("0xc9f020b8e6ef6c5c34483ab4c3a5f45661e8f26e"),
        "astro": Web3.toChecksumAddress("0x72eb7ca07399ec402c5b7aa6a65752b6a1dc0c27"),
        "wag": Web3.toChecksumAddress("0xabf26902fd7b624e0db40d31171ea9dddf078351"),
        "busd": Web3.toChecksumAddress("0xc111c29a988ae0c0087d97b33c6e6766808a3bd3"),
        "velasPad": Web3.toChecksumAddress("0xa065e0858417dfc7abc6f2bd4d0185332475c180"),
        "qmall": Web3.toChecksumAddress("0x2217e5921b7edfb4bb193a6228459974010d2198"),
        "valhalla": Web3.toChecksumAddress("0x8d9fb713587174ee97e91866050c383b5cee6209"),
        "weway": Web3.toChecksumAddress("0x9ab70e92319f0b9127df78868fd3655fb9f1e322"),
        "pulsePad": Web3.toChecksumAddress("0x8a74bc8c372bc7f0e9ca3f6ac0df51be15aec47a"),
        "bitorbit": Web3.toChecksumAddress("0x09bce7716d46459df7473982fd27a96eabd6ee4d"),
        "BMF": Web3.toChecksumAddress("0x54c159b71262878bf096b45a3c6a8fd0a3250b10"),
        "bambooDefi": Web3.toChecksumAddress("0x300a8be53b4b5557f48620d578e7461e3b927dd0"),
        "swapz": Web3.toChecksumAddress("0x9b6fbf0ea23faf0d77b94d5699b44062e5e747ac")
    }
}

matic = {
    "exchange_address": {
        "sushiswap": Web3.toChecksumAddress("0x1b02da8cb0d097eb8d57a175b88c7d8b47997506"),
        "quickswap": Web3.toChecksumAddress("0xa5e0829caced8ffdd4de3c43696c57f7d7a678ff"),
        "uniswap": Web3.toChecksumAddress("0x68b3465833fb72A70ecDF485E0e4C7bD8665Fc45"),
        "apeswap": Web3.toChecksumAddress("0xC0788A3aD43d79aa53B09c2EaCc313A787d1d607"),
        "dfyn": Web3.toChecksumAddress("0xA102072A4C07F06EC3B4900FDC4C7B80b6c57429"),
        "polycat": Web3.toChecksumAddress("0x8CFD1B9B7478E7B0422916B72d1DB6A9D513D734"),
        "cometh": Web3.toChecksumAddress("0x93BCdB8D11Bc4E1bCc5C524E03bA31E21a682D12"),
        "jetswap": Web3.toChecksumAddress("0x5C6EC38fb0e2609672BDf628B1fD605A523E5923")
    },
    "currency_address": {
        "base": Web3.toChecksumAddress("0x0d500b1d8e8ef31e21c99d1db9a6444d3adf1270"),  # WMATIC
        # Stablecoins
        "usdc": Web3.toChecksumAddress("0x2791bca1f2de4661ed88a30c99a7a9449aa84174"),
        "usdt": Web3.toChecksumAddress("0xc2132d05d31c914a87c6611c10748aeb04b58e8f"),
        "dai": Web3.toChecksumAddress("0x8f3cf7ad23cd3cadbd9735aff958023239c6a063"),
        "eurs": Web3.toChecksumAddress("0xe111178a87a3bff0c8d18decba5798827539ae99"),
        "busd": Web3.toChecksumAddress("0xdab529f40e671a1d4bf91361c21bf9f0c9712ab7"),
        
        # Wrapped tokens
        "weth": Web3.toChecksumAddress("0x7ceb23fd6bc0add59e62ac25578270cff1b9f619"),
        "wbtc": Web3.toChecksumAddress("0x1bfd67037b42cf73acf2047067bd4f2c47d9bfd6"),
        "wbnb": Web3.toChecksumAddress("0xecdcb5b88f8e3c15f95c720c51c71c9e2080525d"),
        
        # DeFi tokens
        "aave": Web3.toChecksumAddress("0xd6df932a45c0f255f85145f286ea0b292b21c90b"),
        "crv": Web3.toChecksumAddress("0x172370d5cd63279efa6d502dab29171933a610af"),
        "link": Web3.toChecksumAddress("0x53e0bca35ec356bd5dddfebbd1fc0fd03fabad39"),
        "bal": Web3.toChecksumAddress("0x9a71012b13ca4d3d0cdc72a177df3ef03b0e76a3"),
        "cel": Web3.toChecksumAddress("0xd85d1e945766fea5eda9103f918bd915fbca63e6"),
        
        # Polygon ecosystem tokens
        "quick": Web3.toChecksumAddress("0x831753dd7087cac61ab5644b308642cc1c33dc13"),
        "sushi": Web3.toChecksumAddress("0x0b3f868e0be5597d5db7feb59e1cadbb0fdda50a"),
        "ghst": Web3.toChecksumAddress("0x385eeac5cb85a38a9a07a70c73e0a3271cfb54a7"),
        "route": Web3.toChecksumAddress("0x16eccfdbb4ee1a85a33f3a9b21175cd7ae753db4"),
        "dfyn": Web3.toChecksumAddress("0xc168e40227e4ebd8c1cae80f7a55a4f0e6d66c97"),
        "titan": Web3.toChecksumAddress("0xaaa5b9e6c589642f98a1cda99b9d024b8407285a"),
        "fish": Web3.toChecksumAddress("0x3a3df212b7aa91aa0402b9035b098891d276572b"),
        
        # Gaming and metaverse tokens
        "sand": Web3.toChecksumAddress("0xbbba073c31bf03b8acf7c28ef0738decf3695683"),
        "mana": Web3.toChecksumAddress("0xa1c57f48f0deb89f569dfbe6e2b7f46d33606fd4"),
        "ape": Web3.toChecksumAddress("0xb7b31a6bc18e48888545ce79e83e06003be70930"),
        "grt": Web3.toChecksumAddress("0x5fe2b58c013d7601147dcdd68c143a77499f5531")
    }
}


def exchange_address():
    if network == "vlx":
        return vlx["exchange_address"]
    if network == "matic":
        return matic["exchange_address"]
    if network == "bnb":
        return bnb["exchange_address"]


def currency_address():
    currency_address = {}
    if network == "vlx":
        currency_address = vlx["currency_address"]
    if network == "matic":
        currency_address = matic["currency_address"]
    if network == "bnb":
        currency_address = bnb["currency_address"]
    if base_token is not None:
        currency_address["base"] = Web3.toChecksumAddress(base_token)
    return currency_address

