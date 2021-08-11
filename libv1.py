import math
from random import random

SAMPLE_RATE = 44100

def gen_samples(freq: float, duration_sec: float) -> list[float]:
    samples_cnt = int(duration_sec * SAMPLE_RATE)
    res = []
    for sample_idx in range(samples_cnt):
        time = sample_idx / SAMPLE_RATE
        res.append(math.sin(time * 2 * math.pi * freq))
    return res


def gen_samples2(freq: float, duration_sec: float) -> list[float]:
    samples_cnt = int(duration_sec * SAMPLE_RATE)
    period_size = int(1 / freq * SAMPLE_RATE)
    res = [random() * 2 - 1 for _ in range(period_size)]
    for sample_idx in range(period_size, samples_cnt):
        period_before_idx = sample_idx - period_size
        sample = (res[period_before_idx] + res[period_before_idx + 1]) / 2
        res.append(sample)
    return res


def write_samples(file_name: str, samples: list[float]) -> None:
    cnt_samples = len(samples)
    data_size = cnt_samples * 2

    with open(file_name, "wb") as file:
        file.write(b"RIFF")                        # chunkId
        file.write(
          (data_size + 36).to_bytes(4, 'little')   # chunkSize
        )
        file.write(b"WAVE")                        # format
        file.write(b"fmt ")                        # subchunk1Id
        file.write((16).to_bytes(4, 'little'))     # subchunk1Size
        file.write((1).to_bytes(2, 'little'))      # audioFormat
        file.write((1).to_bytes(2, 'little'))      # numChannels
        file.write((44100).to_bytes(4, 'little'))  # sampleRate
        file.write((88200).to_bytes(4, 'little'))  # byteRate
        file.write((2).to_bytes(2, 'little'))      # blockAlign
        file.write((16).to_bytes(2, 'little'))     # bitsPerSample
        file.write(b"data")                        # subchunk2Id
        file.write(
          data_size.to_bytes(4, 'little')          # subchunk2Size
        )
        short_range = (2 ** 15) - 1
        for sample in samples:
            sample_short = int(sample * short_range)
            file.write(sample_short.to_bytes(2, 'little', signed=True))

TONE_MAP = {
    "C": 0,
    "D": 2,
    "E": 4,
    "F": 5,
    "G": 7,
    "A": 9,
    "B": 11,
}

def get_freq(note: str) -> float:
    octave = int(note[1])
    tone_idx = octave * 12 + TONE_MAP[note[0]]
    if len(note) == 3:
        if note[2] == "b":
            tone_idx -= 1
        if note[2] == "#":
            tone_idx += 1
    diff = tone_idx - 57   # A4
    return 440 * math.pow(2, (diff / 12))
