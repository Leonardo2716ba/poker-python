class Player:
    def __init__(self):
        self.score = 3
        self.addr = 0
        self.username = ""
        self.resposta = ""
        
    def updare(self, score, username, addr):
        self.set_score(score)
        self.set_username(username)
        self.set_addr(addr)

    def get_score(self):
        return self.score

    def set_score(self, score):
        self.score = score

    def get_username(self):
        return self.username

    def set_username(self, username):
        self.username = username
    def set_addr(self, adrr):
        self.addr = adrr
        
    def get_addr(self):
        return self.addr
    
    def display_info(self):
        return f"Player Information:\nScore: {self.score}\nUsername: {self.username}\nAddr:{self.addr}"

# Example usage:
if __name__ == "__main__":
    # Create a Player instance
    player1 = Player(score=100, username="john123")

    # Display player information
    print(player1.display_info())

    # Use setter method to change the score
    player1.score = 150

    # Display updated information using getter methods
    print(player1.display_info())
