from web3 import Web3
import time
import numpy as np
from numpy import array
import json
import requests
from random import *
import configparser
import pickle
import sys
import argparse
import csv
web3 = Web3(Web3.HTTPProvider('http://192.168.0.24:8545'))
#web3_infura = Web3(Web3.HTTPProvider('your infura link here))



cc_eth_root_url = 'https://min-api.cryptocompare.com/data/v2/histohour?fsym=ETH&tsym=USD&e=Coinbase&limit=1'
cc_bat_root_url = 'https://min-api.cryptocompare.com/data/v2/histohour?fsym=BAT&tsym=USDC&e=Coinbase&limit=1'
#cc_key = '&api_key=your crypto compare api key here'

ETH_SCALE = 1000000000000000000
ETH27_SCALE = 1000000000000000000000000000
ETH44_SCALE = 1000000000000000000000000000000000000000000000

FIRST_BLOCK = 8920000
#FIRST_BLOCK = 9100000
LAST_BLOCK = 9172000
#LAST_BLOCK = 8957600

vat0x = '0x35D1b3F3D7966A1DFe207aa4514C12a259A0492B'
ethAflip0x = '0xd8a04F5412223F513DC55F839574430f5EC15531'
batAflip0x = '0xaA745404d55f88C108A28c86abE7b5A1E7817c07'
cat0x = '0x78F2c2AF65126834c51822F56Be0d7469D7A523E'
spotter0x = '0x65C79fcB50Ca1594B025960e539eD7A9a6D434A3'
osmweth0x = '0x81FE72B5A8d1A857d176C3E7d5Bd2679A9B85763'
osmbat0x = '0xB4eb54AF9Cc7882DF0121d26c5b97E802915ABe6'
vaultmanager0x = '0x5ef30b9986345249bc32d8928B7ee64DE9435E39'
daijoin0x = '0x9759A6Ac90977b93B58547b4A71c78317f391A28'
migrationdaijoin0x = '0xad37fd42185Ba63009177058208dd1be4b136e6b'
wethjoin0x = '0x2F0b23f53734252Bda2277357e97e1517d6B042A'
batjoin0x = '0x3D0B1912B66114d4096F48A8CEe3A56C231772cA'
ethAflipabi = json.loads('[{"inputs":[{"internalType":"address","name":"vat_","type":"address"},{"internalType":"bytes32","name":"ilk_","type":"bytes32"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"id","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"lot","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"bid","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"tab","type":"uint256"},{"indexed":true,"internalType":"address","name":"usr","type":"address"},{"indexed":true,"internalType":"address","name":"gal","type":"address"}],"name":"Kick","type":"event"},{"anonymous":true,"inputs":[{"indexed":true,"internalType":"bytes4","name":"sig","type":"bytes4"},{"indexed":true,"internalType":"address","name":"usr","type":"address"},{"indexed":true,"internalType":"bytes32","name":"arg1","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"arg2","type":"bytes32"},{"indexed":false,"internalType":"bytes","name":"data","type":"bytes"}],"name":"LogNote","type":"event"},{"constant":true,"inputs":[],"name":"beg","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"bids","outputs":[{"internalType":"uint256","name":"bid","type":"uint256"},{"internalType":"uint256","name":"lot","type":"uint256"},{"internalType":"address","name":"guy","type":"address"},{"internalType":"uint48","name":"tic","type":"uint48"},{"internalType":"uint48","name":"end","type":"uint48"},{"internalType":"address","name":"usr","type":"address"},{"internalType":"address","name":"gal","type":"address"},{"internalType":"uint256","name":"tab","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"deal","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"uint256","name":"lot","type":"uint256"},{"internalType":"uint256","name":"bid","type":"uint256"}],"name":"dent","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"usr","type":"address"}],"name":"deny","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"bytes32","name":"what","type":"bytes32"},{"internalType":"uint256","name":"data","type":"uint256"}],"name":"file","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"ilk","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"usr","type":"address"},{"internalType":"address","name":"gal","type":"address"},{"internalType":"uint256","name":"tab","type":"uint256"},{"internalType":"uint256","name":"lot","type":"uint256"},{"internalType":"uint256","name":"bid","type":"uint256"}],"name":"kick","outputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"kicks","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"usr","type":"address"}],"name":"rely","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"tau","outputs":[{"internalType":"uint48","name":"","type":"uint48"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"uint256","name":"lot","type":"uint256"},{"internalType":"uint256","name":"bid","type":"uint256"}],"name":"tend","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"tick","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"ttl","outputs":[{"internalType":"uint48","name":"","type":"uint48"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"vat","outputs":[{"internalType":"contract VatLike","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"wards","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"yank","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"}]')
batAflipabi = json.loads('[{"inputs":[{"internalType":"address","name":"vat_","type":"address"},{"internalType":"bytes32","name":"ilk_","type":"bytes32"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"id","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"lot","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"bid","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"tab","type":"uint256"},{"indexed":true,"internalType":"address","name":"usr","type":"address"},{"indexed":true,"internalType":"address","name":"gal","type":"address"}],"name":"Kick","type":"event"},{"anonymous":true,"inputs":[{"indexed":true,"internalType":"bytes4","name":"sig","type":"bytes4"},{"indexed":true,"internalType":"address","name":"usr","type":"address"},{"indexed":true,"internalType":"bytes32","name":"arg1","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"arg2","type":"bytes32"},{"indexed":false,"internalType":"bytes","name":"data","type":"bytes"}],"name":"LogNote","type":"event"},{"constant":true,"inputs":[],"name":"beg","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"bids","outputs":[{"internalType":"uint256","name":"bid","type":"uint256"},{"internalType":"uint256","name":"lot","type":"uint256"},{"internalType":"address","name":"guy","type":"address"},{"internalType":"uint48","name":"tic","type":"uint48"},{"internalType":"uint48","name":"end","type":"uint48"},{"internalType":"address","name":"usr","type":"address"},{"internalType":"address","name":"gal","type":"address"},{"internalType":"uint256","name":"tab","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"deal","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"uint256","name":"lot","type":"uint256"},{"internalType":"uint256","name":"bid","type":"uint256"}],"name":"dent","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"usr","type":"address"}],"name":"deny","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"bytes32","name":"what","type":"bytes32"},{"internalType":"uint256","name":"data","type":"uint256"}],"name":"file","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"ilk","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"usr","type":"address"},{"internalType":"address","name":"gal","type":"address"},{"internalType":"uint256","name":"tab","type":"uint256"},{"internalType":"uint256","name":"lot","type":"uint256"},{"internalType":"uint256","name":"bid","type":"uint256"}],"name":"kick","outputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"kicks","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"usr","type":"address"}],"name":"rely","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"tau","outputs":[{"internalType":"uint48","name":"","type":"uint48"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"uint256","name":"lot","type":"uint256"},{"internalType":"uint256","name":"bid","type":"uint256"}],"name":"tend","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"tick","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"ttl","outputs":[{"internalType":"uint48","name":"","type":"uint48"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"vat","outputs":[{"internalType":"contract VatLike","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"wards","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"yank","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"}]')
catabi = json.loads('[{"inputs":[{"internalType":"address","name":"vat_","type":"address"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"ilk","type":"bytes32"},{"indexed":true,"internalType":"address","name":"urn","type":"address"},{"indexed":false,"internalType":"uint256","name":"ink","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"art","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"tab","type":"uint256"},{"indexed":false,"internalType":"address","name":"flip","type":"address"},{"indexed":false,"internalType":"uint256","name":"id","type":"uint256"}],"name":"Bite","type":"event"},{"anonymous":true,"inputs":[{"indexed":true,"internalType":"bytes4","name":"sig","type":"bytes4"},{"indexed":true,"internalType":"address","name":"usr","type":"address"},{"indexed":true,"internalType":"bytes32","name":"arg1","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"arg2","type":"bytes32"},{"indexed":false,"internalType":"bytes","name":"data","type":"bytes"}],"name":"LogNote","type":"event"},{"constant":false,"inputs":[{"internalType":"bytes32","name":"ilk","type":"bytes32"},{"internalType":"address","name":"urn","type":"address"}],"name":"bite","outputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"cage","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"usr","type":"address"}],"name":"deny","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"bytes32","name":"ilk","type":"bytes32"},{"internalType":"bytes32","name":"what","type":"bytes32"},{"internalType":"uint256","name":"data","type":"uint256"}],"name":"file","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"bytes32","name":"what","type":"bytes32"},{"internalType":"address","name":"data","type":"address"}],"name":"file","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"bytes32","name":"ilk","type":"bytes32"},{"internalType":"bytes32","name":"what","type":"bytes32"},{"internalType":"address","name":"flip","type":"address"}],"name":"file","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"name":"ilks","outputs":[{"internalType":"address","name":"flip","type":"address"},{"internalType":"uint256","name":"chop","type":"uint256"},{"internalType":"uint256","name":"lump","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"live","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"usr","type":"address"}],"name":"rely","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"vat","outputs":[{"internalType":"contract VatLike","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"vow","outputs":[{"internalType":"contract VowLike","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"wards","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"}]')
vatabi = json.loads('[{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":true,"inputs":[{"indexed":true,"internalType":"bytes4","name":"sig","type":"bytes4"},{"indexed":true,"internalType":"bytes32","name":"arg1","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"arg2","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"arg3","type":"bytes32"},{"indexed":false,"internalType":"bytes","name":"data","type":"bytes"}],"name":"LogNote","type":"event"},{"constant":true,"inputs":[],"name":"Line","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"cage","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"can","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"dai","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"debt","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"usr","type":"address"}],"name":"deny","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"bytes32","name":"ilk","type":"bytes32"},{"internalType":"bytes32","name":"what","type":"bytes32"},{"internalType":"uint256","name":"data","type":"uint256"}],"name":"file","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"bytes32","name":"what","type":"bytes32"},{"internalType":"uint256","name":"data","type":"uint256"}],"name":"file","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"bytes32","name":"ilk","type":"bytes32"},{"internalType":"address","name":"src","type":"address"},{"internalType":"address","name":"dst","type":"address"},{"internalType":"uint256","name":"wad","type":"uint256"}],"name":"flux","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"bytes32","name":"i","type":"bytes32"},{"internalType":"address","name":"u","type":"address"},{"internalType":"int256","name":"rate","type":"int256"}],"name":"fold","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"bytes32","name":"ilk","type":"bytes32"},{"internalType":"address","name":"src","type":"address"},{"internalType":"address","name":"dst","type":"address"},{"internalType":"int256","name":"dink","type":"int256"},{"internalType":"int256","name":"dart","type":"int256"}],"name":"fork","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"bytes32","name":"i","type":"bytes32"},{"internalType":"address","name":"u","type":"address"},{"internalType":"address","name":"v","type":"address"},{"internalType":"address","name":"w","type":"address"},{"internalType":"int256","name":"dink","type":"int256"},{"internalType":"int256","name":"dart","type":"int256"}],"name":"frob","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"bytes32","name":"","type":"bytes32"},{"internalType":"address","name":"","type":"address"}],"name":"gem","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"bytes32","name":"i","type":"bytes32"},{"internalType":"address","name":"u","type":"address"},{"internalType":"address","name":"v","type":"address"},{"internalType":"address","name":"w","type":"address"},{"internalType":"int256","name":"dink","type":"int256"},{"internalType":"int256","name":"dart","type":"int256"}],"name":"grab","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"rad","type":"uint256"}],"name":"heal","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"usr","type":"address"}],"name":"hope","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"name":"ilks","outputs":[{"internalType":"uint256","name":"Art","type":"uint256"},{"internalType":"uint256","name":"rate","type":"uint256"},{"internalType":"uint256","name":"spot","type":"uint256"},{"internalType":"uint256","name":"line","type":"uint256"},{"internalType":"uint256","name":"dust","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"bytes32","name":"ilk","type":"bytes32"}],"name":"init","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"live","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"src","type":"address"},{"internalType":"address","name":"dst","type":"address"},{"internalType":"uint256","name":"rad","type":"uint256"}],"name":"move","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"usr","type":"address"}],"name":"nope","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"usr","type":"address"}],"name":"rely","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"sin","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"bytes32","name":"ilk","type":"bytes32"},{"internalType":"address","name":"usr","type":"address"},{"internalType":"int256","name":"wad","type":"int256"}],"name":"slip","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"u","type":"address"},{"internalType":"address","name":"v","type":"address"},{"internalType":"uint256","name":"rad","type":"uint256"}],"name":"suck","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"bytes32","name":"","type":"bytes32"},{"internalType":"address","name":"","type":"address"}],"name":"urns","outputs":[{"internalType":"uint256","name":"ink","type":"uint256"},{"internalType":"uint256","name":"art","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"vice","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"wards","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"}]')
vaultmanagerabi = json.loads('[{"inputs":[{"internalType":"address","name":"vat_","type":"address"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":true,"inputs":[{"indexed":true,"internalType":"bytes4","name":"sig","type":"bytes4"},{"indexed":true,"internalType":"address","name":"usr","type":"address"},{"indexed":true,"internalType":"bytes32","name":"arg1","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"arg2","type":"bytes32"},{"indexed":false,"internalType":"bytes","name":"data","type":"bytes"}],"name":"LogNote","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"usr","type":"address"},{"indexed":true,"internalType":"address","name":"own","type":"address"},{"indexed":true,"internalType":"uint256","name":"cdp","type":"uint256"}],"name":"NewCdp","type":"event"},{"constant":false,"inputs":[{"internalType":"uint256","name":"cdp","type":"uint256"},{"internalType":"address","name":"usr","type":"address"},{"internalType":"uint256","name":"ok","type":"uint256"}],"name":"cdpAllow","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"address","name":"","type":"address"}],"name":"cdpCan","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"cdpi","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"count","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"src","type":"address"},{"internalType":"uint256","name":"cdp","type":"uint256"}],"name":"enter","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"first","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"bytes32","name":"ilk","type":"bytes32"},{"internalType":"uint256","name":"cdp","type":"uint256"},{"internalType":"address","name":"dst","type":"address"},{"internalType":"uint256","name":"wad","type":"uint256"}],"name":"flux","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"cdp","type":"uint256"},{"internalType":"address","name":"dst","type":"address"},{"internalType":"uint256","name":"wad","type":"uint256"}],"name":"flux","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"cdp","type":"uint256"},{"internalType":"int256","name":"dink","type":"int256"},{"internalType":"int256","name":"dart","type":"int256"}],"name":"frob","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"cdp","type":"uint256"},{"internalType":"address","name":"dst","type":"address"}],"name":"give","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"ilks","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"last","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"list","outputs":[{"internalType":"uint256","name":"prev","type":"uint256"},{"internalType":"uint256","name":"next","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"cdp","type":"uint256"},{"internalType":"address","name":"dst","type":"address"},{"internalType":"uint256","name":"rad","type":"uint256"}],"name":"move","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"bytes32","name":"ilk","type":"bytes32"},{"internalType":"address","name":"usr","type":"address"}],"name":"open","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"owns","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"cdp","type":"uint256"},{"internalType":"address","name":"dst","type":"address"}],"name":"quit","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"cdpSrc","type":"uint256"},{"internalType":"uint256","name":"cdpDst","type":"uint256"}],"name":"shift","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"usr","type":"address"},{"internalType":"uint256","name":"ok","type":"uint256"}],"name":"urnAllow","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"urnCan","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"urns","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"vat","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"}]')

