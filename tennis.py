# -*- coding: utf-8 -*-

class TennisGame1:
    def __init__(self, player_1_name, player_2_name):
        self.player_1_name = player_1_name
        self.player_2_name = player_2_name
        self.player_1_points = 0
        self.player_2_points = 0

    def won_point(self, playerName):
        if playerName == self.player_1_name:
            self.player_1_points += 1
        else:
            self.player_2_points += 1

    def score(self):
        default_score_name = {
            0 : "Love",
            1 : "Fifteen",
            2 : "Thirty",
            3 : "Forty",
        }

        tie_score_name = {
            0 : "Love-All",
            1 : "Fifteen-All",
            2 : "Thirty-All",
        }

        advantage_phrase = "Advantage %s"
        winning_phrase = "Win for %s"

        result = ""
        # Handling special case
        if self.player_1_points == self.player_2_points:
            result = tie_score_name.get(self.player_1_points, "Deuce")
        elif self.player_1_points <= 3 and self.player_2_points <= 3:
            result = "%s-%s" % (default_score_name[self.player_1_points], default_score_name[self.player_2_points])
        else:
            if self.player_1_points - self.player_2_points == 1:
                result = advantage_phrase % self.player_1_name
            elif self.player_2_points - self.player_1_points == 1:
                result = advantage_phrase % self.player_2_name
            elif self.player_1_points - self.player_2_points >= 2:
                result = winning_phrase % self.player_1_name
            else:
                result = winning_phrase % self.player_2_name

        return result


class TennisGame2:
    def __init__(self, player1Name, player2Name):
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.p1points = 0
        self.p2points = 0

    def won_point(self, playerName):
        if playerName == self.player1Name:
            self.IncreaseP1Point()
        else:
            self.IncreaseP2Point()

    def score(self):
        result = ""
        if self.p1points == self.p2points and self.p1points < 3:
            if self.p1points == 0:
                result = "Love"
            if self.p1points == 1:
                result = "Fifteen"
            if self.p1points == 2:
                result = "Thirty"
            result += "-All"
        if self.p1points == self.p2points and self.p1points>2:
            result = "Deuce"

        P1res = ""
        P2res = ""
        if self.p1points > 0 and self.p2points == 0:
            if self.p1points == 1:
                P1res = "Fifteen"
            if self.p1points == 2:
                P1res = "Thirty"
            if self.p1points == 3:
                P1res = "Forty"

            P2res = "Love"
            result = P1res + "-" + P2res
        if self.p2points > 0 and self.p1points == 0:
            if self.p2points == 1:
                P2res = "Fifteen"
            if self.p2points == 2:
                P2res = "Thirty"
            if self.p2points == 3:
                P2res = "Forty"

            P1res = "Love"
            result = P1res + "-" + P2res


        if self.p1points>self.p2points and self.p1points < 4:
            if self.p1points == 2:
                P1res = "Thirty"
            if self.p1points == 3:
                P1res = "Forty"
            if self.p2points == 1:
                P2res = "Fifteen"
            if self.p2points == 2:
                P2res = "Thirty"
            result = P1res + "-" + P2res
        if self.p2points>self.p1points and self.p2points < 4:
            if self.p2points == 2:
                P2res = "Thirty"
            if self.p2points == 3:
                P2res = "Forty"
            if self.p1points == 1:
                P1res = "Fifteen"
            if self.p1points == 2:
                P1res = "Thirty"
            result = P1res + "-" + P2res

        if self.p1points > self.p2points and self.p2points >= 3:
            result = "Advantage " + self.player1Name

        if self.p2points > self.p1points and self.p1points >= 3:
            result = "Advantage " + self.player2Name

        if self.p1points >= 4 and self.p2points >= 0 and (self.p1points-self.p2points) >= 2:
            result = "Win for " + self.player1Name
        if self.p2points >= 4 and self.p1points >= 0 and (self.p2points-self.p1points) >= 2:
            result = "Win for " + self.player2Name
        return result

    def SetP1Score(self, number):
        for i in range(number):
            self.IncreaseP1Point()

    def SetP2Score(self, number):
        for i in range(number):
            self.IncreaseP2Point()

    def IncreaseP1Point(self):
        self.p1points += 1


    def IncreaseP2Point(self):
        self.p2points += 1

class TennisGame3:
    def __init__(self, player1Name, player2Name):
        self.p1N = player1Name
        self.p2N = player2Name
        self.p1 = 0
        self.p2 = 0

    def won_point(self, n):
        if n == self.p1N:
            self.p1 += 1
        else:
            self.p2 += 1

    def score(self):
        if (self.p1 < 4 and self.p2 < 4) and (self.p1 + self.p2 < 6):
            p = ["Love", "Fifteen", "Thirty", "Forty"]
            s = p[self.p1]
            return s + "-All" if (self.p1 == self.p2) else s + "-" + p[self.p2]
        else:
            if (self.p1 == self.p2):
                return "Deuce"
            s = self.p1N if self.p1 > self.p2 else self.p2N
            return "Advantage " + s if ((self.p1-self.p2)*(self.p1-self.p2) == 1) else "Win for " + s
