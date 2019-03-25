#! usr/bin/env/python
# coding:utf8
# author:turpure


from pythonds.graphs import PriorityQueue, Graph, Vertex


def dijkstra(aGraph,start):
    pq = PriorityQueue()
    start.setDistance(0)
    pq.buildHeap([(v.getDistance(),v) for v in aGraph])
    while not pq.isEmpty():
        currentVert = pq.delMin()
        for nextVert in currentVert.getConnections():
            newDist = currentVert.getDistance() \
                    + currentVert.getWeight(nextVert)
            if newDist < nextVert.getDistance():
                nextVert.setDistance( newDist )
                nextVert.setPred(currentVert)
                pq.decreaseKey(nextVert,newDist)


if __name__ == "__main__":
    g = Graph()
    for v in ['u', 'v', 'w', 'x', 'y', 'z']:
        g.addVertex(v)
