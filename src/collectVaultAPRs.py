def vaultAPRs ():
    import pandas as pd

    #import pprint
    #for prettifying output

    path = '/home/imimim/alchemix/APRs/'
    mainnetFile = 'mainnetDailyAprs.csv'
    optimismFile = 'optimismDailyAprs.csv'
    arbitrumFile = 'arbitrumDailyAprs.csv'

    mainnetDF = pd.read_csv(path+mainnetFile)
    optimismDF = pd.read_csv(path+optimismFile)
    arbitrumDF = pd.read_csv(path+arbitrumFile)

    # Convert the Unix timestamps to datetime
    mainnetDF['timestamp'] = pd.to_datetime(mainnetDF['timestamp'], unit='s')
    optimismDF['timestamp'] = pd.to_datetime(optimismDF['timestamp'], unit='s')
    arbitrumDF['timestamp'] = pd.to_datetime(arbitrumDF['timestamp'], unit='s')

    # Sort by timestamp in descending order
    mainnetDF = mainnetDF.sort_values(by='timestamp', ascending=False)
    optimismDF = optimismDF.sort_values(by='timestamp', ascending=False)
    arbitrumDF = arbitrumDF.sort_values(by='timestamp', ascending=False)

    # Group by 'name' and get the first row (most recent) for each group
    mainnetMostRecent = mainnetDF.groupby('name').first()
    optimismMostRecent = optimismDF.groupby('name').first()
    arbitrumMostRecent = arbitrumDF.groupby('name').first()

    # Ensure all 'apr' values are numeric, replacing non-numeric with 0
    mainnetMostRecent['apr'] = pd.to_numeric(mainnetMostRecent['apr'], errors='coerce').fillna(0)
    optimismMostRecent['apr'] = pd.to_numeric(optimismMostRecent['apr'], errors='coerce').fillna(0)
    arbitrumMostRecent['apr'] = pd.to_numeric(arbitrumMostRecent['apr'], errors='coerce').fillna(0)

    print('Most recent mainnet things')
    print(mainnetMostRecent)
    print('-------------')
    print('Most recent optimism things')
    print(optimismMostRecent)
    print('-------------')
    print('Most recent arbitrum things')
    print(arbitrumMostRecent)
    print('-------------')

    # Convert the result to a dictionary
    mainnetDict = mainnetMostRecent['apr'].to_dict()
    optimismDict = optimismMostRecent['apr'].to_dict()
    arbitrumDict = arbitrumMostRecent['apr'].to_dict()

    '''print('Mainnet Aprs')
    print(mainnetDict)
    print('-------------')
    print('Optimism Aprs')
    print(optimismDict)
    print('-------------')
    print('Arbitrum Aprs')
    print(arbitrumDict)'''

    returnData = {
        'mainnet' : mainnetDict,
        'optimism' : optimismDict,
        'arbitrum' : arbitrumDict
    }

    return returnData