# from bark import SAMPLE_RATE, generate_audio, preload_models
# from scipy.io.wavfile import write as write_wav
# from IPython.display import Audio

# # download and load all models
# preload_models()

# # generate audio from text
# text_prompt = """
#      Hello, my name is Suno. And, uh — and I like pizza. [laughs] 
#      But I also have other interests such as playing tic tac toe.
# """
# audio_array = generate_audio(text_prompt)

# # save audio to disk
# write_wav("bark_generation.wav", SAMPLE_RATE, audio_array)
  
# # play text in notebook
# Audio(audio_array, rate=SAMPLE_RATE)

from bark import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import write as write_wav
import os

# download and load all models
preload_models()

# generate audio from text
text_prompt = """
     Hello, my name is Suno. And, uh — and I like pizza. [laughs] 
     But I also have other interests such as playing tic tac toe.
"""
audio_array = generate_audio(text_prompt)

# save audio to disk
output_file = "bark_generation.wav"
write_wav(output_file, SAMPLE_RATE, audio_array)

# play audio file (Windows)
os.system(f'start {output_file}')
