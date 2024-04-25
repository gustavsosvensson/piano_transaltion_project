from mido import MidiFile

def midi_file_ticks(midi_file_path):
    midi = MidiFile(midi_file_path)
    tempo = 250000  # Default MIDI tempo (microseconds per beat)
    ticks_per_beat = midi.ticks_per_beat
    total_length_ticks = 0
    total_length_seconds = 0.0

    for track in midi.tracks:
        track_length_ticks = 0
        for msg in track:
            track_length_ticks += msg.time
            if msg.type == 'set_tempo':
                tempo = msg.tempo
        total_length_ticks += track_length_ticks
        # Convert the track length from ticks to seconds

    return track_length_ticks

# Example usage
#file_path = r"C:\Users\User\OneDrive\Dokument\Audiveris\output_page_0\output_page_0.mid"
#length_ticks = midi_file_length_in_seconds(file_path)
#print(f"Total length of the MIDI file is {length_ticks} ticks.")
