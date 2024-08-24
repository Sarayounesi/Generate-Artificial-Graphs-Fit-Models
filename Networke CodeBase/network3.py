import networkx as nx
import networkx
import matplotlib.pyplot as plt
import pylab as plt

G = nx.Graph()
G.add_edges_from([('Dr.Rahmani', 'Dr.Khanjari',{'weight': 100}), ('Dr.Rahmani', 'Dr.Ashtiani',{'weight': 200}), ('Dr.Ashtiani', 'Dr.Khanjari',{'weight': 300}), ('Dr.etemadi', 'Dr.Khanjari',{'weight': 300}), ('Dr.Parsa', 'Dr.Mozaieni',{'weight': 100}),
                 ('Dr.Parsa', 'Dr.Jahed',{'weight': 100}), ('Dr.Rahmani', 'Dr.Ashtiani',{'weight': 400}), ('Dr.etemadi', 'Dr.Jahed'  ,{'weight': 100}), ('Dr.movahedi', 'Dr.etemadi',{'weight': 200}), ('Dr.Khanjari', 'Dr.movahedi',{'weight': 100}) ,('Dr.Jahed', 'Dr.Minaii',{'weight': 300}) ,('Dr.Mozaieni', 'Dr,maleki',{'weight': 100}),('Dr.Minaii', 'Dr.Kangavari',{'weight': 100}),('Dr.Mozaieni', 'Dr.Entezari',{'weight': 100}) ,('Dr,maleki', 'Dr.Rashidi',{'weight': 100}),('Dr,maleki', 'Dr.Smali',{'weight': 100}) ,('Dr.Khanjari', 'Dr.Smali',{'weight': 100}) , ('Dr.Khanjari', 'Dr.beitollahi',{'weight': 100}),('Dr.Smali', 'Dr.Kabiri',{'weight': 100})])

plt.figure() 
plt.grid(True)

plt.legend(['In-degree', 'Out-degree'])
plt.xlabel('Degree')
plt.ylabel('Number of nodes')
plt.title('network of places in Cambridge')
plt.xlim([0, 2*10**2])
plt.close()

pos = nx.spring_layout(G)

nx.draw_networkx_nodes(G, pos, node_size=200, node_color='red')
nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color='black')
nx.draw_networkx_labels(G, pos)
plt.show()

ER = nx.erdos_renyi_graph(16, 0.5)
plt.title('ER BEFOR Fit' )
nx.draw(ER, with_labels=True)

plt.show()


WS = nx.watts_strogatz_graph(16, 4, 0.5)
plt.title('WS BEFOR Fit' )
nx.draw(WS, with_labels=True)
plt.show()


NWS = nx.newman_watts_strogatz_graph(16, 4, 0.5)
plt.title('NWS BEFOR Fit' )
nx.draw(NWS, with_labels=True)
plt.show()


CWS = nx.connected_watts_strogatz_graph(16, 4, 0.5, 5)
plt.title('CSW BEFOR Fit' )
nx.draw(CWS, with_labels=True)
plt.show()


BA = nx.barabasi_albert_graph(16, 2)
plt.title('BA BEFOR Fit' )
nx.draw(BA, with_labels=True)
plt.show()


n = len(G.nodes())
m = len(G.edges())
p = 2 * m / (n * (n - 1))
ER = nx.erdos_renyi_graph(n, p)
WS = nx.watts_strogatz_graph(n, 5, 0.65)
BA = nx.barabasi_albert_graph(n, 5)


plt.figure(figsize=(15, 5))
plt.subplot(131)
nx.draw(ER, with_labels=True)
plt.title('ER After Fit' )

plt.subplot(132)
nx.draw(WS, with_labels=True)
plt.title('Watts Strogatz After Fit')

plt.subplot(133)
nx.draw(BA, with_labels=True)
plt.title('Barabási Albert After Fit')

plt.show()


degrees = [degree for node, degree in G.degree()]
degree_hist_1 = nx.degree_histogram(G)


avg_clustering_1 = nx.average_clustering(G)




degrees = [degree for node, degree in BA.degree()]
degree_hist_2 = nx.degree_histogram(BA)


avg_clustering_2 = nx.average_clustering(BA)
degrees = [degree for node, degree in WS.degree()]
degree_hist_3 = nx.degree_histogram(WS)


avg_clustering_3 = nx.average_clustering(WS)




graph_transitivity = nx.transitivity(G)
graph_transitivity = nx.transitivity(ER)
graph_transitivity = nx.transitivity(WS)
graph_transitivity = nx.transitivity(BA)




def plot_degree_dist(G):
    degrees = [G.degree(n) for n in G.nodes()]
    plt.hist(degrees)
    plt.show()


plot_degree_dist(G)


print("--------------------------------------------------------------------------------------------------------------")
print("2.View Of network IUST Professor")
print("--------------------------------------------------------------------------------------------------------------")
print("--------------------------------------------------------------------------------------------------------------")
print("REAL NETWORK")
print("--------------------------------------------------------------------------------------------------------------")
print(G)
print('3.Average degree', sum(dict(G.degree).values()) / len(G.nodes))
print('4.Density of graph', ((len(G.edges) / (len(G.nodes) * (len(G.nodes) - 1)))))
print('5.Clustering coefficient 1', nx.clustering(G))
print('6.Clustering coefficient 2', list(nx.triangles(G, (0, 1)).values()))
print('7.Diametr',  max([max(j.values())
      for (i, j) in nx.shortest_path_length(G)]))
print('8.Avrage shortest path', (nx.average_shortest_path_length(G)))
print('9.Assortativity (Degree Correlation) ',
      nx.degree_assortativity_coefficient(G))
print("--------------------------------------------------------------------------------------------------------------")
print("ARTIFICIAL NETWORK")
print("--------------------------------------------------------------------------------------------------------------")
print(f"Transitivity of the BA graph: {graph_transitivity}")
print(f"Transitivity of the WS:: {graph_transitivity}")
print(f"Transitivity of the ER: {graph_transitivity}")
print(f"Transitivity of the G: {graph_transitivity}")
print("--------------------------------------------------------------------------------------------------------------")
print("--------------------------------------------------------------------------------------------------------------")
print(f'Degree distribution G: {degree_hist_1}')
print(f'Average clustering coefficient G: {avg_clustering_1}')
print(f'Degree distribution BA: {degree_hist_2}')
print(f'Average clustering coefficient BA: {avg_clustering_2}')
print(f'Degree distribution WS: {degree_hist_3}')
print(f'Average clustering coefficient iS: {avg_clustering_3}')
print("--------------------------------------------------------------------------------------------------------------")
print("--------------------------------------------------------------------------------------------------------------")