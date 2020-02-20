
file_name = 'a_example.txt'

with open(file_name, 'r') as fin:
    B, L, D = fin.readline().split()
    B = int(B)
    L = int(L)
    D = int(D)

    scores = [int(x) for x in fin.readline().split()]


    library_data = {}
    library_books = {}
    i = 0


    for i in range(L):
        line = fin.readline()
        data = [int(x) for x in line.split()]
        library_data[i] = data

        line = fin.readline()
        
        books = [int(x) for x in line.split()]
        library_books[i] = books

        i = i + 1

