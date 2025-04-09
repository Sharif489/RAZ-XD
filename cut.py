import random
import os

def print_logo():
    logo = """
        \033[32m
    ______      _           _         ______
    | ___ \    | |         | |        | ___ \ 
    | |_/ /__ _| |__   __ _| |_ ______| |_/ /__ _ ____
    |    // _` | '_ \ / _` | __|______|    // _` |_  /
    | |\ \ (_| | | | | (_| | |_       | |\ \ (_| |/ /
    \_| \_\__,_|_| |_|\__,_|\__|      \_| \_\__,_/___/
    ⋆━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━⋆
    """
    
    print(logo)

# List of 497 valid names
valid_names = [
    "Akter", "Islam", "Khatun", "Hossain", "Rahman", "Hasan", "Ahmed", "Begum", "Khan", "Uddin",
    "Chowdhury", "Ali", "Sultana", "Miah", "Jahan", "Nessa", "Rana", "Zaman", "Mollah", "Ferdous",
    "Zubair", "Muni", "Bithi", "Sayed", "Jamal", "Parvin", "Salahuddin", "Shafi", "Parvin", "Rashid",
    "Sultana", "Nahar", "Tariq", "Dipu", "Ahsan", "Mim", "Tanjin", "Hasina", "Papia", "Shamim", "Rafiq",
    "Amin", "Ruksana", "Monowar", "Samsul", "Shahida", "Afroza", "Hossain", "Imran", "Alim", "Bari",
    "Yasmin", "Mollika", "Chowdhury", "Shamim", "Amin", "Khatun", "Miya", "Abdur", "Rahman", "Mazid",
    "Sana", "Monir", "Zaman", "Bala", "Aziz", "Rahman", "Rafique", "Kazi", "Mizan", "Shafique", "Taher",
    "Fatema", "Zahid", "Afsana", "Kamal", "Farzana", "Mariam", "Samir", "Tahmina", "Zillur", "Abdul",
    "Ali", "Kabir", "Aminul", "Sohana", "Rasheda", "Muktadir", "Anwar", "Rahman", "Jannatul", "Nushrat",
    "Sakib", "Moshin", "Riya", "Sabrina", "Abdullah", "Anwar", "Majid", "Fariha", "Rabiul", "Shefali",
    "Selina", "Sajeda", "Sakir", "Moyna", "Samira", "Habiba", "Shima", "Khaled", "Nafisa", "Mokhlesur",
    "Khan", "Samim", "Shibli", "Masud", "Arman", "Simi", "Sukanya", "Lia", "Junaid", "Mamun", "Meher",
    "Mim", "Tahmina", "Azmi", "Alisha", "Tariq", "Sabrina", "Samiya", "Humayra", "Shanta", "Arif",
    "Hina", "Nazmul", "Monzur", "Sabbir", "Shirin", "Manzura", "Sokhina", "Basha", "Zubair", "Sumaiya",
    "Choudhury", "Monjur", "Shakil", "Mursalin", "Rina", "Samiul", "Afnan", "Tanjina", "Sajeda", "Ali",
    "Umar", "Musiha", "Saiful", "Amena", "Shahina", "Harun", "Jewel", "Shabab", "Abir", "Mehedi", "Shahida",
    "Marium", "Shahla", "Fayza", "Mizanur", "Fahad", "Esha", "Jasmin", "Fatema", "Sadiya", "Morsheda",
    "Chowdhury", "Samia", "Taha", "Mohsin", "Rabia", "Fahmida", "Feroza", "Ammar", "Tariq", "Bithi",
    "Nasrin", "Sumaiya", "Sadia", "Rubina", "Akram", "Raisa", "Sharif", "Ayesha", "Asma", "Shilpi",
    "Anwar", "Abu", "Ria", "Alvi", "Sohana", "Kabir", "Farida", "Riyad", "Ovi", "Aklima", "Tariq",
    "Sifat", "Sharmin", "Afnan", "Murshed", "Jannatul", "Shahina", "Samiha", "Dulal", "Shagor", "Farzana",
    "Arman", "Nila", "Shahina", "Ruhul", "Ishika", "Hassan", "Mariam", "Hadiya", "Zannatul", "Aminul",
    "Shahnaaz", "Shahinur", "Fahim", "Muni", "Shima", "Raihan", "Mushfiq", "Alma", "Shuvon", "Kausar",
    "Farhana", "Rizwan", "Sushmita", "Shahin", "Rumi", "Kazi", "Rabiul", "Nayeem", "Mahfuz", "Habiba",
    "Aminul", "Tumpa", "Imam", "Akhtar", "Moinul", "Samia", "Marzan", "Madhur", "Mehedi", "Kazi",
    "Tahmina", "Moyna", "Sultana", "Wasi", "Uzzal", "Shabnam", "Fahim", "Selim", "Juthi", "Imran",
    "Asiya", "Abdul", "Sumon", "Rahima", "Sumaya", "Rashed", "Zaynab", "Shamsul", "Nilufa", "Khaleda",
    "Sakil", "Sumon", "Sami", "Nayeem", "Rasel", "Sharif", "Shakil", "Rufaida", "Riya", "Alif",
    "Firoza", "Amin", "Syed", "Nabil", "Shakila", "Mizan", "Nazia", "Monika", "Nusrat", "Rina",
    "Sabrina", "Sharon", "Mubeen", "Rojina", "Mintu", "Mokhles", "Zubair", "Jalil", "Monirul",
    "Rabiul", "Akhtar", "Meher", "Fahad", "Ishita", "Ayesha", "Sima", "Mushfiq", "Samiha",
    "Ruhul", "Tariq", "Mahmud", "Musharraf", "Ismail", "Rifat", "Shariar", "Madhur", "Mannan",
    "Rifat", "Shabnam", "Zafrin", "Imran", "Sadia", "Sohel", "Sumaiya", "Hafiza", "Shaila",
    "Rubel", "Tamanna", "Manar", "Sakib", "Rohman", "Imtiaz", "Farida", "Jahid", "Shoma"
]

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
    
    except Exception as e:
        print(f"An error occurred: {e}")

