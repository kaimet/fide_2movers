import re

def filter_pgn(input_file, output_file, event_filter):
    with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
        keep_game = False
        for line in f_in:
            if line.startswith('[Event'):
                keep_game = event_filter in line
            if keep_game:
                f_out.write(line)

input_file = 'Mate en Dos.pgn'
output_file = 'output.pgn'
event_filter = 'FIDE Album'
filter_pgn(input_file, output_file, event_filter)