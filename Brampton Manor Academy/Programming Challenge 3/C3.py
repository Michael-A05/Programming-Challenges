

def calculation(answer):
    factor = 99 - answer

    friends_int = int(input('*Player* Pick any number 50-99: '))

    factor += friends_int

    factor = str(factor)
    factor_1 = factor[0]
    factor_2 = factor[1:3]
    factor = int(factor_1) + int(factor_2)

    answer = friends_int -+ factor
    return answer


def run():
    print('Hello Sentient\n')
    print('We are going to play a game.I want you to pick a number then do a series of calculations. I bet I know what the result of those calculations will be!\n')
    answer = int(input('*You* This will be the answer. Select a number between 10-49: '))
    value = calculation(answer)
    print(f'\nI said the answer was {value} and the calculation result is {value}')

if __name__ == '__main__':
    run()
