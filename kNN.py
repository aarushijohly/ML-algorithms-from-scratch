import numpy as np

def kNN(inX, dataSet, labels, k):
    diffMat = np.tile(inX, (dataSet.shape[0], 1)) - dataSet
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5
    sortedDistIndices = distances.argsort()
    classCount = {}
    for i in range(k):
        labelNumber = labels[sortedDistIndices[i]]
        classCount[labelNumber] = classCount.get(labelNumber, 0) + 1
    classCountAns = sorted(classCount.items(), key=lambda item: item[1], reverse=1)
    return classCountAns[0][0]