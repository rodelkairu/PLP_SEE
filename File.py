import os

def read_and_write_modified_file():

    input_filename = input("Please enter the name of the input file: ")
    output_filename = input("Please enter the name of the output file (e.g., 'output.txt'): ")

    modified_content = []
    
    try:
        # 1. Read the input file
        with open(input_filename, 'r', encoding='utf-8') as infile:
            print(f"Attempting to read from '{input_filename}'...")
            for line_num, line in enumerate(infile, 1):
                # Example modification: Convert each line to uppercase
                modified_line = line.upper()
                modified_content.append(modified_line)
            print(f"Successfully read and modified content from '{input_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found. Please check the filename and try again. 🚫")
        return
    except PermissionError:
        print(f"Error: Permission denied to access '{input_filename}'. Make sure you have the necessary read permissions. 🔒")
        return
    except IOError as e:
        print(f"Error: An I/O error occurred while reading '{input_filename}': {e} 💔")
        return
    except Exception as e:
        print(f"An unexpected error occurred during file reading: {e} ⚠️")
        return

    # 2. Write the modified content to the output file
    try:
        with open(output_filename, 'w', encoding='utf-8') as outfile:
            print(f"Attempting to write modified content to '{output_filename}'...")
            outfile.writelines(modified_content)
            print(f"Successfully wrote modified content to '{output_filename}'. 🎉")
    except PermissionError:
        print(f"Error: Permission denied to write to '{output_filename}'. Make sure you have the necessary write permissions. 🔒")
        return
    except IOError as e:
        print(f"Error: An I/O error occurred while writing to '{output_filename}': {e} 💔")
        return
    except Exception as e:
        print(f"An unexpected error occurred during file writing: {e} ⚠️")
        return

    print("\nProgram finished.")

# Call the function to run the program
if __name__ == "__main__":
    # Create a dummy input file for testing if it doesn't exist
    test_input_file = "sample_input.txt"
    if not os.path.exists(test_input_file):
        with open(test_input_file, 'w', encoding='utf-8') as f:
            f.write("Hello, this is a test line.\n")
            f.write("Another line for the file read challenge.\n")
        print(f"Created a dummy file '{test_input_file}' for testing. You can use this as your input.")

    read_and_write_modified_file()
