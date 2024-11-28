# Making Change

## Description
This project involves creating a function, `makeChange`, that determines the fewest number of coins required to achieve a given total.

## Requirements
- Allowed editors: vi, vim, emacs
- Python 3.4.3 on Ubuntu 20.04 LTS
- PEP 8 style guide
- All files are executable

## Usage
To use the `makeChange` function:
1. Import the function:
    ```python
    makeChange = __import__('0-making_change').makeChange
    ```
2. Call the function with a list of coin denominations and a target total.

## Example
```python
makeChange([1, 2, 25], 37)  # Returns: 7
makeChange([1256, 54, 48, 16, 102], 1453)  # Returns: -1

