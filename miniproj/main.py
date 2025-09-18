from checkmate import checkmate

def main():
    board = """\
R...
.K..
..P.
....\
"""
    checkmate(board)  


    board1 = """\
R...
.K..
...P
....\
"""
    checkmate(board1)  

if __name__ == "__main__":
    main()
