import sqlite3

conn = sqlite3.connect("youtube.db")

cursor = conn.cursor()

cursor.execute('''
               CREATE TABLE IF NOT EXISTS videos(
                   id INTEGER PRIMARY KEY,
                   name VARCHAR(255) NOT NULL,
                   time VARCHAR(255) NOT NULL
               )
               ''')

def list_videos():
    cursor.execute('''SELECT * FROM videos''')
    for row in cursor.fetchall():
        print(row)

def add_video(name, time):
    cursor.execute('''INSERT INTO videos(name, time) VALUES(?, ?)''', (name, time))
    conn.commit()


def update_video(videoId, new_name, new_time):
    cursor.execute('''UPDATE videos SET name=?, time=? WHERE id=?''', (new_name, new_time, videoId))
    conn.commit()

def delete_video(videoId):
    cursor.execute('''DELETE FROM videos WHERE id=?''', (videoId,))
    conn.commit()

def main():
    while True:
        print("\n Youtube manager app with DB")
        print("1. List Videos")
        print("2. Add Video")
        print("3. Update Video")
        print("4. Delete Video")
        print("5. Exit")
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
    conn.close()

if __name__ == '__main__':
    main()