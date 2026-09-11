import bcrypt

# Task 05 - Part 3: Secure Password Hashing with bcrypt + Salt
password = b"MySecurePassword@123"
print(f"Original Password: {password.decode()}")

# Hash with random salt and work factor 12
hashed_password = bcrypt.hashpw(password, bcrypt.gensalt(rounds=12))
print(f"Hashed Password (with salt): {hashed_password.decode()}")

# Verify - Correct password
if bcrypt.checkpw(password, hashed_password):
    print("Verification 1: Correct Password - Login Success!")

# Verify - Wrong password
wrong_password = b"WrongPassword"
if not bcrypt.checkpw(wrong_password, hashed_password):
    print("Verification 2: Wrong Password - Login Failed (as expected)")

print("\nBest Practice: Never store plain text passwords, only hashes!")
