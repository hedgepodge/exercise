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
