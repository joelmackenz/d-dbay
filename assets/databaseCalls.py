import pymongo
from pymongo import MongoClient
import os
from dotenv import load_dotenv
import state
import seaborn as sns
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib import pyplot as plt
import pandas
import csv

load_dotenv()

cluster = MongoClient(os.getenv('CLUSTER'))
db = cluster[os.getenv('DB')]
collection = db[os.getenv('COLLECTION')]

def saveToDatabase():
    post = {
    "version": "1.0",  
    "userInfo": {
        "current_user": state.current_user,
        "hype": state.hype,
        "modifier": state.modifier,
    },
    "itemInfo": {
        "itemName": state.item,
        "item_value": state.item_value,
        "item_percent": state.item_percent,
        "rarity": state.rarity
    },
    "auctionInfo": {
        "total_bidders": state.total_bidders,
        "winning_bid": state.winning_bid,
        "finalPrizeMoney": state.finalPrizeMoney,
        "auctionRounds": state.auctionRound
    }
    
}
    collection.insert_one(post)
    print("Auction results saved to database for user " + state.current_user + ".")

async def getPrizeMoneyPercentages(rarity):
    data = {}
    dataList = []
    for x in collection.find({ "itemInfo.rarity": rarity },{ "_id": 0, "itemInfo.item_value": 1, "auctionInfo.finalPrizeMoney": 1 }):
        percentToNearest10 = (x["auctionInfo"]["finalPrizeMoney"] / x["itemInfo"]["item_value"]) * 100
        percentToNearest10 = int(round(percentToNearest10, -1))
        if percentToNearest10 in data:
            data[percentToNearest10] += 1
        else:
            data[percentToNearest10] = 1
    for key, value in data.items():
        dataList.append([key, value])
    return dataList

async def saveDataToCSV(rarity):
    data = await getPrizeMoneyPercentages(rarity)
    header = ['percent', 'repetitions (rounded to nearest ten)']
    with open('csvDataFiles/data.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(data)

async def getAuctionInfoBarGraph(rarity):
    await saveDataToCSV(rarity)
    data = pandas.read_csv("csvDataFiles/data.csv")
    sns.set(style="darkgrid")
    df = sns.barplot(data=data, x="percent", y="repetitions (rounded to nearest ten)")
    plt.show()