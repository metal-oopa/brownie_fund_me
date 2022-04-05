from brownie import accounts, config, network, MockV3Aggregator
from web3 import Web3

LOCAL_DEVELOPMENT_CHAIN = ["development", "ganache-local"]
FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork", "mainnet-fork-dev"]


def get_account():
    if (
        network.show_active() in LOCAL_DEVELOPMENT_CHAIN
        or network.show_active() in FORKED_LOCAL_ENVIRONMENTS
    ):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])
