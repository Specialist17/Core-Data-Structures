#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order."""
    # TODO: Check that all adjacent items are in order, return early if not
    for index, item in enumerate(items):
        if index+1 < len(items):
            if item > items[index+1]:
                return False

    return True

def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order."""
    # TODO: Repeat until all items are in sorted order
    while not is_sorted(items):
        for index, item in enumerate(items):
            if index+1 < len(items):
                if item > items[index+1]:
                    items[index], items[index+1] = items[index+1], items[index]
    # TODO: Swap adjacent items that are out of order



def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order."""
    # TODO: Repeat until all items are in sorted order
    # TODO: Find minimum item in unsorted items
    # TODO: Swap it with first unsorted item

    # Traverse through all array elements
    for i in range(len(items)):
        # Find the minimum element in remaining
        # unsorted array
        min_index = i
        for j in range(i+1, len(items)):
            if items[min_index] > items[j]:
                min_index = j

        # Swap the found minimum element with
        # the first element
        items[i], items[min_index] = items[min_index], items[i]


def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order."""
    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items

    for index in range(1, len(items)):
        current_item = items[index]
        current_position = index - 1


        while current_position >= 0 and items[current_position] > current_item:
            items[current_position + 1] = items[current_position]
            current_position -= 1

        items[current_position + 1] = current_item


def test_sorting(sort=insertion_sort, num_items=20, max_value=50):
    """Test sorting algorithms with a small list of random items."""
    # Create a list of 8 or 16 items in arbitrary order
    # items = [1,2,3,4,5,6,7,8,9,8]

    # items = [3, 5, 4, 2, 6, 8, 1, 7]
    items = [11, 13, 8, 4, 12, 2, 14, 3, 5, 18, 6, 10, 1, 7, 9, 15]
    print(is_sorted(items))
    # Create a list of items randomly sampled from range [1...max_value]
    import random
    items = random.sample(range(1, max_value + 1), num_items)
    # item_range = list(range(1, max_value + 1))
    # items = [random.choice(item_range for _ in range(num_items))]
    print('Initial items: {!r}'.format(items))

    # Change this sort variable to the sorting algorithm you want to test
    # sort = bubble_sort
    print('Sorting items with {}(items)'.format(sort.__name__))
    sort(items)
    print('Sorted items:  {!r}'.format(items))


def main():
    """Read command-line arguments and test sorting algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name

    # Get sort function by name
    if len(args) >= 1:
        sort_name = args[0]
        # Terrible hack abusing globals
        sort = globals()[sort_name]
    else:
        sort = insertion_sort

    # Get num_items and max_value, but don't explode if input is not an integer
    try:
        num_items = int(args[1]) if len(args) >= 2 else 20
        max_value = int(args[2]) if len(args) >= 3 else 50
    except:
        print('Integer required for `num` and `max` command-line arguments')

    # Test sort function, but don't explode if sort function does not exist
    try:
        test_sorting(sort, num_items, max_value)
    except NameError:
        script = sys.argv[0]  # Get script file name
        print('Usage: {} sort num max'.format(script))
        print('Test sorting algorithm `sort` with a list of `num` integers')
        print('\trandomly sampled from the range [1...`max`] (inclusive)')
        print('\nExample: {} bubble_sort 10 20'.format(script))
        print('Initial items: [3, 15, 4, 7, 20, 6, 18, 11, 9, 7]')
        print('Sorting items with ' + str(sort.__name__) + '(items)')
        print('Sorted items:  [3, 4, 6, 7, 7, 9, 11, 15, 18, 20]')


if __name__ == '__main__':
    main()