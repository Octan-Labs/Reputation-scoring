# import libraries
import networkx as nx
import pandas as pd
from BatchPageRank import BatchPageRank

# loading graph dataset
data = pd.read_csv("data/transactions_data.csv")

# build graph from input data with nx
graph_au = nx.from_pandas_edgelist(data, source="from", target="to", create_using=nx.DiGraph())

# init parameters for pagerank
batchPageRank = BatchPageRank(graph=graph_au, damping_factor=0.85)

# compute
pagerank_score = batchPageRank.computePageRank()

# print output
print(pagerank_score)