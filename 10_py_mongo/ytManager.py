from pymongo import MongoClient
from bson import ObjectId

client = MongoClient("mongodb+srv://umesh:umeshmehta@clusterpython.rxccw50.mongodb.net/", tlsAllowInvalidCertificates=True)

db = client["ytManager"]

video_collection = db["videos"]

print(video_collection)


def list_videos():
    for video in video_collection.find():
        print(f"id: {video["_id"]}, name: {video["name"]}, time: {video["time"]}")

def add_video(video, time):
    video_collection.insert_one({"name":video, "time":time})

def update_video(id,video, time):
    video_collection.update_one({"_id": ObjectId(id)},{"$set":{"name":video, "time":time}})

def delete_video(id):
    video_collection.delete_one({"_id":ObjectId(id)})

def main():
    while True:
        print("\nYoutube Manager | Choose an Option\n")
        print("1. List All Youtube Videos ")
        print("2. Add a Youtube Video ")
        print("3. Update a Youtube Video ")
        print("4. Delete a Youtube Video ")
        print("5. Exit App ")
        choice = input("Enter Your Choice: ")

        match choice:
            case '1':
                list_videos()
            case '2':
                name = input("Enter your video name: ")
                time = input("Enter your video time: ")
                add_video(name, time)
            case '3':
                video_id = input("Enter your video id to update")
                name = input("Enter your new video name: ")
                time = input("Enter your new video time: ")
                update_video(video_id, name, time)
            case '4':
                video_id = input("Enter your video id to delete")
                delete_video(video_id)
            case '5':
                break
            case _:
                print("Invalid Choice")

if __name__ == '__main__':
    main()