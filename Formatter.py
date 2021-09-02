from datetime import datetime
from dateutil import tz


class Formatter:
    def __init__(self):
        self.games = []

    @staticmethod
    def is_valid_game(football_game):
        is_soccer = football_game[0] == 'soccer'
        has_proper_length = len(football_game) == 10
        if is_soccer:
            odds_in_range = float(football_game[7]) <= 2.5
            is_draw = football_game[3] == 'X'
        else:
            odds_in_range = False
            is_draw = False

        bookies = ['William Hill', 'Bet365', 'bwin', 'BetVictor', 'Paddy Power', 'Betfair', 'Unibet', 'Betway']
        is_valid_bookie = football_game[6] in bookies

        return is_soccer and has_proper_length and odds_in_range and not is_draw and is_valid_bookie

    def is_new_game(self, new_game):
        return not any([True if new_game[1] == gg[1] else False for gg in self.games])

    @staticmethod
    def format_time(time_str):
        hr_min_sec = time_str.split(':')
        hour = str(int(hr_min_sec[0])) + 'hr'
        if int(hr_min_sec[0]) < 1 and int(hr_min_sec[1]) < 1:
            minute = '01 min'
        else:
            minute = hr_min_sec[1] + 'min'
        return hour + ' ' + minute

    def format_message(self, lst):
        if lst[3] == '1':
            result = 'Home'
        elif lst[3] == '2':
            result = 'Away'
        else:
            result = 'Draw'

        time_to_kickoff = self.format_time(lst[5])
        cet = datetime.strptime(lst[4], '%Y-%m-%d %H:%M:%S')
        from_zone = tz.gettz('Europe/Berlin')
        to_zone = tz.gettz('Europe/London')

        local_time = cet.replace(tzinfo=from_zone).astimezone(to_zone)
        kick_off_time = local_time.strftime("%Y-%m-%d %H:%M:%S")

        message = f'''
        *New Value Opportunity*\n \
        *Match*: {lst[1]}\n \
        *League*: {lst[2]}\n \
        *Result to bet*: {result}\n \
        *Targeted Value Odds*: {lst[7]}\n \
        *Bookmaker*: {lst[6]}\n \
        *Kick off time*: {kick_off_time}\n \
        Time to start of the game: {time_to_kickoff}\n \
        \n_Remember to only bet if the value odds are still live and only bet with the same stake (1/50th of total bankroll)._
        '''
        return message


