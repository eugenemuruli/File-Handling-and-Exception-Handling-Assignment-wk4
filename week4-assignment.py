# Eugene's File Read & Write with Error Handling
# This program reads a file, converts content to uppercase, and saves it to a new file.

def modify_file_content(input_filename, output_filename):
    """
    Reads a file, converts its content to uppercase,
    and writes the result to a new file.
    """
    try:
        # Attempt to open and read the input file
        with open(input_filename, 'r', encoding='utf-8') as infile:
            content = infile.read()
        
        # Modify content: convert to uppercase
        modified_content = content.upper()
        
        # Write modified content to the output file
        with open(output_filename, 'w', encoding='utf-8') as outfile:
            outfile.write(modified_content)
        
        print(f"✅ Success! Modified content has been written to '{output_filename}'.")
    
    except FileNotFoundError:
        print(f"❌ Error: The file '{input_filename}' was not found.")
    except PermissionError:
        print(f"❌ Error: Permission denied when accessing '{input_filename}' or '{output_filename}'.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

def main():
    print("File Read & Write Challenge with Error Handling")
    print("This program reads a file, converts text to uppercase, and saves it to a new file.\n")
    
    # Ask user for input filename
    input_file = input("Enter the name of the file to read: ").strip()
    
    # Define output filename
    output_file = "modified_" + input_file
    
    # Call the function to process the file
    modify_file_content(input_file, output_file)

# Run the program
if __name__ == "__main__":
    main()