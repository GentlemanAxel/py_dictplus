# py_dictplus

![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

A simple yet useful python library for dictionaries.
## This project is amenable to enhancement -  Feel free to contribute to the project
---

## Overview

The dictplus.py module introduces a custom class called DictPlus, which extends the functionality of the built-in Python dictionary (dict). This extension includes additional methods for performing various operations on dictionaries, such as fusion, filtering, mapping, handling nested keys and values, swapping keys and values, updating values, flattening, recursion, selection, and conversion between tuples and lists.

---

## List of Features

- Method: fusion <br/>
Description: Merges two dictionaries, performing addition for numeric values and concatenation for lists.
Filtering:

- Method: filter_by <br/>
Description: Filters dictionary items based on a specified condition function.
Mapping:

- Method: map <br/>
Description: Applies transformation functions to keys and values.
Nested Keys and Values:

- Methods: nested_keys, nested_values <br/>
Description: Extracts nested keys and values from a dictionary.
Swap Keys and Values:

- Method: swap_keys_values <br/>
Description: Swaps keys and values, recursively applying the operation.
Update Values:

- Method: update_values <br/>
Description: Updates values in the dictionary based on a provided key-value mapping.
Flattening:

- Method: flatten <br/>
Description: Flattens a nested dictionary, joining keys with a specified separator.
Recursion:

- Method: recursive <br/>
Description: Applies a function recursively to all values in the dictionary.

- Method: selection <br/>
Description: Selects specific keys from the dictionary.

- Methods: to_tuples, to_lists <br/>
Description: Converts the dictionary and its nested structures to tuples or lists.

---

## Usage

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/GentlemanAxel/py_dictplus.git
    ```

2. Navigate to the project directory:

    ```bash
    cd py_dictplus
    ```
    
### Import the module in your python application :

```bash
from dictplus import DictPlus
```


---


### Example Usage
You can explore dictplus_usage.py on the github page !

### Credits

<a href='https://github.com/GentlemanAxel' target="_blank"><img alt='GitHub' src='https://img.shields.io/badge/GentlemanAxel-100000?style=for-the-badge&logo=GitHub&logoColor=white&labelColor=black&color=CA2C2C'/></a>

