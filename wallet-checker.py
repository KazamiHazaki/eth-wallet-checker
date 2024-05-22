from web3 import Web3
from eth_utils import to_checksum_address, from_wei
from web3.middleware import geth_poa_middleware

def get_eth_balance(web3, address):
    try:
        # Convert address to checksum address
        address = to_checksum_address(address)
        
        # Get ETH balance
        balance = web3.eth.get_balance(address)
        
        return balance
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    try:
        # Input Ethereum node URL
        infura_url = input("Input your HTTP Provider: ")
        
        # Initialize Web3 with the provided Ethereum node URL
        web3 = Web3(Web3.HTTPProvider(infura_url))
        
        # Adding middleware for interacting with POA networks like Rinkeby or Goerli
        web3.middleware_onion.inject(geth_poa_middleware, layer=0)
        
        # Input Ethereum address
        eth_address = input("Input your ETH Wallet: ")
        
        # Get ETH balance
        eth_balance = get_eth_balance(web3, eth_address)
        if isinstance(eth_balance, str):
            print("Error:", eth_balance)
        else:
            print("ETH balance for address:", eth_address)
            print("ETH:", from_wei(eth_balance, 'ether'))

    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
    except Exception as e:
        print("An error occurred:", str(e))
