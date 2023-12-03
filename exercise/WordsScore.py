# https://www.hackerrank.com/challenges/words-score/problem

vowels = list("aeiouy")

def score_words(word):
    count = 0
    for letter in word:
        if letter in vowels:
            count += 1

    if count % 2 == 0:
        return 2
    else:
        return 1

n = int(input())
sum = 0
for word in input().split():
    sum += score_words(word)
print(sum)
