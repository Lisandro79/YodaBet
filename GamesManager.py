class GamesManager:
    def __init__(self):
        self.games = []

    @staticmethod
    def is_valid_game(football_game):
        is_soccer = football_game[0] == 'soccer'
        has_proper_length = len(football_game) == 9
        if is_soccer:
            odds_in_range = float(football_game[7]) <= 2.5
            is_draw = football_game[3] == 'X'
        else:
            odds_in_range = False
            is_draw = False

        return is_soccer and has_proper_length and odds_in_range and not is_draw

    def is_new_game(self, new_game):
        return not any([True if new_game[1] == gg[1] else False for gg in self.games])

    def remove_game_from_list(self):
        pass

    def add_game_to_list(self):
        pass

    @staticmethod
    def format_message(lst):
        if lst[3] == '1':
            result = 'Home'
        elif lst[3] == '2':
            result = 'Away'
        else:
            result = 'Draw'

        message = f'''
        *New Value Opportunity!*\n \
        Match: {lst[1]}\n \
        League: {lst[2]}\n \
        Result to bet: *{result}*\n \
        @odds: *{lst[7]}*\n \
        Bookmaker: {lst[6]}\n \
        Time to start of the game: {lst[5]}\n
        '''
        return message
