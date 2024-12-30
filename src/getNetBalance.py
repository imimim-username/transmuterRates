def calculateNetBalance (alassetAmount, underlyingAmount):
#if net balance is negative, it returns 0

    netAmount = alassetAmount - underlyingAmount

    if netAmount < 0:
        return 0.01
    else:
        return netAmount