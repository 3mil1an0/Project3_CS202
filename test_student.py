from proj3 import (
    Node, MinHeap,
    heapify_up, insert, extract_min,
    count_frequency, create_priority_queue,
    build_tree_from_queue, generate_codes,
    encode, decode, huffman_encoding
)
 
 
# --- Test heapify_up ---

heap = MinHeap([Node(freq=10, char="z"), Node(freq=1, char="a")])
result = heapify_up(heap, 1)
assert result.data[0].char == "a", "heapify_up failed: smallest should be at the top"
print("PASS: heapify_up")
 
 
# --- Test insert ---------

heap = MinHeap([])
heap = insert(heap, Node(freq=5, char="a"))
assert len(heap.data) == 1, "insert failed: heap should have 1 element"
print("PASS: insert")
 
 
# --- Test extract_min -------------

heap = MinHeap([])
heap = insert(heap, Node(freq=8, char="b"))
heap = insert(heap, Node(freq=2, char="a"))
heap, min_node = extract_min(heap)
assert min_node.char == "a", "extract_min failed: should return the smallest node"
print("PASS: extract_min")
 
 
# --- Test encoding and decoding a normal string ---------

encoded, decoded, codes = huffman_encoding("hello")
assert decoded == "hello", "roundtrip failed for 'hello'"
print("PASS: encode/decode normal string")
 
 
# --- Test a single repeated character ---=

encoded, decoded, codes = huffman_encoding("aaaa")
assert decoded == "aaaa", "roundtrip failed for 'aaaa'"
print("PASS: encode/decode repeated character")
 
 
# --- Test a single character ---=====
encoded, decoded, codes= huffman_encoding("z")
assert decoded == "z", "roundtrip failed for single character"
print("PASS: encode/decode single character")
 
 
print("\nTests Passed")