import time
from urllib.request import urlopen
from bs4 import BeautifulSoup
from GamesManager import GamesManager
from config import url, token, chat_id
import telegram


if __name__ == '__main__':
    request = telegram.utils.request.Request(read_timeout=10)  # The read timeout for network connections in seconds.
    bot = telegram.Bot(token, request=request)
    gm = GamesManager()

    while True:
        try:
            page = urlopen(url)
        except Exception as e:
            print(e)
            break

        soup = BeautifulSoup(page, 'html.parser')
        rows = soup.find_all('tr', class_='accordion-toggle')
        for row in rows:
            game = [x.text for x in row.find_all('td')]
            game.append(row['data-matchid'])
            if gm.is_valid_game(game):
                if gm.is_new_game(game):
                    msg = gm.format_message(game)
                    print(msg)
                    # bot.sendMessage(chat_id, msg, parse_mode="Markdown")
                    gm.games.append(game)
        time.sleep(10)

