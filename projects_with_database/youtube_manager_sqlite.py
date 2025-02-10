import sqlite3

con = sqlite3.connect('youtube_videos.db')

cursor = con.cursor()

cursor.execute('''
    CREATE TABLE if not exists videos(
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        time TEXT NOT NULL
    )
''')
 
#try executing by giving comma to cursor tuple

def list_of_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        if row == None:
            print("List is empty!!!")
        else:
            print(row)

def add_videos(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    con.commit()

def update_videos(video_id, new_name, new_time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_name, new_time, video_id)) 
    con.commit()

def delete_videos(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_id))

def main():
    while True:
        print("\n---!YouTube Manager with DataBase!---")
        print("1. List of videos")
        print("2. Add Videos")
        print("3. Update Videos")
        print("4. Delete Videos")
        print("5. Exit Application")
        choice = input("Enter a Choice: ")
 
        match choice:
            case '1':
                list_of_videos()

            case '2':
                name = input("Enter the Video name: ")
                time = input("Enter the Video Time: ")
                add_videos(name, time)
            case '3':
                video_id = input("Enter Video ID to Update: ")
                name = input("Enter the Video name to Update: ")
                time = input("Enter the Video Time to Update: ")
                update_videos(video_id, name, time)
            case '4':
                video_id = input("Enter Video ID to Update: ")                                
                delete_videos(video_id)
            case '5':
                break
            case _:
                print("Invalid Option selected!!!")
    con.close()

if __name__ == "__main__":
    main()