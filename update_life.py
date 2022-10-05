#!/usr/bin/env python3

import re
from pprint import pprint

with open('README.md', 'r') as readme:
    lines = readme.readlines()
assert lines[16] == '\n'
emoji_board = lines[:16]
assert all(map(re.compile('(?::(?:white|black)_large_square:  ){16}\n').fullmatch, emoji_board))

cell = re.compile(':(white|black)_large_square:')
board = [ [c == "black" for c in cell.findall(line)] for line in emoji_board ]

N = len(board)
# My clever midnight brain: assert all(map(N.__eq__, map(list.__len__, board)))
assert all(len(line) == N for line in board)

def neighbors(board, i, j):
    return (
        board[(i-1)%N][(j-1)%N] + board[(i-1)%N][j%N] + board[(i-1)%N][(j+1)%N] +
        board[(i)%N][(j-1)%N]                         + board[(i)%N][(j+1)%N]   +
        board[(i+1)%N][(j-1)%N] + board[(i+1)%N][j%N] + board[(i+1)%N][(j+1)%N]
    )

def game_step(board):
    new_board = []
    for i in range(N):
        new_row = []
        for j in range(N):
            n = neighbors(board, i, j)
            if board[i][j]:
                new_row.append(n == 2 or n == 3)
            else:
                new_row.append(n == 3)
        new_board.append(new_row)
    return new_board

board = game_step(board)

for i, line in enumerate(board):
    lines[i] = ''
    for cell in line:
        lines[i] += f':{"black" if cell else "white"}_large_square:  '
    lines[i] += '\n'

with open('README.md', 'w') as readme:
    readme.writelines(lines)

# vim:ts=4 et
