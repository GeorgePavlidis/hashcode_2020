import sys
import numpy as np

file_name = sys.argv[1]

with open(file_name, 'r') as fin:
    
    B, L, D = fin.readline().split()
    B = int(B)
    L = int(L)
    D = int(D)

    scores = np.array([int(x) for x in fin.readline().split()])

    
    sorted_scores_index = np.argsort(scores*(-1))
    
    # [number of books, signup finish, no. can be shipped]
    library_data = []

    # books in library
    library_books = []
    
    for i in range(L):
        line = fin.readline()
        data = [int(x) for x in line.split()]

        library_data.append(data)

        line = fin.readline()
        
        books = [(scores[int(x)],int(x)) for x in line.split()]
        
        sorted_books = sorted(books, reverse=True)
        

        library_books.append([x[1] for x in sorted_books])

signup_times = np.array([x[1] for x in library_data])
sorted_libraries = np.argsort(signup_times)

current_day = 0
total_scanned = []
output = {}

for library in sorted_libraries:
    # print('Current day ',current_day, ' Library ', library)
    if current_day >= D:
        break
    signup_time = library_data[library][1]

    max_books = (D - current_day - signup_time)*library_data[library][2]
    
    current_day = current_day + signup_time
    
    scanned = []
    for i in range(min(len(library_books[library])-1, max_books)):
        scanned.append(library_books[library][i])

    # i = 0
    # while max_books >= 0 and i < len(sorted_scores_index):
    #     curr_book = sorted_scores_index[i]
        
    #     if np.isin(curr_book, library_books[library]):
    #         scanned.append(curr_book)
    #         sorted_scores_index = np.delete(sorted_scores_index, i)
    #         max_books = max_books - 1
        
    #     i = i + 1
    if scanned:
        output[library] = scanned

with open(sys.argv[2], 'w') as fout:

    fout.write(str(len(output))+'\n')

    for library, value in output.items():

        fout.write(str(library)+' ')
        fout.write(str(len(value)))
        fout.write('\n')
        
        for v in value:
            fout.write(str(v)+' ')
    
        fout.write('\n')