import os

def absolute_output_png_folders():
    output_png_folder = os.path.join("..", "..", "Ideal Piano (for Windows)", "Ideal Piano", "data", "pdf_to_png_output_folder")
    absolute_output_png_folder = os.path.abspath(output_png_folder)
    return absolute_output_png_folder

def absolute_output_mxl_folders():
    output_mxl_folder = os.path.join("..\..", "Ideal Piano (for Windows)", "Ideal Piano", "data", "png_to_mxl_output")
    absolute_output_mxl_folder = os.path.abspath(output_mxl_folder)
    return absolute_output_mxl_folder

def absolute_output_mid_folders():
    output_mid_folder = os.path.join("..\..", "Ideal Piano (for Windows)", "Ideal Piano", "data", "mxl_to_mid_output")
    absolute_output_mid_folder = os.path.abspath(output_mid_folder)
    return absolute_output_mid_folder

def absolute_output_merged_midi_folders():
    output_merged_midi_folder = os.path.join("..\..", "Ideal Piano (for Windows)", "Ideal Piano", "data", "merged_midi_output")
    absolute_output_merged_midi_folders = os.path.abspath(output_merged_midi_folder)
    return absolute_output_merged_midi_folders
