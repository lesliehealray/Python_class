def sumProblem(x, y):
    sum = x + y
    sentence = 'The sum of {} and {} is {}.'.format(x, y, sum)
    print(sentence)

def main():
    sumProblem(2, 3)
    sumProblem(543, 10)
    a = int(raw_input("Enter an integer: "))
    b = int(raw_input("Enter another integer: "))
    sumProblem(a, b)

main()
