def matrixMultiply(matrixA, matrixB):
    return(
        [[sum(a * b for a, b in zip(aRow, bCol)) 
                            for bCol in zip(*matrixB)]
                                    for aRow in matrixA]
                                    )

def arrayToVector(array):
    return([[element] for element in array])

def vectorToArray(vector):
    return([value for sublist in vector for value in sublist])

def addToElements(array, values):
    return [[sublist[i] + values[i] for i in range(len(values))] for sublist in array]