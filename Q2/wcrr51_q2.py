def count_ephemeral(n1, n2, k):
    ephemerals = [0 for _ in range(10000001)]
    ephemeral_count = 0
    for n in range(n1, n2):
        if is_ephemeral(n, k, ephemerals):
            ephemeral_count += 1
    return ephemeral_count


def is_ephemeral(n, k, ephemerals):
    children = []
    while n != 1 and n not in children:
        if ephemerals[n] != 0:
            if ephemerals[n] == -1: return False
            elif ephemerals[n] == 1: return True

        children.append(n)
        n = next_child(n, k)

    for child in children:
        ephemerals[child] = 1 if n == 1 else -1
    return n == 1


def next_child(n, k):
    total = 0
    while n > 0:
        total += (n % 10) ** k
        n //= 10
    return total
