while True:
    password = input("Enter a password: ")
    has_letter = any(char.isalpha() for char in password)
    has_number = any(char.isdigit() for char in password)

    if has_letter and has_number:
        print("Password accepted.")
        break
    else:
        if not has_letter:
            print("Password needs at least one letter.")
        if not has_number:
            print("Password needs at least one number.")