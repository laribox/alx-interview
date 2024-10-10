def canUnlockAll(boxes):
    """
    Determines if all the boxes can be unlocked.
    
    Args:
        boxes (list of lists): A list where each index represents a box, and the 
                               value at each index is a list of keys found in that box.
    
    Returns:
        bool: True if all boxes can be unlocked, otherwise False.
    
    Rules:
        - You start with the first box (boxes[0]) unlocked.
        - A key to a box is represented by the index of that box.
        - A box can only be opened if you have the corresponding key.
    """
    n = len(boxes)  # Total number of boxes
    unlocked = [False] * n  # To track whether each box is unlocked (initially all locked)
    unlocked[0] = True  # Box 0 is unlocked from the start
    keys = [0]  # Start with the key to box 0
    
    for key in keys:  # Iterate over the list of keys you have
        for new_key in boxes[key]:  # For each key found in the current box
            if new_key < n and not unlocked[new_key]:  # If the new key is for a valid, locked box
                unlocked[new_key] = True  # Unlock that box
                keys.append(new_key)  # Add the new key to the list
    
    # Return True if all boxes have been unlocked, otherwise False
    return all(unlocked)
