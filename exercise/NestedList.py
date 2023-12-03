# https://www.hackerrank.com/challenges/nested-list/problem

# print the students name that have second-lowest grades in alphabetical order

# item is a tuple of 2 values
# sort by item[1] first
# if item[1] tie, sort by item[0]
def sort_func(item):
    return (item[1], item[0])

if __name__ == '__main__':

    students = {"Harry": 37.21, "Berry": 37.21, "Tina": 37.2, "Ari": 41, "Harsh": 39}

    result = sorted(students.items(), key=sort_func)
    lowest_grade = result[0][1]

    second_lowest_grade = lowest_grade
    for key, value in result:
        if (value != lowest_grade):
           second_lowest_grade = value
           break

    for key, value in result:
        if (value == second_lowest_grade):
           print(key)
        elif (value > second_lowest_grade):
            break

