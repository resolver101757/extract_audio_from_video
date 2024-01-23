
# Video to Text Transcription Tool

## Introduction
This project provides a tool for extracting audio from video files and then transcribing the extracted audio into text. It utilizes `moviepy` for video processing, `pydub` for audio handling, and the `openai` API for transcribing audio.

## Table of Contents
- Introduction
- Installation
- Usage
- Features
- Dependencies
- Configuration
- Documentation
- Examples
- Troubleshooting
- Contributors
- License

## Installation
```bash
pip install moviepy pydub python-dotenv openai
```
Note: Ensure you have Python installed on your system.

## Usage
To use this tool:
1. Set your OpenAI API key in a `.env` file.
2. Run the script with your video file path.

## Features
- Extracts audio from video files.
- Splits audio into manageable chunks.
- Uses OpenAI for accurate audio transcription.
- Saves the transcript to a text file.

## Dependencies
- moviepy
- pydub
- python-dotenv
- openai

## Configuration
Create a `.env` file in your project root with the following content:
```
open_ai_API_KEY='Your-OpenAI-API-Key'
```

## Documentation
The tool is divided into two main functions:
1. `extract_audio_from_video(video_path, audio_path)`: Extracts audio from the provided video file.
2. `extract_text_from_audio(audio_file_path)`: Transcribes the audio into text.

## how to use 
To transcribe a video, run the script as follows:
```python
video_path = 'path_to_your_video.mkv'
audio_path = 'output_audio.mp3'
extract_audio_from_video(video_path, audio_path)
transcript = extract_text_from_audio(audio_path)
```

## Troubleshooting
- Ensure all dependencies are installed.
- Check if the `.env` file is correctly configured.
 - it requires open_ai_API_KEY= 'Your-OpenAI-API-Key' in .env file
- Make sure the video and audio paths are correct.

## Contributors
List of contributors (if any).

## License
Specify the license under which your project is released.