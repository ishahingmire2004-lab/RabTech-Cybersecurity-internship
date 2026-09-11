# Task 05: Cryptography, Key Management & Secure Authentication

Intern: Isha Hingmire | ID: RTA.CY.26.CAC.00313
Tools Used: Python, cryptography library, bcrypt, AES-256-GCM, RSA 2048

### 1. AES-256-GCM Encryption & Decryption
- Implemented random 12-byte IV/nonce
- 256-bit key generation
- Authenticated encryption

### 2. RSA 2048 Key Pair & Digital Signature
- Generated 2048-bit RSA key pair
- Signed document with PSS padding + SHA256
- Verified signature for integrity

### 3. Password Hashing with bcrypt
- Hashed password with salt + work factor 12
- Verified secure password matching

### Best Practices for Key Storage & Rotation
1. Never hardcode keys - use ENV or Vault (AWS KMS, HashiCorp Vault)
2. Rotate AES keys every 90 days, RSA every 1 year
3. Least Privilege - only app service should access keys
4. Use random IV/nonce every encryption
5. Store hashed passwords, never plain text

### How to Run
pip install cryptography bcrypt
python aes_256_gcm.py
python rsa_signature.py
python password_hashing.py
