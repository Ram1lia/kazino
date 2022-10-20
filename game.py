# import os
# from envparse import env
# from lottery import stavka
#
# env.read_envfile('settings.env')
# money = int(os.getenv(MY_MONEY))
# jk = 0
# th = 0
# total = 0
# while True:
#     jm = input(f'Введите вашу ставку или напишите "exit"для выхода')
#     if jm == 'exit':
#         print(f'Программа завершена оставшаяся сумма {money}')
#         break
#     if not 1 <= int(jm) <= 30:
#         print(f'Неправильный слот')
#         continue
#
#     if int(jm[1]) > money or int(jm[1]) <= 0:
#         print(f'Неправильная сумма')
#     result = stavka(int(jm[0])), int(jm[1])
#     if result < 0:
#         th += result
#     else:
#         jk += result
#     total += result
#     money += result
#     if money == 0:
#         print('Вы проиграли деньги')

from random import randint
from balanc import many
slot = randint(1,30)
bank = many
def game():
    global bank
    print('Здравствуйте , вас приветствуует игра казино)')
    try:
        while 1:
            print(f'Ваш нынешний баланс: {bank}')
            com = input('Сделайте свой выбор\n1 Играть \n2 Выйти\n')
            if com == '1':
                insrt = int(input('Выберите слот: '))
                stav = int(input('Сколько хотите поставить: '))
                if insrt == slot and stav <= bank:
                    bank += (stav*5)
                    print('Вы угодали!')
                elif slot != insrt and stav <= bank:
                    if bank > 0 and stav <= bank:
                        bank -= stav
                        print('Вы не угодали!')
                elif bank == 0:
                    print('Вы проиграли все свои денги')
                    continue
                elif stav > bank:
                    print('У вас не хватает средств!')
            elif com == '2':
                if bank < 1000:
                    print('Вы в проиграше')
                    print('Игра окончена')
                    print(f'Ваша баланс {bank}')
                    break
                elif bank > 1000:
                    print('ВЫ в выйграше')
                    print('Игра окончена')
                    print(f'Ваш баланс {bank}')
                    break
            else:
                print('Нет такой меню!')
    except TypeError:
        print('Что-то пошлшо не так!')
    except ValueError:
        print('Пишите только числа!')
    except Exception:
        print('Что-то пошло не так')
