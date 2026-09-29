from typing import Any, Dict, List
import utils


def histogram(values: List[Any]) -> Dict[Any, int]:
    '''
    i use a dictionary because dictionary keys can represent each distinct value
    while the stored value for each key is the number of times that item has been
    seen As i iterate through the list i either create a new counter for a value
    or increment the existing one This produces the frequency map required by the
    assignment such as {3: 2, 5: 1} for [3, 5, 3]

    '''
    frequencies: Dict[Any, int] = {}

    for value in values:
        if value in frequencies:
            frequencies[value] += 1
        else:
            frequencies[value] = 1

    return frequencies