# Tower of hanoi
def towerOfHanoi(n, source, destination, auxiliary):
    if n == 1:
        print("Move disk 1 from source", source, "to destination", destination)
        return
    towerOfHanoi(n-1, source, auxiliary, destination)
    print("Move disk", n, "from source", source, "to destination", destination)
    towerOfHanoi(n-1, auxiliary, destination, source)


# Driver code
n = 4
towerOfHanoi(n, 'A', 'C', 'B')
