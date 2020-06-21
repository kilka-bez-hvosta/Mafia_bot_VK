import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random


GAME_VARIATIONS = [['мафия' * 2, "доктор", "комиссар", "ночная бабочка", "маньяк"],
                                       ["мафия" * 2, "комиссар", "доктор"], ["маньяк", "комиссар"]]


def main():
    games = {}
    vk_session = vk_api.VkApi(
        token='0c5b21d5f55712b34f5cca5ccd19497bc201845c5360714020981d4bba07162c4788e6c4ed2b2e7225d75')

    longpoll = VkBotLongPoll(vk_session, 193531598)
    vk = vk_session.get_api()
    for event in longpoll.listen():
        print(event)
        if event.type == VkBotEventType.MESSAGE_NEW and event.from_chat:
            if event.obj.message['text'] == 'Кто играет - ставьте плюс:' and event.chat_id not in games.keys() :
                games[event.chat_id] = ['подключение игроков', dict()]
            if event.chat_id in games.keys() and games[event.chat_id][0] == 'подключение игроков':
                if event.obj.message['text'] == '+':
                    games[event.chat_id][1][event.from_id] = 'мирный житель'
                if event.obj.message['text'] == 'Начали!':

                    games[event.chat_id][0] = 'идет игра'
                    for player in games[event.chat_id][1].keys():
                        if ((len(games[event.chat_id][1].keys()) == 5)):
                            variant = GAME_VARIATIONS[-1]
                        elif ((len(games[event.chat_id][1].keys()) <= 8)):
                            variant = GAME_VARIATIONS[-2]
                        elif ((len(games[event.chat_id][1].keys()) >= 8)):
                            variant = GAME_VARIATIONS[0]
                        variant[-1] += ["мирный житель"]
                        games[event.chat_id][1][player] = variant[-1].pop(variant[-1].index(random.choice(variant[-1])))

                        vk.messages.send(user_id=event.obj.message['from_id'],
                                        message=games[event.chat_id][1][player],
                                        random_id=random.randint(0, 2 ** 64))




if __name__ == '__main__':
    main()
