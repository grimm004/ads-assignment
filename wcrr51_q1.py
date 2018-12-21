def hash_quadratic(items):
    hashed = ['-' for _ in range(19)]

    for item in items:
        hash_ = compute_hash(item)
        if hashed[hash_] == '-':
            hashed[hash_] = item
        else:
            rehash_index = 1
            while True:
                rehash = (hash_ + (rehash_index * rehash_index)) % 19
                if hashed[rehash] == '-':
                    hashed[rehash] = item
                    break
                rehash_index += 1
                if rehash_index > 18: break
    
    return hashed


def hash_double(items):
    hashed = ['-' for _ in range(19)]

    for item in items:
        hash_ = compute_hash(item)
        if hashed[hash_] == '-':
            hashed[hash_] = item
        else:
            rehash_index = 1
            while True:
                rehash = (hash_ + (rehash_index * (11 - (item % 11)))) % 19
                if hashed[rehash] == '-':
                    hashed[rehash] = item
                    break
                rehash_index += 1
                if rehash_index > 18: break

    return hashed


def compute_hash(k):
    return ((6 * k) + 3) % 19


def compute_quadratic_hash(k):
    return k * k

if __name__ == '__main__':
    pass
