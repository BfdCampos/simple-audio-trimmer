# 🎵 Audio Trimmer - Remove Audio Segments 🎵

A simple Python tool to remove segments from audio files using FFmpeg.

## 🛠️ Installation

### Step 1: Install FFmpeg

First, you need to install FFmpeg, which is the core audio processing engine:

```bash
# For macOS users
brew install ffmpeg

# For Ubuntu/Debian users
sudo apt-get install ffmpeg
```

### Step 2: Install the Python wrapper

Next, install the Python package that interfaces with FFmpeg:

```bash
pip3 install ffmpeg-python
```

⚠️ Make sure you install `ffmpeg-python`, not just `ffmpeg` (which is a different package).

## 🚀 Usage

```bash
python3 audio_trim.py -p PATH_TO_AUDIO -s START_TIME -e END_TIME [-o OUTPUT_PATH]
```

### Arguments

- `-p`, `--path`: Path to your audio file 🎵
- `-s`, `--start`: Start time of the segment to remove (in seconds) ⏱️
- `-e`, `--end`: End time of the segment to remove (in seconds) ⏱️
- `-o`, `--output`: (Optional) Custom output file path 💾

If you don't specify an output path, the result will be saved in the same directory as the input file with a name like: `original_name_trimmed_start_end.mp3`

## 📋 Examples

Remove a segment from 10 to 14 seconds:

```bash
python3 audio_trim.py -p ~/Music/song.mp3 -s 10 -e 14
```

Remove the first 5 seconds and save with a custom name:

```bash
python3 audio_trim.py -p ~/Downloads/podcast.mp3 -s 0 -e 5 -o ~/Music/edited_podcast.mp3
```

## 💡 How It Works

1. The script takes the audio before the segment you want to remove
2. Then takes the audio after the segment
3. Joins these two parts seamlessly
4. Saves the result to your specified location

## 🐛 Troubleshooting

- If you see `No such file or directory: 'ffmpeg'`, make sure FFmpeg is installed and in your PATH
- If you get an error about `module 'ffmpeg' has no attribute 'input'`, you probably installed the wrong package - uninstall with `pip3 uninstall ffmpeg` and install the correct one with `pip3 install ffmpeg-python`

## 🙏 Credits

This script uses FFmpeg, a powerful multimedia framework, and the ffmpeg-python wrapper, which provides a friendly Python interface.

