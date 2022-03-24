#improved merge sort implementation
#copying overhead removed


def recMergeSort(theSeq, first, last, tmpArray):

    if first == last:
        #single element list if sorted
        return;
    else:
        mid = (first + last) // 2

        recMergeSort(theSeq, first, mid, tmpArray)
        recMergeSort(theSeq, mid + 1, last, tmpArray)

        return mergeVirtualSeq (theSeq, first, mid + 1, last + 1, tmpArray)

def mergeVirtualSeq(theSeq, left, right, end, tmpArray):
    a = left
    b = right

    m = 0

    while a < right and b < end:
        if theSeq[a] < theSeq[b]:
            tmpArray[m] = theSeq[a]
            a += 1

        else:
            tmpArray[m] = theSeq[b]
            b += 1

        m += 1


    while a < right:
        tmpArray[m] = theSeq[a]
        a += 1
        m += 1

    while b < end:
        tmpArray[m] = theSeq[b]
        b +=1
        m += 1

    for i in range (end - left):
        theSeq[i + left] = tmpArray[i]

    return theSeq


def mergeSort(theSeq):
    n = len(theSeq)

    tmpArray = [0] * n

    return recMergeSort(theSeq, 0, n-1, tmpArray)


