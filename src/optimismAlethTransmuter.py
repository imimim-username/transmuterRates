def calculateOptimismAlethStats (allAPRs, tvls, alETHpricePiece, wETHpricePiece):
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

        if vault[-3:] == 'ETH':
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

    alETHbalance = getBalance ('optimism', '0x3E29D3A9316dAB217754d13b28646B76607c5f04', '0xb7C4250f83289ff3Ea9f21f01AAd0b02fb19491a') / 1e18

    print('alETH balance')
    print(alETHbalance)

    wethBalance = getBalance ('optimism', '0x4200000000000000000000000000000000000006', '0x7f50923EE8E2BC3596a63998495baf2948a28f68') / 1e18

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

