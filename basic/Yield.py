# can produce a sequence of objects
# can resume execution

def producer():
    for num in range(0, 10, 1):
        if num % 2 == 0:
            yield num

for n in producer():
    print("Next number", n)