ethAflip = web3.eth.contract(address=ethAflip0x, abi=ethAflipabi)
batAflip = web3.eth.contract(address=batAflip0x, abi=batAflipabi)
cat = web3.eth.contract(address=cat0x, abi=catabi)
vat = web3.eth.contract(address=vat0x, abi=vatabi)
vault_manager = web3.eth.contract(address=vaultmanager0x, abi=vaultmanagerabi)

TEND_TOPIC = ['0x4b43ed1200000000000000000000000000000000000000000000000000000000']
DENT_TOPIC = ['0x5ff3a38200000000000000000000000000000000000000000000000000000000']
DEAL_TOPIC = ['0xc959c42b00000000000000000000000000000000000000000000000000000000']
BITE_TOPIC = ['0xa716da86bc1fb6d43d1493373f34d7a418b619681cd7b90f7ea667ba1489be28']
KICK_TOPIC = ['0xc84ce3a1172f0dec3173f04caaa6005151a4bfe40d4c9f3ea28dba5f719b2a7a']
NEW_VAULT_TOPIC = ['0xd6be0bc178658a382ff4f91c8c68b542aa6b71685b8fe427966b87745c3ea7a2']
POKE_TOPIC = ['0xdfd7467e425a8107cfd368d159957692c25085aacbcf5228ce08f10f2146486e']
LOGVALUE_TOPIC = ['0x296ba4ca62c6c21c95e828080cb8aec7481b71390585605300a8a76f9e95b527']
DAI_JOIN_DRAW_TOPIC = ['0xef693bed00000000000000000000000000000000000000000000000000000000']
DAI_JOIN_WIPE_TOPIC = ['0x3b4da69f00000000000000000000000000000000000000000000000000000000']
WETH_JOIN_LOCK_TOPIC = ['0x3b4da69f00000000000000000000000000000000000000000000000000000000']
WETH_JOIN_FREE_TOPIC = ['0xef693bed00000000000000000000000000000000000000000000000000000000']
BAT_JOIN_LOCK_TOPIC = ['0x3b4da69f00000000000000000000000000000000000000000000000000000000']
BAT_JOIN_FREE_TOPIC = ['0xef693bed00000000000000000000000000000000000000000000000000000000']
SHIFT_TOPIC = ['0xe50322a200000000000000000000000000000000000000000000000000000000']


