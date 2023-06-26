import random
from src.leet_script import leet_pass

try:
    with open("media/art.txt", "r") as file:
        banner = file.read()
        print(banner)
except FileNotFoundError:
    print("Error: The ASCII banner file was not found.")

special_chars = ["$", "@", "#", "%" "!", "&", "$$", "@@", "##", "!!", "%%", "&&"]


def generate_passwords(words1, numbers2, qty3, use_leet=False):
    passwords1 = set()
    generated_qty = 0
    for word in words1:
        for number in numbers2:
            passwords1.add(word + number)
            passwords1.add(number + word)
            passwords1.add(number + number)
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
            passwords1.add(word + '-' + number)
            passwords1.add(number + '-' + word)
            passwords1.add(word.capitalize() + '-' + number)
            passwords1.add(number + '-' + word.capitalize())
            passwords1.add(word.upper() + '-' + number)
            passwords1.add(number + '-' + word.upper())
            passwords1.add(word[0].upper() + word[1:] + '-' + number)
            passwords1.add(number + '-' + word[0].upper() + word[1:])
            passwords1.add(word[0].lower() + word[1:] + '-' + number)
            passwords1.add(number + '-' + word[0].lower() + word[1:])
            passwords1.add(word + '.' + number)
            passwords1.add(number + '.' + word)
            passwords1.add(word.capitalize() + '.' + number)
            passwords1.add(number + '.' + word.capitalize())
            passwords1.add(word.upper() + '.' + number)
            passwords1.add(number + '.' + word.upper())
            passwords1.add(word[0].upper() + word[1:] + '.' + number)
            passwords1.add(number + '.' + word[0].upper() + word[1:])
            passwords1.add(word[0].lower() + word[1:] + '.' + number)
            passwords1.add(number + '.' + word[0].lower() + word[1:])
            passwords1.add(word + '1234')
            passwords1.add('1234' + word)
            passwords1.add(word + '123')
            passwords1.add('123' + word)
            passwords1.add(word.capitalize() + '123')
            passwords1.add('123' + word.capitalize())
            passwords1.add(word.capitalize() + '1234')
            passwords1.add('1234' + word.capitalize())
            passwords1.add(word + random.choice(special_chars))

            if use_leet:
                leet_passwords = leet_pass([word], [number], qty3)
                passwords1.update(leet_passwords)

            generated_qty += 1

            if generated_qty >= qty3:
                break

        if generated_qty >= qty3:
            break

    generated_passwords = list(passwords1)
    generated_qty = len(generated_passwords)
    if generated_qty < qty3:
        print(f"[!] Not enough combinations available.\n[-] Unable to generate {qty3} passwords."
              f"\n[+] Generated {generated_qty}"
              f"passwords instead.")

    return generated_passwords[:qty3]


# Get the file path from the user
file_path = input("\n[*] Enter the file path: ").strip('"')

try:
    with open(file_path, 'r') as file:
        lines = file.read().splitlines()
        words = [line for line in lines if not line.isdigit()]
        numbers = [line for line in lines if line.isdigit()]

        user_input = input("[*] How many passwords do you want to generate (Default 100): ")
        qty = 100 if user_input == "" else int(user_input)

        use_leet_speak = input("[*] Do you want to use leet speak in the passwords (Y/N)? ").lower() == 'y'

        passwords = generate_passwords(words, numbers, qty, use_leet=use_leet_speak)

        output_file = 'passwords.txt'
        with open(output_file, 'w') as output:
            for password in passwords:
                output.write(password + '\n')

        if len(passwords) == qty:
            print(f"[+] {qty} passwords generated and saved to {output_file}.")


except FileNotFoundError:
    print("[!] File not found. Please make sure the file exists and try again.")
except ValueError:
    print("[-] Enter a valid integer for the quantity.")
except KeyboardInterrupt:
    print("[-] Keyboard interrupt detected, exiting....")
