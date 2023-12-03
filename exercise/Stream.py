class Stream(object):
    def __init__(self, current, step):
        self.current = current
        self.step = step
    def get_next(self):
        to_return = self.current
        self.current += self.step
        return to_return

class EvenStream(Stream):
    def __init__(self):
        super().__init__(0, 2)

class OddStream(Stream):
    def __init__(self):
        super().__init__(1, 2)

def print_from_stream(n, stream=EvenStream()):
    for _ in range(n):
        print(stream.get_next())


queries = int(input())
for _ in range(queries):
    stream_name, n = input().split()
    n = int(n)
    if stream_name == "even":
        print_from_stream(n, EvenStream())
        # this does not work as EvenStream() will be shared among all the calls
        # print_from_stream(n)
    else:
        print_from_stream(n, OddStream())