URN_TOPIC = '0x7608870300000000000000000000000000000000000000000000000000000000'
ETH_A_ILK = '0x4554482d41000000000000000000000000000000000000000000000000000000'
BAT_A_ILK = '0x4241542d41000000000000000000000000000000000000000000000000000000'
MIGRATED_ILK = '0x5341490000000000000000000000000000000000000000000000000000000000'
DAI_DRAW_MANAGER = '0x45e6bdcd00000000000000000000000000000000000000000000000000000000'
DAI_WIPE_MANAGER = '0x45e6bdcd00000000000000000000000000000000000000000000000000000000'
GIVE_TOPIC = '0xfcafcc6800000000000000000000000000000000000000000000000000000000'

VAULT_OBJ_FILENAME = 'vaultids.obj'
URN_TO_ID_DICT_FILENAME = 'urntoiddict.obj'
LID_TO_ID_DICT_FILENAME = 'lidtoiddict.obj'
WETH_OSM_PRICES_FILENAME = 'wethosmprices.obj'
BAT_OSM_PRICES_FILENAME = 'batosmprices.obj'
LIQUIDATED_VAULTS_FILENAME = 'liquidatedvaultids.obj'
LIQUIDATED_DEALS_FILENAME = 'liquidateddeals.obj'
VAULT_INIT_FILENAME = 'vaultinit.csv'
VAULT_INTERACTIONS_FILENAME = 'vaultinteractions.csv'
DEALS_FILENAME = 'deals.csv'
ETH_PRICE_CSV = 'ethosm.csv'
BAT_PRICE_CSV = 'batosm.csv'

STEP_SIZE = 100

class Vault():
	def __init__(self):
		self.vaultid = 0
		self.block_created = 0
		self.actions = []
		self.kicks = []
		self.tends = []
		self.winning_tends = []
		self.dents = []
		self.winning_dents = []
		self.deals = []
		self.debt = 0
		self.max_debt = 0
		self.owners = []
		self.urn = ''
		self.ilk_type = ''

	def display_vault(self):
		print('id: {0}\n bc: {1}\n actions: {2}\n owners: {3}\n kicks: {4}\n tends{5}\n winning_tends {6}\n dents {7}\n winning_dents\n {8} deals{9}\n urn: {10}\n'.format(self.vaultid, self.block_created, self.actions, self.owners, self.kicks, self.tends, self.winning_tends, self.dents, self.winning_dents, self.deals, self.urn))
	def display_actions(self):
		for p in self.actions:
			print(p)

def get_filled_vault_id():
	try:
		with (open(VAULT_OBJ_FILENAME, "rb")) as openfile:
			while True:
				try:
					return pickle.load(openfile)
				except EOFError:
					break
	except FileNotFoundError:
		print("\nFile " + CDP_OBJ_FILENAME + " does not exist. Run 'update_spells' command.\n")
		sys.exit(-1)

