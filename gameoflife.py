import random


def initialise(n):
    matrix = []

    for i in range(n):  # rows
        for j in range(n):  # columns

            choice = random.choice([" ", "A"])

            try:
                matrix[i].append(choice)
            except IndexError:
                matrix.append([choice])

    return matrix


def update(uMatrix):
    length = len(uMatrix)

    for row in range(length):
        for column in range(length):

            neighbours = []

            for nRow in range(3):
                for nColumn in range(3):
                    neighbour = (row - 1 + nRow, column - 1 + nColumn)

                    if neighbour != (row, column):
                        neighbours.append(neighbour)

            aliveCount = 0

            for row1, column1 in neighbours:
                if (length > row1 >= 0) and (length > column1 >= 0):
                    if uMatrix[row1][column1] == "A":
                        aliveCount += 1

            if aliveCount == 1:
                uMatrix[row][column] = " "
            elif aliveCount == 2 and uMatrix[row][column] == "A":
                uMatrix[row][column] = "A"
            elif aliveCount == 3:
                uMatrix[row][column] = "A"
            else:
                uMatrix[row][column] = " "
    return uMatrix


def printMatrix(pMatrix):
    print("-" * len(pMatrix))

    for row in pMatrix:
        for element in row:
            print(element, end="")
        print("|")

def main():
    depth = int(input("How big should the field be? ( n x n matrix ):"))
    matrix = initialise(depth)

    mode = input("Auto (a), Manual(m):")

    printMatrix(matrix)

    if mode == "m":
        flag = "y"

        while flag == "y":
            flag = input("Continue (y/n)?")
            matrix = update(matrix)
            printMatrix(matrix)

    elif mode == "a":
        times = int(input("Number of times to run?:"))

        for i in range(times):
            matrix = update(matrix)
            printMatrix(matrix)


main()

"""
00 01 02 03 04
10 11 12 13 14
20 21 22 23 24
"""