def split_file(file_path, num_parts):
    """Split a file into multiple parts."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        if not lines:
            print("Error: File is empty!")
            return
        
        total_lines = len(lines)
        lines_per_part = total_lines // num_parts
        remainder = total_lines % num_parts
        
        for i in range(num_parts):
            start = i * lines_per_part
            end = start + lines_per_part + (1 if i < remainder else 0)
            part_lines = lines[start:end]
            
            part_file = f"{file_path[:-4]}_part{i+1}.txt"
            with open(part_file, 'w', encoding='utf-8') as file:
                file.writelines(part_lines)
            
            print(f"Created {part_file} with {len(part_lines)} lines.")
    
    except Exception as e:
        print(f"Error while splitting file: {e}")

def remove_duplicates(file_path):
    """Remove duplicate lines from a file and save as NoDuplicates.txt."""
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
        
        # Remove duplicates while maintaining the order
        unique_lines = list(dict.fromkeys(lines))

        # Save the result to NoDuplicates.txt
        output_file = os.path.join(os.path.dirname(file_path), "NoDuplicates.txt")
        with open(output_file, 'w', encoding='utf-8') as file:
            file.writelines(unique_lines)
        
        print(f"Duplicate removal completed! The file without duplicates has been saved as: {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

def filter_valid_names(input_file_path, output_file_path):
    """Filter lines containing valid names from the input file and save to a new file."""
    if not os.path.exists(input_file_path):
        print("Error: Input file not found! Check the path.")
        return
    if not input_file_path.endswith('.txt'):
        print("Error: Only .txt files are supported!")
        return
    
    try:
        with open(input_file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        if not lines:
            print("Warning: The file is empty!")
            return
        
        # Filter lines based on valid names list
        filtered_lines = [line for line in lines if any(name in line for name in valid_names)]
        
        if filtered_lines:
            with open(output_file_path, 'w', encoding='utf-8') as file:
                file.writelines(filtered_lines)
            print(f"Filtering completed! The file with valid names has been saved as: {output_file_path}")
        else:
            print("No valid names were found in the file.")
    except Exception as e:
        print(f"An error occurred: {e}")

def process_file(input_file_path):
    """Run all processes (cutter, duplicate remover, filter) on the file."""
    print("Processing file...")

    # Step 1: Shuffle the lines in the file
    print("Shuffling the file...")
    shuffle_lines(input_file_path)

    # Step 2: Remove duplicates from the shuffled file
    shuffled_file_path = os.path.join(os.path.dirname(input_file_path), "Mix.txt")
    print("Removing duplicates from the shuffled file...")
    remove_duplicates(shuffled_file_path)

    # Step 3: Filter valid names from the file
    no_duplicates_file_path = os.path.join(os.path.dirname(input_file_path), "NoDuplicates.txt")
    output_file_path = os.path.join(os.path.dirname(input_file_path), "FilteredNames.txt")
    print("Filtering valid names from the file...")
    filter_valid_names(no_duplicates_file_path, output_file_path)

    print("Processing completed!")

def main():
    """Main menu for user to select the operation."""
    print_logo()
    while True:
        # Set color to red for the menu
        print("\033[31m")
        print("\nSelect an option:")
        print("1. Mix File")
        print("2. File Cutter / Duplicate Remover")
        print("3. Ready File 1 Click")
        print("\033[0m")  # Reset color to default
        
        # Get user input for menu choice
        choice = input("\033[34mEnter your choice (1, 2, or 3): \033[0m")

        # Perform actions based on choice
        if choice == '1':
            file_path = input("\033[31mEnter file path (e.g., /sdcard/file.txt): \033[0m")
            shuffle_lines(file_path)
        
        elif choice == '2':
            file_path = input("\033[31mEnter file path (e.g., /sdcard/file.txt): \033[0m")
            num_parts = int(input("\033[31mEnter number of parts to split: \033[0m"))
            split_file(file_path, num_parts)
            remove_duplicates(file_path)
        
        elif choice == '3':
            file_path = input("\033[31mEnter file path (e.g., /sdcard/file.txt): \033[0m")
            process_file(file_path)
        
        else:
            print("\033[31mInvalid choice. Please try again.\033[0m")
        
        # Ask if user wants to perform another operation
        cont = input("\033[3m\nDo you want to perform another operation? (y/n): \033[0m").lower()
        if cont != 'y':
            print("Exiting program...")
            break

if __name__ == "__main__":
    main()