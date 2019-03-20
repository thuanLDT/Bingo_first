import random

# ビンゴの数字
int_bingo = list(range(1, 76))
str_bingo = ['{:0>2}'.format(str_bingo) for str_bingo in int_bingo]

# ビンゴの数字リスト
bingo_list = []

#ビンゴカードの列

line_B = str_bingo[0:15]
line_I = str_bingo[15:30]
line_N = str_bingo[30:45]
line_G = str_bingo[45:60]
line_O = str_bingo[60:75]

# 表示用カード
card = ''

# 表示用カードを作成

for i in range(1, 6):
    random_B = random.choice(line_B)
    bingo_list.append(random_B)
    line_B.remove(random_B)
    B = ' ' + random_B + ' '

    random_I = random.choice(line_I)
    bingo_list.append(random_I)
    line_I.remove(random_I)
    I = ' ' + random_I + ' '

    if i == 3:
        N = 'FREE'
        bingo_list.append(N)
    else:
        random_N = random.choice(line_N)
        bingo_list.append(random_N)
        line_N.remove(random_N)
        N = ' ' + random_N + ' '

    random_G = random.choice(line_G)
    bingo_list.append(random_G)
    line_G.remove(random_G)
    G = ' ' + random_G + ' '

    random_O = random.choice(line_O)
    bingo_list.append(random_O)
    line_O.remove(random_O)
    O = ' ' + random_O + ' '


    card_row = B + I + N + G + O + '\n'
    card += card_row


# 判定リスト

# 縦ライン

line_1_numbers = bingo_list[0::5]
line_2_numbers = bingo_list[1::5]
line_3_numbers = bingo_list[2::5]
line_3_numbers.remove('FREE')
line_4_numbers = bingo_list[3::5]
line_5_numbers = bingo_list[4::5]

# 横ライン

line_6_numbers = bingo_list[0:5]
line_7_numbers = bingo_list[5:10]
line_8_numbers = bingo_list[10:15]
line_8_numbers.remove('FREE')
line_9_numbers = bingo_list[15:20]
line_10_numbers = bingo_list[20:25]


# 斜めライン

line_11_numbers = []
line_12_numbers = []

list_clossline_1 = [i * 6 for i in range(0, 5)]
list_clossline_2 = [i * 4 for i in range(1, 6)]

for i in list_clossline_1:
    line_11_numbers.append(bingo_list[i])

for i in list_clossline_2:
    line_12_numbers.append(bingo_list[i])

line_11_numbers.remove('FREE')
line_12_numbers.remove('FREE')

# カードの書き換えと判定用リスト削除

num = 1
while num <= 75:
    input()
    get = random.choice(str_bingo)
    print('ball[', num, ']: ', get, sep='')
    get_num = ' ' + get + ' '
    reach = 0
    bingo = 0

    if get_num in card:
        change = '(' + get + ')'
        card = card.replace(get_num, change)

        if get in line_1_numbers:
            line_1_numbers.remove(get)
            if get in line_6_numbers:
                line_6_numbers.remove(get)
            if get in line_7_numbers:
                line_7_numbers.remove(get)
            if get in line_8_numbers:
                line_8_numbers.remove(get)
            if get in line_9_numbers:
                line_9_numbers.remove(get)
            if get in line_10_numbers:
                line_10_numbers.remove(get)
            if get in line_11_numbers:
                line_11_numbers.remove(get)
            if get in line_12_numbers:
                line_12_numbers.remove(get)

        elif get in line_2_numbers:
            line_2_numbers.remove(get)

            if get in line_6_numbers:
                line_6_numbers.remove(get)
            if get in line_7_numbers:
                line_7_numbers.remove(get)
            if get in line_8_numbers:
                line_8_numbers.remove(get)
            if get in line_9_numbers:
                line_9_numbers.remove(get)
            if get in line_10_numbers:
                line_10_numbers.remove(get)
            if get in line_11_numbers:
                line_11_numbers.remove(get)
            if get in line_12_numbers:
                line_12_numbers.remove(get)


        elif get in line_3_numbers:
            line_3_numbers.remove(get)

            if get in line_6_numbers:
                line_6_numbers.remove(get)
            if get in line_7_numbers:
                line_7_numbers.remove(get)
            if get in line_8_numbers:
                line_8_numbers.remove(get)
            if get in line_9_numbers:
                line_9_numbers.remove(get)
            if get in line_10_numbers:
                line_10_numbers.remove(get)
            if get in line_11_numbers:
                line_11_numbers.remove(get)
            if get in line_12_numbers:
                line_12_numbers.remove(get)

        elif get in line_4_numbers:
            line_4_numbers.remove(get)

            if get in line_6_numbers:
                line_6_numbers.remove(get)
            if get in line_7_numbers:
                line_7_numbers.remove(get)
            if get in line_8_numbers:
                line_8_numbers.remove(get)
            if get in line_9_numbers:
                line_9_numbers.remove(get)
            if get in line_10_numbers:
                line_10_numbers.remove(get)
            if get in line_11_numbers:
                line_11_numbers.remove(get)
            if get in line_12_numbers:
                line_12_numbers.remove(get)

        elif get in line_5_numbers:
            line_5_numbers.remove(get)

            if get in line_6_numbers:
                line_6_numbers.remove(get)
            if get in line_7_numbers:
                line_7_numbers.remove(get)
            if get in line_8_numbers:
                line_8_numbers.remove(get)
            if get in line_9_numbers:
                line_9_numbers.remove(get)
            if get in line_10_numbers:
                line_10_numbers.remove(get)
            if get in line_11_numbers:
                line_11_numbers.remove(get)
            if get in line_12_numbers:
                line_12_numbers.remove(get)

    # リーチとビンゴの集計

    if len(line_1_numbers) == 1:
        reach += 1
    elif len(line_1_numbers) == 0:
        bingo += 1

    if len(line_2_numbers) == 1:
        reach += 1
    elif len(line_2_numbers) == 0:
        bingo += 1

    if len(line_3_numbers) == 1:
        reach += 1
    elif len(line_3_numbers) == 0:
        bingo += 1

    if len(line_4_numbers) == 1:
        reach += 1
    elif len(line_4_numbers) == 0:
        bingo += 1

    if len(line_5_numbers) == 1:
        reach += 1
    elif len(line_5_numbers) == 0:
        bingo += 1

    if len(line_6_numbers) == 1:
        reach += 1
    elif len(line_6_numbers) == 0:
        bingo += 1

    if len(line_7_numbers) == 1:
        reach += 1
    elif len(line_7_numbers) == 0:
        bingo += 1

    if len(line_8_numbers) == 1:
        reach += 1
    elif len(line_8_numbers) == 0:
        bingo += 1

    if len(line_9_numbers) == 1:
        reach += 1
    elif len(line_9_numbers) == 0:
        bingo += 1

    if len(line_10_numbers) == 1:
        reach += 1
    elif len(line_10_numbers) == 0:
        bingo += 1

    if len(line_11_numbers) == 1:
        reach += 1
    elif len(line_11_numbers) == 0:
        bingo += 1

    if len(line_12_numbers) == 1:
        reach += 1

    elif len(line_12_numbers) == 0:
        bingo += 1

    #表示
    print(card)
    print('REACH: ' + str(reach))
    print('BINGO: ' + str(bingo))
    print('--------------------')

    str_bingo.remove(get)
    num += 1
    if bingo == 12:
        print("\nビンゴゲームしゅーりょー！！！\n")
        break
