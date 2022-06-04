
import numpy as np
import random
PLAYER_1 = "X"
PLAYER_2 = "O"
mark_to_add = [[" ", " ", " "],
               [" ", " ", " "],
               [" ", " ", " "]]
score_board = np.zeros((3, 3))
if __name__ == '__main__':
    stop_playing = False
    old_raw_index = 3
    old_col_index = 3
    old_raw_index_random = 3
    old_col_index_random = 3
    while not stop_playing:
        print("player1: ")
        raw_index = int(input("add pour mark in position (row index [0,1,2]):  "))
        col_index = int(input("add pour mark in position (column index [0,1,2]):  "))
        if raw_index < 3 and col_index < 3 and score_board[raw_index, col_index] < 1:
            score_board[raw_index, col_index] = 1
            mark_to_add[raw_index][col_index] = PLAYER_1
            player_2_random_choice_row = random.randint(0, 2)
            player_2_random_choice_col = random.randint(0, 2)
            while score_board[player_2_random_choice_row, player_2_random_choice_col] > 0:
                player_2_random_choice_row = random.randint(0, 2)
                player_2_random_choice_col = random.randint(0, 2)
            score_board[player_2_random_choice_row, player_2_random_choice_col] = 4
            mark_to_add[player_2_random_choice_row][player_2_random_choice_col] = PLAYER_2
            print(f"""
           |------|-------|-------|
           |  {mark_to_add[0][0]}   |   {mark_to_add[0][1]}   |   {mark_to_add[0][2]}   |
           |------|-------|-------|
           |  {mark_to_add[1][0]}   |   {mark_to_add[1][1]}   |   {mark_to_add[1][2]}   |
           |------|-------|-------|
           |  {mark_to_add[2][0]}   |   {mark_to_add[2][1]}   |   {mark_to_add[2][2]}   |
           |------|-------|-------|
            """)
            sum_raw = np.sum(score_board, axis=1)
            sum_col = np.sum(score_board, axis=0)
            sum_diagonal = np.sum(score_board.diagonal())
            if (sum_diagonal == 3) or (3 in sum_raw) or (3 in sum_col):
                stop_playing = True
                print("You win!")
            if (sum_diagonal == 12) or (12 in sum_raw) or (12 in sum_col):
                stop_playing = True
                print("You lose.")

        else:
            print("choose another index in this range [0, 1, 2]")
    print("GAME OVER")
