from openai import OpenAI
from pydub import AudioSegment
from dotenv import load_dotenv
from moviepy.editor import VideoFileClip
from datetime import date
import os
import glob, os


# Load the .env file
load_dotenv()

# Get the API key
api_key = os.getenv('open_ai_API_KEY')

# open ai key 
client = OpenAI(api_key=api_key)


video_path = r'\\tbh.local\users\RedirectedFolders\alex.kelly\My Documents\My Videos\2024-01-20 13-05-13.mkv'  # Replace with your video file path
audio_path = 'output_audio.mp3'        # Replace with your desired audio file path

def extract_audio_from_video(video_path, audio_path):
    video = VideoFileClip(video_path)
    audio = video.audio
    audio.write_audiofile(audio_path)

audio_transcript = []
def extract_text_from_audio(audio_file_path):
    
    audio = AudioSegment.from_file(audio_file_path)

    # Length of each chunk in milliseconds
    chunk_length = 10 * 10000  # 10 seconds

    chunks = [audio[i:i + chunk_length] for i in range(0, len(audio), chunk_length)]

    for i, chunk in enumerate(chunks):
        chunk.export(f".\chunked\chunk{i}.mp3", format="mp3")
        print(f".\chunked\chunk{i}.mp3")

    for i in range(len(chunks)):
        with open(f".\chunked\chunk{i}.mp3", "rb") as audio_file:
            transcript = client.audio.transcriptions.create(
                model="whisper-1", 
                file=audio_file
            )
            print(transcript)
            audio_transcript.append(transcript)
    return audio_transcript

extract_audio_from_video(video_path, audio_path)
transcript = extract_text_from_audio(audio_path)

today = date.today()
file_name = f".\\transcripts\\{today.strftime('%Y-%m-%d-%t')}_transcript.txt"

with open(file_name, "w") as transcript_file:
    for t in transcript:
        transcript_file.write(t)

[os.remove(f) for f in glob.glob(".\\chunked\\*.mp3")]
