vocab = open('vocabulary.txt', 'w')

while True:
    eng_word = input("영어 단어를 입력하세요: ")
    if eng_word == "q":
        break
    kor_word = input("한글 단어를 입력하세요: ")
    vocab.write("%s: %s\n" % (eng_word, kor_word))

vocab.close()



vocab = open('vocabulary.txt', 'r')

for line in vocab:
    word = line.strip().split(": ")
    guess = input("%s: " % word[1])
    if guess == word[0]:
        print("맞았습니다!\n")
    else:
        print("아쉽습니다. 정답은 %s입니다.\n" % word[0])

vocab.close()



from random import randint

vocab = open('vocabulary.txt', 'r')

word_dict = {}
for line in vocab:
    word = line.strip().split(": ")
    word_dict[word[1]] = word[0]

keys = list(word_dict.keys())

while True:
    index = randint(0, len(keys) - 1)
    kor_word = keys[index]
    eng_word = word_dict[kor_word]

    guess = input("%s: " % (kor_word))
    if guess == eng_word:
        print("맞았습니다!\n")
    elif guess == "q":
        break
    else:
        print("아쉽습니다. 정답은 %s입니다.\n" % (eng_word))

vocab.close()
