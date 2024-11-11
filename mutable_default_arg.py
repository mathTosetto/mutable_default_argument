from typing import List


def add_to_list_mutable_default(item: str, list_items: List[str] = []) -> List[str]:
    list_items.append(item)
    return list_items


print("Mutable Default Argument")
print(add_to_list_mutable_default("banana"))  # ['banana']
print(add_to_list_mutable_default("apple"))  # ['banana', 'apple']
print("-" * 40)


def add_to_list_fixed(item: str, list_items: List[str] = None) -> List[str]:
    if list_items is None:
        list_items = []
    list_items.append(item)
    return list_items


print("Fixed Mutable Default Argument")
print(add_to_list_fixed("banana"))  # ['banana']
print(add_to_list_fixed("apple"))  # ['apple']
print("-" * 40)
