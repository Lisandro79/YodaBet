import time
from urllib.request import urlopen
from bs4 import BeautifulSoup
from GamesManager import GamesManager
from config import url, token, chat_id
import telegram


if __name__ == '__main__':
    request = telegram.utils.request.Request(read_timeout=2)
    bot = telegram.Bot(token, request=request)
    gm = GamesManager()

    while True:
        try:
            page = urlopen(url)
        except Exception as e:
            print(e)

        soup = BeautifulSoup(page, 'html.parser')
        content = soup.find('table', {'class': 'table table-striped table-bordered'})
        for row in soup.select('tbody tr'):
            game = [x.text for x in row.find_all('td')]
            if gm.is_valid_game(game):
                if gm.is_new_game(game):
                    msg = gm.format_message(game)
                    bot.sendMessage(chat_id, msg, parse_mode="Markdown")
                    gm.games.append(game)
        time.sleep(10)
