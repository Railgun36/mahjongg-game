class Mahjongg:
    players = [
        {"player1": {"name": "", "score": 0, "direction": "EAST", "roundpoints": 0}},
        {"player2": {"name": "", "score": 0, "direction": "SOUTH", "roundpoints": 0}},
        {"player3": {"name": "", "score": 0, "direction": "WEST", "roundpoints": 0}},
        {"player4": {"name": "", "score": 0, "direction": "NORD", "roundpoints": 0}},
    ]
    directions = ["NORD", "WEST", "SOUTH", "EAST"]

    def __init__(self):
        pass

    def get_roundPointsPlayer(
        self,
        roundpoints_p1,
        roundpoints_p2,
        roundpoints_p3,
        roundpoints_p4,
        winner_value,
    ):
        for number in (roundpoints_p1, roundpoints_p2, roundpoints_p3, roundpoints_p4):
            self.is_valid_number(number)
        self.players[0]["player1"]["roundpoints"] = roundpoints_p1
        self.players[1]["player2"]["roundpoints"] = roundpoints_p2
        self.players[2]["player3"]["roundpoints"] = roundpoints_p3
        self.players[3]["player4"]["roundpoints"] = roundpoints_p4
        # ====== defended ?
        print(
            "Winner is: "
            + self.players[(winner_value - 1)][
                list(self.players[(winner_value - 1)].keys())[0]
            ]["name"]
        )
        self.points_of_winner = self.players[(winner_value - 1)][
            list(self.players[(winner_value - 1)].keys())[0]
        ]["roundpoints"]
        # ==check ob verteidigt oder nicht
        if (
            self.players[(winner_value - 1)][
                list(self.players[(winner_value - 1)].keys())[0]
            ]["direction"]
            == "EAST"
        ):
            self.defended(self.players[(winner_value - 1)])
        else:
            self.not_defended(self.players[(winner_value - 1)])

    def is_valid_number(self, number):
        try:
            return int(number) >= 0
        except:
            return False

    def defended(self, defender_dict):
        # ==Berechnung, wenn verteidigt wurde
        for player in self.players:
            if player == defender_dict:
                player[list(player.keys())[0]]["score"] += (
                    6 * player[list(player.keys())[0]]["roundpoints"]
                )  # RECHNUNG
                print("defender = " + defender_dict[list(player.keys())[0]]["name"])
            else:
                player[list(player.keys())[0]]["score"] -= (
                    2 * self.points_of_winner
                )  # RECHNUNG
                for abrechner in self.players:
                    if abrechner != defender_dict:
                        player[list(player.keys())[0]]["score"] = player[
                            list(player.keys())[0]
                        ]["score"] + (
                            player[list(player.keys())[0]]["roundpoints"]
                            - abrechner[list(abrechner.keys())[0]]["roundpoints"]
                        )
        self.reset_player()

    def not_defended(self, winner_dict):
        print("No Defender")
        # ==Berechnung, wenn nicht verteidigt wurde
        for player in self.players:
            if player == winner_dict:
                player[list(player.keys())[0]]["score"] += (
                    4 * player[list(player.keys())[0]]["roundpoints"]
                )
            elif player[list(player.keys())[0]]["direction"] == "EAST":
                player[list(player.keys())[0]]["score"] -= 2 * self.points_of_winner
                for abrechner in self.players:
                    if abrechner != winner_dict and abrechner != player:
                        player[list(player.keys())[0]]["score"] += 2 * (
                            player[list(player.keys())[0]]["roundpoints"]
                            - abrechner[list(abrechner.keys())[0]]["roundpoints"]
                        )
            else:
                player[list(player.keys())[0]]["score"] -= self.points_of_winner
                for abrechner in self.players:
                    if abrechner[list(abrechner.keys())[0]]["direction"] == "EAST":
                        player[list(player.keys())[0]]["score"] += 2 * (
                            player[list(player.keys())[0]]["roundpoints"]
                            - abrechner[list(abrechner.keys())[0]]["roundpoints"]
                        )

                    elif (
                        abrechner != winner_dict
                        and abrechner != player
                        and abrechner[list(abrechner.keys())[0]]["direction"] != "EAST"
                    ):
                        player[list(player.keys())[0]]["score"] += (
                            player[list(player.keys())[0]]["roundpoints"]
                            - abrechner[list(abrechner.keys())[0]]["roundpoints"]
                        )
            # == direction resetten
        for player in self.players:
            if (
                self.directions.index(player[list(player.keys())[0]]["direction"]) + 1
            ) <= 3:
                player[list(player.keys())[0]]["direction"] = self.directions[
                    (
                        self.directions.index(
                            player[list(player.keys())[0]]["direction"]
                        )
                        + 1
                    )
                ]
            else:
                player[list(player.keys())[0]]["direction"] = self.directions[
                    (
                        self.directions.index(
                            player[list(player.keys())[0]]["direction"]
                        )
                        - 3
                    )
                ]
        self.reset_player()

    def reset_player(self):
        for player in self.players:
            player[list(player.keys())[0]]["roundpoints"] = 0
