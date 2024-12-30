def getTokenPrice (coingeckoString):
    import requests
    from datetime import datetime

    import time
    #to pause execution because of rate limit

    pauseInterval = 30

    print('Pausing for', pauseInterval, 'seconds...')
    time.sleep(pauseInterval)  # Pauses the execution for pauseInterval seconds

    #Get today's date
    today = datetime.today()

    # Format the date as "d-m-yyyy"
    formatted_date = today.strftime('%-d-%-m-%Y')

    coingeckAPI = 'https://api.coingecko.com/api/v3/coins/' + coingeckoString + '/history?date=' + formatted_date

    headers = {
        "Content-Type": "application/json"
    }
    #api call request headers

    tokenInfo = requests.get(coingeckAPI, headers=headers)
    tokenInfo = tokenInfo.json()

    print(coingeckoString, 'price')
    print(tokenInfo['market_data']['current_price']['usd'])

    return float(tokenInfo['market_data']['current_price']['usd'])

#price = getTokenPrice('alchemix-eth')
#print(price)