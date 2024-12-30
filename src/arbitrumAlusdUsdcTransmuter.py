def calculateArbitrumAlusdUsdcStats (allAPRs, tvls, alUSDprice):
#    import requests
 #   import pandas as pd


   # from collectVaultAPRs import vaultAPRs
    #from collectTVLs import allTVLs
    from getTokenBalance import getBalance #(network, tokenAddress, holderAddress)
    from getNetBalance import calculateNetBalance #(alassetAmount, underlyingAmount)
    from getTokenPrice import getTokenPrice #(coingeckoString)

    #calculate ethereum weth
    weighted = []
    values = []

    for vault in allAPRs['arbitrum']:

        if vault[-4:] == 'USDC':
            print('apr')
            print(vault, ' ', allAPRs['arbitrum'][vault])
            print('tvl')
            print(vault, ' ', tvls['arbitrum'][vault])

            weighted.append((allAPRs['arbitrum'][vault] * 0.9) * tvls['arbitrum'][vault])
            values.append(tvls['arbitrum'][vault])

    print('weighted values')
    print(weighted)
    print('tvl values')
    print(values)

    sumWeights = sum(weighted)
    sumValues = sum(values)

    weightedAverage = sumWeights / sumValues

    print('Weighted Average')
    print(weightedAverage)
    print('TVL')
    print(sumValues)

    alUSDbalance = getBalance ('arbitrum', '0xCB8FA9a76b8e203D8C3797bF438d8FB81Ea3326A', '0xe7ec71B894583E9C1b07873fA86A7e81f3940eA8') / 1e18

    print('alUSD balance')
    print(alUSDbalance)

    usdcBalance = getBalance ('arbitrum', '0xaf88d065e77c8cC2239327C5EDb3A432268e5831', '0x00E33722ba54545667E76a18CE9D544130eEAbcC') / 1e6

    print('USDC balance')
    print(usdcBalance)

    netBalance = calculateNetBalance (alUSDbalance, usdcBalance)

    print('net aleth balance')
    print(netBalance)

    timeToTransmute = netBalance / (weightedAverage * sumValues)

    print('Time to transmute')
    print(timeToTransmute)

    #alETHpricePiece = getTokenPrice ('alchemix-eth')
    #wETHpricePiece = getTokenPrice ('weth')

    #alETHprice = alETHpricePiece / wETHpricePiece

    print('alUSD price')
    print(alUSDprice)

    projectedRate = ((1/alUSDprice)-1) * (100/timeToTransmute)

    print('Projected Rate')
    print(projectedRate)

    returnData = {
        'timeToTransmute' : timeToTransmute,
        'projectedRate' : projectedRate
    }
    return returnData

