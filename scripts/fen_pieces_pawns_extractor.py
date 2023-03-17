import re

def filter_pgn(input_file, output_file, fen_filter):
    with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
        game_lines = []
        keep_game = False
        for line in f_in:
            if line.startswith('[Event'):
                if game_lines and keep_game:
                    f_out.writelines(game_lines)
                game_lines = [line]
            elif line.startswith('[FEN'):
                fen = re.search(r'\"(.+?)\"', line).group(1)
                pieces = fen.split()[0].replace('/', '')
                num_pieces = sum(1 for c in pieces if c.isalpha())
                num_pawns = pieces.count('p') + pieces.count('P')
                keep_game = num_pieces == fen_filter[0] and num_pawns == fen_filter[1]
                game_lines.append(line)
            else:
                game_lines.append(line)
        if game_lines and keep_game:
            f_out.writelines(game_lines)

input_file = 'fide.pgn'
for num_pieces in range(5, 21):
    for num_pawns in range(0, num_pieces - 2):
        output_file = f'fide_{num_pieces}_pieces_{num_pawns}_pawns.pgn'
        fen_filter = (num_pieces, num_pawns)
        filter_pgn(input_file, output_file, fen_filter)