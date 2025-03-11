def read_file(filename):
    print ("Reading file content\n")
    try:
        file = open(filename, "r")
        line_number = 1
        for line in file:
            # Print each line
            print(f"Line {line_number}: {line}")
            line_number += 1
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        try:
            file.close()
        except NameError:
            pass
filename = "sample.txt"
read_file(filename)
