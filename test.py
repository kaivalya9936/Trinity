from os import system
from googleapiclient.discovery import build
from secret_stuff import api_key


def bash_command(user_input):
    _ = system(user_input)


def check_for_updates():
    youtube = build('youtube', 'v3', developerKey=api_key)

    request = youtube.channels().list(
        part='statistics',
        forUsername='RandomYouTuberNumberOneOrSomething'
    )

    response = request.execute()
    bash_command('rm test_file.py')
    bash_command(f"""echo 'yt_data = "{response}"' >> test_file.py""")

    from test_file import yt_data
    string_data = str(yt_data)
    video_count = int(string_data[-8:-4])
    print(video_count)


starting_video_count = check_for_updates()

while True:
    new_video_count = check_for_updates()
    if new_video_count == starting_video_count:
        print(f'Still {starting_video_count} videos.')
    else:
        print(f'There are now {new_video_count} videos!')