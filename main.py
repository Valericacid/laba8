def kbig(nums, k):

    count = []
    for e in nums:
        if e + 1 > len(count):
            for i in range(e - len(count) +1 ):
                count.append(0)
        count[e] += 1

    d = 1
    l = len(count)
    res = l - 1

    for i in range(k):
        if count[l-d]==0:
            res -= 1
            d += 1
        count[l - d] -= 1

    return res


