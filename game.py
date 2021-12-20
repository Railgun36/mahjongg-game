class Mahjongg():
    
    def __init__(self):
        self.players = [{"player1": {"name": "", "score": 0, "direction": "EAST", "win": 0, "roundpoints": 0}},
        {"player2": {"name": "", "score": 0, "direction": "SOUTH", "win": 0, "roundpoints": 0}},
        {"player3": {"name": "", "score": 0, "direction": "WEST", "win": 0, "roundpoints": 0}},
        {"player4": {"name": "", "score": 0, "direction": "NORD", "win": 0, "roundpoints": 0}}]
        self.players[0]["player1"]["name"] = input("Please insert Name for Player 1 (EAST): ")
        self.players[1]["player2"]["name"] = input("Please insert Name for Player 2 (SOUTH): ")
        self.players[2]["player3"]["name"] = input("Please insert Name for Player 3 (WEST): ")
        self.players[3]["player4"]["name"] = input("Please insert Name for Player 4 (NORD): ")
        
        self.round = 0

    def get_round_points(self):
        print(f"Please insert Points for Round Number {str(self.round)}")
        self.get_roundPointsPlayer1(self.players[0])
        self.get_roundPointsPlayer2(self.players[1])
        self.get_roundPointsPlayer3(self.players[2])
        self.get_roundPointsPlayer4(self.players[3])

    def get_winner(self):
        roundwinner = input("Please type in the winners name: ")
        self.is_winner(roundwinner)

        
    def get_roundPointsPlayer1(self, player):
        player[list(player.keys())[0]]["roundpoints"] = int(input(player["player1"]["name"] + " (" + player["player1"]["direction"] + "): "))
        if self.is_valid_number(player[list(player.keys())[0]]["roundpoints"]):
            return
        else:
            print("Invalid. Please try again")
            self.get_roundPointsPlayer1(self.players[0])            

    def get_roundPointsPlayer2(self, player):
        player[list(player.keys())[0]]["roundpoints"]  = int(input(player["player2"]["name"] + " (" + player["player2"]["direction"] + "): "))
        if self.is_valid_number(player[list(player.keys())[0]]["roundpoints"]):
            return
        else:
            print("Invalid. Please try again")
            self.get_roundPointsPlayer1(self.players[1])

    def get_roundPointsPlayer3(self, player):
        player[list(player.keys())[0]]["roundpoints"] = int(input(player["player3"]["name"] + " (" + player["player3"]["direction"] + "): "))
        if self.is_valid_number(player[list(player.keys())[0]]["roundpoints"]):
            return
        else:
            print("Invalid. Please try again")
            self.get_roundPointsPlayer1(self.players[2])

    def get_roundPointsPlayer4(self, player):
        player[list(player.keys())[0]]["roundpoints"] = int(input(player["player4"]["name"] + " (" + player["player4"]["direction"] + "): "))
        if self.is_valid_number(player[list(player.keys())[0]]["roundpoints"]):
            return
        else:
            print("Invalid. Please try again")
            self.get_roundPointsPlayer1(self.players[3])

    def is_valid_number(self, number):
        try:
            return int(number) >= 0
        except:
            return False

    def is_winner(self, winner):
        player_list = []
        for player in self.players:
            for key, value in player.items():
                player_list.append(value["name"])

        if winner in player_list:
            for player in self.players:
                for key, value in player.items():
                    if value["name"].lower() == winner.lower():
                        print(f"{winner} won the Game. Congrats.")
                        value["win"] = 1
                        
        else:
            print("Invalid input. Please try again")
            return self.get_winner()
    
    def calc_points(self):
        bool_defended = False
        defender = {}
        for player in self.players:
            if player[list(player.keys())[0]]["direction"] == "EAST" and player[list(player.keys())[0]]["win"] == 1:
                bool_defended = True
                defender.update(player)                    
        
        if bool_defended == True:
            self.defended(defender)
        else:
            self.not_defended()                                 

    def defended(self, defender):
        for player in self.players:
            if player == defender:
                player[list(player.keys())[0]]["score"] += (2*player[list(player.keys())[0]]["roundpoints"]) #RECHNUNG
                print("defender = " + defender[list(player.keys())[0]]["name"])
                player[list(player.keys())[0]]["roundpoints"] = 0
                player[list(player.keys())[0]]["win"] = 0 
            else:
                player[list(player.keys())[0]]["score"] += player[list(player.keys())[0]]["roundpoints"] #RECHNUNG
                player[list(player.keys())[0]]["roundpoints"] = 0
                player[list(player.keys())[0]]["win"] = 0

        

    def not_defended(self):
        print("No Defender")
        for player in self.players:
            player[list(player.keys())[0]]["score"] += player[list(player.keys())[0]]["roundpoints"] #RECHNUNG
            player[list(player.keys())[0]]["roundpoints"] = 0
            player[list(player.keys())[0]]["win"] = 0
            if player[list(player.keys())[0]]["direction"] == "EAST":
                player[list(player.keys())[0]]["direction"] = "SOUTH"
                continue
            elif player[list(player.keys())[0]]["direction"] == "SOUTH":
                player[list(player.keys())[0]]["direction"] = "WEST"
                continue
            elif player[list(player.keys())[0]]["direction"] == "WEST":
                player[list(player.keys())[0]]["direction"] = "NORD"
                continue
            elif player[list(player.keys())[0]]["direction"] == "NORD":
                player[list(player.keys())[0]]["direction"] = "EAST"

    def roundcounter(self, round):
        self.round = round + 1

    def print_points(self):
        print("AKTUELLER PUNKTESTAND: ")
        for player in self.players:
            print(player[list(player.keys())[0]]["name"] + " (" + player[list(player.keys())[0]]["direction"] + "): " + str(player[list(player.keys())[0]]["score"]))

    def play(self):
        while True:
            self.roundcounter(self.round)
            self.get_round_points()
            self.get_winner()
            self.calc_points()
            self.print_points()


    if __name__ == "__main__":
        play()


#Mahjongg().play()