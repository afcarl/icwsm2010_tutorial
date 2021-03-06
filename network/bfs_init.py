#!/usr/bin/env python
#
# file: bfs_init.py
#
# description: initialize breadth-first search
#
# usage: see run_toygraph
#
# author: jake hofman (gmail: jhofman)
#

import sys
sys.path.append('.')
from hstream import HStream
from collections import defaultdict

class BreadthFirstSearchInit(HStream):

    def mapper_init(self):
        # get source node id from argument (specified as source=node after -[m|r|l] switch) 
        self.source = self.args['source']

    def mapper(self, record):
        if len(record) != 5:
            sys.stderr.write("\t".join(record)+'\n')
            return

        node, in_degree, out_degree, in_neighbors, out_neighbors = record

        # mark distance to source node as 0, other nodes as inf
        if node == self.source:
            distance = 0
        else:
            distance = float('inf')

        self.write_output( (node, distance, out_neighbors) )
                    
if __name__=='__main__':
    BreadthFirstSearchInit()
                        

