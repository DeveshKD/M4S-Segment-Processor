start_index = 1  # Start of the segment range
end_index = 2026  # End of the segment range

# Directories for audio and video segments
audio_dir = "audio_segments"
video_dir = "video_segments"

# Output files for ffmpeg concatenation lists
audio_list_file = "audio_file_list.txt"
video_list_file = "video_file_list.txt"

# Function to generate file lists
def create_file_list(output_file, directory, prefix):
    with open(output_file, "w") as f:
        for i in range(start_index, end_index + 1):
            f.write(f"file '{directory}/{prefix}-seg-{i}.m4s'\n")

# Generate file lists for audio and video
create_file_list(audio_list_file, audio_dir, "audio")
create_file_list(video_list_file, video_dir, "video")

print(f"File lists generated:\n- {audio_list_file}\n- {video_list_file}")