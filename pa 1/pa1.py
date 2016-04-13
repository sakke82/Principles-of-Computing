"""
Merge function for 2048 game.
"""

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    
    newline = []
    count = 0
    merged = False
    
    for cell in line:
        if cell == 0:
            count += 1
        else:
            if len(newline) > 0:
                if cell == newline[-1] and not merged:
                    newline.pop()
                    newline.append(2*cell)
                    count += 1
                    merged = True
                    continue
            newline.append(cell)
            merged = False
    
    
    newline = newline + [0] * count
    
    return newline

print merge([2,2,0,2,2])