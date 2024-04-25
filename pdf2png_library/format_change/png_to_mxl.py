import subprocess
import os
import glob


def transcribe_with_audiveris(png_directory, audiveris_path, output_directory):
    """
    Process PNG files with Audiveris, transcribing them to music notation and exporting as MXL files.

    :param png_directory: Directory containing PNG files to be processed.
    :param audiveris_path: Full path to the Audiveris batch file.
    :param output_directory: Directory where the output MXL files will be saved.
    """
    # Ensure the output directory exists
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    num = 0
    for png_file in os.listdir(png_directory):
        num += 1
        if png_file.lower().endswith(".png"):
            png_name = os.path.basename(png_file)
            input_path = os.path.join(png_directory, png_file)
            print(f"Transcribing: {png_name} {num}")

            # Construct the command
            command = [
                audiveris_path,
                "-batch",
                "-transcribe",
                "-export",
                "-output", output_directory,
                input_path
            ]

            # Execute the command
            subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)

    cleanup_output_directory(output_directory)

def cleanup_output_directory(output_directory):
    """
    Remove .omr and .log files from the specified directory.
    """
    for extension in ['.omr', '.log']:
        for file in glob.glob(os.path.join(output_directory, f'*{extension}')):
            os.remove(file)

