import math
import wave

import pygame

# Define the parameters of the WAV file
nChannels = 1
sample_width = 2
framerate = 44100


# Define the function to create a sine wave
def createWave(freq, duration):
    num_samples = int(duration * framerate)
    amplitude = 32767
    increment = freq * (2 * math.pi) / framerate
    samples = [int(amplitude * math.sin(increment * n)) for n in range(num_samples)]
    return samples


def generateSound(arr):
    # Generate and save the audio file for each element in the array

    for element in arr:
        freq = 100 + element * 5000/len(arr)
        duration = 0.01
        samples = createWave(freq, duration)
        wave_file = wave.open(f"audio/{element - 1}.wav", "w")
        wave_file.setnchannels(nChannels)
        wave_file.setsampwidth(sample_width)
        wave_file.setframerate(framerate)
        for sample in samples:
            wave_file.writeframesraw(sample.to_bytes(sample_width, byteorder="little", signed=True))
        wave_file.close()


def playSound(index):
    sound = pygame.mixer.Sound(f"audio/{index}.wav")
    sound.play()
    pygame.time.wait(int(sound.get_length() * 1000))
