def push(heap, data):
    cur = len(heap)
    heap.append(data)
    siftDown(heap, 0, cur)


def siftDown(heap, zero, end):
    while end > zero:
        parent = (end - 1) // 2
        if heap[parent] <= heap[end]:
            break
        heap[end], heap[parent] = heap[parent], heap[end]
        end = parent

def pop(heap):
    ret = heap[0]
    last = heap.pop()
    size = len(heap)


    if size == 0:
        return ret
    heap[0] = last
    cur = 0
    while True:
        ch1 = 2 * cur + 1
        if ch1 >= size:
            return ret
        ch2 = ch1 + 1
        child = ch2 if ch2 < size and heap[ch2] < heap[ch1] else ch1
        if heap[cur] <= heap[child]:
            return ret
        heap[child], heap[cur] = heap[cur], heap[child]
        cur = child
        pass
    pass