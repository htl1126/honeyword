import sys
import csv
 
def read_data(filename, num_set, num_sweetword):
    data = []
    with open(filename, 'r') as f:
        csv_data = csv.reader(f, delimiter=',')
        for row in csv_data:
            data.append(row)
    return data
 
def guess_honeyword(input_data):
    # perform guessing here
    pass
 
def main(num_sweetword, num_set, filename):
    input_data = read_data(filename, num_set, num_sweetword)
    guesses = guess_honeyword(input_data)
    for guess in guesses:
        print guess
 
if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3])
