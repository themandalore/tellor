import pytest
import os
from hexbytes import HexBytes
from web3.datastructures import AttributeDict
os.environ['WEB3_HTTP_PROVIDER_URI'] = 'https://mainnet.infura.io'
from tellor.auto import tellor

print("Tellor Addres: ", tellor.address)
print("Current Network: ",tellor.network)
print("Tellor Total Supply: ",tellor.total_supply)
print("Tellor Most recent Dispute: ",tellor.get_dispute(tellor.dispute_count))
print("Get Tellor Value Example: ", tellor.get_value(3, 1572377640))
print("Get Tellor Dispute Count: ",tellor.get_dispute(tellor.dispute_count))
