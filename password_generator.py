import random
import string

def generate_password(length):
    all_chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

def main():
    print("\n Password Generator")
    try:
        length = int(input("Enter desired password length: "))
        if length < 4:
            print("Password too short! Minimum length is 4.")
            return
        password = generate_password(length)
        print(f"Generated Password: {password}")
    except ValueError:
        print("Please enter a valid number!")

if __name__ == "__main__":
    main()
