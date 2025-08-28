def modify_content(content):
    """Example modification function - converts text to uppercase"""
    return content.upper()

def main():
    print("File Read & Write Challenge with Error Handling 🖋️")
    print("=" * 55)
    
    # Get input filename from user
    input_filename = input("Please enter the input filename: ").strip()
    
    # Validate input filename
    if not input_filename:
        print("Error: No filename provided. Please try again.")
        return
    
    # Get output filename from user
    output_filename = input("Please enter the output filename: ").strip()
    
    # Validate output filename
    if not output_filename:
        print("Error: No output filename provided. Please try again.")
        return
    
    # Check if output file already exists
    try:
        with open(output_filename, 'r'):
            pass
        overwrite = input(f"The file '{output_filename}' already exists. Overwrite? (y/n): ").strip().lower()
        if overwrite != 'y':
            print("Operation cancelled.")
            return
    except FileNotFoundError:
        pass  # This is good - file doesn't exist yet
    except Exception as e:
        print(f"Error checking output file: {e}")
        return
    
    # Try to read the input file
    try:
        with open(input_filename, 'r') as file:
            content = file.read()
        print(f"Successfully read from '{input_filename}'")
        
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
        return
    except PermissionError:
        print(f"Error: Permission denied to read '{input_filename}'.")
        return
    except IOError as e:
        print(f"Error reading file: {e}")
        return
    except Exception as e:
        print(f"Unexpected error: {e}")
        return
    
    # Modify the content
    modified_content = modify_content(content)
    
    # Try to write to the output file
    try:
        with open(output_filename, 'w') as file:
            file.write(modified_content)
        print(f"Successfully wrote modified content to '{output_filename}'")
        print(f"Original size: {len(content)} characters")
        print(f"Modified size: {len(modified_content)} characters")
        
    except PermissionError:
        print(f" Error: Permission denied to write to '{output_filename}'.")
        return
    except IOError as e:
        print(f"Error writing to file: {e}")
        return
    except Exception as e:
        print(f"Unexpected error while writing: {e}")
        return

if __name__ == "__main__":
    main()