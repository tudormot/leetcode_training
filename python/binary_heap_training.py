from typing import Optional

from binarytree import heap, Node, build

#unsafe funs, might give indexes out of the heap array.
# put the checks in a place where it is more efficient
def get_parent_i(i):
    return (i-1)//2
def get_right_child_i(i):
    return 2*i + 1

def get_left_child_i(i):
    return 2*i + 2

def heapify_up(heap, new_elem_index):
    if new_elem_index == 0:
        return
    parent_i = get_parent_i(new_elem_index)
    temp = heap[new_elem_index]
    temp1 = heap[parent_i]
    if temp > temp1:
        heap[new_elem_index] = temp1
        heap[parent_i] = temp
        heapify_up(heap,parent_i)
    else:
        return

def heapify_down(heap, start_i, heap_end_i):
    if start_i is None:
        return
    start_v = heap[start_i]
    rc_i = get_right_child_i(start_i)
    lc_i = get_left_child_i(start_i)
    if lc_i >= heap_end_i:
        return
    elif rc_i >= heap_end_i:
        lc_v = heap[rc_i]
        if start_v < lc_v:
            heap[start_i] = lc_v
            heap[lc_i] = start_v
        return
    else:
        rc_v = heap[rc_i]
        lc_v = heap[rc_i]
        if rc_v > lc_v:
            maxc_v = rc_v
            maxc_i = rc_i
        else:
            maxc_v = lc_v
            maxc_i = lc_i
        heap[start_i] = maxc_v
        heap[maxc_i] = start_v
        heapify_down(heap,maxc_i,heap_end_i)
        return

def insert(heap, value):
    heap.append(value)
    heapify_up(heap,len(heap)-1)


def extract_max(heap)->int:
    result = heap[0]
    last = heap.pop(-1)
    heap[0] = last
    heapify_down(heap,0,len(heap))
    return result


if __name__ == "__main__":
    my_heap = heap(height=4, is_perfect=False, is_max=True)
    heap_array = my_heap.values2
    print(my_heap)
    insert_v = 40
    print(f"Inserting value = {insert_v}")
    insert(heap_array,insert_v)
    print(build(heap_array))
    print(f"Extracting max. max = {extract_max(heap_array)}")
    print("After extraction:")
    print(build(heap_array))
