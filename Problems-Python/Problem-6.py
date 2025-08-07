'''
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

Example 1:
Input: head = [1,1,2]
Output: [1,2]

Example 2:
Input: head = [1,1,2,3,3]
Output: [1,2,3]
'''
def deleteDuplicates(head):
    store_old_value = {}
    for num in head:
        if num not in store_old_value:
            store_old_value[num] = num
    result = list(store_old_value.keys())
    result.sort()
    return result
print(deleteDuplicates([1,1,2]))