### lottery_driver.py ###

import lottery

# html for <head>
head_html = '''
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <title>로또</title>

    <style type="text/css" media="screen">
        body {
            background-color: #FAFAFA;
            padding-top: 80px;
        }

        .navbar {
            background-color: #29B895;
            border-radius: 0 !important;
        }

        .navbar-brand {
            color: white;
        }

        .navbar-brand:hover {
            color: white;
        }

        .jumbotron {
            border-radius: 10px;
            padding: 20px;
        }

        .jumbotron h1 {
            margin: 0 0 20px 0;
            font-size: 24px !important;
        }

        .cash-div {
            font-size: 24px;
        }

        .cash-div b {
            margin-right: 10px;
        }

        .red {
            background-color: #D84134;
            color: white;
        }

        .green {
            background-color: #6AC83B;
        }

        .yellow {
            background-color: #FBC34B;
        }

        .blue {
            background-color: #528FD2;
            color: white;
        }

        .black {
            background-color: #414141;
        }

        .plus {
            font-size: 30px;
            margin: 0 10px 0 10px;
        }

        .ball {
            color: white;
            font-size: 20px;
            border-radius: 50%;
            display: inline-block;
            width: 60px;
            height: 60px;
            text-align: center;
            line-height: 60px;
        }

        .attempt-numbers {
            font-size: 18px;
            outline: 1px solid black;
            display: inline-block;
            margin-bottom: 20px;
            margin-right: 20px;
            height: 30px;
        }

        .attempt-number {
            display: inline-block;
            width: 30px;
            text-align: center;
            line-height: 30px;
        }

        .attempt-prize {
            display: inline-block;
            font-size: 18px;
        }
    </style>

    <!-- Latest compiled and minified CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" integrity="sha384-1q8mTJOASx8j1Au+a5WDVnPi2lkFfwwEAa8hDDdjZlpLegxhjVME1fgjWPGmkzs7" crossorigin="anonymous">

    <!-- Optional theme -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap-theme.min.css" integrity="sha384-fLW2N01lMqjakBkx3l/M9EahuwpSfeNvV63J5ezn3uZzapT0u7EYsXMjQV+0En5r" crossorigin="anonymous">

    <!-- Latest compiled and minified JavaScript -->
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js" integrity="sha384-0mSbJDEHialfmuBBQP6A4Qrprq5OVfW37PRR3j5ELqxss1yVqOtnepnHVP9aJ7xS" crossorigin="anonymous"></script>
</head>
'''

# html for the rest
main_html = '''
<!DOCTYPE html>
<html>
    <body>
        <nav class="navbar navbar-fixed-top">
            <div class="container-fluid">
                <!-- Brand and toggle get grouped for better mobile display -->
                <div class="navbar-header">
                    <a class="navbar-brand" href="#">LOTTO</a>
                </div>
            </div><!-- /.container-fluid -->
        </nav>

        <div class="col-xs-10 col-xs-offset-1">
            <div class="jumbotron">
                <h1><b>당첨 번호</b></h1>
                {numbers}
            </div>
        </div>

        <div class="col-xs-5 col-xs-offset-1">
            <div class="jumbotron cash-div">
                <b>당첨 금액</b>
                <span>‎₩{total_prize}</span>
            </div>
        </div>

        <div class="col-xs-5">
            <div class="jumbotron cash-div">
                <b>쓴 금액</b>
                <span>‎₩{total_cost}</span>
            </div>
        </div>

        <div class="col-xs-10 col-xs-offset-1">
            <div class="jumbotron">
                <h1><b>내 번호</b></h1>
                {attempts}
            </div>
        </div>

        <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
        <!-- Include all compiled plugins (below), or include individual files as needed -->
    </body>
</html>
'''

# get color of ball
def get_color(number):
    if number <= 10:
        return "yellow"
    elif number <= 20:
        return "blue"
    elif number <= 30:
        return "red"
    elif number <= 40:
        return "black"
    else:
        return "green"

# generate html for winning balls
def generate_numbers_html(numbers):
    # template for winning ball
    ball_html = '''
    <div class="ball {color}">
        {number}
    </div>
    '''

    html = ""
    for number in numbers[:6]:
        html += ball_html.format(number = number, color = get_color(number))
    html += '<span class="plus">+</span>'
    html += ball_html.format(number = numbers[-1], color = get_color(numbers[-1]))
    return html

# generate html for each attempt
def generate_attempt_html(attempt, winning_numbers):
    number_html = '''
    <span class="attempt-number">{number}</span>
    '''

    red_number_html = '''
    <span class="attempt-number red">{number}</span>
    '''

    blue_number_html = '''
    <span class="attempt-number blue">{number}</span>
    '''

    attempt_html = ""
    for num in attempt[0]:
        if num in winning_numbers[:6]:
            attempt_html += red_number_html.format(number=num)
        elif num in winning_numbers[6:]:
            attempt_html += blue_number_html.format(number=num)
        else:
            attempt_html += number_html.format(number=num)

    html = '''
    <div class="attempt">
        <div class="attempt-numbers">
            {attempt}
        </div>
        <div class="attempt-prize">
            ‎₩{prize}
        </div>
    </div>
    '''.format(attempt=attempt_html, prize=attempt[1])
    return html

