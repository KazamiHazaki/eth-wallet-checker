# Ethereum Wallet Balance Checker

This Python script allows you to check the balance of an Ethereum wallet address. It retrieves the balance of Ether (ETH) associated with the address and displays it in both Wei and Ether.

## Prerequisites

- Python 3 installed on your system
- Required Python packages: `web3`, `eth_utils`

You can install these packages using pip:

```bash
pip install web3 eth_utils
```

# Usage
Clone or download the repository to your local machine.

Navigate to the directory containing the script.

Open a terminal or command prompt in that directory.

Run the script using the following command:

```bash
python eth_balance_checker.py
```
You will be prompted to input the HTTP provider for Ethereum node. Provide the URL of the Ethereum node you want to connect to (e.g., Infura).

Next, you'll be asked to input your Ethereum wallet address.

After providing the wallet address, the script will display the balance of Ether associated with that address.

# Example
```bash
Your HTTP Provider: https://mainnet.infura.io/v3/your_infura_project_id
Input your ETH Wallet: 0x6a5C69ea2Fe700E7e6AA008a0193666594F8C48b

ETH balance for address: 0x6a5C69ea2Fe700E7e6AA008a0193666594F8C48b
ETH: 1.2345
```

Notes
Ensure that you have a stable internet connection while running the script as it interacts with the Ethereum blockchain via an Ethereum node.
Make sure to replace "https://mainnet.infura.io/v3/your_infura_project_id" with your Infura project ID or the URL of your preferred Ethereum node.
