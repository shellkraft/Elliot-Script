def generate_passwords(words1, numbers2, qty3):
    passwords1 = set()  # Use a set to store unique passwords1
    for word in words1:
        for number in numbers2:
            passwords1.add(word + number)
            passwords1.add(number + word)
            passwords1.add(word.capitalize() + number)
            passwords1.add(number + word.capitalize())
            passwords1.add(word.upper() + number)
            passwords1.add(number + word.upper())
            passwords1.add(word[0].upper() + word[1:] + number)
            passwords1.add(number + word[0].upper() + word[1:])
            passwords1.add(word[0].lower() + word[1:] + number)
            passwords1.add(number + word[0].lower() + word[1:])
            passwords1.add(word + '_' + number)
            passwords1.add(number + '_' + word)
            passwords1.add(word.capitalize() + '_' + number)
            passwords1.add(number + '_' + word.capitalize())
            passwords1.add(word.upper() + '_' + number)
            passwords1.add(number + '_' + word.upper())
            passwords1.add(word[0].upper() + word[1:] + '_' + number)
            passwords1.add(number + '_' + word[0].upper() + word[1:])
            passwords1.add(word[0].lower() + word[1:] + '_' + number)
            passwords1.add(number + '_' + word[0].lower() + word[1:])
    return list(passwords1)[:qty3]


# Get the file path from the user
file_path = input("[*] Enter the file path: ").strip('"')

try:
    with open(file_path, 'r') as file:
        lines = file.read().splitlines()
        words = [line for line in lines if not line.isdigit()]
        numbers = [line for line in lines if line.isdigit()]

        user_input = input("[*] How many passwords do you want to generate: ")
        qty = 100 if user_input == "" else int(user_input)

        passwords = generate_passwords(words, numbers, qty)

        # Save passwords to a text file
        output_file = 'passwords.txt'
        with open(output_file, 'w') as output:
            for password in passwords:
                output.write(password + '\n')

        print(f"[+] Passwords generated and saved to {output_file}.")
except FileNotFoundError:
    print("[!] File not found. Please make sure the file exists and try again.")
except ValueError:
    print("[-] Enter a valid integer for the quantity.")
