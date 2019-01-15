def count_ephemeral(n1, n2, k):
    # Define sets to store known ephemerals and eternals
    ephemerals = set()
    eternals = set()
    # Define a counter for the number of ephemerals
    ephemeral_count = 0
    # Loop through each number n between n1 and n2
    for n in range(n1, n2):
        # If n is k-ephemeral, increment the counter by `
        if is_ephemeral(n, k, ephemerals, eternals):
            ephemeral_count += 1
    # Return the ephemeral count
    return ephemeral_count


def is_ephemeral(n, k, ephemerals, eternals):
    # Define a set to store the k-children of n
    children = set()

    # While true...
    while True:
        # If current n is 1 or it is already in the ephemeral set
        if n == 1 or n in ephemerals:
            # Loop through each k-child and add it to the ephemerals set
            for child in children:
                ephemerals.add(child)
            # Return true (n is ephemeral)
            return True
        # If current n is already in the children or eternals set
        if n in children or n in eternals:
            # Loop through each k-child and add it to the eternals set
            for child in children:
                eternals.add(child)
            # Return false (n is eternal / not ephemeral)
            return False

        # If current n is neither known to be eternal or ephemeral,
        # add n to the child set
        children.add(n)
        # Calculate, retreive and set the next value of n
        n = next_child(n, k)


def next_child(n, k):
    # Initialise a totoal counter to zero
    total = 0
    # While n is greater than zero
    while n > 0:
        # Add the current digit of n raised to the power of k to the total
        total += (n % 10) ** k
        # Integer divide n by 10 to access the next digit on the next iteration
        n //= 10
    # Return the next k-child
    return total
