def process_text(text, fill_char='x'):
    """Process input text by removing spaces, converting to lowercase, and handling duplicates"""
    if not text:
        return ""
    # Clean the input text
    text = text.lower().replace(" ", "").replace("j", "i")
    if not text.isalpha():
        raise ValueError("Text must contain only letters")
    # Handle repeated letters and odd length
    processed = []
    i = 0
    while i < len(text):
        if i + 1 >= len(text):
            processed.extend([text[i], fill_char])
            break
        elif text[i] == text[i + 1]:
            processed.extend([text[i], fill_char])
            i += 1
        else:
            processed.extend([text[i], text[i + 1]])
            i += 2
    return ''.join(processed)
def create_matrix(key):
    """Create 5x5 Playfair matrix from key"""
    if not key or not key.strip():
        raise ValueError("Key cannot be empty")
    # Clean and validate the key
    key = key.lower().replace(" ", "").replace("j", "i")
    if not key.isalpha():
        raise ValueError("Key must contain only letters")
    # Create matrix content
    alphabet = 'abcdefghiklmnopqrstuvwxyz'
    key_chars = []
    matrix = []
    # Add key characters (without duplicates)
    for char in key:
        if char not in key_chars and char in alphabet:
            key_chars.append(char)
    
    # Add remaining alphabet characters
    for char in alphabet:
        if char not in key_chars:
            key_chars.append(char)
    
    # Create 5x5 matrix
    for i in range(0, 25, 5):
        matrix.append(key_chars[i:i + 5])
    
    return matrix
def find_positions(matrix, a, b):
    """Find positions of two characters in matrix"""
    positions = []
    
    for char in (a, b):
        for i, row in enumerate(matrix):
            if char in row:
                j = row.index(char)
                positions.append((i, j))
                break
    
    return positions[0], positions[1]
def encrypt(text, key):
    """Encrypt text using Playfair cipher"""
    try:
        # Process input and create matrix
        text = process_text(text)
        matrix = create_matrix(key)
        result = []
        
        # Encrypt pairs
        for i in range(0, len(text), 2):
            p1, p2 = find_positions(matrix, text[i], text[i + 1])
            
            if p1[0] == p2[0]:  # Same row
                result.append(matrix[p1[0]][(p1[1] + 1) % 5])
                result.append(matrix[p2[0]][(p2[1] + 1) % 5])
            elif p1[1] == p2[1]:  # Same column
                result.append(matrix[(p1[0] + 1) % 5][p1[1]])
                result.append(matrix[(p2[0] + 1) % 5][p2[1]])
            else:  # Rectangle rule
                result.append(matrix[p1[0]][p2[1]])
                result.append(matrix[p2[0]][p1[1]])
        
        return ''.join(result)
    
    except Exception as e:
        return f"Encryption error: {str(e)}"
def decrypt(text, key):
    """Decrypt text using Playfair cipher"""
    try:
        # Validate input
        if len(text) % 2 != 0:
            raise ValueError("Ciphertext length must be even")
        matrix = create_matrix(key)
        result = []
        # Decrypt pairs
        for i in range(0, len(text), 2):
            p1, p2 = find_positions(matrix, text[i], text[i + 1])
            
            if p1[0] == p2[0]:  # Same row
                result.append(matrix[p1[0]][(p1[1] - 1) % 5])
                result.append(matrix[p2[0]][(p2[1] - 1) % 5])
            elif p1[1] == p2[1]:  # Same column
                result.append(matrix[(p1[0] - 1) % 5][p1[1]])
                result.append(matrix[(p2[0] - 1) % 5][p2[1]])
            else:  # Rectangle rule
                result.append(matrix[p1[0]][p2[1]])
                result.append(matrix[p2[0]][p1[1]])
        return ''.join(result)
    except Exception as e:
        return f"Decryption error: {str(e)}"
def main():
    try:
        print("\nPlayfair Cipher Encoder/Decoder")
        print("-" * 30)
        
        plaintext = input("Enter plaintext: ").strip()
        if not plaintext:
            raise ValueError("Plaintext cannot be empty")
            
        key = input("Enter key: ").strip()
        if not key:
            raise ValueError("Key cannot be empty")
        
        encrypted = encrypt(plaintext, key)
        print(f"\nEncrypted: {encrypted}")
        
        decrypted = decrypt(encrypted, key)
        print(f"Decrypted: {decrypted}")
    except Exception as e:
        print(f"Error: {str(e)}")
if __name__ == "__main__":
    main()