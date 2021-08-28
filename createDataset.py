import argparse
from CoinbaseAPI import CoinbaseAPI
from Config import *
from Dataset import Dataset

downloadDatasets = [
    # {"start": "2013-01-01", "end": "2013-02-01"}
]

startYear = 2013
endYear = 2020

for x in range(startYear, endYear+1):
    for y in range(1, 12):
        downloadDatasets.append({"start": f'{x}-{y:02}-01', "end": f'{x}-{(y+1):02}-01'})



for x in downloadDatasets:
    dataset = Dataset()
    start_date = x["start"]
    end_date = x["end"]
    tokens = start_date.split("-")
    month = tokens[0] + "_" + tokens[1] + "_"

    coinbaseAPI = CoinbaseAPI()
    historic_data = coinbaseAPI.getCoinHistoricData(COIN_PAIR, start=start_date, end=end_date,granularity=GRANULARITY)
    dataset.storeRawCoinHistoricData(month,COIN_PAIR,historic_data)
    print("> Using Coinbase API to build dataset for ",COIN_PAIR)



# print(downloadDatasets)


# start_date = "2020-01-01"
# end_date = "2020-02-02"
# tokens = start_date.split("-")
# month = tokens[0] + "_" + tokens[1] + "_"

# coinbaseAPI = CoinbaseAPI()
# historic_data = coinbaseAPI.getCoinHistoricData(COIN_PAIR, start=start_date, end=end_date,granularity=GRANULARITY)
# dataset.storeRawCoinHistoricData(month,COIN_PAIR,historic_data)

# print("> Using Coinbase API to build dataset for ",COIN_PAIR)