def get_vault_id():
	vaults = []
	urn_to_id_dict = {}
	lid_to_id_dict = {}
	print("getting the ids starting with 1")
	vv = Vault()
	# this is the dummy vault
	vv.vaultid = 0
	vv.owners = ['0x0000000000000000000000000000000000000002']
	vv.block_created = FIRST_BLOCK
	vv.actions = []
	vv.kicks = []
	vv.tends = []
	vv.winning_tends = []
	vv.winning_dents = []
	vv.dents = []
	vv.deals = []
	vv.ilk_type = 'ETHA'
	vv.urn = '0x0000000000000000000000000000000000000003'
	vaults.append(vv)

	for i in range(FIRST_BLOCK, LAST_BLOCK, STEP_SIZE):
		#doing this because it goes so slow here and through 8965000ish for some reason
		if ((i > 8944000) and (i < 8952500)):
			continue
		newcup_pre = []
		newdraw_pre = []
		newwipe_pre = []
		newlock_pre = []
		newfree_pre = []
		newkick_pre = []
		newcup = []
		newdraw = []
		newwipe = []
		newlock = []
		newfree = []
		newkick = []
		print("getting ids for block {0}".format(i))

		newcup_filter = web3.eth.filter({"address":vaultmanager0x, "fromBlock":i, "toBlock":i + STEP_SIZE - 1, "topics":NEW_VAULT_TOPIC})
		newdraw_filter = web3.eth.filter({"address":daijoin0x, "fromBlock":i, "toBlock":i + STEP_SIZE - 1, "topics":DAI_JOIN_DRAW_TOPIC})
		newmigratedraw_filter = web3.eth.filter({"address":migrationdaijoin0x, "fromBlock":i, "toBlock":i + STEP_SIZE - 1, "topics":DAI_JOIN_DRAW_TOPIC})
		newwipe_filter = web3.eth.filter({"address":daijoin0x, "fromBlock":i, "toBlock":i + STEP_SIZE - 1, "topics":DAI_JOIN_WIPE_TOPIC})
		newwethlock_filter = web3.eth.filter({"address":wethjoin0x, "fromBlock":i, "toBlock":i + STEP_SIZE - 1, "topics":WETH_JOIN_LOCK_TOPIC})
		newbatlock_filter = web3.eth.filter({"address":batjoin0x, "fromBlock":i, "toBlock":i + STEP_SIZE - 1, "topics":BAT_JOIN_LOCK_TOPIC})
		newwethfree_filter = web3.eth.filter({"address":wethjoin0x, "fromBlock":i, "toBlock":i + STEP_SIZE - 1, "topics":WETH_JOIN_FREE_TOPIC})
		newbatfree_filter = web3.eth.filter({"address":batjoin0x, "fromBlock":i, "toBlock":i + STEP_SIZE - 1, "topics":BAT_JOIN_FREE_TOPIC})
		newwethkick_filter = web3.eth.filter({"address":ethAflip0x, "fromBlock":i, "toBlock":i + STEP_SIZE - 1, "topics":KICK_TOPIC})
		newwethtend_filter = web3.eth.filter({"address":ethAflip0x, "fromBlock":i, "toBlock":i + STEP_SIZE - 1, "topics":TEND_TOPIC})
		newwethdent_filter = web3.eth.filter({"address":ethAflip0x, "fromBlock":i, "toBlock":i + STEP_SIZE - 1, "topics":DENT_TOPIC})
		newwethdeal_filter = web3.eth.filter({"address":ethAflip0x, "fromBlock":i, "toBlock":i + STEP_SIZE - 1, "topics":DEAL_TOPIC})
		newbatkick_filter = web3.eth.filter({"address":batAflip0x, "fromBlock":i, "toBlock":i + STEP_SIZE - 1, "topics":KICK_TOPIC})
		newbattend_filter = web3.eth.filter({"address":batAflip0x, "fromBlock":i, "toBlock":i + STEP_SIZE - 1, "topics":TEND_TOPIC})
		newbatdent_filter = web3.eth.filter({"address":batAflip0x, "fromBlock":i, "toBlock":i + STEP_SIZE - 1, "topics":DENT_TOPIC})
		newbatdeal_filter = web3.eth.filter({"address":batAflip0x, "fromBlock":i, "toBlock":i + STEP_SIZE - 1, "topics":DEAL_TOPIC})
		newshift_filter = web3.eth.filter({"address":vaultmanager0x, "fromBlock":i, "toBlock":i + STEP_SIZE - 1, "topics":SHIFT_TOPIC})


		newcup_pre = newcup_filter.get_all_entries()
		newdraw_pre = newdraw_filter.get_all_entries()
		newmigratedraw_pre = newmigratedraw_filter.get_all_entries()
		newwipe_pre = newwipe_filter.get_all_entries()
		newwethlock_pre = newwethlock_filter.get_all_entries()
		newbatlock_pre = newbatlock_filter.get_all_entries()
		newwethfree_pre = newwethfree_filter.get_all_entries()
		newbatfree_pre = newbatfree_filter.get_all_entries()
		newwethkick_pre = newwethkick_filter.get_all_entries()
		newwethtend_pre = newwethtend_filter.get_all_entries()
		newwethdent_pre = newwethdent_filter.get_all_entries()
		newwethdeal_pre = newwethdeal_filter.get_all_entries()
		newbatkick_pre = newbatkick_filter.get_all_entries()
		newbattend_pre = newbattend_filter.get_all_entries()
		newbatdent_pre = newbatdent_filter.get_all_entries()
		newbatdeal_pre = newbatdeal_filter.get_all_entries()
		newshift_pre = newshift_filter.get_all_entries()


		for j in range(0, len(newcup_pre)):
			vv = Vault()
			vv.vaultid = web3.toInt(newcup_pre[j]['topics'][3])
			vv.owners = []
			vv.owners.append(web3.toChecksumAddress(vault_manager.functions.owns(vv.vaultid).call()))
			vv.block_created = web3.toInt(newcup_pre[j]['blockNumber'])
			vv.actions = []
			vv.kicks = []
			vv.tends = []
			vv.winning_tends = []
			vv.dents = []
			vv.winning_dents = []
			vv.deals = []
			vv.urn = vault_manager.functions.urns(vv.vaultid).call()
			print(vv.vaultid)
			ii = web3.toHex(vault_manager.functions.ilks(vv.vaultid).call())
			urn_to_id_dict[vv.urn] = vv.vaultid
			
			
			if (ii == ETH_A_ILK):
				vv.ilk_type = 'ETHA'
			elif(ii == BAT_A_ILK):
				vv.ilk_type = 'BATA'
				#print("batid {0}".format(vv.vaultid))
					
			vaults.append(vv)

		# draws
		for j in range(0, len(newdraw_pre)):
			amt = web3.toInt(newdraw_pre[j]['topics'][3])
			rec = web3.eth.getTransactionReceipt(newdraw_pre[j]['transactionHash'])
			for k in rec['logs']:
				if ((k['address'] == vaultmanager0x) and (web3.toHex(k['topics'][0]) == DAI_DRAW_MANAGER) and (amt != 0)):
					ii = web3.toInt(k['topics'][2])
					act = {'action':'draw', 'amount':amt, 'blockNumber':newdraw_pre[j]['blockNumber']}
					vaults[ii].actions.append(act)
					break

		#special migratation draws
		for j in range(0, len(newmigratedraw_pre)):
			amt = web3.toInt(newmigratedraw_pre[j]['topics'][3])
			rec = web3.eth.getTransactionReceipt(newmigratedraw_pre[j]['transactionHash'])
			for k in rec['logs']:
				if ((k['address'] == vaultmanager0x) and (web3.toHex(k['topics'][0]) == DAI_DRAW_MANAGER) and (amt != 0)):
					ii = web3.toInt(k['topics'][2])
					act = {'action':'draw', 'amount':amt, 'blockNumber':newmigratedraw_pre[j]['blockNumber']}
					vaults[ii].actions.append(act)
					break


		# wipes
		for j in range(0, len(newwipe_pre)):
			amt = web3.toInt(newwipe_pre[j]['topics'][3])
			rec = web3.eth.getTransactionReceipt(newwipe_pre[j]['transactionHash'])
			for k in rec['logs']:
				if ((k['address'] == vaultmanager0x) and (web3.toHex(k['topics'][0]) == DAI_WIPE_MANAGER) and (amt != 0)):
					ii = web3.toInt(k['topics'][2])
					act = {'action':'wipe', 'amount':amt, 'blockNumber':newwipe_pre[j]['blockNumber']}
					vaults[ii].actions.append(act)
					break

		# WETH locks
		for j in range(0, len(newwethlock_pre)):
			amt = web3.toInt(newwethlock_pre[j]['topics'][3])
			rec = web3.eth.getTransactionReceipt(newwethlock_pre[j]['transactionHash'])
			for k in rec['logs']:
				if ((k['address'] == vat0x) and (web3.toHex(k['topics'][0]) == URN_TOPIC) and (amt != 0)):
					urnn = web3.toChecksumAddress(web3.toHex(k['topics'][2][12:]))
					if (urnn == '0xc73e0383F3Aff3215E6f04B0331D58CeCf0Ab849'):
						continue
					ii = urn_to_id_dict[urnn]
					act = {'action':'lock', 'amount':amt, 'blockNumber':newwethlock_pre[j]['blockNumber']}
					vaults[ii].actions.append(act)
					break

		# BAT locks
		for j in range(0, len(newbatlock_pre)):
			amt = web3.toInt(newbatlock_pre[j]['topics'][3])
			rec = web3.eth.getTransactionReceipt(newbatlock_pre[j]['transactionHash'])
			for k in rec['logs']:
				if ((k['address'] == vat0x) and (web3.toHex(k['topics'][0]) == URN_TOPIC) and (amt != 0)):
					urnn = web3.toChecksumAddress(web3.toHex(k['topics'][2][12:]))
					if (urnn == '0xc73e0383F3Aff3215E6f04B0331D58CeCf0Ab849'):
						continue
					ii = urn_to_id_dict[urnn]
					act = {'action':'lock', 'amount':amt, 'blockNumber':newbatlock_pre[j]['blockNumber']}
					vaults[ii].actions.append(act)
					break

		# WETH frees
		for j in range(0, len(newwethfree_pre)):
			amt = web3.toInt(newwethfree_pre[j]['topics'][3])
			rec = web3.eth.getTransactionReceipt(newwethfree_pre[j]['transactionHash'])
			for k in rec['logs']:
				if ((k['address'] == vat0x) and (web3.toHex(k['topics'][0]) == URN_TOPIC) and (amt != 0)):
					urnn = web3.toChecksumAddress(web3.toHex(k['topics'][2][12:]))
					if (urnn == '0xc73e0383F3Aff3215E6f04B0331D58CeCf0Ab849'):
						continue
					ii = urn_to_id_dict[urnn]
					act = {'action':'free', 'amount':amt, 'blockNumber':newwethfree_pre[j]['blockNumber']}
					vaults[ii].actions.append(act)
					break

		# BAT frees
		for j in range(0, len(newbatfree_pre)):
			amt = web3.toInt(newbatfree_pre[j]['topics'][3])
			rec = web3.eth.getTransactionReceipt(newbatfree_pre[j]['transactionHash'])
			for k in rec['logs']:
				if ((k['address'] == vat0x) and (web3.toHex(k['topics'][0]) == URN_TOPIC) and (amt != 0)):
					urnn = web3.toChecksumAddress(web3.toHex(k['topics'][2][12:]))
					if (urnn == '0xc73e0383F3Aff3215E6f04B0331D58CeCf0Ab849'):
						continue
					ii = urn_to_id_dict[urnn]
					act = {'action':'free', 'amount':amt, 'blockNumber':newbatfree_pre[j]['blockNumber']}
					vaults[ii].actions.append(act)
					break

		# WETH kicks
		for j in range(0, len(newwethkick_pre)):
			liquidation_id = web3.toInt(hexstr=newwethkick_pre[j]['data'][2:66].lstrip('0'))
			urnn = web3.toChecksumAddress(web3.toHex(newwethkick_pre[j]['topics'][1][12:]))
			rec = web3.eth.getTransactionReceipt(newwethkick_pre[j]['transactionHash'])
			keeper = web3.toChecksumAddress(rec['from'])
			ii = urn_to_id_dict[urnn]
			lid_to_id_dict[liquidation_id] = ii
			act = {'action':'kick', 'amount':0, 'liquidationid':liquidation_id, 'keeper': keeper, 'blockNumber':newwethkick_pre[j]['blockNumber']}
			vaults[ii].kicks.append(act)
					
		# WETH tends
		for j in range(0, len(newwethtend_pre)):
			liquidation_id = web3.toInt(hexstr=newwethtend_pre[j]['data'][190:202].lstrip('0'))
			lot = web3.toInt(hexstr=newwethtend_pre[j]['data'][230:266].lstrip('0'))
			bid = web3.toInt(hexstr=newwethtend_pre[j]['data'][269:330].lstrip('0'))
			keeper = web3.toChecksumAddress(web3.toHex(newwethtend_pre[j]['topics'][1][12:]))
			act = {'action':'tend', 'lot':lot, 'bid':bid, 'liquidationid':liquidation_id, 'keeper': keeper, 'blockNumber':newwethtend_pre[j]['blockNumber']}
			ii = lid_to_id_dict[liquidation_id]
			vaults[ii].tends.append(act)

		# WETH dents
		for j in range(0, len(newwethdent_pre)):
			liquidation_id = web3.toInt(hexstr=newwethdent_pre[j]['data'][190:202].lstrip('0'))
			lot = web3.toInt(hexstr=newwethdent_pre[j]['data'][230:266].lstrip('0'))
			bid = web3.toInt(hexstr=newwethdent_pre[j]['data'][269:330].lstrip('0'))
			keeper = web3.toChecksumAddress(web3.toHex(newwethdent_pre[j]['topics'][1][12:]))
			act = {'action':'dent', 'lot':lot, 'bid':bid, 'liquidationid':liquidation_id, 'keeper': keeper, 'blockNumber':newwethdent_pre[j]['blockNumber']}
			ii = lid_to_id_dict[liquidation_id]
			vaults[ii].dents.append(act)

		# WETH deals
		for j in range(0, len(newwethdeal_pre)):
			liquidation_id = web3.toInt(hexstr=web3.toHex(newwethdeal_pre[j]['topics'][2]))
			keeper = web3.toChecksumAddress(web3.toHex(newwethdeal_pre[j]['topics'][1][12:]))
			act = {'action':'deal', 'liquidationid':liquidation_id, 'keeper':keeper, 'blockNumber':newwethdeal_pre[j]['blockNumber']}
			ii = lid_to_id_dict[liquidation_id]
			vaults[ii].deals.append(act)

		# BAT kicks
		for j in range(0, len(newbatkick_pre)):
			liquidation_id = web3.toInt(hexstr=newbatkick_pre[j]['data'][2:66].lstrip('0'))
			urnn = web3.toChecksumAddress(web3.toHex(newbatkick_pre[j]['topics'][1][12:]))
			rec = web3.eth.getTransactionReceipt(newbatkick_pre[j]['transactionHash'])
			keeper = web3.toChecksumAddress(rec['from'])
			ii = urn_to_id_dict[urnn]
			lid_to_id_dict[liquidation_id] = ii
			act = {'action':'kick', 'amount':0, 'liquidationid':liquidation_id, 'keeper': keeper, 'blockNumber':newbatkick_pre[j]['blockNumber']}
			vaults[ii].kicks.append(act)
					
		# BAT tends
		for j in range(0, len(newbattend_pre)):
			liquidation_id = web3.toInt(hexstr=newbattend_pre[j]['data'][190:202].lstrip('0'))
			lot = web3.toInt(hexstr=newbattend_pre[j]['data'][230:266].lstrip('0'))
			bid = web3.toInt(hexstr=newbattend_pre[j]['data'][269:330].lstrip('0'))
			keeper = web3.toChecksumAddress(web3.toHex(newbattend_pre[j]['topics'][1][12:]))
			act = {'action':'tend', 'lot':lot, 'bid':bid, 'liquidationid':liquidation_id, 'keeper': keeper, 'blockNumber':newbattend_pre[j]['blockNumber']}
			ii = lid_to_id_dict[liquidation_id]
			vaults[ii].tends.append(act)

		# BAT dents
		for j in range(0, len(newbatdent_pre)):
			liquidation_id = web3.toInt(hexstr=newbatdent_pre[j]['data'][190:202].lstrip('0'))
			lot = web3.toInt(hexstr=newbatdent_pre[j]['data'][230:266].lstrip('0'))
			bid = web3.toInt(hexstr=newbatdent_pre[j]['data'][269:330].lstrip('0'))
			keeper = web3.toChecksumAddress(web3.toHex(newbatdent_pre[j]['topics'][1][12:]))
			act = {'action':'dent', 'lot':lot, 'bid':bid, 'liquidationid':liquidation_id, 'keeper': keeper, 'blockNumber':newbatdent_pre[j]['blockNumber']}
			ii = lid_to_id_dict[liquidation_id]
			vaults[ii].dents.append(act)

		# BATdeals
		for j in range(0, len(newbatdeal_pre)):
			liquidation_id = web3.toInt(hexstr=web3.toHex(newbatdeal_pre[j]['topics'][2]))
			keeper = web3.toChecksumAddress(web3.toHex(newbatdeal_pre[j]['topics'][1][12:]))
			act = {'action':'deal', 'liquidationid':liquidation_id, 'keeper':keeper, 'blockNumber':newbatdeal_pre[j]['blockNumber']}
			ii = lid_to_id_dict[liquidation_id]
			vaults[ii].deals.append(act)

		# shift
		# this is really to account how instadapp was doing their migration tool
		# _i think_ they created new vaults each time there was enough SAI in the migration contract
		# then they would shift the vaults with an other vault that the user wanted
		# I'm not 100% sure. Let's see if this works
		# here are some hashes to look at in case it doesn't
		# https://oasis.app/borrow/1238
		# https://oasis.app/borrow/575
		# https://etherscan.io/tx/0x0ca52b8e154b06c8c432560cb9dbba23066329218a151b084be1617f2d14c81c
		# https://etherscan.io/loans/maker/cdp/147301?p=2
		# https://etherscan.io/tx/0x876b27ca03824c09ecc24e43e9c1f7cbaf7b558c7f44400fad1f9a8617bd44fc#eventlog
		for j in range(0, len(newshift_pre)):
			vault_to_close = web3.toInt(newshift_pre[j]['topics'][2])
			vault_to_shift_with = web3.toInt(newshift_pre[j]['topics'][3])
			print("found a new shift {0} into {1}".format(vault_to_close, vault_to_shift_with))
			for k in vaults[vault_to_close].actions:
				vaults[vault_to_shift_with].actions.append(k)
			vaults[vault_to_close].actions = []









		# removing losing tends
		for i in vaults:
			sorted_tends = sorted(i.tends, key=lambda x: x['liquidationid'])
			uniq_ids = []
			for j in sorted_tends:
				if(j['liquidationid'] not in uniq_ids):
					uniq_ids.append(j['liquidationid'])

			winning_tends = []
			for j in uniq_ids:
				current_winning_bid = 0
				winning_index = 0
				for k in range(0, len(sorted_tends)):
					if(j == sorted_tends[k]['liquidationid']):
						if(sorted_tends[k]['bid'] > current_winning_bid):
							current_winning_bid = sorted_tends[k]['bid']
							winning_index = k
				winning_tends.append(sorted_tends[winning_index])

			i.winning_tends = winning_tends

		# removing losing dents
		for i in vaults:
			sorted_dents = sorted(i.dents, key=lambda x: x['liquidationid'])
			uniq_ids = []
			for j in sorted_dents:
				if(j['liquidationid'] not in uniq_ids):
					uniq_ids.append(j['liquidationid'])

			winning_dents = []
			for j in uniq_ids:
				current_winning_lot = 99999999999999999999999999999999999999999999999999999
				winning_index = 0
				for k in range(0, len(sorted_dents)):
					if(j == sorted_dents[k]['liquidationid']):
						if(sorted_dents[k]['lot'] < current_winning_lot):
							current_winning_lot = sorted_dents[k]['lot']
							winning_index = k
				winning_dents.append(sorted_dents[winning_index])

			i.winning_dents = winning_dents

	


	#need to sort vault actions by bn
	for i in vaults:
		sorted_vault_actions = sorted(i.actions, key = lambda x: x['blockNumber'])
		i.actions = sorted_vault_actions
		sorted_vault_kicks = sorted(i.kicks, key = lambda x: x['blockNumber'])
		i.kicks = sorted_vault_kicks
		sorted_vault_deals = sorted(i.deals, key = lambda x: x['blockNumber'])
		i.deals = sorted_vault_deals

	filehandler = open(VAULT_OBJ_FILENAME, 'wb')
	pickle.dump(vaults, filehandler)
	filehandler2 = open(URN_TO_ID_DICT_FILENAME, 'wb')
	pickle.dump(urn_to_id_dict, filehandler2)
	filehandler3 = open(LID_TO_ID_DICT_FILENAME, 'wb')
	pickle.dump(lid_to_id_dict, filehandler3)	

