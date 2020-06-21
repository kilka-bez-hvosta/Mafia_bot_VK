import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random


class Game:
    pass


def main():
    games = {}
    vk_session = vk_api.VkApi(
        token='0c5b21d5f55712b34f5cca5ccd19497bc201845c5360714020981d4bba07162c4788e6c4ed2b2e7225d75')

    longpoll = VkBotLongPoll(vk_session, 193531598)
    vk = vk_session.get_api()
    for event in longpoll.listen():
        print(event)
        if event.type == VkBotEventType.MESSAGE_NEW and event.from_chat:
            if event.text == 'Начали!':
                pass



if __name__ == '__main__':
    main()
