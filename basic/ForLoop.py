# specify end (exclusive): will start from 0
for number in range(5):
    print(number)

# specify start (inclusive) and end (exclusive)
for number in range(5, 10):
    print(number)

# specify step
for number in range(5, 10, 2):
    print(number)

name = 'Kevin'
for letter in name:
    print(letter)
# execute right after for loop ends
else:
    print("Done printing letter")
