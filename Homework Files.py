def read_integers_from_file(file_path):
    integers = []
    with open(file_path, 'r') as file:
        for line in file:
            integers.append(int(line.strip()))
    return integers

def write_integers_to_file(file_path, integers):
    with open(file_path, 'w') as file:
        for integer in integers:
            file.write(str(integer) + '\n')

def main():
    file_path = 'integers.txt'
    integers = read_integers_from_file(file_path)

    print('File starts with the following values:')
    for integer in integers:
        print(integer)

    while True:
        new_integer = int(input('Please enter an integer. Enter zero (0) to end: '))
        if new_integer == 0:
            break
        integers.append(new_integer)

    print('\nAll values entered:')
    for integer in integers:
        print(integer)

    write_integers_to_file(file_path, integers)

if __name__ == '__main__':
    main()
    