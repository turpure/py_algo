#! usr/bin/env/python
# coding:utf8
# author:turpure

from pythonds.graphs import Graph


class DFSGraph(Graph, object):

    def __init__(self):
        super(DFSGraph, self).__init__()
        self.time = 0

    def dfs(self):
        for aVertex in self:
            aVertex.setColor('white')
            aVertex.setPred(-1)
        for aVertex in self:
            if aVertex.getColor() == 'white':
                self.dfs_visit(aVertex)

    def dfs_visit(self, startVertex):
        startVertex.setColor('gray')
        self.time += 1
        startVertex.setDiscovery(self.time)
        for nextVertex in startVertex.getConnections():
            if nextVertex.getColor() == 'white':
                nextVertex.setPred(startVertex)
                self.dfs_visit(nextVertex)
        startVertex.setColor('black')
        self.time += 1
        startVertex.setFinish(self.time)


def draw_graph():
    g = DFSGraph()
    for i in range(6):
        g.addVertex(i)
    g.addEdge(0, 1, 5)
    g.addEdge(0, 3, 6)
    g.addEdge(1, 4, 8)
    g.addEdge(2, 5, 1)
    g.addEdge(3, 1, 3)
    g.addEdge(4, 2, 7)
    g.addEdge(5, 3, 6)
    g.dfs()


if __name__ == "__main__":
    draw_graph()
