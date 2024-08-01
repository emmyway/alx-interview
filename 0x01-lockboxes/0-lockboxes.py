#!/usr/bin/python3
'''
You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1
and each box may contain keys to the other boxes.
'''


def canUnlockAll(boxes):
    '''
    method determines if all the boxes can be opened.
    '''
    from collections import deque

    # Initialize the queue with the first box (box 0)
    # and the set of opened boxes
    queue = deque([0])
    opened_boxes = set([0])

    while queue:
        current_box = queue.popleft()

        # Iterate through all the keys in the current box
        for key in boxes[current_box]:
            if key < len(boxes) and key not in opened_boxes:
                opened_boxes.add(key)
                queue.append(key)

    # Check if all boxes are opened
    return len(opened_boxes) == len(boxes)
