# Locked-Boxes Problem

My first solution solves the problem using a depth first solution approach.

```python
"""
0-lockboxes.py
"""

def visit_box(box_id, visited_boxes, boxes):
  ...
  pass


def canUnlockAll(boxes):
    """
    function to solve the lockboxes problem.
    """
    n = len(boxes)
    visited_boxes = [False] * n
    visit_box(0, visited_boxes, boxes)
    """the all function returns true if all its values are true"""
    return all(visited_boxes)
```

This is a decent solution, except it fails for large data. It solves the problem using a recursive approach. for large data, there's a chance of hitting the maximum recursion depth (in python).

## The problem

Given `n` number of lockboxes. Each box may contain keys to other boxes and each box is numbered sequentially from `0` to `n-1`. The task is to determine if all the boxes can be opened.

For example:

```
boxes = [[2], [0], [1, 2]]
```

<span style="color: green; padding-left: 6px; border-left: 2px solid grey; font-size: 16px;" id="note">**`Note`: The first box of the boxes provided is always open. `boxes[0]` and a key with the same number as a box opens that box**</span>

here are the lockboxes provided:

```
L0 -> [2]
L1 -> [0]
L2 -> [1, 2]
```

- `L0` contains 2, which is the key to **`boxes[2]`**
- `L1` contains 0, which is the key to **`boxes[0]`**
- `L2` contains 1, 2, which are the keys to **`boxes[1]`** and **`boxes[2]`** respectively.

## How to determine if the boxes can be opened:

To determine if the boxes can be opened, we need to keep record of all opened boxes. to do this. the record will be stored in **`visited_boxes`**. At its initial state, all the boxes are considered unvisited.

```py
n = len(boxes) # number of boxes provided
visited_boxes = [False] * n # initial state of all boxes.
```

For instance, we have a collection of lock boxes. Each box can either be empty or contain one or more keys. Each key found in a box refers to the index of another box in that collection. However, there's a possibility that the key found in a box refers to another box that's not part of the current collection. for example, we have three boxes, one of the boxes may contain a key that refers to a seventh boxes, which is not among the initial three boxes.

The first box `boxes[0]`, is always opened by instruction. The search begins from there. We take the key(s) in the first box, update the `visited_boxes` and use the key as reference to another box in `boxes`. However, we want to avoid exploring the same box again.

```python
def visit_box(box_id, visited_boxes, boxes):
  visited_boxes[box_id] = True
  ...
```

After checking the box as visited, we'll use the keys in box to explore other boxes.

```python
def visit_box(box_id, visited_boxes, boxes):
  visited_boxes[box_id] = True
  box = boxes[box_id]
  for key in box:
    if key < len(boxes) and visited_boxes[key] is False:
      visit_box(key, visited_boxes, boxes)
    continue
```

To use the key from a box, certain conditions are required. the key of the box must be less than the number of boxes in the collection, and the box in reference must be unexplored. We can pay a visit to an explored box as the keys provided is already use to visit other boxes. This is to prevent circular exploration of the collection. If this criteria are met, we can visit other boxes referenced by the keys in the latest visited box.

Remember the `visited_boxes` keeps record of all visited box throughout the journey and a visited box is an opened box because there was a key provided to open it. Any visited box is check this way `visited_boxes[box_id] = True`. So, by the end of the exploration we just need to check if the whole boxes are marked as visited.

```python
def canUnlockAll(boxes):
  n = len(boxes)
  # record of all boxes, initially marked as unvisited
  visited_boxes = [False] * n
  # start the exploration starting from the first box
  visit_box(0, visited_boxes, boxes)

  return all(visited_boxes)
```

`all` is a python function that checks if the `bool(x)` of all values `x` in the provided iterable is `True`. The function `canUnlockAll` returns `True` if the whole boxes are visited.

Now, that's how to solve the locked-boxes problem recursively. However, be warned that you'll get an error if you're running this solution on a large data, this is due to the [RecursionError](https://chat.openai.com/share/1e2766d1-9324-439f-bb5a-3a429714bb16) in python `:(`.

Another solution is to go through the boxes and keep record of all the keys you've seen in the collection of boxes. If the key matches the current box then don't add the key to the collection.

After the whole iteration, you must make sure the record you kept does not contain duplicates. This can be done by converting the records to a set, which will scrape out any duplicates in the record or by checking for duplicates before adding a key to the record. After this, the number of keys in the record you've kept must match the number of boxes provided.

Since the key is a reference to a box. Each key in the record represents a box that can be opened, which is the box in reference to the key. When the number of keys in the record is equal to the number of boxes provided (remember duplicates have been scraped-out), then it means the whole boxes can be unlocked. This solves the problem without an error, unlike the recursive solution.

Here's the iterable-solution.

```python
def canUnlockAll(boxes):
  unlocked_boxes = [0] # remember the first box is unlocked
  for box_id, box in enumerate(boxes):
    for key in box:
      if key != box_id and key < len(boxes):
        unlocked_boxes.append(key)
      continue
  # remove duplicates
  unlocked_boxes = set(unlocked_boxes)
  return len(unlocked_boxes) == len(boxes)
```

By [@coderoyalty](https://twitter.com/coderoyalty)
