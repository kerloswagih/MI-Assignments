import utils

def subsequence_search(subsequence: str, string: str) -> int:
    '''
    I count all ways to choose three positions x < y < z such that the characters at
    those positions match the required subsequence order
    instead of checking every three-letter subsequence
    iwatched  how many times the first required letter has
    appeared and how many times the third required letter appears in the
    remaining suffix
    when the current character matches the middle letter
     the number of valid subsequences ending here is -> previous_first_count * remaining_third_count
    this counts each valid subsequence exactly once and works efficiently for long strings.
    '''
    if len(subsequence) != 3:
        return 0

    first, middle, last = subsequence[0], subsequence[1], subsequence[2]
    suffix_last = [0] * (len(string) + 1)

    for i in range(len(string) - 1, -1, -1):
        suffix_last[i] = suffix_last[i + 1] + (1 if string[i] == last else 0)

    previous_first = 0
    total = 0

    for i, ch in enumerate(string):
        if ch == middle:
            total += previous_first * suffix_last[i + 1]
        if ch == first:
            previous_first += 1

    return total
    