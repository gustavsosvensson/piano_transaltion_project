import os
import subprocess

def convert_mxl_to_mid(musescore_path, source_folder, output_folder):
    # Ensure the output directory exists
    os.makedirs(output_folder, exist_ok=True)

    # List all MXL files in the source directory
    mxl_files = [f for f in os.listdir(source_folder) if f.endswith('.mxl')]

    # Convert each MXL file to MIDI
    num = 0
    for mxl_file in mxl_files:
        num += 1
        mxl_name = os.path.basename(mxl_file)
        print(f"Converting {mxl_name} {num} into a  midi file")
        full_mxl_path = os.path.join(source_folder, mxl_file)
        midi_file = os.path.splitext(mxl_file)[0] + '.mid'  # Change extension to .mid
        full_midi_path = os.path.join(output_folder, midi_file)

        # Construct and run the conversion command
        command = [musescore_path, "-o", full_midi_path, full_mxl_path]
        subprocess.run(command, check=True)

