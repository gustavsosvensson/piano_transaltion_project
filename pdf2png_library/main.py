import argparse
import os
import subprocess

from data_folder_manegment.clear_folders import clear_output_folder
from data_folder_manegment.folder_definition import absolute_output_png_folders, absolute_output_mxl_folders, \
    absolute_output_mid_folders, absolute_output_merged_midi_folders
from final_midi.merge_mxl_files import merge_midi_files_sequentially
from format_change.mxl_to_mdi import convert_mxl_to_mid
from format_change.pdf_to_png import convert_pdf_to_png
from format_change.png_to_mxl import transcribe_with_audiveris


def pdf_to_mid(input_file):
    output_png_folder = absolute_output_png_folders()
    output_mxl_folder = absolute_output_mxl_folders()
    output_mid_folder = absolute_output_mid_folders()
    output_merged_mid_folder = absolute_output_merged_midi_folders()

    folder_list = [output_mid_folder, output_mxl_folder, output_png_folder]

    for folder in folder_list:
        clear_output_folder(folder)

    relative_path = os.path.join("../Ideal Piano (for Windows)/Ideal Piano/data/pdf_files", input_file)
    pdf_path = os.path.abspath(relative_path)
    convert_pdf_to_png(output_png_folder, pdf_path)

    audiveris_path = r"C:\dev\Piano visual\Audiveris\bin\Audiveris.bat"
    transcribe_with_audiveris(output_png_folder, audiveris_path, output_mxl_folder)

    musescore_path = r"C:\dev\Piano visual\MuseScore 4\bin\MuseScore4.exe"
    convert_mxl_to_mid(musescore_path, output_mxl_folder, output_mid_folder)

    mid_files = [f for f in os.listdir(output_mid_folder) if f.endswith('.mid')]
    full_mid_paths = [os.path.join(output_mid_folder, mid_file) for mid_file in mid_files]

    merge_midi_files_sequentially(output_merged_mid_folder, *full_mid_paths)


# This is the entry point of your script
if __name__ == "__main__":
    # Create the parser
    parser = argparse.ArgumentParser(description="Convert PDF music sheets to MIDI files.")

    # Add an argument for the input file
    parser.add_argument("input_file", type=str, help="The name of the PDF file to be converted.")

    # Parse the arguments
    args = parser.parse_args()

    # Call the main function with the provided arguments
    pdf_to_mid(args.input_file)