# main
def main(winning_numbers, tries, total_prize, total_cost):
    # Create or overwrite the output file
    out_file = open('lottery.html', 'w', encoding='utf-8')

    winning_numbers_html = generate_numbers_html(winning_numbers)

    attempts_html = ""

    for attempt in tries:
        attempts_html += generate_attempt_html(attempt, winning_numbers)

    # Output the file
    out_file.write(head_html + main_html.format(numbers=winning_numbers_html, 
        attempts=attempts_html, total_prize=total_prize, total_cost=total_cost))
    out_file.close()

# define constants
WINNING_NUMBERS = lottery.draw_winning_numbers()
NUM_TRIES = 100

# define variables
tries = []
total_prize = 0
total_cost = 0

for i in range(NUM_TRIES):
    attempt = lottery.generate_numbers()
    prize = lottery.check(attempt, WINNING_NUMBERS)
    tries.append((attempt, prize))

    total_prize += prize
    total_cost += 1000

main(WINNING_NUMBERS, sorted(tries, key=lambda x: -x[1]), total_prize, 
    total_cost)





### lottery.py ###
from random import randint

# 무작위로 정렬된 1 - 45 사이의 숫자 여섯개 뽑기
def generate_numbers():
    while True:
        user_number = [randint(1, 45), randint(1, 45), randint(1, 45), randint(1, 45), randint(1, 45), randint(1, 45)]
        user_number.sort()
        check = 0
        for i in range(len(user_number) - 1):
            if user_number[i] == user_number[i + 1]:
                check += 1
        if check == 0:
            break
    return user_number

# 보너스까지 포함해 7개 숫자 뽑기
# 정렬된 6개의 당첨 번호와 1개의 보너스 번호 리스트를 리턴
# 예: [1, 7, 13, 23, 31, 41, 15]
def draw_winning_numbers():
    while True:
        jackpot = generate_numbers()
        bonus_number = randint(1, 45)
        if bonus_number not in jackpot:
            return jackpot + [bonus_number]
        else:
            continue

# 두 리스트에서 중복되는 숫자가 몇개인지 구하기
def count_matching_numbers(list1, list2):
    count = 0
    for i in range(len(list1)):
        if list1[i] in list2:
            count += 1
    return count

# 로또 등수 확인하기
def check(numbers, winning_numbers):
    count = count_matching_numbers(numbers, winning_numbers[0:6])
    bonus_count = count_matching_numbers(numbers, winning_numbers[6])
    if count == 6:
        return 1000000000
    elif count == 5:
        if bonus_count == 1:
            return 50000000
        else:
            return 1000000
    elif count == 4:
        return 50000
    elif count == 3:
        return 5000
    else:
        return 0
        

        
### sample answer ###
from random import randint

# 무작위로 1 - 45 사이의 숫자 6개 뽑기
def generate_numbers():
    # 숫자 6개를 보관할 리스트 생성
    numbers = []

    # 6개의 요소가 있을때까지 반복
    while len(numbers) < 6:
        # 새로 뽑은 수가 numbers에 없을 경우에만 추가
        new_number = randint(1, 45)
        if new_number not in numbers:
            numbers.append(new_number)

    # 정렬하고 리턴
    return sorted(numbers)

# 보너스까지 포함해 7개 숫자 뽑기
def draw_winning_numbers():
    winning_numbers = generate_numbers()
    while len(winning_numbers) < 7:
        new_number = randint(1, 45)
        while new_number not in winning_numbers:
            winning_numbers.append(new_number)

    # 정렬하지 않고 리턴
    return winning_numbers

# 두 리스트에서 중복되는 숫자가 몇개인지 구하기
def count_matching_numbers(numbers, winning_numbers):
    count = 0

    for num in numbers:
        # num이 winning_numbers에 있으면 count에 1 추가
        if num in winning_numbers:
            count = count + 1

    return count

# 로또 등수 확인하기
def check(numbers, winning_numbers):
    # 번호 당첨 개수 확인
    count = count_matching_numbers(numbers, winning_numbers[:6])

    # 보너스 당첨 확인
    bonus_count = count_matching_numbers(numbers, winning_numbers[6:])

    # 상금 확인
    if count == 6:
        return 1000000000
    elif count == 5 and bonus_count == 1:
        return 50000000
    elif count == 5:
        return 1000000
    elif count == 4:
        return 50000
    elif count == 3:
        return 5000
    else:
        return 0
