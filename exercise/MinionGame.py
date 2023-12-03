vowels = list("AEIOU")

def score(string, start_with_vowel):
    score = 0
    length = len(string)
    for index, letter in enumerate(string):
        letter = string[index].capitalize()
        if start_with_vowel:
            if letter in vowels:
                score += length - index
        else:
            if not (letter in vowels):
                score += length - index
    return score

def minion_game(string):
    # your code goes here
    stuart_score = score(string, False)
    kevin_score = score(string, True)

    if stuart_score == kevin_score:
        print("Draw")
    elif stuart_score > kevin_score:
        print("Stuart", stuart_score)
    else:
        print("Kevin", kevin_score)

if __name__ == '__main__':
    s = input()
    minion_game(s)
