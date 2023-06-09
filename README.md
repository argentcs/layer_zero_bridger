# Stargate bridger
#### Software to automate the use of Stargate Bridge by multiple accounts

## Features
- Support for all popular EVM networks - Ethereum, Arbitrum, Optimism, Polygon, Fantom (not working for now), Avalance, BSC. 6 networks for 10$
- Scanning of networks for stablecoins on balance
- Bridge via Stargate 
- Complete randomization of paths and timings. No patterns
- Simultaneous operation of multiple accounts in different threads
- Automatic refuel from the Okex exchange (withdraw of the native token to pay gas)
- for LayerZero fans.

### Usage
1. Install Python 3.9.2 (another version is possible, but I can't vouch for it)
2. Go to the directory with the repository (you will probably have a different path):
```
cd stargate-bridger
```
3. Initialize the virtual environment and install the dependencies:
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
4. Set up config.py (timings, supported networks)
5. Add private keys in private_keys.txt
6. Run:
```
python3 main.py
```

