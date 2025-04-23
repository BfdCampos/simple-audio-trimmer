import ffmpeg
import os
import argparse
import sys

def trim_audio(input_path, start_time, end_time, output_path=None):
    # Get input file info for default output naming
    input_dir = os.path.dirname(input_path)
    input_filename = os.path.basename(input_path)
    input_name, input_ext = os.path.splitext(input_filename)

    # If no output path is provided, create one using the input name with a suffix
    if not output_path:
        output_filename = f"{input_name}_trimmed_{start_time}_{end_time}{input_ext}"
        output_path = os.path.join(input_dir, output_filename)

    print(f"Removing segment from {start_time}s to {end_time}s in {input_path}")

    try:
        # Get the input file
        input_file = ffmpeg.input(input_path)

        # Split the audio into two parts - before and after the segment to remove
        before_segment = input_file.filter('atrim', end=start_time)
        after_segment = input_file.filter('atrim', start=end_time)

        # Concatenate the parts
        joined = ffmpeg.concat(before_segment, after_segment, v=0, a=1)

        # Output the result
        (
            ffmpeg
            .output(joined, output_path)
            .overwrite_output()
            .run()
        )
        print(f"Processing complete! Output saved to {output_path}")
        return True
    except ffmpeg.Error as e:
        print(f"Error occurred: {e.stderr.decode()}", file=sys.stderr)
        return False

if __name__ == "__main__":
    # Set up command line argument parsing
    parser = argparse.ArgumentParser(description="Remove segment from audio files using ffmpeg")
    parser.add_argument("--path", "-p", required=True, help="Path to the input audio file")
    parser.add_argument("--start", "-s", type=float, required=True, help="Start time of segment to remove (seconds)")
    parser.add_argument("--end", "-e", type=float, required=True, help="End time of segment to remove (seconds)")
    parser.add_argument("--output", "-o", help="Output file path (optional)")

    # Parse arguments
    args = parser.parse_args()

    # Process audio with parsed arguments
    trim_audio(args.path, args.start, args.end, args.output)
