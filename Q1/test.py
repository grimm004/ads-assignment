def hash_quadratic(items):
    hashed = ['-' for _ in range(19)]
    return hashed


def hash_double(keys):
    hash_table = ['-' for _ in range(19)]

    for key in keys:
        key_hash = compute_hash(key)
        if hash_table[key_hash] == '-':
            hash_table[key_hash] = key
        else:
            second_hash = 11 - (key_hash % 11)
            j = 1
            while True:
                # Calculate the next position by adding the
                # multiple of the iteration count multiplier and
                # the second hash value to the initial key hash
                # and getting the remainder when divided by the
                # length of the hash table.
                next_position = (key_hash + (j * second_hash)) % len(hash_table)
                # If the bucket at the calculated position is empty,
                # place the key in it and exit the loop
                if hash_table[next_position] == '-':
                    hash_table[next_position] = key
                    break
                # Increment the second hash probe multiplier
                j += 1
                # All possible second hash buckets are full,
                # exit the loop without adding the key.
                if j > len(hash_table) - 1: break
    
    return hash_table


def compute_hash(k):
    return ((6 * k) + 3) % 19


def compute_double_hash(k):
    return 

if __name__ == '__main__':
    print(hash_double([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]))

    

def hash_double(items):
    hashed = ['-' for _ in range(19)]

    for item in items:
        hash_ = compute_hash(item)
        if hashed[hash_] == '-':
            hashed[hash_] = item
        else:
            rehash_index = 1
            while True:
                rehash = (hash_ + (rehash_index * compute_double_hash(item))) % 19
                if hashed[rehash] == '-':
                    hashed[rehash] = item
                    break
                rehash_index += 1
                if rehash_index > 18: break

    return hashed
