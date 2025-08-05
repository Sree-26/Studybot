import networkx as nx
import matplotlib.pyplot as plt
import uuid

def generate_mindmap(text):
    G = nx.Graph()
    lines = text.split("\u2022") if "\u2022" in text else text.split("\n")
    lines = [line.strip() for line in lines if line.strip()]

    central = "StudyBot Summary"
    G.add_node(central)

    for line in lines:
        G.add_node(line)
        G.add_edge(central, line)

    fig, ax = plt.subplots()
    nx.draw(G, with_labels=True, node_color='lightblue', node_size=2500, font_size=10, ax=ax)

    filename = f"mindmap_{uuid.uuid4().hex}.png"
    plt.savefig(filename)
    return filename
