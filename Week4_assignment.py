# File handling and error handling
# The code below reads from a file, modifies the content, and writes it to a new file.
# It includes error handling to deal with common file access issues.

def main():
    # Ask the user to enter the name of the file to read
    input_filename = input("Please enter the name of the file you want to read: ")

    try:
        # Try opening the input file for reading
         # This will raise a FileNotFoundError if the file does not exist.
        with open(input_filename, 'r') as infile:
            content = infile.read()  # Read all content from the file

        # Modify the content e.g by converting it to uppercase
        modified_content = content.upper()

        # Ask the user for the output file name
        output_filename = input("Please enter the name of the new file to write the modified content: ")

        # Open the output file in write mode and write the modified content
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)

        print(f"\nSuccess! Modified content has been written to '{output_filename}'.")

    # Handling the case when the file does not exist
    except FileNotFoundError:
        print(f"\nError: The file '{input_filename}' was not found.")

    # Handle the case when the file cannot be read due to permission issues
    except PermissionError:
        print(f"\nError: You do not have permission to access '{input_filename}'.")

    # Other exceptions handling
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")


# Call the main function to run the program
if __name__ == "__main__":
    main()
