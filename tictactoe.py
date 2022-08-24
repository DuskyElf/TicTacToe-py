# tictactoe by DuskyElf

# Board representation class
class Board:
    # Constants
    N = 0
    X = 1
    O = 2
    
    # Initialization
    def __init__(self):
        self.boardState = [
            [Board.N, Board.N, Board.N],
            [Board.N, Board.N, Board.N],
            [Board.N, Board.N, Board.N]
        ]
    
    # For playing a move
    def move(self, place, player):
        self.boardState[place[0]][place[1]] = player
    
    # String representation for the board
    def display(self):
        result = ""
        result += "___________\n"
        for i in self.boardState:
            result += "|"
            for j in i:
                if j==Board.N:
                    result += '_ _'
                elif j==Board.X:
                    result += '_X_'
                elif j==Board.O:
                    result += '_O_'
            result += "|\n"
        return result

# Game representation class
class Game():
    #utility
    def s(player):
        if player==Board.N:
            return ''
        if player==Board.X:
            return 'X'
        if player==Board.O:
            return 'O'
    
    #Initialization
    def __init__(self):
        self.board = Board()
        self.current_player = Board.N
        self.running = True
        self.gameLap = 0
        self.winner = Board.N
    
    # Main Game loop
    def gameLoop(self):
        # Initializing the first move's player
        self.current_player = Board.X
        
        while self.running:
            self.gameLap += 1
            
            responce = self.askPlayer(self.current_player)
            self.board.move(responce, self.current_player)
            self.incrementPlayer()
            print(self.board.display())
            
            self.winner = self.winCheck()
            
            if self.winner != Board.N:
                self.winAnnounce()
    
    # Player input
    def askPlayer(self, player):
        done = False
        while not done:
            row = int(input(f"[{self.gameLap}] Player {Game.s(player)} your turn row number (1, 2, 3): ")) - 1
            collum = int(input(f"[{self.gameLap}] Player {Game.s(player)} your turn collum number (1, 2, 3): ")) - 1
            done = self.validMove((row, collum))
        
        return row, collum
    
    # Checking if the move is valid or not
    def validMove(self, move):
        if move[0] > 2 or move[1] > 2:
            return False
        return self.board.boardState[move[0]][move[1]] == Board.N
    
    # Incrementing for the next player
    def incrementPlayer(self):
        if self.current_player == Board.X:
            self.current_player = Board.O
        else:
            self.current_player = Board.X
    
    # Announcment for the win    
    def winAnnounce(self):
        print(f"Player {Game.s(self.winner)} won the game in {self.gameLap} Game laps.")
        print("Whoooo!!")
        self.running = False
    
    # Check for the win
    def winCheck(self):
        b = self.board.boardState
        winner = Board.N
        
        for i in range(3):
            #Horizontal check
            if b[i][0] == b[i][1] == b[i][2]:
                winner = b[i][0]
            
            #Vertical check
            if b[0][i] == b[1][i] == b[2][i]:
                winner = b[0][i]
        
        # Diagonal checks
        if b[0][0] == b[1][1] == b[2][2]:
            winner = b[0][0]
            
        if b[2][0] == b[1][1] == b[0][2]:
            winner = b[2][0]
        
        return winner

def main():
    game = Game()
    game.gameLoop()

if __name__ == "__main__":
    main()
