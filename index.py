import gradio as gr
from use_case import AudioHandlerUseCase

def handle_audio(file_path):
    output = ""
    with open(file_path, "rb") as f:
        audio_handler = AudioHandlerUseCase()
        output = audio_handler.handle_audio(f)
    return output  

input_audio = gr.Audio(
    sources=["microphone"],
    type="filepath",  # importante: retorna caminho para arquivo .ogg
    label="Grave seu áudio",
    waveform_options=gr.WaveformOptions(
        waveform_color="#01C6FF",
        waveform_progress_color="#0066B4",
        skip_length=2,
        show_controls=False,
    ),
)

output = gr.Textbox(label="Output")

demo = gr.Interface(
    fn=handle_audio,
    inputs=input_audio,
    outputs=output
)

demo.launch(share=False)