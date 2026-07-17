!pip install -q gradio gTTS
import gradio as gr
from gtts import gTTS
import tempfile

def text_to_speech(text):
    if not text.strip():
        return None

    # Create temporary MP3 file
    audio_path = tempfile.NamedTemporaryFile(
        suffix=".mp3",
        delete=False
    ).name

    # Convert text to speech
    tts = gTTS(text=text, lang="en")
    tts.save(audio_path)

    return audio_path


with gr.Blocks(title="Text to Speech") as demo:

    gr.Markdown("# 🔊 Text to Speech")

    text = gr.Textbox(
        label="Enter Text",
        lines=6,
        placeholder="Type something here..."
    )

    btn = gr.Button("Generate Speech")

    audio = gr.Audio(
        label="Speech Output",
        type="filepath"
    )

    btn.click(
        fn=text_to_speech,
        inputs=text,
        outputs=audio
    )

demo.launch()
