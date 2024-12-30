def calculateMainnetAlusdUsdcStats (allAPRs, tvls, alUSDprice):
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

        if vault[-4:] == 'USDC':
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

    alUSDbalance = getBalance ('mainnet', '0xBC6DA0FE9aD5f3b0d58160288917AA56653660E9', '0x49930AD9eBbbc0EB120CCF1a318c3aE5Bb24Df55') / 1e18

    print('alUSD balance')
    print(alUSDbalance)

    usdcBalance = getBalance ('mainnet', '0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48', '0x1EEd2DbeB9fc23Ab483F447F38F289cA15f79Bac') / 1e6

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