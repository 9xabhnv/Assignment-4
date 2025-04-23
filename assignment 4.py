# Task 1

try:
    with open('sample.txt','r') as file1:
        print('Reading file content:')
        count = 0
        for line in file1:
            count += 1
            print(f'Line{count}: {line.strip()}')

except FileNotFoundError:
    print('Error: The file "sample.txt" was not found.')

# ------------------------------------------------------------------------------------------------

# Task 2

x = input('Enter text to write to the file: ')
with open('output.txt', 'w') as file2:
    writing = file2.write(x)
    print('Data successfully written to output.txt.\n')

y = input('Enter additional text to append: ')
with open('output.txt', 'a') as file2:
    append = file2.write(f'\n{y}')
    print('Data successfully appended.\n')

with open('output.txt', 'r') as file2:
    read = file2.read()
    print('final content of the output.txt:\n', read)
