import pydot
import random
l = ["a","b","c","d","e","f","g","h","i"]

graph = pydot.Dot('my_graph', graph_type='graph', bgcolor='yellow')
count = 1
while True:
    graph.add_edge(pydot.Edge(random.choice(l), random.choice(l), color='blue'))
    count += 1
    if count > 20:
        break
graph.write_png("result.png")

'''
import pydot

graph = pydot.Dot('my_graph', graph_type='graph', bgcolor='yellow')


# Add nodes
my_node = pydot.Node('a', label='Foo')
graph.add_node(my_node)
# Or, without using an intermediate variable:
graph.add_node(pydot.Node('b', shape='circle'))

my_edge = pydot.Edge('a', 'b', color='blue')
graph.add_edge(my_edge)
# Or, without using an intermediate variable:
graph.add_edge(pydot.Edge('b', 'c', color='blue'))
graph.write_png("result.png")

'''