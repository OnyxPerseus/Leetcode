def solve(chars):
    """
    Compresses an array of characters in-place.

    Args:
        chars: A list of characters.

    Returns:
        The new length of the compressed array. The input array `chars` is modified in-place.
    """
    n = len(chars)
    if n == 0:
        return 0

    write_idx = 0  # Pointer for writing compressed characters
    read_idx = 0   # Pointer for reading original characters

    while read_idx < n:
        current_char = chars[read_idx]
        count = 0
        # Find the count of consecutive identical characters
        while read_idx < n and chars[read_idx] == current_char:
            read_idx += 1
            count += 1

        # Write the character
        chars[write_idx] = current_char
        write_idx += 1

        # Write the count if it's greater than 1
        if count > 1:
            count_str = str(count)
            for digit in count_str:
                chars[write_idx] = digit
                write_idx += 1

    return write_idx

if __name__ == '__main__':
    chars = ['a', 'a', 'b', 'b', 'c', 'c', 'c']
    # print the result of string compression
    print(solve(chars))
