def calculateOptimismAlusdUsdtStats (allAPRs, tvls, alUSDprice):
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

    for vault in allAPRs['optimism']:

        if vault[-4:] == 'USDT':
            print('apr')
            print(vault, ' ', allAPRs['optimism'][vault])
            print('tvl')
            print(vault, ' ', tvls['optimism'][vault])

            weighted.append((allAPRs['optimism'][vault] * 0.9) * tvls['optimism'][vault])
            values.append(tvls['optimism'][vault])

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

    alUSDbalance = getBalance ('optimism', '0xCB8FA9a76b8e203D8C3797bF438d8FB81Ea3326A', '0x4e7d2115E4FeEcD802c96E77B8e03D98104415fa') / 1e18

    print('alUSD balance')
    print(alUSDbalance)

    usdtBalance = getBalance ('optimism', '0x94b008aA00579c1307B0EF2c499aD98a8ce58e58', '0xe99a9A717c60F9639B235ede422c27d60FBEB3b9') / 1e6

    print('USDT balance')
    print(usdtBalance)

    netBalance = calculateNetBalance (alUSDbalance, usdtBalance)

    print('net alUSD balance')
    print(netBalance)

    timeToTransmute = netBalance / (weightedAverage * sumValues)

    print('Time to transmute')
    print(timeToTransmute)

    #alUSDpricePiece = getTokenPrice ('alchemix-usd')
    #wETHpricePiece = getTokenPrice ('weth')

    #alUSDprice = alUSDpricePiece

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

