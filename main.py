per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}


def calcpercent(capital: int) -> list:
    return [capital * percent/100 for percent in per_cent.values()]


if __name__ == '__main__':
    money = input("Введите сумму для пополнения на вклад: ")
    deposit = calcpercent(capital=int(money))
    print(f'Через год получите:{deposit} процентами в зависимости от банка')
    print(f'Максимальная сумма процентов: {max(deposit)}')
