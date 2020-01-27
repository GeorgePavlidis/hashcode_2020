filenames = ['a_example','b_small','c_medium','d_quite_big','e_also_big']


def read_file(file_name):
    with open('input/' + file_name+'.in', 'r') as fin:
        
        line = [int(x) for x in fin.readline().split()]
        pieces_left = line[0]
        total = line[1]
        pizzas = [int(x) for x in fin.readline().split()]
    
    return pieces_left, pizzas, total

def write_file(file_name, selected):

    with open('output/'+file_name+'.out', 'w') as fout:
        fout.write(f"{str(len(selected))}")
        fout.write('\n')
        fout.write(f"{' '.join([str(x) for x in selected])}")

def solution_1(pizzas, pieces_left):
    selected = []
    # partial_sum = 0
    for i in range(len(pizzas)-1,-1,-1):
        p = pizzas[i]
        
        if p <= pieces_left:
            
            if i not in selected:
                pieces_left = pieces_left - p
                selected.insert(0, i)
        if pieces_left == 0:
            break
    
    return selected

def solution_2(pizzas, pieces_left):
    return sum(pizzas)


if __name__ == '__main__':
    filenames = ['a_example','b_small','c_medium','d_quite_big','e_also_big']

    for file in filenames:
        pieces_left, pizzas, total = read_file(file)

        selected = solution_1(pizzas, pieces_left)
        
        write_file(file, selected)