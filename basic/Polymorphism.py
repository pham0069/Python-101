# Polymorphism: ability of an object to take many forms
# achieved by inheritance and abstraction
# e.g. len() function can calculate size of different objects - list, string, dict

class SortingAlgorithm:

    def sort(self):
        pass

class InsertionSortingAlgorithm(SortingAlgorithm):
    def sort(self):
        print('Insertion sort')

class QuickSortingAlgorithm(SortingAlgorithm):
    def sort(self):
        print('Quick sort')

class BubbleSortingAlgorithm(SortingAlgorithm):
    def sort(self):
        print('Bubble sort')

# NULL value
sortingAlgorithm = None
num = input("Please enter a sorting algo (insert = 0, quick = 1, bubble = 2): ")
num = int(num)

if num == 0:
    sortingAlgorithm = InsertionSortingAlgorithm()
elif num == 1:
    sortingAlgorithm = QuickSortingAlgorithm()
elif num == 2:
    sortingAlgorithm = BubbleSortingAlgorithm()

# you dont know the type of sorting algorithm at the compile time
# but you still can call the sort function
if not sortingAlgorithm is None:
    sortingAlgorithm.sort()
else:
    print("Oops no algorithm")
