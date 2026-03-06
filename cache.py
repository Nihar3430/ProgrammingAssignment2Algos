import sys

def read_input(filename):
    file = open(filename, "r")
    data = file.read().split()
    file.close()
    k = int(data[0])
    m = int(data[1])
    requests = []
    for i in range(2, len(data)):
        requests.append(int(data[i]))

    return k, m, requests


def fifo_misses(k, requests):
    cache = []
    misses = 0
    for i in requests:
        if i in cache:
            continue

        misses += 1
        if len(cache) < k:
            cache.append(i)
        else:
            cache.pop(0)
            cache.append(i)
    return misses

def lru_misses(k, requests):
    cache = []
    misses = 0

    for item in requests:
        if item in cache:
            cache.remove(item)
            cache.append(item)
        else:
            misses += 1

            if len(cache) < k:
                cache.append(item)
            else:
                cache.pop(0)
                cache.append(item)

    return misses

def optff_misses(k, requests):
    cache = []
    misses = 0

    for i in range(len(requests)):
        item = requests[i]

        if item in cache:
            continue

        misses += 1

        if len(cache) < k:
            cache.append(item)
        else:
            remove_index = 0
            farthest_next_use = -1

            for j in range(len(cache)):
                current_cache_item = cache[j]
                next_use_position = -1

                for p in range(i + 1, len(requests)):
                    if requests[p] == current_cache_item:
                        next_use_position = p
                        break

                if next_use_position == -1:
                    remove_index = j
                    break

                if next_use_position > farthest_next_use:
                    farthest_next_use = next_use_position
                    remove_index = j

            cache.pop(remove_index)
            cache.append(item)

    return misses



def main():
    if len(sys.argv) != 2:
        return

    filename = sys.argv[1]
    k, m, requests = read_input(filename)

    fifo_miss_return = fifo_misses(k, requests)
    lru_miss_return = lru_misses(k, requests)
    optff_miss_return = optff_misses(k, requests)

    print("FIFO  :", fifo_miss_return)
    print("LRU   :", lru_miss_return)
    print("OPTFF :", optff_miss_return)


if __name__ == "__main__":
    main()