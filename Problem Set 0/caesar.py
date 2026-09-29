from typing import Tuple, List
import utils

'''
    The DecipherResult is the type defintion for a tuple containing:
    - The deciphered text (string).
    - The shift of the cipher (non-negative integer).
        Assume that the shift is always to the right (in the direction from 'a' to 'b' to 'c' and so on).
        So if you return 1, that means that the text was ciphered by shifting it 1 to the right, and that you deciphered the text by shifting it 1 to the left.
    - The number of words in the deciphered text that are not in the dictionary (non-negative integer).
'''
DechiperResult = Tuple[str, int, int]

def caesar_dechiper(ciphered: str, dictionary: List[str]) -> DechiperResult:
    '''

    the cipher shifts each lowercase letter forward by a fixed amount  to decode it,
    i try every possible shift from 0 to 25 and reverse the shift for each candidate text
    a correct original english sentence should contain the fewest unknown words
    so I count how many words in each candidate are missing from the provided dictionary 
    the candidate with the smallest number of missing words is selected
    and its shift is returned with the final deciphered text

    '''
    valid_words = set(dictionary)
    best_text = ciphered
    best_shift = 0
    best_wrong = len(ciphered.split())

    for shifts in range(26):
        decoded_chars = []
        for ch in ciphered:
            if ch == ' ':
                decoded_chars.append(' ')
            else:
                shifted = ord(ch) - ord('a')
                original = (shifted - shifts) % 26
                decoded_chars.append(chr(ord('a') + original))

        decoded_text = ''.join(decoded_chars)
        words = decoded_text.split(' ')
        wrong = sum(1 for word in words if word and word not in valid_words)

        if wrong < best_wrong:
            best_text = decoded_text
            best_shift = shifts
            best_wrong = wrong

    return (best_text, best_shift, best_wrong)


caesar_decipher = caesar_dechiper