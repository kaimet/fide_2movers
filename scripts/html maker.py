import re

html_part1 = """
<!DOCTYPE html>
<html>
<head>
  <link rel="stylesheet" href="css/chessboard-1.0.0.min.css">
  <script src="https://code.jquery.com/jquery-3.5.1.min.js"></script>
  <script src="js/chessboard-1.0.0.min.js"></script>
</head>
<body>

<div id="boards" style="width: 400px"></div>

<script type="text/javascript">
  // Wrap the generated JavaScript code in a function
  function createBoards() {
  
"""

html_part2 = ""

html_part3a = """

  }

  // Number of Chessboard objects
  var num_boards = """

html_part3b = """;

  // Loop through each Chessboard object
  for (var i = 0; i < num_boards; i++) {
    // Generate a unique ID for this Chessboard object
    var board_id = 'board' + i;

    // Create a new DOM node with this ID
    var board_node = $('<div>').attr('id', board_id);

    // Append this node to the #boards container
    $('#boards').append(board_node);

    // Add a line break after this board
    $('#boards').append('<br>');
  }

  // Call the createBoards function to create the Chessboard objects
  createBoards();
</script>

</body>
</html>
  
"""

def filter_pgn(input_file, output_file, fen_filter):
    i = 0
    html_part2 = ""
    fen = ""
    with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
        for line in f_in:
            if line.startswith('[FEN'):
                fen = re.search(r'\"(.+?)\"', line).group(1)
                pieces = fen.split()[0].replace('/', '')
                num_pieces = sum(1 for c in pieces if c.isalpha())
                num_pawns = pieces.count('p') + pieces.count('P')
                keep_game = num_pieces == fen_filter[0] and num_pawns == fen_filter[1]
                if keep_game:
                    board_id = f"board{i}"
                    html_part2 += f"var board{i} = Chessboard('{board_id}', {{ position: '{fen}' }});\n"
                    i += 1
                    
        f_out.write(html_part1 + html_part2 + html_part3a + str(i) + html_part3b)
        
        
input_file = 'fide.pgn'
for num_pieces in range(7, 25):
    for num_pawns in range(0, num_pieces-2):
        output_file = f'fide_{num_pieces}_pieces_{num_pawns}_pawns.html'
        fen_filter = (num_pieces, num_pawns)
        filter_pgn(input_file, output_file, fen_filter)




