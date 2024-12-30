def calculateArbitrumAlethStats (allAPRs, tvls, alETHpricePiece, wETHpricePiece):
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

        #if vault[-3:] == 'ETH':
        if vault == 'farmdWETHV3' or vault[-3:] == 'ETH':
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

    alETHbalance = getBalance ('arbitrum', '0x17573150d67d820542EFb24210371545a4868B03', '0x1EB7D78d7f6D73e5de67Fa62Fd8b55c54Aa9c0D4') / 1e18

    print('alETH balance')
    print(alETHbalance)

    wethBalance = getBalance ('arbitrum', '0x82aF49447D8a07e3bd95BD0d56f35241523fBab1', '0xECAd08EE07f1AA87f3E080997eBa6d02d28bb9D2') / 1e18

    print('weth balance')
    print(wethBalance)

    netBalance = calculateNetBalance (alETHbalance, wethBalance)

    print('net aleth balance')
    print(netBalance)

    timeToTransmute = netBalance / (weightedAverage * sumValues)

    print('Time to transmute')
    print(timeToTransmute)

    #alETHpricePiece = getTokenPrice ('alchemix-eth')
    #wETHpricePiece = getTokenPrice ('weth')

    alETHprice = alETHpricePiece / wETHpricePiece

    print('alETH price')
    print(alETHprice)

    projectedRate = ((1/alETHprice)-1) * (100/timeToTransmute)

    print('Projected Rate')
    print(projectedRate)

    returnData = {
        'timeToTransmute' : timeToTransmute,
        'projectedRate' : projectedRate
    }
    return returnData

