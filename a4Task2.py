# Write, append, and read from a text file

def write_to_file(filename):
    with open(filename, "w") as file:
        user_input = input("Enter text to write to the file: ")
        file.write(user_input + "\n")
        print("Data Successfully written to output.txt")


def append_to_file(filename):
    with open(filename, "a") as file:
        additional_input = input("Enter additional text to append: ")
        file.write(additional_input + "\n")
        print("Data Successfully appended.")

filename = "output.txt"

# Perform file operations
write_to_file(filename)
append_to_file(filename)

#Read
file1= open("output.txt","r")
reading_file=file1.read()
print("Final content of output.txt file\n",reading_file)
file1.close()