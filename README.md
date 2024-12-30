# M4S Segment Processor

A simple tool to process and merge fragmented `.m4s` audio and video files into complete media files using FFmpeg.

## Features
- Converts fragmented `.m4s` segments into usable `.mp4` files.
- Merges video and audio segments.
- Combines processed video and audio into a final output file.

---

## Prerequisites
1. **FFmpeg**: Ensure FFmpeg is installed and added to your system's PATH.
   - [FFmpeg Installation Guide](https://ffmpeg.org/download.html)
2. **Python**: Required for automating the conversion process.

---

## Directory Structure
```
project/
├── video_segments/          # Folder containing video .m4s files
├── audio_segments/          # Folder containing audio .m4s files
├── processed_video/         # Output folder for processed video files
├── processed_audio/         # Output folder for processed audio files
├── video_file_list.txt      # File list for video segments
├── audio_file_list.txt      # File list for audio segments
├── donwload.py              # Script to download .m4s files from the website
└── generate_file_lists.py   # Script to generate file lists
```

---

## Usage

### 1. Download .m4s Segments
Use `download.py` to download video and audio `.m4s` segments:
```bash
python download.py
```

### 2. Generate File Lists
Run the following Python script to create `video_file_list.txt` and `audio_file_list.txt`:
```bash
python generate_list.py
```

### 3. Convert Segments to Usable MP4
Process `.m4s` segments using an initialization file (`init.mp4`):
```bash
python process_segments.py
```

### 4. Concatenate Segments
Merge all processed video and audio segments into single media files:
```bash
ffmpeg -f concat -safe 0 -i video_file_list.txt -c copy video_output.mp4
ffmpeg -f concat -safe 0 -i audio_file_list.txt -c copy audio_output.mp4
```

### 5. Combine Video and Audio
Merge the final video and audio files into a single output:
```bash
ffmpeg -i video_output.mp4 -i audio_output.mp4 -c copy final_output.mp4
```
---

## Notes
- Replace `init.mp4` with the actual initialization segment if required.
- Ensure `.m4s` files are downloaded correctly before running the script.
