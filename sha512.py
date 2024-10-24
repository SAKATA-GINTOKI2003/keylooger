import hashlib

def compute_hashes(input_string):
    algorithms = ['sha256', 'sha384', 'sha224', 'sha512', 'sha1']
    # Iterate through each algorithm, compute the hash, and print the result
    for algo in algorithms:
        hash_result = getattr(hashlib, algo)(input_string.encode()).hexdigest()
        print(f"The hexadecimal equivalent of {algo.upper()} is : {hash_result}\n")

input_string = "Geeks for Geeks"
compute_hashes(input_string)
