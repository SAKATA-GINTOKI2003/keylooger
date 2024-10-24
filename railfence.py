def encrypt(text, rails):
    """Encrypt text using Rail Fence cipher"""
    # Create the rail fence pattern
    fence = [[None] * len(text) for _ in range(rails)]
    rail, direction = 0, 1

    # Fill the pattern
    for i, char in enumerate(text):
        fence[rail][i] = char
        rail += direction
        if rail in (0, rails - 1):
            direction *= -1
    
    # Read off the cipher text
    return ''.join(char for rail in fence for char in rail if char)

def decrypt(cipher, rails):
    """Decrypt text using Rail Fence cipher"""
    # Create the fence pattern
    fence = [[None] * len(cipher) for _ in range(rails)]
    rail, direction = 0, 1

    # Mark the fence pattern
    for i in range(len(cipher)):
        fence[rail][i] = True
        rail += direction
        if rail in (0, rails - 1):
            direction *= -1

    # Fill the fence with cipher text
    index = 0
    for i in range(rails):
        for j in range(len(cipher)):
            if fence[i][j] and index < len(cipher):
                fence[i][j] = cipher[index]
                index += 1

    # Read off the plain text
    rail, direction = 0, 1
    result = []
    for i in range(len(cipher)):
        result.append(fence[rail][i])
        rail += direction
        if rail in (0, rails - 1):
            direction *= -1

    return ''.join(result)

if __name__ == "__main__":
    # Test cases
    tests = [
        ("attack at once", 2),
        ("GeeksforGeeks", 3),
        ("defend the east wall", 3)
    ]
    
    for text, rails in tests:
        encrypted = encrypt(text, rails)
        decrypted = decrypt(encrypted, rails)
        print(f"Original: {text}")
        print(f"Encrypted: {encrypted}")
        print(f"Decrypted: {decrypted}\n")
