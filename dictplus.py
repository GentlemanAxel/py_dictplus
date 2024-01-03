def hashable(obj):
    try:
        hash(obj)
    except TypeError:
        return False
    return True


class DictPlus(dict):
    def __getitem__(self, key):
        return super().__getitem__(key)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return dict.__eq__(self, other)
        return False

    def __hash__(self):
        return hash(tuple(sorted(self.items())))

    def fusion(self, other):
        if not isinstance(other, dict):
            raise TypeError("Argument must be a dictionary")

        result = DictPlus(self)
        for key, value in other.items():
            if key in result:
                if isinstance(value, (int, float)):
                    result[key] += value
                elif isinstance(value, (list, tuple)):
                    result[key] = list(result[key]) + list(value)
                elif isinstance(value, dict):
                    result[key] = DictPlus(result[key]).fusion(value)
            else:
                result[key] = value
        return result

    def filter_by(self, condition):
        if not callable(condition):
            raise TypeError("Condition must be a function")

        result = DictPlus()
        for key, value in self.items():
            if condition(value):
                result[key] = value
        return result

    def map(self, key_mapper, value_mapper):
        if not callable(key_mapper) or not callable(value_mapper):
            raise TypeError("Key and value mappers must be functions")

        result = DictPlus()
        for key, value in self.items():
            new_key = key_mapper(key)
            new_value = value_mapper(value)
            result[new_key] = new_value
        return result

    def nested_keys(self):
        nested_keys_list = []

        def _nested_keys(d, prefix=None):
            for key, value in d.items():
                if prefix is not None:
                    new_key = prefix + [key]
                else:
                    new_key = [key]

                if isinstance(value, dict):
                    _nested_keys(value, new_key)
                else:
                    nested_keys_list.append(new_key)

        _nested_keys(self)
        return nested_keys_list

    def nested_values(self):
        nested_values_list = []

        def _nested_values(d):
            for key, value in d.items():
                if isinstance(value, dict):
                    _nested_values(value)
                else:
                    nested_values_list.append(value)

        _nested_values(self)
        return nested_values_list

    def swap_keys_values(self):
        result = DictPlus()
        for key, value in self.items():
            if isinstance(value, dict):
                value = DictPlus(value).swap_keys_values()
            elif isinstance(key, list):
                key = tuple(key)
            elif isinstance(value, list):
                value = tuple(value)
            elif not hashable(value):
                continue  # Skip non-hashable values
            result[value] = key
        return result

    def update_values(self, key_value_pairs):
        if not isinstance(key_value_pairs, dict):
            raise TypeError("Key-value pairs must be a dictionary")

        result = DictPlus(self)
        for key, value in key_value_pairs.items():
            if key in result:
                result[key] = value
        return result

    def flatten(self, separator='_'):
        result = DictPlus()

        def _flatten(d, prefix=''):
            for key, value in d.items():
                new_key = prefix + key if prefix else key
                if isinstance(value, dict):
                    _flatten(value, new_key + separator)
                else:
                    result[new_key] = value

        _flatten(self)
        return result

    def recursive(self, func):
        result = DictPlus()
        for key, value in self.items():
            if isinstance(value, dict):
                result[key] = DictPlus(value).recursive(func)
            else:
                result[key] = func(value)
        return result

    def selection(self, keys):
        if not isinstance(keys, (list, tuple)):
            raise TypeError("Keys must be a list or tuple")

        result = DictPlus()
        for key in keys:
            if key in self:
                result[key] = self[key]
        return result

    def to_tuples(self):
        result = DictPlus()
        for key, value in self.items():
            if isinstance(value, dict):
                result[key] = DictPlus(value).to_tuples()
            elif isinstance(value, list):
                result[key] = tuple(value)
            else:
                result[key] = value
        return result

    def to_lists(self):
        result = DictPlus()
        for key, value in self.items():
            if isinstance(value, dict):
                result[key] = DictPlus(value).to_lists()
            elif isinstance(value, tuple):
                result[key] = list(value)
            else:
                result[key] = value
        return result
