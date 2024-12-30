def getBalance (network, tokenAddress, holderAddress):
# for a given network, gets token balance of a token for a holder using token address and holder address.
# returns integer value in full decimals.

    import requests
    import json

    headers = {
        "Content-Type": "application/json"
    }
    #api call request headers

    keyString = '/home/imimim/alchemix/user_debt/alchemy_api_key_mainnet.txt'

    apiKey = open(keyString, "r")
    # get the alchemy api key for network

    keyValue = apiKey.read()
    # read the key from the file

    apiKey.close()
    # close the opened file

    print(network)
    if network == 'mainnet':
        alchemyBase = 'https://eth-mainnet.g.alchemy.com/v2/'
    elif network == 'optimism':
        alchemyBase = 'https://opt-mainnet.g.alchemy.com/v2/'
    elif network == 'arbitrum':
        alchemyBase = 'https://arb-mainnet.g.alchemy.com/v2/'
    else:
        print('Oops. No bullets (network)')
        return 0

    apiString = alchemyBase + keyValue

    dataStr = '0x70a08231000000000000000000000000' + holderAddress[2:]

    requestPayload = {
        "id": 1,
        "jsonrpc": "2.0",
        "method": "eth_call",
        "params": [
            {
                "to": tokenAddress,
                "data": dataStr
            },
            "latest"
        ]
    }

    print("Looking up token balance")

    apiPost = requests.post(apiString, headers=headers, data=json.dumps(requestPayload))
    apiPost = apiPost.json()

    return int(apiPost['result'], 16)

#balance = getBalance('mainnet', '0x0100546F2cD4C9D97f798fFC9755E47865FF7Ee6', '0x03323143a5f0D0679026C2a9fB6b0391e4D64811')

#print(balance)