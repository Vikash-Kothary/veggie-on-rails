#!/usr/bin/venv python3
"""
sampling.py - Convert a video into frames
"""

import ffmpeg


def main():
    """
    See: https://github.com/kkroening/ffmpeg-python
    """
    stream = ffmpeg.input('input.mp4')
    .output(stream, 'output.mp4')
    .run(stream)

    # Flip video horizontally: stream.hflip(stream)

if __name__ == '__main__':
    main()
