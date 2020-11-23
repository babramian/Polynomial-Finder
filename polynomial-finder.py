import numpy as np
from sympy import symbols, expand, factor, evaluate

class interpolater():
    dt = None
    inter_poly = None
    simp_poly = None


    def __init__(self, data):
        self.dt = data

    
    def create_divdif_table(self):
        N = len(self.dt[0])
        limit = N-1
        difference = 1

        # Chose 2 to N+1 so the calculations don't effect first row (x) and second row (f[x]) in the datatable
        for i in range(2, N+1):
            new_row = []
            for j in range(N):
                if j < limit:
                    new_row.append((self.dt[i-1][j+1] - self.dt[i-1][j])/(self.dt[0][j+difference] - self.dt[0][j]))
                else:
                    new_row.append(None)

            self.dt.append(new_row)
            difference += 1
            limit -= 1
        
        return self.dt
    

    def print_div_table(self):
        N = len(self.dt[0])

        print('x', end='\t\t')
        comma = ','
        for i in range(N):
            print(f'f[{i}*,]', end='\t\t')
        print()

        for i in range(N):
            for j in range(N+1):
                if self.dt[j][i] == None:
                    pass
                else:
                    print(f'{"{:.3f}".format(self.dt[j][i])}', end='\t\t')
            print()
    

    def get_inter_poly(self):
        N = len(self.dt[0])
        x = symbols('x')
        expr = self.dt[1][0]
        count = 1

        for i in range(2, N+1):
            with evaluate(False):
                next_expr = 1

                for j in range(count):
                    next_expr = next_expr * (x - self.dt[0][j])
                next_expr = next_expr * self.dt[i][0]

                expr = expr + next_expr
                count += 1

        self.inter_poly = expr

        return expr

    
    def simplify(self):
        self.simp_poly = expand(self.inter_poly)
        return self.simp_poly



def get_file(filename):
    # asks for file name
    equ_list = []
    with open(filename, 'r') as file:
        count = 0
        for line in file:
            count += 1
            if count > 2:
                print("Please run the program with a proper set of values. (Too many lines provided)")
                quit()
            number_strings = line.split() # Split the line on runs of whitespace
            numbers = [float(n) for n in number_strings] # Convert to integers
            equ_list.append(numbers) # Add the "row" to your list.
            
    
    # Removes empty lists (caused by empty lines)
    equ_list = [x for x in equ_list if x!=[]]
    # Checks to make sure the number x = number of f[x]
    if len(equ_list[0]) != len(equ_list[1]):
        print("Please run the program with a proper set of values. (Number of x and f[x] values mismatching)")
        quit()
    
    return equ_list




def main():
    buffer = interpolater(get_file('values.txt'))
    div_table = buffer.create_divdif_table()
    buffer.print_div_table()
    print(f'Interpolating Polynomial is:\n {buffer.get_inter_poly().evalf(4)}')
    print(f'Simplified Polynomial is:\n{buffer.simplify().evalf(4)}')



if __name__ == "__main__":
    main()
