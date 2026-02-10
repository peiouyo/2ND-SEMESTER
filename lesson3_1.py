correct_password = "user123"

entered_password = input("Enter your password: ")

if entered_password == correct_password:
    print("Logged in.")
else:
    print("Access denied")