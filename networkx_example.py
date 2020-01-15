import networkx as nx

#instantiate graph
G=nx.Graph()

#add node 1 (note: node names can be integers, floats, or strings).
G.add_node(1)

#this will add node 'spam.'
G.add_node('spam')

#add nodes 2 and 3 (note: This method passes a list)
G.add_nodes_from([2,3])

#add edges to the graph.  Edges are represented as tuples, indicating the nodes they connect.  In this case, node 1 is connected to nodes 2 and 3.
G.add_edges_from([(1,2),(1,3)])

#to view a list of all nodes or all edges:
G.nodes()
G.edges()

#to see which nodes are connected to node 1:
G.neighbors(1)

#you can also add other attributes to edges.  To add the attribute 'color' = 'blue' to edge (1,3):
G[1][3]['color']='blue'

#node attributes can be set similarly.  To set the attribute 'room' = 714 in node 1:
G.node[1]['room'] = 714

#computing centralities

#degree centrality
c = nx.degree_centrality(G)

#eigenvector centrality
d = nx.eigenvector_centrality(G)

#betweenness centrality
e = nx.betweenness_centrality(G)


