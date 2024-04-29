#Erfan zeinadini
#github.com/erph82


import networkx as nx
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class GraphSimulator:
    def __init__(self):
        self.graph = nx.Graph()
        self.root = tk.Tk()
        self.root.title("Graph Simulator")
        self.figure = plt.figure()
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.root)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.ax = self.figure.add_subplot(111)
        self.ax.set_axis_off()
        self.canvas.draw()

    def add_node(self, node):
        if node == '':
            self.show_message("Invalid Node")
        else:
            self.graph.add_node(node)
            self.draw_graph()

    def remove_node(self, node):
        if node in self.graph:
            self.graph.remove_node(node)
            self.draw_graph()
        else:
            self.show_message("Node not found.")

    def draw_graph(self):
        self.ax.clear()
        pos = nx.spring_layout(self.graph)
        nx.draw(self.graph, pos, with_labels=True, ax=self.ax)
        labels = nx.get_edge_attributes(self.graph, 'weight')
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=labels,font_color='r', ax=self.ax)
        self.canvas.draw()

    def show_message(self, message):
        messagebox.showinfo("Message", message)

    def add_remove_node_window(self):
        new_window = tk.Toplevel(self.root)
        new_window.title("add or remove node")
        label = tk.Label(new_window, text="Enter the node:")
        label.pack()

        node_entry = tk.Entry(new_window)
        node_entry.pack()

        add_button = tk.Button(new_window, text="Add node",
                               command=lambda: self.add_node(node_entry.get()))
        add_button.pack()

        remove_button = tk.Button(new_window, text="Remove node",
                                  command=lambda: self.remove_node(node_entry.get()))
        remove_button.pack()
    def remove_edge(self, node1, node2):
        if self.graph.has_edge(node1, node2):
            self.graph.remove_edge(node1, node2)
            self.draw_graph()
        else:
            self.show_message("Edge not found.")

    def add_edge(self, node1, node2, weight):
        try:
            weight = float(weight)
            self.graph.add_edge(node1, node2, weight=weight)
            self.draw_graph()
        except ValueError:
            self.show_message("Invalid weight. Please enter a number.")

    def add_remove_edge_window(self):
        new_window = tk.Toplevel(self.root)
        new_window.title("add or remove adge")
        label_1 = tk.Label(new_window, text="Enter the node 1:")
        label_1.pack()

        node_1_entry = tk.Entry(new_window)
        node_1_entry.pack()

        label_2 = tk.Label(new_window, text="Enter the node 2:")
        label_2.pack()

        node_2_entry = tk.Entry(new_window)
        node_2_entry.pack()

        label_3 = tk.Label(new_window, text="edge weight:")
        label_3.pack()

        edge_weight_entry = tk.Entry(new_window)
        edge_weight_entry.pack()

        add_button = tk.Button(new_window, text="Add edge",
                     command=lambda: self.add_edge
                     (node_1_entry.get(), node_2_entry.get(),edge_weight_entry.get()))
        add_button.pack()

        remove_button = tk.Button(new_window,text="Remove edge",
                    command=lambda: self.remove_edge(node_1_entry.get(), node_2_entry.get()))
        remove_button.pack()

    def path_window(self):

        new_window = tk.Toplevel(self.root)
        new_window.title("Enter Nodes for Shortest Path")

        label = tk.Label(new_window, text="Enter the start and end nodes:")
        label.pack()

        start_node_entry = tk.Entry(new_window)
        start_node_entry.pack()

        end_node_entry = tk.Entry(new_window)
        end_node_entry.pack()

        submit_button = tk.Button(new_window, text="Find Shortest Path",
                                  command=lambda:
                                  self.shortest_path(start_node_entry.get(), end_node_entry.get()))
        submit_button.pack()
    def shortest_path(self,start_node, end_node):

        try:
            shortest_path=nx.astar_path(self.graph,source=start_node,target=end_node)
            self.show_message(f"path: {shortest_path}")
            self.draw_graph()
        except nx.NetworkXNoPath:
            self.show_message("No path.")


def main():
    graph_simulator = GraphSimulator()

    add_remove_node_button = tk.Button(graph_simulator.root, text="Add or remove node",
                                       command=lambda: graph_simulator.add_remove_node_window())
    add_remove_node_button.pack()

    edge_button = tk.Button(graph_simulator.root, text="Add or remove edge",
                    command=lambda: graph_simulator.add_remove_edge_window())
    edge_button.pack()

    shortest_path_button = tk.Button(graph_simulator.root, text="Shortest Path",
                                     command=graph_simulator.path_window)
    shortest_path_button.pack()



    graph_simulator.root.mainloop()

if __name__ == "__main__":
    main()