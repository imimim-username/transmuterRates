def calculateOptimismAlusdUsdcStats (allAPRs, tvls, alUSDprice):
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

        if vault[-4:] == 'USDC':
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

    alUSDbalance = getBalance ('optimism', '0xCB8FA9a76b8e203D8C3797bF438d8FB81Ea3326A', '0xA7ea9ef9E2b5e15971040230F5d6b75C68Aab723') / 1e18

    print('alUSD balance')
    print(alUSDbalance)

    usdcBalance = getBalance ('optimism', '0x7F5c764cBc14f9669B88837ca1490cCa17c31607', '0xe99a9A717c60F9639B235ede422c27d60FBEB3b9') / 1e6

    print('USDC balance')
    print(usdcBalance)

    netBalance = calculateNetBalance (alUSDbalance, usdcBalance)

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

