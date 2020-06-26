### Version 1 ###

from random import randint

numbers = []

while len(numbers) < 3:
    new_number = randint(0, 9)

    while new_number in numbers:
        new_number = randint(0, 9)
    numbers.append(new_number)
print("0과 9 사이의 서로 다른 세 숫자를 랜덤한 순서로 뽑았습니다.\n")

print("세 수를 하나씩 차례대로 입력하세요.")

strike, tries = 0, 0
while strike < 3:
    strike, ball = 0, 0

    guesses = ['a', 'a', 'a']

    for i in range(len(guesses)):
        while True: 
            guesses[i] = input("%d번째 수를 입력하세요: " % (i + 1))
            interim = guesses[:]
            del interim[i]
            if guesses[i] not in list(map(str, range(10))): #정수를 입력하지 않을 가능성 때문에 str으로 input을 설정
                print("범위를 벗어나는 수입니다. 다시 입력해주세요.")
                guesses[i] = 'a'
            elif guesses[i] in interim:
                print("중복되는 수 입니다. 다시 입력해주세요.")
                guesses[i] = 'a'
            else:
                break
    
    for i in range(len(guesses)):
        guesses[i] = int(guesses[i])
    
    i = 0
    while i < len(guesses):
        if guesses[i] == numbers[i]:
            strike += 1
        elif guesses[i] in numbers:
            ball += 1
        i += 1
    print("%dS %dB\n" %(strike, ball))
    tries += 1
    
print("축하합니다. %d번만에 세 숫자의 값과 위치를 모두 맞추셨습니다." % tries)


### version 2 ###
from random import randint

numbers = []

while len(numbers) < 3:
    new_number = randint(0, 9)

    while new_number in numbers:
        new_number = randint(0, 9)
    numbers.append(new_number)
print("0과 9 사이의 서로 다른 세 숫자를 랜덤한 순서로 뽑았습니다.\n")

print("세 수를 하나씩 차례대로 입력하세요.")

strike, tries = 0, 0
while strike < 3:
    strike, ball = 0, 0

    guesses = ['a', 'a', 'a']

    index = 0
    while index < len(guesses):
        try:
            guesses[index] = int(input("%d번째 수를 입력하세요: " % (index + 1)))
            interim = guesses[:]
            del interim[index]
            if guesses[index] < 0 or guesses[index] > 9:
                print("범위를 벗어나는 수입니다. 다시 입력해주세요.")
                continue
            if guesses[index] in interim:
                print("중복되는 수 입니다. 다시 입력해주세요.")
                continue
            index += 1
        except ValueError:
            print("범위를 벗어나는 수입니다. 다시 입력해주세요.")
            continue

    index = 0
    while index < len(guesses):
        if guesses[index] == numbers[index]:
            strike += 1
        elif guesses[index] in numbers:
            ball += 1
        index += 1
    print("%dS %dB\n" % (strike, ball))
    tries += 1

print("축하합니다. %d번만에 세 숫자의 값과 위치를 모두 맞추셨습니다." % tries)

### sample answer ###
from random import randint

# 번호 뽑기
def generate_numbers():
    # 숫자 3개를 보관할 리스트 생성
    numbers = []

    # 3개의 요소가 있을때까지 반복
    while len(numbers) < 3:
        # 새로 뽑은 수가 numbers에 없을 경우에만 추가
        new_number = randint(0, 9)
        if new_number not in numbers:
            numbers.append(new_number)

    # 리스트 리턴
    return numbers

# 정답 뽑기
ANSWER = generate_numbers()

# 변수 초기값 설정
tries = 0        # 시도 횟수
strike_count = 0 # 스트라이크 개수
ball_count = 0   # 볼 개수

# 번호를 모두 맞출때까지 반복
while strike_count < 3:
    # 번호 3개 입력 받기
    guess = []
    while len(guess) < 3:
        # 새로 입력한 수가 guess에 없을 경우에만 추가
        new_number = int(input("%d번째 수를 입력하세요: " % (len(guess) + 1)))

        # 범위를 벗어나면 설명 메시지 출력
        if new_number < 0 or new_number > 9:
            print("0에서 9까지의 수를 입력해주세요!")
        # 중복된 수를 입력하면 설명 메시지 출력
        elif new_number in guess:
            print("새로운 수를 입력해주세요!")
        # 타당한 값이면 guess에 추가
        else:
            guess.append(new_number)

    # 스트라이크, 볼 개수 세기
    strike_count = 0 # 스트라이크 개수
    ball_count = 0   # 볼 개수
    i = 0            # 인덱싱 변수

    while i < 3:
        if guess[i] == ANSWER[i]:
            strike_count = strike_count + 1
        elif guess[i] in ANSWER:
            ball_count = ball_count + 1
        i = i + 1

    print("%dS %dB" % (strike_count, ball_count))

    # 시도 횟수 추가
    tries = tries + 1

# 축하 메시지
print("축하합니다. %d번 만에 세 숫자의 값과 위치를 모두 맞추셨습니다." % (tries))
