import os


class OptimismConstants:
    NAME = "Optimism"
    NATIVE_TOKEN = "ETH"
    RPC = os.getenv("OPTIMISM_RPC", "https://opt-mainnet.g.alchemy.com/v2/demo")
    CHAIN_ID = 10
    STARGATE_CHAIN_ID = 111

    # Contracts
    USDC_CONTRACT_ADDRESS = "0x7F5c764cBc14f9669B88837ca1490cCa17c31607"
    USDC_DECIMALS = 6

    STARGATE_ROUTER_CONTRACT_ADDRESS = "0xB0D502E938ed5f4df2E681fE6E419ff29631d62b"

    APPROVE_GAS_LIMIT = 100_000
