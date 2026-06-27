import string
import secrets

def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    """Generates a secure password based on chosen complexity criteria."""
    # Build the available pool of characters
    character_pool = ""
    if use_upper:
        character_pool += string.ascii_uppercase
    if use_lower:
        character_pool += string.ascii_lowercase
    if use_digits:
        character_pool += string.digits
    if use_symbols:
        character_pool += string.punctuation

    # Guard clause: ensure at least one criteria is selected
    if not character_pool:
        return "Error: You must select at least one character type."

    # Generate a cryptographically secure random password
    password = "".join(secrets.choice(character_pool) for _ in range(length))
    return password

def get_boolean_input(prompt):
    """Helper function to confirm yes/no choices clearly."""
    while True:
        choice = input(prompt).strip().lower()
        if choice in ['y', 'yes', '']:
            return True
        if choice in ['n', 'no']:
            return False
        print("Please enter 'y' for Yes or 'n' for No.")

def main():
    print("=== Secure Password Generator ===")
    
    # 1. Capture and validate password length
    while True:
        try:
            length = int(input("Enter the desired password length (minimum 8 recommended): "))
            if length <= 0:
                print("Length must be a positive number.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    # 2. Configure password complexity settings
    print("\n--- Configure Password Complexity ---")
    use_upper = get_boolean_input("Include uppercase letters? (A-Z) [Y/n]: ")
    use_lower = get_boolean_input("Include lowercase letters? (a-z) [Y/n]: ")
    use_digits = get_boolean_input("Include numbers? (0-9) [Y/n]: ")
    use_symbols = get_boolean_input("Include symbols? (@, #, $, etc.) [Y/n]: ")

    # 3. Process, build, and display the secure password string
    password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)
    
    print("\n----------------------------------------")
    print(f"Your Generated Password: {password}")
    print("----------------------------------------")

if __name__ == "__main__":
    main()
