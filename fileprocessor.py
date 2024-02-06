# Open the file
with open('fileprocessor.input', 'r') as file:
    # Read lines into a list, skipping lines that start with "#"
    lines = [line.strip() for line in file if not line.startswith('#')]
    
    # Split each line into a list using ":" as delimiter
    user_data = [line.split(':') for line in lines]

print("Printing out User Data:\n")
for user in user_data:
    # Ensure each line has exactly 4 parts to avoid 'IndexError'
    if len(user) == 4:
        print(f"The user {user[0]} has a password of {user[1]} and has userid {user[2]} and groupid {user[3]}")
    else:
        print(f"Skipping invalid line: {' '.join(user)}")  # Handling lines that don't match the expected format
print("\nEnd of User Data")
