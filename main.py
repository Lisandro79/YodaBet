import time
from urllib.request import urlopen
from bs4 import BeautifulSoup
from Formatter import Formatter
from config import url, token, chat_id, log_file_name, token_saldinor, chat_id_saldinor
import telegram
from Logger import Logger


if __name__ == '__main__':
    request = telegram.utils.request.Request(read_timeout=10)  # The read timeout for network connections in seconds.
    bot = telegram.Bot(token, request=request)
    bot_test = telegram.Bot(token_saldinor, request=request)
    gm = Formatter()
    logger = Logger(log_file_name)  # load games into dataframe
    df = logger.load_games()

    while True:
        try:
            page = urlopen(url)
        except Exception as e:
            print(e)
            bot_test.sendMessage(chat_id_saldinor, "Server Down!", parse_mode="Markdown")
            break

        soup = BeautifulSoup(page, 'html.parser')
        rows = soup.find_all('tr', class_='accordion-toggle')
        for row in rows:
            match_id = row['data-matchid']
            game = [x.text for x in row.find_all('td')]
            game.append(match_id)
            if gm.is_valid_game_format(game) and logger.is_new_game(df, match_id):
                msg = gm.format_message(game)
                print(msg)
                bot.sendMessage(chat_id, msg, parse_mode="Markdown")
                time.sleep(0.1)
                bot_test.sendMessage(chat_id_saldinor, msg, parse_mode="Markdown")
                time.sleep(0.1)
                df = logger.add_game(df, game)
        time.sleep(5)
        # serialize games
        df.to_csv(logger.file_name, index=False)
