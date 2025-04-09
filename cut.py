import random
import os

def shuffle_lines(file_path):
    """Shuffle lines of a text file and save the result as Mix.txt."""
    if not os.path.exists(file_path):
        print("Error: File not found! Check the path.")
        return
    if not file_path.endswith('.txt'):
        print("Error: Only .txt files are supported!")
        return

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        if not lines:
            print("Warning: The file is empty!")
            return
        
        random.shuffle(lines)

        # Save as Mix.txt in the same folder
        output_file = os.path.join(os.path.dirname(file_path), "Mix.txt")
        
        with open(output_file, 'w', encoding='utf-8') as file:
            file.writelines(line if line.endswith('\n') else line + '\n' for line in lines)
        
        print(f"Success! Shuffled file saved as: {output_file}")
        print(f"Total lines: {len(lines)}")
    
    except PermissionError:
        print("Error: No permission to write to the output location!")
    except Exception as e:
        print(f"Unexpected error: {e}")

def split_file(file_path, num_parts, content=None):
    """Split a file into multiple parts."""
    try:
        if content is None:
            with open(file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()
        else:
            lines = content.splitlines(keepends=True)
        
        total_lines = len(lines)
        if total_lines == 0:
            print("Error: File is empty!")
            return
        
        lines_per_part = total_lines // num_parts
        remainder = total_lines % num_parts
        
        for i in range(num_parts):
            start = i * lines_per_part
            end = start + lines_per_part + (1 if i < remainder else 0)
            part_lines = lines[start:end]
            
            part_file = f"{file_path[:-4]}_part{i+1}.txt"
            with open(part_file, 'w', encoding='utf-8') as file:
                file.writelines(part_lines)
            
            print(f"Created {part_file} with {len(part_lines)} lines")
    
    except Exception as e:
        print(f"Error splitting file: {e}")

def remove_duplicates(file_path):
    """Remove duplicate lines from a file."""
    if not os.path.exists(file_path):
        print("Error: File not found!")
        return None
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        unique_lines = []
        seen = set()
        
        for line in lines:
            stripped = line.strip()
            if stripped not in seen:
                seen.add(stripped)
                unique_lines.append(line)
        
        if len(unique_lines) == len(lines):
            print("No duplicates found!")
            return None
        
        output_file = f"{file_path[:-4]}_unique.txt"
        with open(output_file, 'w', encoding='utf-8') as file:
            file.writelines(unique_lines)
        
        print(f"Success! Unique file saved as: {output_file}")
        print(f"Original lines: {len(lines)}, Unique lines: {len(unique_lines)}")
        return '\n'.join(line.strip() for line in unique_lines)
    
    except Exception as e:
        print(f"Error removing duplicates: {e}")
        return None

def main():
    green = "\033[92m"
    red = "\033[91m"
    reset = "\033[0m"

    custom_logo = green + r"""
______      _           _         ______
| ___ \    | |         | |        | ___ \
| |_/ /__ _| |__   __ _| |_ ______| |_/ /__ _ ____
|    // _` | '_ \ / _` | __|______|    // _` |_  /
| |\ \ (_| | | | | (_| | |_       | |\ \ (_| |/ /
\_| \_\__,_|_| |_|\__,_|\__|      \_| \_\__,_/___/
⋆━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━⋆
""" + reset

    print(custom_logo)
    
    print(red + "1. Mix File" + reset)
    print(red + "2. File Cutter / Duplicate Remover" + reset)
    
    try:
        print(green + "Enter your choice (1 or 2): " + reset, end="")  # Prompt in green
        choice = int(input())
        
        if choice == 1:
            file_path = input("Enter file path (e.g., /sdcard/file.txt): ").strip()
            shuffle_lines(file_path)
        
        elif choice == 2:
            print("\nSub-options:")
            print("  1. Split file into parts")
            print("  2. Remove duplicates")
            print("  3. Both (Remove duplicates then split)")
            sub_choice = int(input("Enter sub-choice (1, 2, or 3): "))
            file_path = input("Enter file path (e.g., /sdcard/file.txt): ").strip()
            
            if sub_choice == 1:
                num_parts = int(input("Number of parts to split into: "))
                if num_parts <= 0:
                    print("Error: Enter a positive number!")
                else:
                    split_file(file_path, num_parts)
            
            elif sub_choice == 2:
                remove_duplicates(file_path)
            
            elif sub_choice == 3:
                num_parts = int(input("Number of parts after deduplication: "))
                if num_parts <= 0:
                    print("Error: Enter a positive number!")
                else:
                    unique_content = remove_duplicates(file_path)
                    if unique_content:
                        split_file(file_path, num_parts, unique_content)
            
            else:
                print("Error: Invalid choice!")
        
        else:
            print("Error: Invalid choice!")
    
    except ValueError:
        print("Error: Enter a valid number!")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("\nExiting...")

if __name__ == "__main__":
    main()