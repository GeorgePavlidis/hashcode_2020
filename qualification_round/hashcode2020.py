import numpy as np
import sys

file_name = sys.argv[1]

with open(file_name, 'r') as fin:
    
    B, L, D = fin.readline().split()
    B = int(B)
    L = int(L)
    D = int(D)

    print('Start')
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


        sorted_books = [x for _,x in sorted(zip(sorted_scores_index, books))]
        library_books[i] = sorted_books


libraries_times = np.array([x[1] for _, x in library_data.items()])
libraries_sorted = np.argsort(libraries_times)

current_day = 0
output = {}


# for i in sorted_scores_index:
#     if current_day >= D:
#         break
#     print(current_day)
#     for library in libraries_sorted:
#         list_books = library_books[library]
#         if np.isin(i, list_books):
            
#             # library: (max, [which])
#             # max = (D - current_day - signup_time)*per_day
#             if not library in output:
#                 sign_up = library_data[library][1]
#                 max_books = (D - current_day - sign_up) * library_data[library][2]
#                 current_day = current_day + sign_up
#                 books = []
#                 books.append(i)
#                 output[library] = [max_books-1, books]
                
#                 # sorted_scores_index.remove(i)
                
#                 break
#             elif output[library][0] > 0:
#                 output[library][1].append(i)
#                 output[library][0] = output[library][0] - 1

#                 # sorted_scores_index.remove(i)

#                 break

for i in sorted_scores_index:
    if current_day >= D:
        break
    print(current_day)
    for library in libraries_sorted:
        library_list = library_books[library]
        #print(library_list)
        if np.isin(i, library_list):

            sign_up = library_data[library][1]
            max_books = (D - current_day - sign_up) * library_data[library][2]
            print('Max books '+str(max_books)+' library '+ str(library) +  ' library length ' + str(len(library_list)))
            
            current_day = current_day + sign_up
            
            index = library_list.index(i)
            print('index ' + str(index))
            
            books = []
            books.append(i)
            output[library] = books
            max_books = max_books - 1

            for j in range(index+1, min((len(library_list) - index), max_books)):
                output[library].append(library_list[j])
                np.delete(sorted_scores_index, library_list[j])
            
            library_books[library] = []
                
with open(sys.argv[2], 'w') as fout:

    fout.write(str(len(output))+'\n')

    for library, value in output.items():

        fout.write(str(library)+' ')
        fout.write(str(len(value)))
        fout.write('\n')
        
        for v in value:
            fout.write(str(v)+' ')

        fout.write('\n')
        
