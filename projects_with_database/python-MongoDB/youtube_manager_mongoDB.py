
#from pymongo import MongoClient
#client = MongoClient("mongodb+srv://username: password@cluster0.njq6q.mongodb.net/YT-Manager")

##also we can write the import statements in this manner, instead of always writing (pymongo.MongoClient) we can directly write MongoClient by just importing MongoClient from Pymongo
#-----------------------------------------------------------------------------------------#

import pymongo
from bson import ObjectId

client = pymongo.MongoClient("mongodb+srv://username: password@cluster0.njq6q.mongodb.net/")
#not a good idea to include Id and Password in code files

print(client)
db = client['YT-Manager'] #Naming the Database as "YT-Manager" and instead of writing Client repeatedly, storing it in a variable 

video_collection = db["videos"]
#print(video_collection)


def list_all_videos():
    for video in video_collection.find():
        print(f"ID. {video['_id']}, Name: {video['name']}, Duration: {video['time']}")

def add_video(name, time):
    #values are passed as objects here so written in{}
    video_collection.insert_one({"name": name, "time": time})

def update_video(video_id, new_name, new_time):
    #update_one takes two parameters. First parameter takes what/whom has to be updated and second parameter takes values of what has to be updated
    video_collection.update_one(
        {"_id": ObjectId(video_id)},
        {"$set": {"name": new_name, "time": new_time}}
    )

def delete_video(video_id):
    video_collection.delete_one({"_id": ObjectId(video_id)})


def main():
    while True:
        print("YouTube Manager|Choose an Option")
        print("1. List all YT videos")
        print("2. Add a YT Videos")
        print("3. Update a YT Video")
        print("4. Delete a YT Video")
        print("5. Exit the app")
        choice = input("Enter a Choice: ") 

        match choice:
            case '1':
                print('--'*25)
                list_all_videos()
                print('--'*25)
            case '2':
                name = input("Enter your Video name: ")
                time = input("Enter your Video duration: ")
                add_video(name, time)
            case '3':
                video_id = input("Enter your video Id: ")
                name = input("Enter your Video name: ")
                time = input("Enter your Video duration: ")
                update_video(video_id, name, time)                
            case '4':
                list_all_videos()
                video_id = input("Enter your video Id: ")
                delete_video(video_id)    
            case '5':
                break
            case _:
                print("Invalid option selected!!!")
if __name__ == "__main__":
    main()