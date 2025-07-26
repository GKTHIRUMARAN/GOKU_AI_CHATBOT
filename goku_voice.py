import edge_tts
import os

async def speak_and_save(text, filename="goku_reply.mp3"):
    communicate = edge_tts.Communicate(
        text=text,
        voice="ja-JP-KeitaNeural"
    )
    await communicate.save(filename)

def play_audio(filename="goku_reply.mp3"):
    from IPython.display import Audio
    if os.path.exists(filename):
        return Audio(filename, autoplay=True)
    else:
        raise FileNotFoundError(f"{filename} not found.")