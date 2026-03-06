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

