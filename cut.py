def remove_duplicates(file_path):
    """Remove duplicate lines from a file and return unique lines."""
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.readlines()
    
    unique_content = list(dict.fromkeys(line.strip() for line in content))
    
    if not unique_content:
        print("The file is empty after removing duplicates!")
        return None
    
    output_file = f"{file_path[:-4]}_no_duplicates.txt"
    with open(output_file, 'w', encoding='utf-8') as out_file:
        out_file.writelines(line + '\n' for line in unique_content)
    
    print(f"Duplicates removed! Saved as: {output_file} (Lines: {len(unique_content)})")
    return unique_content

def split_file(file_path, num_parts, content=None):
    """Split a file or content list into specified number of parts."""
    if content is None:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.readlines()
    
    total_lines = len(content)
    if total_lines == 0:
        print("The file is empty!")
        return
    
    lines_per_part = total_lines // num_parts
    extra_lines = total_lines % num_parts

    for i in range(num_parts):
        start = i * lines_per_part + min(i, extra_lines)
        end = start + lines_per_part + (1 if i < extra_lines else 0)
        
        output_file = f"{file_path[:-4]}_part{i+1}.txt"
        with open(output_file, 'w', encoding='utf-8') as part_file:
            part_file.writelines(line if line.endswith('\n') else line + '\n' 
                               for line in content[start:end])
        print(f"Created: {output_file} (Lines: {end - start})")

def main():
    # Your custom ASCII logo with ANSI color codes
    custom_logo = """\033[1;36m
______      _           _         ______          
| ___ \    | |         | |        | ___ \         
| |_/ /__ _| |__   __ _| |_ ______| |_/ /__ _ ____
|    // _` | '_ \ / _` | __|______|    // _` |_  /
| |\ \ (_| | | | | (_| | |_       | |\ \ (_| |/ / 
\_| \_\__,_|_| |_|\__,_|\__|      \_| \_\__,_/___|
\x1b[38;5;46m⋆\x1b[38;5;254m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\x1b[38;5;50m⋆\033[0m
"""
    print(custom_logo)
    
    print("1. File Cutter (Split into parts)")
    print("2. Duplicate Remover")
    print("3. Both (Remove duplicates then split)")
    
    try:
        choice = int(input("Enter your choice (1, 2, or 3): "))
        file_path = input("Enter the path to your .txt file: ")
        
        if choice == 1:
            num_parts = int(input("How many parts to split into? (e.g., 2, 3, 4, 5): "))
            if num_parts <= 0:
                print("Please enter a positive number!")
            else:
                split_file(file_path, num_parts)
        
        elif choice == 2:
            remove_duplicates(file_path)
        
        elif choice == 3:
            num_parts = int(input("How many parts to split into after removing duplicates? (e.g., 2, 3, 4, 5): "))
            if num_parts <= 0:
                print("Please enter a positive number!")
            else:
                unique_content = remove_duplicates(file_path)
                if unique_content:
                    split_file(file_path, num_parts, unique_content)
        
        else:
            print("Invalid choice! Please select 1, 2, or 3.")
        
        print("\n\033[1;32mTask completed! Thanks for using File Organizer.\033[0m")
    
    except FileNotFoundError:
        print("File not found! Please check the path.")
    except ValueError:
        print("Please enter valid numbers where required.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("\033[1;36mExiting...\033[0m")

if __name__ == "__main__":
    main()