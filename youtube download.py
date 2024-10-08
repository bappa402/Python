from pytube import YouTube

# Function to download video
def download_video(url, output_path):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()  # Get highest resolution available
        stream.download(output_path=output_path)  # Download video
        print(f"Downloaded: {yt.title}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Replace with your video URL and output path
video_url = input()
output_folder = r"C:\Users\91700\Downloads"  # Path where you want to save the video

download_video(video_url, output_folder)
