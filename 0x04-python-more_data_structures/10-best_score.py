#!/usr/bin/python3
 if a_dictionary is None or a_dictionary == {}:
        return None

    max_value = max(a_dictionary, key=lambda k: a_dictionary[k])
    return max_value
