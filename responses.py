from dotenv import load_dotenv
import os
from typing import Final
import pymongo

load_dotenv()
URI: Final[str] = os.getenv('MONGODB_URI')

client = pymongo.MongoClient(URI)
db = client.inventory

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()
    task_list = []
 
    if 'furybot' in lowered:
        if 'hello' in lowered:
            return 'Hello there!'
        elif 'how are you' in lowered:
            return 'Good, thanks!'
        elif 'help' in lowered:
            return "**Hey! In order to get my attention, type FuryBot and then follow through with your request.**\n*Features*\n1. I can run an inventory check on any item that we have. To do that, you can say something like 'FuryBot, run an inventory check on the item, 'Shaft Collar'"
        elif 'inventory' in lowered:
            start_index = user_input.find('"') + 1
            end_index = user_input.find('"', start_index)
            item = user_input[start_index:end_index]
            item = item.strip('"')
            filter_query = {'item': item}
            print("Filter Query:", filter_query)
            for i in db.records.find(filter_query):
                print("Found record:", i)
                quantity = i['quantity'].strip('"')
                link = i['link'].strip('"')
                return f"There are {quantity} more of the item, {item}, left. You can buy more at {link}"
            return "Sorry, I couldn't find that item. Make sure that the item's name is correctly spelled and capitalized."
