def calculateMainnetAlethStats (allAPRs, tvls, alETHpricePiece, wETHpricePiece):
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

    for vault in allAPRs['mainnet']:

        if vault[-3:] == 'ETH':
            print('apr')
            print(vault, ' ', allAPRs['mainnet'][vault])
            print('tvl')
            print(vault, ' ', tvls['ethereum'][vault])

            weighted.append((allAPRs['mainnet'][vault] * 0.9) * tvls['ethereum'][vault])
            values.append(tvls['ethereum'][vault])

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

    alETHbalance = getBalance ('mainnet', '0x0100546F2cD4C9D97f798fFC9755E47865FF7Ee6', '0x03323143a5f0D0679026C2a9fB6b0391e4D64811') / 1e18

    print('alETH balance')
    print(alETHbalance)

    wethBalance = getBalance ('mainnet', '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2', '0xbc2FB245594a68c927C930FBE2d00680A8C90B9e') / 1e18

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

