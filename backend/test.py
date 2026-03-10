from db import menu_collection

for item in menu_collection.find():
    print(item)