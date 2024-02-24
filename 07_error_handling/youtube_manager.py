import json

file_name = "youtube.txt"

def load_data():
    try:
        with open(file_name, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data_helper(videos):
    with open(file_name, 'w') as file:
        json.dump(videos, file)

def list_all_videos(videos):
    print("*" * 80)
    print("\n")
    if len(videos) == 0:
        print("No videos available")
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']}, time: {video['time']} ")
    print("\n")
    print("*" * 80)


def add_video(videos):
    name = input("Enter video name: ")
    time = input("Enter video duration: ")
    videos.append({'name': name, 'time': time})
    save_data_helper(videos)
    print("Video Added successfully\n")

def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter video number to update : "))
    if 1 <= index <= len(videos):
        name = input("Enter new video name : ")
        time = input("Enter new video time : ")
        videos[index-1] = {'name': name, 'time': time}
        save_data_helper(videos)
        print("Video Updated successfully\n")
    else:
        print("Invalid Video Number")

def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter video number to be deleted : "))
    if 1 <= index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)
        print("Video Deleted successfully\n")
    else:
        print("Invalid Video Number")

def main():
    videos = load_data()
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
                list_all_videos(videos)

            case '2':
                add_video(videos)

            case '3':
                update_video(videos)

            case '4':
                delete_video(videos)

            case '5':
                break

            case _:
                print("Invalid Choice")

if __name__ == '__main__':
    main()