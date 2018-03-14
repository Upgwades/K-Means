"""
Author: Will Irwin
Date: 11/13/2017
Inputs:
    valid file location
    number of clusters
    attributes to ignore
Outputs:
    the centroids of the clusters
    the number of instances in each class
    the total square error
    the number iterations that were used to get this result
Notes:
    Runs in python 2.x
"""
import os
import csv
import random
import numpy as np
import math
import copy

def input():

        f = raw_input("Enter file location: ")

        data, headers = processFile(f)

        nclusters = int(raw_input('Enter the number of desired clusters: '))

        for x in range(0,len(headers)):
            string = str(x) + " ,"
            print(str(x) + " - " + headers[x])

        ignoreString = raw_input('Enter the numbers (comma seperated) of the attributes you would like to ignore: ')
        ignore = [x.strip() for x in ignoreString.split(',')]
        ignore = map(int, ignore)

        return data, headers, nclusters, ignore

def processFile(f):
        with open(f, 'rb') as f:
            reader = csv.reader(f)
            headers = next(reader)
            data = list(reader)
        return data, headers

def kmeans(data, headers, nclusters, ignore):

        isStillMoving = True

        ignore = sorted(ignore, key=int, reverse=True)
        for row in data:
            for x in ignore:
                del row[x]
        data = np.array(data,dtype=np.float32)

        clusterIDs = np.empty(int(len(data)),dtype=np.int)
        clusterIDs = np.random.randint(low=0, high=nclusters, size=len(data))

        centroids = initCentroids(data, nclusters)
        centroids = np.array(centroids,dtype=np.float32)
        centroids = centroids[0]
        iterations = 1
        instances = []

        while(isStillMoving):
            centroids = calcCentroid(centroids,data,nclusters,clusterIDs)
            clusterIDs,isStillMoving = calcClusters(centroids,data,nclusters,clusterIDs)

            iterations += 1

        unique, instances = np.unique(clusterIDs, return_counts=True)
        tse = calcTSE(data,centroids,clusterIDs,unique)

        return instances, centroids, tse, iterations, unique, clusterIDs

def calcTSE(data,centroids,clusterIDs,unique):

    tse = 0.0
    dist = 0.0
    sqError = 0.0

    for x in range(0,len(centroids)):
        for y in range(0,len(clusterIDs)):
            if(clusterIDs[y] == unique[x]):
                dist = calcDistance(data[y],centroids[x])
                sqError += math.pow(dist,2)
        tse += sqError
    return tse

def initCentroids(data,nclusters):

    centroids = []
    centroids.append(random.sample(data, nclusters))

    return centroids

def calcCentroid(centroids,data,nclusters,clusterIDs):
    totals = np.zeros(len(data[0]),dtype=np.float32)
    totalInCluster = 0

    for j in range(0,nclusters):
        for k in range(len(data)):
            if(clusterIDs[k] == j):
                for x in range(0,len(totals)):
                    totals[x] += data[k][x]
                totalInCluster += 1

    if(totalInCluster > 0):
        for x in range(0,len(totals)):
            centroids[j][x] = totals[x] / totalInCluster

    return centroids


def calcClusters(centroids,data,nclusters,clusterIDs):
    isStillMoving = False
    originalClusterIDs = clusterIDs
    for i in range(0,len(clusterIDs)):
        bestMinimum = math.pow(10, 10)
        currentCluster = 0

        for j in range(0,nclusters):
            distance = calcDistance(centroids[j], data[i])

            if(distance < bestMinimum):
                bestMinimum = distance
                currentCluster = j

        if(clusterIDs[i] != currentCluster):
            clusterIDs[i] = currentCluster
            isStillMoving = True

    return clusterIDs,isStillMoving

def calcDistance(array1, array2):
    # Calculate Euclidean distance.
    distance = float(np.linalg.norm(array1-array2))
    return distance

def main():

    data, headers, nclusters, ignore = input()
    originalData = copy.deepcopy(data)
    instances, centroids, tse, iterations, unique, clusterIDs = kmeans(data, headers, nclusters, ignore)


    print("Here is the associated raw data:")
    for x in range(0,len(originalData)):
        print(str(clusterIDs[x]) + " - " + str(originalData[x]))
        print("")

    for x in range(0,nclusters):
        print("For cluster " + str(x) + ":")
        print("It had " + str(instances[x]) + " instances")
        print("and a final centroid at" + str(centroids[x]) + "\n")
    print("The algorithm took " + str(iterations) + " iterations and had a total square error of " + str(tse))





main()
