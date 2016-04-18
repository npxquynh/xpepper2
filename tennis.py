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
    def __init__(self, player_1_name, player_2_name):
        self.player_1_name = player_1_name
        self.player_2_name = player_2_name
        self.player_1_points = 0
        self.player_2_points = 0

    def won_point(self, playerName):
        if playerName == self.player_1_name:
            self._increase_player_1_point()
        else:
            self._increase_player_2_point()

    def score(self):
        result = ""
        if self.player_1_points == self.player_2_points and self.player_1_points < 3:
            if self.player_1_points == 0:
                result = "Love"
            if self.player_1_points == 1:
                result = "Fifteen"
            if self.player_1_points == 2:
                result = "Thirty"
            result += "-All"
        if self.player_1_points == self.player_2_points and self.player_1_points>2:
            result = "Deuce"

        player_1_pointsres = ""
        player_2_pointsres = ""
        if self.player_1_points > 0 and self.player_2_points == 0:
            if self.player_1_points == 1:
                player_1_pointsres = "Fifteen"
            if self.player_1_points == 2:
                player_1_pointsres = "Thirty"
            if self.player_1_points == 3:
                player_1_pointsres = "Forty"

            player_2_pointsres = "Love"
            result = player_1_pointsres + "-" + player_2_pointsres
        if self.player_2_points > 0 and self.player_1_points == 0:
            if self.player_2_points == 1:
                player_2_pointsres = "Fifteen"
            if self.player_2_points == 2:
                player_2_pointsres = "Thirty"
            if self.player_2_points == 3:
                player_2_pointsres = "Forty"

            player_1_pointsres = "Love"
            result = player_1_pointsres + "-" + player_2_pointsres


        if self.player_1_points>self.player_2_points and self.player_1_points < 4:
            if self.player_1_points == 2:
                player_1_pointsres = "Thirty"
            if self.player_1_points == 3:
                player_1_pointsres = "Forty"
            if self.player_2_points == 1:
                player_2_pointsres = "Fifteen"
            if self.player_2_points == 2:
                player_2_pointsres = "Thirty"
            result = player_1_pointsres + "-" + player_2_pointsres
        if self.player_2_points>self.player_1_points and self.player_2_points < 4:
            if self.player_2_points == 2:
                player_2_pointsres = "Thirty"
            if self.player_2_points == 3:
                player_2_pointsres = "Forty"
            if self.player_1_points == 1:
                player_1_pointsres = "Fifteen"
            if self.player_1_points == 2:
                player_1_pointsres = "Thirty"
            result = player_1_pointsres + "-" + player_2_pointsres

        if self.player_1_points > self.player_2_points and self.player_2_points >= 3:
            result = "Advantage " + self.player_1_name

        if self.player_2_points > self.player_1_points and self.player_1_points >= 3:
            result = "Advantage " + self.player_2_name

        if self.player_1_points >= 4 and self.player_2_points >= 0 and (self.player_1_points-self.player_2_points) >= 2:
            result = "Win for " + self.player_1_name
        if self.player_2_points >= 4 and self.player_1_points >= 0 and (self.player_2_points-self.player_1_points) >= 2:
            result = "Win for " + self.player_2_name
        return result

    def set_player_1_score(self, number):
        for i in range(number):
            self._increase_player_1_point()

    def set_player_2_score(self, number):
        for i in range(number):
            self._increase_player_2_point()

    def _increase_player_1_point(self):
        self.player_1_points += 1

    def _increase_player_2_point(self):
        self.player_2_points += 1


class TennisGame3:
    def __init__(self, player_1_name, player_2_name):
        self.player_1_name = player_1_name
        self.player_2_name = player_2_name
        self.player_1_points = 0
        self.player_2_points = 0

    def won_point(self, n):
        if n == self.player_1_name:
            self.player_1_points += 1
        else:
            self.player_2_points += 1

    def score(self):
        if (self.player_1_points < 4 and self.player_2_points < 4) and (self.player_1_points + self.player_2_points < 6):
            p = ["Love", "Fifteen", "Thirty", "Forty"]
            s = p[self.player_1_points]
            return s + "-All" if (self.player_1_points == self.player_2_points) else s + "-" + p[self.player_2_points]
        else:
            if (self.player_1_points == self.player_2_points):
                return "Deuce"
            s = self.player_1_name if self.player_1_points > self.player_2_points else self.player_2_name
            return "Advantage " + s if ((self.player_1_points-self.player_2_points)*(self.player_1_points-self.player_2_points) == 1) else "Win for " + s
