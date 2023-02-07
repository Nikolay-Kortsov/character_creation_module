from random import randint

DEFAULT_ATTACK: int = 5
DEFAULT_DEFENCE: int = 10
DEFAULT_STAMINA: int = 80


class Character:
    BRIEF_DESC_CHAR_CLASS: str = 'отважный любитель приключений'
    RANGE_VALUE_ATTACK: tuple = (1, 3)
    RANGE_VALUE_DEFENCE: tuple = (1, 5)
    SPECIAL_BUFF: int = 15
    SPECIAL_SKILL: str = 'Удача'

    def __init__(self, name: str) -> None:
        self.name = name

    def attack(self) -> str:
        value_attack: int = DEFAULT_ATTACK + randint(*self.RANGE_VALUE_ATTACK)
        return (f'{self.name} нанёс противнику урон, равный '
                f'{value_attack}')

    def defence(self) -> str:
        value_defence: int = DEFAULT_DEFENCE + randint(
            *self.RANGE_VALUE_DEFENCE)
        return (f'{self.name} блокировал {value_defence} ед. урона.')

    def special(self) -> str:
        return (f'{self.name} применил специальное умение '
                f'"{self.SPECIAL_SKILL} {self.SPECIAL_BUFF}".')

    def __str__(self) -> str:
        return f'{self.__class__.__name__} - {self.BRIEF_DESC_CHAR_CLASS}.'


class Warrior(Character):
    BRIEF_DESC_CHAR_CLASS: str = (' дерзкий воин ближнего боя. '
                                  'Сильный, выносливый и отважный')
    RANGE_VALUE_ATTACK: tuple = (3, 5)
    RANGE_VALUE_DEFENCE: tuple = (5, 10)
    SPECIAL_BUFF: int = DEFAULT_STAMINA + 25
    SPECIAL_SKILL: str = 'Выносливость'


class Mage(Character):
    BRIEF_DESC_CHAR_CLASS: str = (' находчивый воин дальнего боя. '
                                  'Обладает высоким интеллектом')
    RANGE_VALUE_ATTACK: tuple = (5, 10)
    RANGE_VALUE_DEFENCE: tuple = (-2, 2)
    SPECIAL_BUFF: int = DEFAULT_ATTACK + 40
    SPECIAL_SKILL: str = 'Атака'


class Healer(Character):
    BRIEF_DESC_CHAR_CLASS: str = (' могущественный заклинатель. '
                                  'Черпает силы из природы, веры и духов')
    RANGE_VALUE_ATTACK: tuple = (-3, -1)
    RANGE_VALUE_DEFENCE: tuple = (2, 5)
    SPECIAL_BUFF: int = DEFAULT_DEFENCE + 30
    SPECIAL_SKILL: str = 'Защита'


def start_training(character):
    """
    Принимает на вход имя и класс персонажа.
    Возвращает сообщения о результатах цикла тренировки персонажа.
    """
    commands = {
        'attack': character.attack,
        'defence': character.defence,
        'special': character.special
    }
    print('Потренируйся управлять своими навыками.')
    print('Введи одну из команд: attack — чтобы атаковать противника, '
          'defence — чтобы блокировать атаку противника или '
          'special — чтобы использовать свою суперсилу.')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd = None
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd in commands:
            print(commands[cmd]())
    return 'Тренировка окончена.'


def choice_char_class(char_name: str) -> Character:
    """
    Возвращает строку с выбранным
    классом персонажа.
    """
    game_classes = {'warrior': Warrior, 'mage': Mage, 'healer': Healer}
    approve_choice: str = ''

    while approve_choice != 'y':
        selected_class = input('Введи название персонажа, '
                               'за которого хочешь играть: Воитель — warrior, '
                               'Маг — mage, Лекарь — healer: ')
        char_class: Character = game_classes[selected_class](char_name)
        print(char_class)
        approve_choice = input('Нажми (Y), чтобы подтвердить выбор, '
                               'или любую другую кнопку, '
                               'чтобы выбрать другого персонажа ').lower()
    return char_class


warrior = Warrior('Кодослав')
print(warrior)
print(warrior.attack())
