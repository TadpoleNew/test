from random import randint

# *,是命名关键字参数，可以增加代码的可读性,在调用函数时必须给出参数名和参数值
# def roll_dice(a, *, num = 1):


def roll_dice(*, num=1):
    total = 0
    for _ in range(num):
        total += randint(1, 6)
    return total


def main():
    # first = roll_dice(1, num = 2, 3)  # SyntaxError: positional argument follows keyword argument 位置参数遵循关键字参数
    # first = roll_dice(1, 2)  # TypeError: roll_dice() takes 1 positional
    # argument but 2 were given 类型错误：roll骰（）接受1个位置参数，但是有2个
    money = 1000
    while money > 0:
        print(f'玩家总资产:{money}元')
        while True:
            debt = int(input('请下注：'))
            if 0 < debt <= money:
                break
        first = roll_dice(num=2)
        print(f'玩家摇出了{first}点.')
        game_over = True  # 假设第一次就能分出胜负

        if first == 7 or first == 11:
            money += debt
            print('玩家胜！')
        elif first == 2 or first == 3 or first == 12:
            money -= debt
            print('庄家胜！')
        else:
            game_over = False  # 说明游戏没有分出胜负
        while not game_over:
            current = roll_dice(num=2)
            print(f'玩家摇出了{current}点。')
            if current == 7:
                money -= debt
                print('庄家胜！')
                game_over = True
            elif current == first:
                money += debt
                print('玩家胜')
                game_over = True
        # print(current)
    print('你已破产')

if __name__ == '__main__':
    main()