def get_eth_prices():
	weth_prices = []
	bat_prices = []
	for i in range(FIRST_BLOCK, LAST_BLOCK, STEP_SIZE):
		newpoke = []
		print("getting ids for block {0}".format(i))

		newwethlogvalue_filter = web3.eth.filter({"address":osmweth0x, "fromBlock":i, "toBlock":i + STEP_SIZE - 1, "topics":LOGVALUE_TOPIC})
		newwethlogvalue_pre = newwethlogvalue_filter.get_all_entries()
		newbatlogvalue_filter = web3.eth.filter({"address":osmbat0x, "fromBlock":i, "toBlock":i + STEP_SIZE - 1, "topics":LOGVALUE_TOPIC})
		newbatlogvalue_pre = newbatlogvalue_filter.get_all_entries()

		for j in range(0, len(newwethlogvalue_pre)):
			price = {'value':web3.toInt(hexstr=newwethlogvalue_pre[j]['data']) / ETH_SCALE, 'blockNumber':newwethlogvalue_pre[j]['blockNumber']}
			weth_prices.append(price)
			print(price)
		for j in range(0, len(newbatlogvalue_pre)):
			price = {'value':web3.toInt(hexstr=newbatlogvalue_pre[j]['data']) / ETH_SCALE, 'blockNumber':newbatlogvalue_pre[j]['blockNumber']}
			bat_prices.append(price)
			print(price)

	
	sorted_weth_prices = sorted(weth_prices, key=lambda x: x['blockNumber'])
	weth_prices = sorted_weth_prices
	sorted_bat_prices = sorted(bat_prices, key=lambda x: x['blockNumber'])
	bat_prices = sorted_bat_prices

	filehandler1 = open(WETH_OSM_PRICES_FILENAME, 'wb')
	pickle.dump(weth_prices, filehandler1)
	filehandler2 = open(BAT_OSM_PRICES_FILENAME, 'wb')
	pickle.dump(bat_prices, filehandler2)

