from pymongo import MongoClient
import os
from dotenv import load_dotenv
import state

load_dotenv()

cluster = MongoClient(os.getenv('CLUSTER'))
db = cluster[os.getenv('ZOLTAN_DB')]
collection = db[os.getenv('ZOLTAN_COLLECTION')]


def check_for_returning_player():
    try:
        prev_record = collection.find_one({"playerId": state.message.author.id})
        if prev_record:
            state.returning_player = True
    except Exception as e:
        print("No database found. Exception: \n " + str(e))


def save_future_to_database():
    try:
        prev_record = collection.find_one({"playerId": state.message.author.id})
        if prev_record:
            current_game_id = 2
            gamesSortedById = sorted([key for key in prev_record["games"]])
            lastGameId = int(gamesSortedById[len(gamesSortedById) - 1])
            if lastGameId >= current_game_id:
                current_game_id = int(
                    gamesSortedById[len(prev_record["games"]) - 1]) + 1
            record_id_filter = {"playerId": prev_record['playerId']}
            collection.update(record_id_filter, {
                "$set": {
                    "games." + str(current_game_id): {
                        "version": "1.0",
                        "result": state.zoltan_result
                    }
                }
            }
            )
            print("Updated existing Zoltan entry in database for user " + prev_record["player"] + ".")

        else:
            post = {
                "player": state.message.author.name,
                "playerId": state.message.author.id,
                "games": {
                    "1": {
                        "version": "1.0",
                        "result": state.zoltan_result
                    }
                }
            }
            collection.insert_one(post)
            print("Saved new entry to database for user " + state.message.author.name + ".")
    except Exception as e:
        print("Database error! Exception: \n " + str(e))
