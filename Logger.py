import os
import csv
import pandas as pd


class Logger:
    """Create, open and manipulate game logs """

    def __init__(self, file_name='games_logs.csv'):
        self.file_name = file_name

    def load_games(self):
        self.check_file_name()
        if os.path.isfile(self.file_name):
            return pd.read_csv(self.file_name)
        else:
            return pd.DataFrame(columns=['Sport', 'Match Title', 'League', 'Result to Bet', 'Date', 'Time to Match',
                                         'Best Bookie', 'Best Odds', 'Mean / Median', 'Match_id'])

    @staticmethod
    def is_new_game(df, match_id):
        found = df[df['Match_id'].str.contains(match_id)]
        return found['Match_id'].count() == 0

    def check_file_name(self):
        if not self.file_name:
            raise Exception('File Name cannot be empty')

        if not self.file_name.endswith('.csv'):
            raise Exception('File must have .csv extension')

    @staticmethod
    def add_game(df, game):
        df.loc[df.shape[0]] = game
        return df
