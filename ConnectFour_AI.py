import pygame
import sys
import random

class ConnectFour:
    def __init__(self):
        self.board = [
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
        ]
        self.players = ["Red Side", "Yellow Side"]
        self.current_player = 0

        #Pygame 初始化
        pygame.init()

        #設定顯示尺寸
        self.cell_size = 100
        self.width = 7 * self.cell_size
        self.height = 6 * self.cell_size
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Connect Four")

        #設定顏色
        self.white = (255, 255, 255)
        self.red = (255, 0, 0)
        self.yellow = (255, 255, 0)
        self.black = (0, 0, 0)
        self.blue = (0, 0, 255)

    #畫出遊戲板
    def draw_board(self):
        self.screen.fill(self.white)
        for row in range(6):
            for col in range(7):
                pygame.draw.rect(self.screen, self.blue, (col * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size))
                pygame.draw.circle(self.screen, self.white, (col * self.cell_size + self.cell_size // 2, row * self.cell_size + self.cell_size // 2), self.cell_size // 2 - 5)

        for row in range(6):
            for col in range(7):
                player_piece = self.board[row][col]
                if player_piece == "Red Side":
                    pygame.draw.circle(self.screen, self.red, (col * self.cell_size + self.cell_size // 2, row * self.cell_size + self.cell_size // 2), self.cell_size // 2 - 5)
                elif player_piece == "Yellow Side":
                    pygame.draw.circle(self.screen, self.yellow, (col * self.cell_size + self.cell_size // 2, row * self.cell_size + self.cell_size // 2), self.cell_size // 2 - 5)

    #玩家下棋動作
    def make_move(self, column):
        for row in range(5, -1, -1):
            if self.board[row][column] == " ":
                self.board[row][column] = self.players[self.current_player]
                return True
        return False

    #遊戲主要架構
    def play(self):
        clock = pygame.time.Clock()
        game_over = False

        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                    column = event.pos[0] // self.cell_size
                    if self.make_move(column):
                        if self.check_winner():
                            game_over = True
                            winner_text = f"Winner: {self.players[self.current_player]}"
                        elif self.is_board_full():
                            game_over = True
                            winner_text = "It's a draw!"
                        else:
                            self.current_player = 1 - self.current_player

            self.draw_board()
            pygame.display.flip()
            clock.tick(30)

        #顯示結果
        font = pygame.font.Font(None, 36)
        text = font.render(winner_text, True, self.black)
        text_rect = text.get_rect(center=(self.width // 2, self.height // 2))
        self.screen.blit(text, text_rect)
        pygame.display.flip()

        #等待遊戲自動結束
        pygame.time.wait(2000)
        pygame.quit()
        sys.exit()

    #判定獲勝方
    def check_winner(self):
        #檢查橫列
        for row in range(6):
            for col in range(4):
                if (
                    self.board[row][col]
                    == self.board[row][col + 1]
                    == self.board[row][col + 2]
                    == self.board[row][col + 3]
                    != " "
                ):
                    return True

        #檢查直行
        for col in range(7):
            for row in range(3):
                if (
                    self.board[row][col]
                    == self.board[row + 1][col]
                    == self.board[row + 2][col]
                    == self.board[row + 3][col]
                    != " "
                ):
                    return True

        #檢查斜線
        for row in range(3):
            for col in range(4):
                if (
                    self.board[row][col]
                    == self.board[row + 1][col + 1]
                    == self.board[row + 2][col + 2]
                    == self.board[row + 3][col + 3]
                    != " "
                ):
                    return True

                if (
                    self.board[row][col + 3]
                    == self.board[row + 1][col + 2]
                    == self.board[row + 2][col + 1]
                    == self.board[row + 3][col]
                    != " "
                ):
                    return True

        return False

    #檢查是否已滿
    def is_board_full(self):
        return all(cell != " " for row in self.board for cell in row)

class ConnectFour_ai:
    def __init__(self):
        self.board = [
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
        ]
        self.players = ["Player", "AI"]
        self.current_player = 0

        pygame.init()

        self.cell_size = 100
        self.width = 7 * self.cell_size
        self.height = 6 * self.cell_size
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Connect Four")

        self.white = (255, 255, 255)
        self.red = (255, 0, 0)
        self.yellow = (255, 255, 0)
        self.black = (0, 0, 0)
        self.blue = (0, 0, 255)

    def draw_board(self):
        self.screen.fill(self.white)
        for row in range(6):
            for col in range(7):
                pygame.draw.rect(self.screen, self.blue, (col * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size))
                pygame.draw.circle(self.screen, self.white, (col * self.cell_size + self.cell_size // 2, row * self.cell_size + self.cell_size // 2), self.cell_size // 2 - 5)

        for row in range(6):
            for col in range(7):
                player_piece = self.board[row][col]
                if player_piece == "Player":
                    pygame.draw.circle(self.screen, self.red, (col * self.cell_size + self.cell_size // 2, row * self.cell_size + self.cell_size // 2), self.cell_size // 2 - 5)
                elif player_piece == "AI":
                    pygame.draw.circle(self.screen, self.yellow, (col * self.cell_size + self.cell_size // 2, row * self.cell_size + self.cell_size // 2), self.cell_size // 2 - 5)

    def make_move(self, column):
        #玩家回合
        if self.current_player == 0:
            for row in range(5, -1, -1):
                if self.board[row][column] == " ":
                    self.board[row][column] = self.players[self.current_player]
                    return True
            return False
        #AI回合
        else:
            available_columns = [col for col in range(7) if self.board[0][col] == " "]
            for ai_column in available_columns:
                for row in range(5, -1, -1):
                    if self.board[row][ai_column] == " ":
                        #檢查AI是否能獲勝
                        self.board[row][ai_column] = self.players[self.current_player]
                        if self.check_winner():
                            return True
                        self.board[row][ai_column] = " "

                        #檢查玩家是否會獲勝
                        self.board[row][ai_column] = self.players[1 - self.current_player]
                        if self.check_winner():
                            self.board[row][ai_column] = self.players[self.current_player]
                            return True
                        self.board[row][ai_column] = " "
                        break

            if available_columns:
                ai_column = random.choice(available_columns)
                for row in range(5, -1, -1):
                    if self.board[row][ai_column] == " ":
                        self.board[row][ai_column] = self.players[self.current_player]
                        return True
            return False

    def play(self):
        clock = pygame.time.Clock()
        game_over = False

        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                    column = event.pos[0] // self.cell_size
                    if self.make_move(column):
                        if self.check_winner():
                            game_over = True
                            winner_text = f"Winner: {self.players[self.current_player]}"
                        elif self.is_board_full():
                            game_over = True
                            winner_text = "It's a draw!"
                        else:
                            self.current_player = 1 - self.current_player

            self.draw_board()
            pygame.display.flip()
            clock.tick(30)

        font = pygame.font.Font(None, 36)
        text = font.render(winner_text, True, self.black)
        text_rect = text.get_rect(center=(self.width // 2, self.height // 2))
        self.screen.blit(text, text_rect)
        pygame.display.flip()

        pygame.time.wait(2000)
        pygame.quit()
        sys.exit()

    def check_winner(self):

        for row in range(6):
            for col in range(4):
                if (
                    self.board[row][col]
                    == self.board[row][col + 1]
                    == self.board[row][col + 2]
                    == self.board[row][col + 3]
                    != " "
                ):
                    return True

        for col in range(7):
            for row in range(3):
                if (
                    self.board[row][col]
                    == self.board[row + 1][col]
                    == self.board[row + 2][col]
                    == self.board[row + 3][col]
                    != " "
                ):
                    return True

        for row in range(3):
            for col in range(4):
                if (
                    self.board[row][col]
                    == self.board[row + 1][col + 1]
                    == self.board[row + 2][col + 2]
                    == self.board[row + 3][col + 3]
                    != " "
                ):
                    return True

                if (
                    self.board[row][col + 3]
                    == self.board[row + 1][col + 2]
                    == self.board[row + 2][col + 1]
                    == self.board[row + 3][col]
                    != " "
                ):
                    return True

        return False

    def is_board_full(self):
        return all(cell != " " for row in self.board for cell in row)

if __name__ == "__main__":
    mode=str(input("(1)One Player (2)Two Players"))
    while 1:
        if mode=="1":
            game = ConnectFour_ai()
            break
        if mode=="2":
            game = ConnectFour()
            break
        else:
            mode=str(input("Please Enter 1 or 2："))
    game.play()
