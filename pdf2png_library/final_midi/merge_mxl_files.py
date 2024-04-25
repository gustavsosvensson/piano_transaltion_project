import os

from mido import MidiFile, MidiTrack
from final_midi.midi_file_length import midi_file_ticks


def merge_midi_files_sequentially(output_folder, *input_files):
    # Create a new MIDI file (type 1 for multiple tracks)
    merged_midi = MidiFile(type=1)
    total_delay_ticks = 0  # Total delay to add to the start of each new file's tracks

    for file_path in input_files:
        midi = MidiFile(file_path)
        length_ticks = midi_file_ticks(file_path)

        for i, track in enumerate(midi.tracks):
            new_track = MidiTrack()
            first_msg = True
            for msg in track:
                # For the first message in each track of subsequent files, add the total delay
                if first_msg and not msg.is_meta:
                    new_msg = msg.copy(time=msg.time + total_delay_ticks)
                    new_track.append(new_msg)
                    first_msg = False
                else:
                    new_track.append(msg)
            merged_midi.tracks.append(new_track)

        # Optionally, increase total_delay_ticks by a fixed amount or based on the length of this file
        # For simplicity, here's a fixed increase, assuming 2 seconds between files at 500000 microseconds per beat
        # Adjust this based on the actual tempo and desired spacing between files
        total_delay_ticks += length_ticks + 240

    base_name = os.path.basename(input_files[0])
    base_name = base_name.split('.pdf_1')[0]

    filename = f"{base_name}.mid"

    full_path = os.path.join(output_folder, filename)

    # Save the merged MIDI file
    print("Conversion complete")
    merged_midi.save(full_path)