def get_pickle(fn):
	try:
		with (open(fn, "rb")) as openfile:
			while True:
				try:
					return pickle.load(openfile)
				except EOFError:
					break
	except FileNotFoundError:
		print("\nFile " + CDP_OBJ_FILENAME + " does not exist. Run 'update_spells' command.\n")
		sys.exit(-1)

def reduce_vaults():
	vaults = get_pickle(VAULT_OBJ_FILENAME)
	new_vaults = []

	for i in vaults:
		if(len(i.kicks) != 0):
			new_vaults.append(i)
	filehandler1 = open(LIQUIDATED_VAULTS_FILENAME, 'wb')
	pickle.dump(new_vaults, filehandler1)
	
	for i in new_vaults:
		i.display_vault()


def find_liquidation_purchase_price():
	vaults = get_pickle(LIQUIDATED_VAULTS_FILENAME)

	# init these because I didn't earlier
	for i in vaults:
		i.debt = 0
		i.max_debt = 0
	# calculating the max debt for ordering them
	for i in vaults:
		for k in i.actions:
			if(k['action'] == 'draw'):
				i.debt += k['amount']
			if(k['action'] == 'wipe'):
				i.debt -= k['amount']
			if(i.max_debt < i.debt):
				i.max_debt = i.debt
	
	for i in vaults:
		for j in i.deals:
			current_lid = j['liquidationid']
			tend_lot, tend_bid = find_auction_price(current_lid, i.tends)
			dent_lot, dent_bid = find_auction_price(current_lid, i.dents)
			deal_price = 0
			deal_lot = 0
			deal_bid = 0
			if(dent_lot == -1):
				deal_lot = tend_lot
				deal_bid = tend_bid
				deal_price = deal_bid / deal_lot
			else:
				deal_lot = dent_lot
				deal_bid = dent_bid
				deal_price = deal_bid / deal_lot
			j['deallot'] = deal_lot
			j['dealbid'] = deal_bid
			j['dealprice'] = deal_price
			p_at_deal = find_cc_p(j['blockNumber'], i.ilk_type)
			
			j['discount'] = (1 - (j['dealprice'] / p_at_deal)) * 100
			kicked_on = find_kicked_on(current_lid, i.kicks)
			j['kickedon'] = kicked_on
			print(j)
			
	filehandler1 = open(LIQUIDATED_DEALS_FILENAME, 'wb')
	pickle.dump(vaults, filehandler1)


