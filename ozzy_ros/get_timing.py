from playsound import playsound
 

# print('playing sound using  playsound')

from pydub import AudioSegment
import numpy as np

def get_phoneme_timings(text):
    timings = []
    for char in text:
        if char in phoneme_durations:
            timings.append(phoneme_durations[char])
    return timings

def get_audio_length(filename="rcx.wav"):
    audio = AudioSegment.from_mp3(filename)
    return len(audio) / 1000.0  # Return length in seconds

def scale_phoneme_timings(phoneme_timings, audio_length):
    total_phoneme_time = sum(phoneme_timings)
    scale_factor = audio_length / (total_phoneme_time / 1000.0)  # Convert total phoneme time to seconds
    scaled_timings = [timing * scale_factor for timing in phoneme_timings]
    return scaled_timings

phoneme_durations = {
    'a': 150,
    'b': 80,
    'c': 70,
    'd': 90,
    'e': 140,
    'f': 60,
    'g': 100,
    'h': 50,
    'i': 100,
    'j': 90,
    'k': 80,
    'l': 70,
    'm': 100,
    'n': 90,
    'o': 160,
    'p': 70,
    'q': 90,
    'r': 80,
    's': 70,
    't': 80,
    'u': 180,
    'v': 90,
    'w': 70,
    'x': 100,
    'y': 80,
    'z': 70
}




if __name__ =="__main__":
    text="Olá queridos e queridas do Brasil, vocês estão prontos para encher meu saco na RCX ? Venha conversar comigo nesse evento único cheio de robôs, explosões e caveiras muito loucas"

    phoneme_timings = get_phoneme_timings(text)
    audio_length = get_audio_length()
    print(audio_length)
    scaled_phoneme_timings = scale_phoneme_timings(phoneme_timings, audio_length)

    print("Original phoneme timings (ms):", phoneme_timings)
    print("Scaled phoneme timings (ms):", scaled_phoneme_timings)

    timing= [89.58246346555325, 115.17745302713989, 230.35490605427978, 
    179.1649269311065, 102.37995824634658, 127.97494780793322, 115.17745302713989, 204.75991649269315, 
    89.58246346555325, 179.1649269311065, 115.17745302713989, 230.35490605427978, 179.1649269311065, 
    102.37995824634658, 127.97494780793322, 115.17745302713989, 191.96242171189982, 89.58246346555325, 
    115.17745302713989, 204.75991649269315, 102.37995824634658, 191.96242171189982, 89.58246346555325, 
    127.97494780793322, 89.58246346555325, 115.17745302713989, 204.75991649269315, 89.58246346555325, 
    89.58246346555325, 179.1649269311065, 89.58246346555325, 102.37995824634658, 204.75991649269315, 
    89.58246346555325, 102.37995824634658, 204.75991649269315, 115.17745302713989, 102.37995824634658, 
    204.75991649269315, 89.58246346555325, 89.58246346555325, 191.96242171189982, 102.37995824634658, 
    191.96242171189982, 179.1649269311065, 115.17745302713989, 89.58246346555325, 63.98747390396661, 
    179.1649269311065, 102.37995824634658, 127.97494780793322, 179.1649269311065, 230.35490605427978, 
    89.58246346555325, 191.96242171189982, 89.58246346555325, 204.75991649269315, 115.17745302713989, 
    191.96242171189982, 179.1649269311065, 115.17745302713989, 63.98747390396661, 191.96242171189982, 
    89.58246346555325, 204.75991649269315, 115.17745302713989, 115.17745302713989, 179.1649269311065, 
    102.37995824634658, 89.58246346555325, 191.96242171189982, 102.37995824634658, 89.58246346555325, 
    204.75991649269315, 127.97494780793322, 127.97494780793322, 127.97494780793322, 204.75991649269315, 
    115.17745302713989, 179.1649269311065, 89.58246346555325, 89.58246346555325, 179.1649269311065, 
    179.1649269311065, 115.17745302713989, 179.1649269311065, 115.17745302713989, 102.37995824634658, 
    204.75991649269315, 115.17745302713989, 127.97494780793322, 89.58246346555325, 204.75991649269315, 
    89.58246346555325, 63.98747390396661, 179.1649269311065, 127.97494780793322, 204.75991649269315, 
    115.17745302713989, 179.1649269311065, 102.37995824634658, 204.75991649269315, 102.37995824634658, 
    89.58246346555325, 179.1649269311065, 127.97494780793322, 89.58246346555325, 89.58246346555325, 
    204.75991649269315, 89.58246346555325, 179.1649269311065, 89.58246346555325, 179.1649269311065, 
    89.58246346555325, 191.96242171189982, 115.17745302713989, 179.1649269311065, 127.97494780793322,
     102.37995824634658, 191.96242171189982, 89.58246346555325, 127.97494780793322, 230.35490605427978,
     127.97494780793322, 102.37995824634658, 204.75991649269315, 89.58246346555325, 204.75991649269315,
     230.35490605427978, 89.58246346555325, 191.96242171189982, 89.58246346555325]