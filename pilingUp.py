from collections import deque

testCases = int(input())

for i in range(1, testCases + 1):
    pyramid = []
    d = deque()
    test1Size = int(input())
    test1Lens = input().split()
    d.extend([int(x) for x in test1Lens])

    # Initialize blockSize after adding elements to pyramid
    blockSize = 0

    while d and d[-1] <= blockSize:
        if d[-1] > d[0]:
            block = d.pop()
        else:
            block = d.popleft()
        pyramid.append(block)

        # Update blockSize after adding a block
        blockSize = sum(pyramid)

    # Check if the loop ended because all blocks were stackable or not
    if not d:
        print('Yes')
    else:
        print('No')

