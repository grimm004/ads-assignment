def count_ephemeral(n1, n2, k):
    ephemeral_count = 0
    for n in range(n1, n2):
        if is_ephemeral(n, k):
            ephemeral_count += 1
    return ephemeral_count


def is_ephemeral(n, k):
    children = []
    while n not in children:
        children.append(n)
        n = next_child(n, k)
        if n == 1: return True
    return False


def next_child(n, k):
    total = 0
    while n > 0:
        total += (n % 10) ** k
        n //= 10
    return total
