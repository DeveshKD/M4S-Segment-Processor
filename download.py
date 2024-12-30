import os
import requests

def download_segments(base_url, output_dir, start_index, end_index, file_prefix):
    os.makedirs(output_dir, exist_ok=True)
    for i in range(start_index, end_index + 1):
        segment_url = f"{base_url}seg-{i}.m4s"
        output_file = os.path.join(output_dir, f"{file_prefix}-seg-{i}.m4s")
        try:
            print(f"Downloading: {segment_url}")
            response = requests.get(segment_url, timeout=10)
            if response.status_code == 200:
                with open(output_file, "wb") as f:
                    f.write(response.content)
            else:
                print(f"Segment {i} not found (status code: {response.status_code})")
                break
        except requests.RequestException as e:
            print(f"Error downloading segment {i}: {e}")
            break

# Base URLs
video_base_url = "https://tagmango.com/assets/1727517678757/video_1/"
audio_base_url = "https://tagmango.com/assets/1727517678757/audio_0_0/"

# Output directories
video_output_dir = "video_segments"
audio_output_dir = "audio_segments"

# Download ranges
start_index = 1
end_index = 2026  # Adjust as needed

# Download video and audio segments
download_segments(video_base_url, video_output_dir, start_index, end_index, "video")
download_segments(audio_base_url, audio_output_dir, start_index, end_index, "audio")

print("Download complete.")
