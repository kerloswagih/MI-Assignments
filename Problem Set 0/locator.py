from typing import Any, Set, Tuple
from grid import Grid
import utils

def locate(grid: Grid, item: Any) -> Set[Tuple[int,int]]:
    '''
    I scan every cell in the grid and compare its value to the target item
    the grid class stores values using coordinates in the form (x, y) 
    so I iterate over all valid x and y positions 
    whenever a cell matches the item i add that coordinate to a set
    which automatically removes duplicates 

    '''
    matches: Set[Tuple[int, int]] = set()

    for y in range(grid.height):
        for x in range(grid.width):
            if grid[x, y] == item:
                matches.add((x, y))

    return matches