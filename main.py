# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
sodoku_valide = [
    [3, 8, 7, 4, 9, 1, 6, 2, 5],
    [2, 4, 1, 5, 6, 8, 3, 7, 9],
    [5, 6, 9, 3, 2, 7, 4, 1, 8],
    [7, 5, 8, 6, 1, 9, 2, 3, 4],
    [1, 2, 3, 7, 8, 4, 5, 9, 6],
    [4, 9, 6, 2, 5, 3, 1, 8, 7],
    [9, 3, 4, 1, 7, 6, 8, 5, 2],
    [6, 7, 5, 8, 3, 2, 9, 4, 1],
    [8, 1, 2, 9, 4, 5, 7, 6, 3]
]



def display(sodoku):
        len_sodoku = len(sodoku)
        for row_iterator_index in range(0, len_sodoku):
            if row_iterator_index % 3 == 0 :
                for x in range(0,19): print("-", end="")
                print("")
            for column_iterator_index in range(0, len_sodoku):
                if column_iterator_index % 3 == 0 :
                    print("|", end="")
                else:
                    print(",", end="")
                print(sodoku[row_iterator_index][column_iterator_index], end="")
                if column_iterator_index == len_sodoku -1:
                    print("|")

def main():
    display(sodoku_valide)

if __name__ == '__main__':
    main()


