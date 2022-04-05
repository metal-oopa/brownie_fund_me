from brownie import MockV3Aggregator, network, web3
from web3 import Web3
from scripts.helpful_scripts import get_account

DECIMALS = 8
# This is 2,000 ethers
INITIAL_VALUE = 200000000


def deploy_mocks():
    """
    Use this script if you want to deploy mocks to a testnet
    """
    print(f"The active network is {network.show_active()}")
    print("Deploying Mocks...")
    account = get_account()
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(DECIMALS, INITIAL_VALUE, {"from": account})
    print("Mocks Deployed!")


def main():
    deploy_mocks()
