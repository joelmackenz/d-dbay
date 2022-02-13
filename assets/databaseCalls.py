import pymongo
from pymongo import MongoClient
import os
from dotenv import load_dotenv
import state

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