def find_kicked_on(lid, kicks):
	kk = 0
	for f in kicks:
		if(f['liquidationid'] == lid):
			kk = f['blockNumber']
			break
	return kk

	


def find_cc_p(bn, ilk):
	p = -1
	if(ilk == 'ETHA'):
		ts = web3.eth.getBlock(bn)['timestamp']
		cc_built_url = cc_eth_root_url + '&toTs=' + str(ts + 3600) + cc_key
		pjson = requests.get(cc_built_url)
		pclose = pjson.json()['Data']['Data'][1]['close']
		popen = pjson.json()['Data']['Data'][1]['open']
		p = (pclose + popen) / 2
	elif(ilk == 'BATA'):
		ts = web3.eth.getBlock(bn)['timestamp']
		cc_built_url = cc_bat_root_url + '&toTs=' + str(ts + 3600) + cc_key
		pjson = requests.get(cc_built_url)
		pclose = pjson.json()['Data']['Data'][1]['close']
		popen = pjson.json()['Data']['Data'][1]['open']
		p = (pclose + popen) / 2
	return p


# def find_osm_p(bn, ilk):
# 	p = -1
# 	ethp = get_pickle(WETH_OSM_PRICES_FILENAME)
# 	#ethp = sorted(ethp, key=lambda x: x['blockNumber'])
# 	batp = get_pickle(BAT_OSM_PRICES_FILENAME)
	
	
# 	if(ilk == 'ETHA'):
# 		for i in ethp:
# 			if(i['blockNumber'] >= bn):
# 				p = i['value']
# 				break
# 	elif(ilk == 'BATA'):
# 		for i in batp:
# 			if(i['blockNumber'] >= bn):
# 				p = i['value']
# 				break
# 	return p

	




def find_auction_price(lid, tends):
	ll = -1
	bb = -1
	for f in tends:
		if(f['liquidationid'] == lid):
			bb = f['bid'] / ETH44_SCALE
			ll = f['lot'] / ETH_SCALE
			break
	return ll, bb

