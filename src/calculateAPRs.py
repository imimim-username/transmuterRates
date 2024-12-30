#import requests
#import pandas as pd
#from datetime import datetime



from collectVaultAPRs import vaultAPRs
from collectTVLs import allTVLs, subgraphTVLs
# allTVLs gets TVL from dune query, which is infrequently updated. subgraphTVLs gets TVL from the subgraph, which is up to date

from getTokenPrice import getTokenPrice #(coingeckoString)
#get token prices from coingecko

#from getTokenBalance import getBalance #(network, tokenAddress, holderAddress)
#from getNetBalance import calculateNetBalance #(alassetAmount, underlyingAmount)

from mainnetAlethTransmuter import calculateMainnetAlethStats #(allAPRs, tvls, alETHpricePiece, wETHpricePiece)
from mainnetAlusdUsdcTransmuter import calculateMainnetAlusdUsdcStats #(allAPRs, tvls, alUSDprice)
from mainnetAlusdUsdtTransmuter import calculateMainnetAlusdUsdtStats #(allAPRs, tvls, alUSDprice)
from mainnetAlusdDaiTransmuter import calculateMainnetAlusdDaiStats #(allAPRs, tvls, alUSDprice)
from mainnetAlusdFraxTransmuter import calculateMainnetAlusdFraxStats #(allAPRs, tvls, alUSDprice)

from optimismAlethTransmuter import calculateOptimismAlethStats #(allAPRs, tvls, alETHpricePiece, wETHpricePiece)
from optimismAlusdUsdcTransmuter import calculateOptimismAlusdUsdcStats #(allAPRs, tvls, alUSDprice)
from optimismAlusdUsdtTransmuter import calculateOptimismAlusdUsdtStats #(allAPRs, tvls, alUSDprice)
from optimismAlusdDaiTransmuter import calculateOptimismAlusdDaiStats #(allAPRs, tvls, alUSDprice)

from arbitrumAlethTransmuter import calculateArbitrumAlethStats #(allAPRs, tvls, alETHpricePiece, wETHpricePiece)
from arbitrumAlusdUsdcTransmuter import calculateArbitrumAlusdUsdcStats #(allAPRs, tvls, alUSDprice)

from pinata import pinataHash, pinataPin, pinataDelete, pinataPinFile


allAPRs = vaultAPRs()

print('Here are the most recent APRs')
print(allAPRs)

tvls = subgraphTVLs()

print('Here are the TVLs')
print(tvls)

'''print('Evaluating mainnet tokens for a match')
for token in allAPRs['mainnet']:

    print(token)
    if token in tvls['ethereum']:
        print('there is a match!')
        print('TVL')
        print(tvls['ethereum'][token])
        print('APR')
        print(allAPRs['mainnet'][token])
    else:
        print(token, 'does not have a match in TVL data')'''

alUSDpricePiece = getTokenPrice ('alchemix-usd')
alETHpricePiece = getTokenPrice ('alchemix-eth')
wETHpricePiece = getTokenPrice ('weth')

mainnetAleth = calculateMainnetAlethStats (allAPRs, tvls, alETHpricePiece, wETHpricePiece)
mainnetAlusdUsdc = calculateMainnetAlusdUsdcStats (allAPRs, tvls, alUSDpricePiece)
mainnetAlusdUsdt = calculateMainnetAlusdUsdtStats (allAPRs, tvls, alUSDpricePiece)
mainnetAlusdDai = calculateMainnetAlusdDaiStats (allAPRs, tvls, alUSDpricePiece)
mainnetAlusdFrax = calculateMainnetAlusdFraxStats (allAPRs, tvls, alUSDpricePiece)

optimismAleth = calculateOptimismAlethStats (allAPRs, tvls, alETHpricePiece, wETHpricePiece)
optimismAlusdUsdc = calculateOptimismAlusdUsdcStats (allAPRs, tvls, alUSDpricePiece)
optimismAlusdUsdt = calculateOptimismAlusdUsdtStats (allAPRs, tvls, alUSDpricePiece)
optimismAlusdDai = calculateOptimismAlusdDaiStats (allAPRs, tvls, alUSDpricePiece)

arbitrumAleth = calculateArbitrumAlethStats (allAPRs, tvls, alETHpricePiece, wETHpricePiece)
arbitrumAlusdUsdc = calculateArbitrumAlusdUsdcStats (allAPRs, tvls, alUSDpricePiece)

print('---------------------------------')
print('Mainnet alETH transmuter stats')
print(mainnetAleth)
print('---------------------------------')

print('---------------------------------')
print('Mainnet alUSD USDC transmuter stats')
print(mainnetAlusdUsdc)
print('---------------------------------')

print('---------------------------------')
print('Mainnet alUSD USDT transmuter stats')
print(mainnetAlusdUsdt)
print('---------------------------------')

print('---------------------------------')
print('Mainnet alUSD Dai transmuter stats')
print(mainnetAlusdDai)
print('---------------------------------')

print('---------------------------------')
print('Mainnet alUSD FRAX transmuter stats')
print(mainnetAlusdFrax)
print('---------------------------------')

##################################################
print('---------------------------------')
print('Optimism alETH transmuter stats')
print(optimismAleth)
print('---------------------------------')

print('---------------------------------')
print('Optimism alUSD USDC transmuter stats')
print(optimismAlusdUsdc)
print('---------------------------------')

print('---------------------------------')
print('Optimism alUSD USDT transmuter stats')
print(optimismAlusdUsdt)
print('---------------------------------')

print('---------------------------------')
print('Optimism alUSD Dai transmuter stats')
print(optimismAlusdDai)
print('---------------------------------')

#####################################################
print('---------------------------------')
print('Arbitrum alETH transmuter stats')
print(arbitrumAleth)
print('---------------------------------')

print('---------------------------------')
print('Arbitrum alUSD USDC transmuter stats')
print(arbitrumAlusdUsdc)
print('---------------------------------')


transmuterRates = {}

transmuterRates['mainnet'] = {}
transmuterRates['mainnet']['weth'] = mainnetAleth
transmuterRates['mainnet']['usdc'] = mainnetAlusdUsdc
transmuterRates['mainnet']['usdt'] = mainnetAlusdUsdt
transmuterRates['mainnet']['dai'] = mainnetAlusdDai
transmuterRates['mainnet']['frax'] = mainnetAlusdFrax

transmuterRates['optimism'] = {}
transmuterRates['optimism']['weth'] = optimismAleth
transmuterRates['optimism']['usdc'] = optimismAlusdUsdc
transmuterRates['optimism']['usdt'] = optimismAlusdUsdt
transmuterRates['optimism']['dai'] = optimismAlusdDai

transmuterRates['arbitrum'] = {}
transmuterRates['arbitrum']['weth'] = arbitrumAleth
transmuterRates['arbitrum']['usdc'] = arbitrumAlusdUsdc

print(transmuterRates)

fileName = 'transmuterRates.json'
fileHash = pinataHash(fileName)
pinataDelete(fileHash)
pinataPin(fileName, transmuterRates)
