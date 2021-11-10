# [1,1,2,4] -> [1,2,4]

def remove_duplicates(lst):
    """
    Remove duplicates from a list.
    """
    without_duplicates = []
    for element in lst:
        if element not in without_duplicates:
            without_duplicates.append(element)
    return without_duplicates

def remove_duplicates_set(lst):
    """
    Remove duplicates from a list.
    """
    return list(set(lst))


def main():
    random_list = [1,1,2,2,4]
    print(remove_duplicates(random_list))
    print(remove_duplicates_set(random_list))
    
if __name__ == '__main__':
    main()