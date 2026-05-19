from __future__ import annotations
from dataclasses import dataclass, field

@dataclass(order=True, frozen=True)
class Node:
    freq: int
    char: str
    left: Node | None = None
    right: Node | None  = None

    def __str__(self):
        return f"Node: {self.char}, Freq: {self.freq}"

@dataclass(frozen=True)
class MinHeap:
    data: list[Node] = field(default_factory=list)



def heapify_up(heap: MinHeap, index: int) -> MinHeap:

    data = list(heap.data)
    parent_index  = (index - 1)//2

    while index > 0:
        pearent_index = (index-1)//2
        #swap the child and parent
        if data[index] < data[parent_index]:

            data[index], data[parent_index] = data[parent_index], data[index]

            index = parent_index
        else:
            break
            
    return MinHeap(data)

        


def insert(heap: MinHeap, element: Node) -> MinHeap:

    new_data = list(heap.data) + [element]
    new_heap = MinHeap(new_data)

    return heapify_up(new_heap, len(new_data) - 1)


def heapify_down(heap: MinHeap, index: int) -> MinHeap:
    data = list(heap.data)
    size = len(data)

    while True:
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        smallest = index


        # Is the left child smaller than the current node
        if left_child < size and data[left_child] < data[smallest]:
            smallest = left_child

        # Is the right child even smaller than it
        if right_child < size and data[right_child] < data[smallest]:
            smallest = right_child

        # if child smaller swap and keep going down
        if smallest != index:
            data[index], data[smallest] = data[smallest], data[index]
            index = smallest
        else:
            # Current node is already smaller than both children — done!
            break

    return MinHeap(data)
def extract_min(heap: MinHeap) -> tuple[MinHeap, Node]:
    data = list(heap.data)

    # The smallest element is always root
    min_node = data[0]

    # Special case: if only one element is left
    if len(data) == 1:
        return MinHeap([]), min_node

    # Put the last element at the root and drop the last slot
    new_data = [data[-1]] + data[1:-1]
    new_heap = MinHeap(new_data)

    # push it to its correct positiion
    new_heap = heapify_down(new_heap, 0)

    return new_heap, min_node


        
def count_frequency(s: str)-> dict[str,int]:
    frequency = {}

    for char in s:
        if char in frequency:
           
            frequency[char] = frequency[char] + 1
        else:
         
            frequency[char] = 1

    return frequency

    pass


def create_priority_queue(frequency: dict[str, int]) -> MinHeap:
    heap = MinHeap([])   # empty heap

    for char, freq in frequency.items():
        new_node = Node(freq=freq, char=char)
        heap = insert(heap, new_node)   # Insert returns a brand new heap

    return heap

    pass



def build_tree_from_queue(priority_queue: MinHeap) -> Node:
    
    heap = priority_queue

    while len(heap.data) > 1:
        heap, left  = extract_min(heap)
        heap, right = extract_min(heap)

        combined_freq = left.freq + right.freq
        combined_char = left.char + right.char   # Used as a tiebreaker when comparing

        merged_node = Node(
            freq  = combined_freq,
            char  = combined_char,
            left  = left,
            right = right
        )

        heap = insert(heap, merged_node)

    return heap.data[0]



def generate_codes(node: Node | None, prefix="", code: dict | None =None)-> dict:
    if code is None:
        code = {}  


    if node is None:
        return code  # return

    if node.left is None and node.right is None:
        code[node.char] = prefix if prefix else "0"
        return code

    generate_codes(node.left,  prefix + "0", code)
    generate_codes(node.right, prefix + "1", code)

    return code
    pass


def encode(s: str, codes: dict)-> str:
    pass
    result = ""

    for char in s:
        result = result + codes[char]   # Append the binary code for each character

    return result

def decode(encoded_string: str, root: Node):
    result       = ""
    current_node = root   # Start at the top of the tree

    for bit in encoded_string:
        if current_node.left is None and current_node.right is None:
            result       = result + current_node.char
            current_node = root
            continue

        if bit == "0":
            current_node = current_node.left
        else:
            current_node = current_node.right

        # Did we land on a leaf? (a node with no children is a leaf)
        if current_node.left is None and current_node.right is None:
            result       = result + current_node.char   # Record the character
            current_node = root                          # Restart from the root

    return result
    pass

def huffman_encoding(s:str):
    #Do Not Change this function
    frequency = count_frequency(s)
    pq = create_priority_queue(frequency)
    root = build_tree_from_queue(pq)
    codes = generate_codes(root)
    encoded_string = encode(s, codes)
    decoded_string = decode(encoded_string,root)
    return encoded_string, decoded_string, codes

