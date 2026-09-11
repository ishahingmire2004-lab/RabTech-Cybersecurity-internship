# Task 05 - Cryptography, Key Management & Secure Auth

Intern: Isha Hingmire | ID: RTA.CY.26.CAC.00313

## Implementation Summary
1. AES-256-GCM with random 12-byte nonce
2. RSA 2048 key pair + Digital Signature (PSS + SHA256)
3. bcrypt password hashing with salt + work factor 12

## Best Practices for Secret/Key Storage & Rotation
- Never hardcode keys in code, use ENV variables or Vault (AWS KMS / HashiCorp Vault)
- Rotate AES keys every 90 days, RSA keys every 1 year
- Use Principle of Least Privilege for key access
- Always use random IV/nonce for each encryption
- Store only hashed passwords with salt, not plain text

## How to Run
pip install cryptography bcrypt
python aes_256_gcm.py
python rsa_signature.py
python password_hashing.py
