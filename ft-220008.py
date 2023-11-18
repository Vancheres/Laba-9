import random
import logging

# Настройка логирования
logging.basicConfig(filename='lottery_log.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')
def draw_barrel(bag):
    try:
        drawn_barrel = random.choice(bag)
        bag.remove(drawn_barrel)
        logging.info(f"Бочонок {drawn_barrel} был вытянут.")
        return drawn_barrel
    except IndexError:
        logging.error("Все бочонки были вытянуты.")
        return None