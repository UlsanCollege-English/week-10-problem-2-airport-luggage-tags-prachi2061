EMPTY = object()
DELETED = object()

def make_table_open(m):
    return [EMPTY] * m

def _hash(key, m):
    return sum(ord(c) for c in key) % m

def _find_slot_for_insert(t, key):
    m = len(t)
    index = _hash(key, m)
    first_deleted = None
    for _ in range(m):
        if t[index] is EMPTY:
            return first_deleted if first_deleted is not None else index
        if t[index] is DELETED:
            if first_deleted is None:
                first_deleted = index
        elif t[index][0] == key:
            return index
        index = (index + 1) % m
    return first_deleted

def _find_slot_for_search(t, key):
    m = len(t)
    index = _hash(key, m)
    for _ in range(m):
        if t[index] is EMPTY:
            return None
        if t[index] is not DELETED and t[index][0] == key:
            return index
        index = (index + 1) % m
    return None

def put_open(t, key, value):
    idx = _find_slot_for_insert(t, key)
    if idx is None:
        return False
    t[idx] = (key, value)
    return True

def get_open(t, key):
    idx = _find_slot_for_search(t, key)
    return t[idx][1] if idx is not None else None

def delete_open(t, key):
    idx = _find_slot_for_search(t, key)
    if idx is None:
        return False
    t[idx] = DELETED
    return True

if __name__ == "__main__":
    t = make_table_open(5)
    put_open(t, "A", "1")
    put_open(t, "B", "2")
    print(get_open(t, "A"))
    delete_open(t, "A")
    print(get_open(t, "A"))