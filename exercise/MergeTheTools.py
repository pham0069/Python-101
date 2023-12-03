#https://www.hackerrank.com/challenges/merge-the-tools/problem?isFullScreen=true
def collapse(string):
    occured = set(())
    result = ""
    for index, letter in enumerate(string):
        if not (letter in occured):
            occured.add(letter)
            result = result + letter
    return result

def merge_the_tools(string, k):
    for i in range(0, len(string)//k):
        substring = string[i*k:i*k+k]
        print(collapse(substring))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
