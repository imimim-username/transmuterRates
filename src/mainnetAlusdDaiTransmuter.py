def calculateMainnetAlusdDaiStats (allAPRs, tvls, alUSDprice):
#    import requests
 #   import pandas as pd


   # from collectVaultAPRs import vaultAPRs
    #from collectTVLs import allTVLs
    from getTokenBalance import getBalance #(network, tokenAddress, holderAddress)
    from getNetBalance import calculateNetBalance #(alassetAmount, underlyingAmount)
    from getTokenPrice import getTokenPrice #(coingeckoString)

    #calculate ethereum usdc
    weighted = []
    values = []

    for vault in allAPRs['mainnet']:

        if vault[-3:] == 'DAI':
            print('apr')
            print(vault, ' ', allAPRs['mainnet'][vault])
            print('tvl')
            print(vault, ' ', tvls['ethereum'][vault])

            weighted.append((allAPRs['mainnet'][vault] * 0.9) * tvls['ethereum'][vault])
            values.append(tvls['ethereum'][vault])

    print('weighted values')
    print(weighted)
    print('sum values')
    print(values)

    sumWeights = sum(weighted)
    sumValues = sum(values)

    weightedAverage = sumWeights / sumValues

    print('Weighted Average')
    print(weightedAverage)
    print('TVL')
    print(sumValues)

    alUSDbalance = getBalance ('mainnet', '0xBC6DA0FE9aD5f3b0d58160288917AA56653660E9', '0xA840C73a004026710471F727252a9a2800a5197F') / 1e18

    print('alUSD balance')
    print(alUSDbalance)

    daiBalance = getBalance ('mainnet', '0x6B175474E89094C44Da98b954EedeAC495271d0F', '0x1EEd2DbeB9fc23Ab483F447F38F289cA15f79Bac') / 1e18

    print('Dai balance')
    print(daiBalance)

    netBalance = calculateNetBalance (alUSDbalance, daiBalance)

    print('net alUSD balance')
    print(netBalance)

    timeToTransmute = netBalance / (weightedAverage * sumValues)

    print('Time to transmute')
    print(timeToTransmute)

    #alUSDpricePiece = getTokenPrice ('alchemix-usd')
    #wETHpricePiece = getTokenPrice ('weth')

    #alETHprice = alETHpricePiece / wETHpricePiece
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