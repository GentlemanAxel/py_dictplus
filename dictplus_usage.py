from dictplus import DictPlus

# Here is some dictionaries to work with.
d1 = DictPlus({"a": 1, "b": [1, 2], "c": {"d": 4}})
d2 = {"a": 2, "b": [3, 4], "c": {"e": 5}}

# Fusion: merge dictionaries with addition for numbers and concatenation for lists
fusion_result = d1.fusion(d2)
print("Fusion:", fusion_result)  # Expected: {"a": 3, "b": [1, 2, 3, 4], "c": {"d": 4, "e": 5}}


# Filter: filter dictionary by a condition
def filter_condition(value):
    return isinstance(value, list)


filter_result = d1.filter_by(filter_condition)
print("Filter list:", filter_result)  # Expected: {"b": [1, 2]}


def filter_condition_two(value):
    return isinstance(value, int)


filter_result = d1.filter_by(filter_condition_two)
print("Filter int:", filter_result)  # Expected: {'a': 1}


def filter_condition_three(value):
    return isinstance(value, dict)


filter_result = d1.filter_by(filter_condition_three)
print("Filter dict:", filter_result)  # Expected: {'c': {'d': 4}}

# You can create others filter types.


# Map: apply transformation functions to keys and values
def key_mapper(key):
    return key.upper()


def value_mapper(value):
    if isinstance(value, list):
        return list(reversed(value))
    return value


map_result = d1.map(key_mapper, value_mapper)
print("Map:", map_result)  # Expected: {"A": 1, "B": [2, 1], "C": {"d": 4}}

# Nested keys and values
nested_keys = d1.nested_keys()
nested_values = d1.nested_values()
print("Nested keys:", nested_keys)  # Expected: [['a'], ['b'], ['c', 'd']]
print("Nested values:", nested_values)  # Expected: [1, [1, 2], 4]

# Swap keys and values
swap_result = d1.swap_keys_values()
print("Swap:", swap_result)  # Expected: {1: 'a', [1, 2]: 'b', {'d': 4}: 'c'}

# Update values
update_result = d1.update_values({"a": 5, "c": {"Rf": 7}})
print("Update:", update_result)  # Expected: {"a": 5, "b": [1, 2], "c": {"d": 7}}

# Flatten
flatten_result = d1.flatten()
print("Flatten:", flatten_result)  # Expected: {"a": 1, "b": [1, 2], "c_d": 4}


# Recursive
def double(value):
    return value * 2


recursive_result = d1.recursive(double)
print("Recursive:", recursive_result)  # Expected: {'a': 2, 'b': [1, 2, 1, 2], 'c': {'d': 8}}

# Selection
selection_result = d1.selection(["a", "c"])
print("Selection:", selection_result)  # Expected: {"a": 1, "c": {"d": 4}}

# lists_to_tuples
tuples_result = d1.to_tuples()
print("To tuples:", tuples_result)  # Expected: {"a": 1, "b": (1, 2), "c": {"d": 4}}

# tuples_to_lists
lists_result = d1.to_lists()
print("To lists:", lists_result)  # Expected: {"a": 1, "b": [1, 2], "c": {"d": 4}}
