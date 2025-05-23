
import json
from turtledemo.penrose import start


def load_data():
    try:
        with open('youtube.txt','r')as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data_helper(videos):
    with open('youtube.txt','w') as file:
        json.dump(videos,file)


def list_all_videos(videos):
    for index,video in enumerate(videos,start=1):
        print(f"{index}. {video['name']} - {video['time']}")



def add_video(videos):
    name=input("Enter video name:")
    time=input("Enter video time: ")
    videos.append({'name': name, 'time':time})
    save_data_helper(videos)

def update_video(videos):
    pass


def delete_video(videos):
    pass
def main():
    videos= load_data()
    while True:
        print("\n Youtube Manager")
        print("1. List all Youtube videos")
        print("2. add  videos")
        print("3. update Video")
        print("4. Delete Video")
        print("5. Exit the app")
        choice=input("Enter Your Choice")
        print(videos)

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


if __name__ == "__main__":
    main()




