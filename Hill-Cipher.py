###########################################
# Hill Cipher using python
# Nishant Tomar
# 2020PMD4210
###########################################


# Importing regex library
import re

# Key (3x3 matrix therefore, plaintext matrix possible matrices - 3x1, 3x2, 3x3)
key_matrix = [[6, 5, 1], [3, 2, 3], [4, 3, 2]]
rows = columns = 3                                                                                                                  # Column and row size of matrix


# To get integer associated with that character
def char_to_int(character):
    # Cast chr to int and subtract 65 to get 0-25
    integer = int(ord(character) - 65)

    return integer


# To get character associated with that integer
def int_to_char(integer):
    # Cast int to char and add 65 to get A-Z
    character = chr(integer + 65)

    return character


# Checks if the input message contains any number
def has_numbers(input):
    return any(character.isdigit() for character in input)


# Checks the length of input string (3, 6, 9) - lengths only possible (because of dimension of key_matrix)
def check_length(input):
    return True if len(input) in (3, 6, 9) else False


# Check if any illegal characters present in the string
def check_illegal_char(input):
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')                                                                                 # Regex

    return True if regex.search(input) == None else False


# Checking of input string
def check_input(input):
    # Checking all valid conditions if true
    if not has_numbers(input) and check_length(input) and check_illegal_char(input):
        return True

    return False


# To take plain-text input from the user (Message to be encrypted)
def take_input():
    print("\n\n####################################")
    print("\t\t\tHILL CIPHER")
    print("####################################\n\n")
    input_string = ""

    # Loop till the input is not valid
    while True:
        input_string = input("Enter your message to be encrypted in capital-letters (Input length of message should be 3, 6 or 9): ")
        flag = check_input(input_string)

        if flag:
            break
        else:
            print("\nPlease try again (Invalid input)!")


'''
    # Taking matrix input in one line
    character_input_matrix = [[input("Input[" + str(y+1) + "][" + str(x+1) + "]: ").upper() for x in range(columns)] for y in range(rows)]

    # Printing the input matrix
    print("\n\nEntered input matrix")
    [[print(character_input_matrix[y][x] + " ", end = "\n" if x in (2, 5, 8) else " ") for x in range(columns)] for y in range(rows)]
    print("\n\n")

    # Convertor character matrix to integer matrix
    integer_input_matrix = [[char_to_int(character_input_matrix[y][x]) for x in range(columns)] for y in range(rows)]

    return integer_input_matrix
'''

# Function to perform matrix multiplication between 2 matrices
def matrix_multiplication(matrix1, matrix2):
    # Resultant matrix
    result_matrix = [[0, 0, 0] for i in range(rows)]

    # Iterating by row of matrix1
    for i in range(len(matrix1)):
        # Iterating by column by matrix2
        for j in range(len(matrix2[0])):
            # Iterating by rows of matrix2
            for k in range(len(matrix2)):
                result_matrix[i][j] += matrix1[i][k] * matrix2[k][j]
            result_matrix[i][j] = result_matrix[i][j] % 26                                                                        # Convert to base 26

    return result_matrix


# To display the encrypted message
def display_encrypted_message(matrix):
    print("Encrypted Message: ", end = "")
    [[print(int_to_char(int(matrix[x][y])), end = " ") for y in range(columns)] for x in range(rows)]

# Function to encrypt the message
def encryption(matrix):
    encrypted_matrix = matrix_multiplication(key_matrix, matrix)                                                                  # Matrix multiplication ( C = K * P mod 26)
    display_encrypted_message(encrypted_matrix)

    return encrypted_matrix


# So that this function doesn't run when some other file imports this file
if __name__ == "__main__":
    take_input()
    #message_matrix = take_input()
    #encrypted_matrix = encryption(message_matrix)