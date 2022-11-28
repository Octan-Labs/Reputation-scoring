
# import libraries
import networkx as nx


class BatchPageRank(object):
    """ Batch computation for PageRank analysis of graph structure"""
    def __init__(self, graph, damping_factor):
        self.graph = graph
        self.pagerank = dict()
        self.damping_factor = damping_factor

    def computePageRank(self):
        self.pagerank = self.builtPageRank(self.graph, alpha=self.damping_factor, personalization=None, max_iter=10000, tol=1e-06, nstart=None, weight='weight', dangling=None)
        return self.pagerank

    def builtPageRank(self, G, alpha=0.85, personalization=None, max_iter=100, tol=1.0e-6, nstart=None, weight="weight", dangling=None,):
        if len(G) == 0:
            return {}

        if not G.is_directed():
            D = G.to_directed()
        else:
            D = G

        # Create a copy in (right) stochastic form
        W = nx.stochastic_graph(D, weight=weight)
        N = W.number_of_nodes()

        # Choose fixed starting vector if not given
        if nstart is None:
            x = dict.fromkeys(W, 1.0 / N)
        else:
            # Normalized nstart vector
            s = float(sum(nstart.values()))
            x = {k: v / s for k, v in nstart.items()}

        if personalization is None:
            # Assign uniform personalization vector if not given
            p = dict.fromkeys(W, 1.0 / N)
        else:
            s = float(sum(personalization.values()))
            p = {k: v / s for k, v in personalization.items()}

        if dangling is None:
            # Use personalization vector if dangling vector not specified
            dangling_weights = p
        else:
            s = float(sum(dangling.values()))
            dangling_weights = {k: v / s for k, v in dangling.items()}
        dangling_nodes = [n for n in W if W.out_degree(n, weight=weight) == 0.0]

        # power iteration: make up to max_iter iterations
        for _ in range(max_iter):
            xlast = x
            x = dict.fromkeys(xlast.keys(), 0)
            danglesum = alpha * sum(xlast[n] for n in dangling_nodes)
            for n in x:
                # this matrix multiply looks odd because it is
                # doing a left multiply x^T=xlast^T*W
                for nbr in W[n]:
                    x[nbr] += alpha * xlast[n] * W[n][nbr][weight]
                x[n] += danglesum * dangling_weights.get(n, 0) + (1.0 - alpha) * p.get(n, 0)
            # check convergence, l1 norm
            err = sum([abs(x[n] - xlast[n]) for n in x])
            if err < N * tol:
                return x
        raise nx.PowerIterationFailedConvergence(max_iter)