def output_csvs():
	vaults = get_pickle(LIQUIDATED_DEALS_FILENAME)
	weth_prices = get_pickle(WETH_OSM_PRICES_FILENAME)
	bat_prices = get_pickle(BAT_OSM_PRICES_FILENAME)
	
	list_vaults = []
	for i in vaults:
		templ = [i.vaultid, i.block_created, i.ilk_type, i.max_debt / ETH_SCALE]
		list_vaults.append(templ)
	with open(VAULT_INIT_FILENAME, 'w') as myfile1:
		wr = csv.writer(myfile1)
		wr.writerow(["vaultid", "blockcreated", "ilktype", "maxdebt"],)
		for i in range(0, len(list_vaults)):
			wr.writerow([list_vaults[i][0], list_vaults[i][1], list_vaults[i][2], list_vaults[i][3],])

	list_vault_interactions = []
	for i in vaults:
		for k in i.actions:
			ff = float(k['amount'] / ETH_SCALE)
			list_vault_interactions.append([k['blockNumber'], i.vaultid, k['action'], "{0:.8f}".format(ff)])
	sorted_interactions = sorted(list_vault_interactions, key=lambda x: x[0])
	with open(VAULT_INTERACTIONS_FILENAME, 'w') as myfile2:
		wr = csv.writer(myfile2)
		wr.writerow(["block", "vaultid", "action", "amount"],)
		for i in range(0, len(sorted_interactions)):
			wr.writerow([sorted_interactions[i][0], sorted_interactions[i][1], sorted_interactions[i][2], sorted_interactions[i][3],])

	list_deals = []
	for i in vaults:
		for k in i.deals:
			list_deals.append([k['liquidationid'], i.vaultid, k['kickedon'], k['blockNumber'], k['keeper'], k['deallot'], k['dealbid'], k['discount'],])
	sorted_deals = sorted(list_deals, key=lambda x: x[2])
	with open(DEALS_FILENAME, 'w') as myfile3:
		wr = csv.writer(myfile3)
		wr.writerow(["liquidationid", "vaultid", "kickedon", "dealedon", "keeper", "deallot", "dealbid", "discount"],)
		for i in range(0, len(sorted_deals)):
			wr.writerow([sorted_deals[i][0], sorted_deals[i][1], sorted_deals[i][2], sorted_deals[i][3], sorted_deals[i][4], sorted_deals[i][5], sorted_deals[i][6], sorted_deals[i][7],])

	list_eth_prices = []
	for i in weth_prices:
		temple = [i['blockNumber'], i['value']]
		list_eth_prices.append(temple)
	with open (ETH_PRICE_CSV, 'w') as myfile4:
		wr = csv.writer(myfile4)
		wr.writerow(["blockNumber", "price"])
		for i in range(0, len(list_eth_prices)):
			wr.writerow([list_eth_prices[i][0], list_eth_prices[i][1],])

	list_bat_prices = []
	for i in bat_prices:
		temple = [i['blockNumber'], i['value']]
		list_bat_prices.append(temple)
	with open (BAT_PRICE_CSV, 'w') as myfile5:
		wr = csv.writer(myfile5)
		wr.writerow(["blockNumber", "price"])
		for i in range(0, len(list_bat_prices)):
			wr.writerow([list_bat_prices[i][0], list_bat_prices[i][1],])

def print_keepers():
	vaults = get_pickle(VAULT_OBJ_FILENAME)
	keepers = []
	for i in vaults:
		for k in i.kicks:
			if(k['keeper'] not in keepers):
				keepers.append(k['keeper'])
		for k in i.tends:
			if(k['keeper'] not in keepers):
				keepers.append(k['keeper'])
		for k in i.dents:
			if(k['keeper'] not in keepers):
				keepers.append(k['keeper'])
		for k in i.deals:
			if(k['keeper'] not in keepers):
				keepers.append(k['keeper'])
	print(keepers)

	# running_debt = 0
	# running_collateral = 0

	# for i in vaults:
	# 	if (i.vaultid == 575):
	# 		for k in i.actions:
	# 			if(k['action'] == 'draw'):
	# 				running_debt += k['amount']
	# 			if(k['action'] == 'wipe'):
	# 				running_debt -= k['amount']
	# 			if(k['action'] == 'lock'):
	# 				running_collateral += k['amount']
	# 			if(k['action'] == 'free'):
	# 				running_collateral -= k['amount']
	# print(running_debt)
	# print(running_collateral)

	


def main():
	# arg parsing
	parser = argparse.ArgumentParser(description='gets the data for the liquidation plot')
	parser.add_argument('--getvaultid', action='store_true', dest='getvaultid', help='gets all the cdp ids and their interactions')

	parser.add_argument('--printvaultid', action='store_true', dest='printvaultid', help='prints all the cdp ids their interactions')
	#parser.add_argument('--getmoney', action='store_true', dest='getmoney', help='gets all the money puts in giant .csv and .obj')
	parser.add_argument('--getprices', action='store_true', dest='getprices', help='gets the price feed prices')
	#parser.add_argument('--findpopular', action='store_true', dest='findpopular', help='gets the most used address')
	#parser.add_argument('--outputcdpcsv', action='store_true', dest='outputcdpcsv', help='puts the cdp actions from --getcdpid into a giant csv')
	#parser.add_argument('--outputtapcsv', action='store_true', dest='outputtapcsv', help='puts all the liquidation transfers into a special csv')
	#parser.add_argument('--outputpethratiocsv', action='store_true', dest='outputpethratiocsv', help='gets the peth ratio and puts in csv')
	parser.add_argument('--reducevaults', action='store_true', dest='reducevaults', help='removes everything except for the liquidated')
	parser.add_argument('--findliquidationpurchaseprice', action='store_true', dest='findliquidationpurchaseprice', help='find the amount the keeper paid, the amount bought, and the amount given back')
	parser.add_argument('--outputcsvs', action='store_true', dest='outputcsvs', help='outputs all the csvs')
	parser.add_argument('--printkeepers', action='store_true', dest='printkeepers', help='quick look at all the different keepers')
	#parser.add_argument('--daemon', action='store_true', dest='daemon', help='runs the daemon')
	global argss
	argss = parser.parse_args()

	if argss.getvaultid:
		get_vault_id()
		sys.exit(0)
	if argss.printvaultid:
		vault_idds = get_filled_vault_id()
		for s in vault_idds:
			s.display_vault()
		sys.exit(0)
	# if argss.getmoney:
	# 	get_money()
	# 	sys.exit(0)
	if argss.getprices:
		get_eth_prices()
		sys.exit(0)
	# if argss.findpopular:
	# 	find_popular_addresses()
	# 	sys.exit(0)
	# if argss.outputcdpcsv:
	# 	output_cdp_csv()
	# 	sys.exit(0)
	# if argss.outputtapcsv:
	# 	output_tap_csv()
	# 	sys.exit(0)
	# if argss.outputpethratiocsv:
	# 	output_peth_ratio_csv()
	# 	sys.exit(0)
	if argss.reducevaults:
		reduce_vaults()
		sys.exit(0)
	if argss.findliquidationpurchaseprice:
		find_liquidation_purchase_price()
		sys.exit(0)
	if argss.outputcsvs:
		output_csvs()
		sys.exit(0)
	if argss.printkeepers:
		print_keepers()
		sys.exit(0)


	print("Run 'getflip.py --help'")
if __name__ == "__main__":
	main()





