from solana.rpc.api import Client
from solana.publickey import PublicKey
from spl.token.client import Token
from solana.rpc.types import TxOpts

# Solana network connection
solana_client = Client("https://api.mainnet-beta.solana.com")

# CRAFT token mint address
CRAFT_TOKEN_MINT = PublicKey("CRAFT_TOKEN_MINT_ADDRESS")

def process_payment(from_wallet, to_wallet, amount):
    token = Token(solana_client, CRAFT_TOKEN_MINT, PublicKey(from_wallet))
    transaction = token.transfer(
        source=PublicKey(from_wallet),
        dest=PublicKey(to_wallet),
        amount=amount,
        opts=TxOpts(skip_confirmation=False)
    )
    return str(transaction)