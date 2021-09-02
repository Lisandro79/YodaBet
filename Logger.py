import os
import csv
import pandas as pd


class Logger:
    """Create, open and manipulate game logs """

    def __init__(self, file_name='games_logs.csv'):
        self.file_name = file_name
        self.df = pd.DataFrame(columns=['Sport', 'Match Title', 'League', 'Result to Bet', 'Date', 'Time to Match',
                                        'Best Bookie', 'Best Odds', 'Mean / Median', 'Match_id'])

    def open_log(self):
        self.check_file_name()
        if os.path.isfile(self.file_name):
            self.df = pd.read_csv(self.file_name)

    def check_file_name(self):
        if not self.file_name:
            raise Exception('File Name cannot be empty')

        if not self.file_name.endswith('.csv'):
            raise Exception('File must have .csv extension')

    def add_game(self, game):
        self.df.loc[self.df.shape[0]]
