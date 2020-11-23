import numpy as np
import sympy as sp

class interpolater():
    dt = None


    def __init__(self, data):
        self.dt = data

    
    def divdif_table(self):
        N = len(self.dt[0])




def get_file(filename):
        # asks for file name
        equ_list = []
        with open(filename, 'r') as file:
            count = 0
            for line in file:
                count += 1
                if count > 2:
                    print("Please run the program with a proper set of values.")
                    quit()

                number_strings = line.split() # Split the line on runs of whitespace
                numbers = [float(n) for n in number_strings] # Convert to integers
                equ_list.append(numbers) # Add the "row" to your list.

                
        
        # Removes empty lists (caused by empty lines)
        equ_list = [x for x in equ_list if x!=[]]

        # Checks to make sure the number x = number of f[x]
        if len(equ_list[0]) != len(equ_list[1]):
            print("Please run the program with a proper set of values.")
            quit()
        

        return np.array(equ_list, dtype=float)


def main():
    data = get_file('values.txt')
    print(data)
    #buffer = interpolater(data)


if __name__ == "__main__":
    main()
