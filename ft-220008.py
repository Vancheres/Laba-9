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

def main():
    while True:
        try:
            n = int(input("Введите натуральное число N для количества бочонков: "))
            if n <= 0:
                raise ValueError
            break
        except ValueError:
            print("Неверный ввод. Пожалуйста, введите натуральное число.")
    bag = list(range(1, n + 1))
    random.shuffle(bag)
    print("Нажмите Enter для вытаскивания бочонка или введите 'exit' для выхода.")

    while bag:
        user_input = input()
        if user_input.lower() == 'exit':
            break
        print(f"Вы вытянули бочонок: {draw_barrel(bag)}")

    logging.info("Игра завершена.")


if __name__ == "__main__":
    main()