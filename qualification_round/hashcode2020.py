import numpy as np
import sys

file_name = sys.argv[1]

with open(file_name, 'r') as fin:
    B, L, D = fin.readline().split()
    B = int(B)
    L = int(L)
    D = int(D)


    scores = np.array([int(x) for x in fin.readline().split()])

    sorted_scores_index = np.argsort(scores*(-1))

    # [number of books, signup finish, no. can be shipped]
    library_data = {}

    # books in library
    library_books = {}

    for i in range(L):
        line = fin.readline()
        data = [int(x) for x in line.split()]
        library_data[i] = data

        line = fin.readline()
        
        books = [int(x) for x in line.split()]
        library_books[i] = books

current_day = 0
output = {}


for i in sorted_scores_index:
    for library, list_books in library_books.items():
        if i in list_books:
            
            # library: (max, [which])
            # max = (D - current_day - signup_time)*per_day
            if not library in output:
                sign_up = library_data[library][1]
                max_books = (D - current_day - sign_up) * library_data[library][2]
                current_day = current_day + sign_up
                books = []
                books.append(i)
                output[library] = [max_books-1, books]

                break
            elif output[library][0] > 0:
                output[library][1].append(i)
                output[library][0] = output[library][0] - 1
            
                break
print(len(output))

for library, value in output.items():

    print(library, len(value[1]))
    print(*value[1])
