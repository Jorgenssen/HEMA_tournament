#!/usr/bin/python
#-------------------------------------------------------------------------------------
#             FILE: fencer.py
#      DESCRIPTION: class module providing the base fencer entity
#           AUTHOR: Nikita Tatiannikov, n.tatyannikov@gmail.com
#          COMPANY: Tramazzone
#          VERSION: 0.03
# VERSIONS HISTORY: 2018-01-11 (0.01) - base attributes
#                   2018-01-13 (0.02) - attribute ID was added
#                   2018-02-11 (0.03) - attribute had_fights_with was added
#-------------------------------------------------------------------------------------

class Fencer():
    def __init__(self, ID, name, club, wins, defeats, hits_got, hits_given, had_fights_with):
        self.name = name
        self.club = club
        self.wins = wins
        self.defeats = defeats
        self.hits_got = hits_got
        self.hits_given = hits_given
        self.ID = ID
        self.had_fights_with = had_fights_with
