import json

def load_data():
    try:
        with open('project/youtube1.txt','r') as file:
            return json.load(file)
    except FileNotFoundError:
        #print("List is Empty!!!")
        return []
        


def save_data_helper(videos):
    with open('project/youtube1.txt', 'w') as file:
        json.dump(videos, file) #json.dump takes two values -> first: what to dump/write and second where to dump/place
        #videos data is inserted into file

def list_all_video(videos):
    print("\n")
    print("_ "*20)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. Title: {video['name']} \n   Duration: {video['time']}")
    print("_ "*20)

def add_video(videos):
    name = input("Enter Video Name: ")
    time = input("Enter Video Duration: ")
    videos.append({'name': name,'time': time})
    save_data_helper(videos)

def update_video(videos):
    list_all_video(videos)
    index = int(input("Enter video Number to Update "))

    if 1 <= index <= len(videos):
        name = input("Enter Video Name: ")
        time = input("Ebter Video Duration: ")
        videos[index - 1] = {'name': name, 'time': time}
        save_data_helper(videos)
    else:
        print("Invalid Index selected")

def delete_video(videos):
    list_all_video(videos)
    index = int(input("Enter Index Number to Delete "))

    if 1 <= index <= len(videos):
        del videos[index - 1]
        save_data_helper(videos)
    else:
        print("Invalid Index Selected")




def main():
    videos = load_data()
    while True:
        print("\n Youtube Manager | Choose an Option")
        print("1. list all youtube videos ")
        print("2. Add a youtube video ")
        print("3. Update a video youtube ")
        print("4. Delete a youtube video ")
        print("5. Exit the App ")
        choice = input("Enter your Choice ")
        #print(videos)

        match choice:
            case '1':
                list_all_video(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("**Invalid Choice**")

if __name__ == "__main__":
    main()