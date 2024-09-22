import os
import vlc
import time

# Folder containing video files
VIDEO_FOLDER = '../The Simpsons S01 720p x265 DD5.1/'

# Function to play videos in a loop
def play_videos(video_folder):
    # Create a VLC instance
    vlc_instance = vlc.Instance()
    player = vlc_instance.media_list_player_new()
    
    # Create a media list and add videos to it
    media_list = vlc_instance.media_list_new()
    
    for filename in os.listdir(video_folder):
        if filename.endswith(('.mp4', '.avi', '.mkv', '.mov')):  # Add other video formats if needed
            media_path = os.path.join(video_folder, filename)
            media = vlc_instance.media_new(media_path)
            media_list.add_media(media)
    
    player.set_media_list(media_list)
    
    while True:
        # Play the videos in a loop
        player.play()
        
        # Wait until the current video finishes
        while player.is_playing():
            time.sleep(1)
        
        # Restart the playlist once it finishes
        media_list.set_media(player.get_media())
        player.play()

if __name__ == "__main__":
    play_videos(VIDEO_FOLDER)
