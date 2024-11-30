from manim import *
import itertools as it


# A customizable Sequential Neural Network
class NeuralNetworkMobject(VGroup):
    CONFIG = {
        "neuron_radius": 0.15,
        "neuron_to_neuron_buff": MED_SMALL_BUFF,
        "layer_to_layer_buff": LARGE_BUFF,
        "output_neuron_color": WHITE,
        "input_neuron_color": WHITE,
        "hidden_layer_neuron_color": WHITE,
        "neuron_stroke_width": 2,
        "neuron_fill_color": GREEN,
        "edge_color": LIGHT_GREY,
        "edge_stroke_width": 2,
        "edge_propogation_color": YELLOW,
        "edge_propogation_time": 1,
        "max_shown_neurons": 16,
        "brace_for_large_layers": True,
        "average_shown_activation_of_large_layer": True,
        "include_output_labels": False,
        "arrow": False,
        "arrow_tip_size": 0.1,
        "left_size": 1,
        "neuron_fill_opacity": 1
    }

    # Constructor with parameters of the neurons in a list
    def __init__(self, neural_network, *args, **kwargs):
        VGroup.__init__(self, *args, **kwargs)
        self.layer_sizes = neural_network
        self.add_neurons()
        self.add_edges()
        self.add_to_back(self.layers)

    def add_neurons(self):
        layers = VGroup(*[
            self.get_layer(size, index)
            for index, size in enumerate(self.layer_sizes)
        ])
        layers.arrange_submobjects(RIGHT, buff=self.CONFIG["layer_to_layer_buff"])
        self.layers = layers
        if self.CONFIG["include_output_labels"]:
            self.label_outputs_text()

    def get_nn_fill_color(self, index):
        if index == -1 or index == len(self.layer_sizes) - 1:
            return self.CONFIG["output_neuron_color"]
        if index == 0:
            return self.CONFIG["input_neuron_color"]
        else:
            return self.CONFIG["hidden_layer_neuron_color"]

    def get_layer(self, size, index=-1):
        layer = VGroup()
        n_neurons = size
        if n_neurons > self.CONFIG["max_shown_neurons"]:
            n_neurons = self.CONFIG["max_shown_neurons"]
        neurons = VGroup(*[
            Circle(
                radius=self.CONFIG["neuron_radius"],
                stroke_color=self.get_nn_fill_color(index),
                stroke_width=self.CONFIG["neuron_stroke_width"],
                fill_color=BLACK,
                fill_opacity=self.CONFIG["neuron_fill_opacity"],
            )
            for x in range(n_neurons)
        ])
        neurons.arrange_submobjects(
            DOWN, buff=self.CONFIG["neuron_to_neuron_buff"]
        )
        for neuron in neurons:
            neuron.edges_in = VGroup()
            neuron.edges_out = VGroup()
        layer.neurons = neurons
        layer.add(neurons)

        if size > n_neurons:
            dots = Tex("\\vdots")
            dots.move_to(neurons)
            VGroup(*neurons[:len(neurons) // 2]).next_to(
                dots, UP, MED_SMALL_BUFF
            )
            VGroup(*neurons[len(neurons) // 2:]).next_to(
                dots, DOWN, MED_SMALL_BUFF
            )
            layer.dots = dots
            layer.add(dots)
            if self.CONFIG["brace_for_large_layers"]:
                brace = Brace(layer, LEFT)
                brace_label = brace.get_tex(str(size))
                layer.brace = brace
                layer.brace_label = brace_label
                layer.add(brace, brace_label)

        return layer

    def add_edges(self):
        self.edge_groups = VGroup()
        for l1, l2 in zip(self.layers[:-1], self.layers[1:]):
            edge_group = VGroup()
            for n1, n2 in it.product(l1.neurons, l2.neurons):
                edge = self.get_edge(n1, n2)
                edge_group.add(edge)
                n1.edges_out.add(edge)
                n2.edges_in.add(edge)
            self.edge_groups.add(edge_group)
        self.add_to_back(self.edge_groups)

    def get_edge(self, neuron1, neuron2):
        if self.CONFIG["arrow"]:
            return Arrow(
                neuron1.get_center(),
                neuron2.get_center(),
                buff=self.CONFIG["neuron_radius"],
                stroke_color=self.CONFIG["edge_color"],
                stroke_width=self.CONFIG["edge_stroke_width"],
                tip_length=self.CONFIG["arrow_tip_size"]
            )
        return Line(
            neuron1.get_center(),
            neuron2.get_center(),
            buff=self.CONFIG["neuron_radius"],
            stroke_color=self.CONFIG["edge_color"],
            stroke_width=self.CONFIG["edge_stroke_width"],
        )

    def label_inputs(self, l):
        self.output_labels = VGroup()
        for n, neuron in enumerate(self.layers[0].neurons):
            # Add $...$ around the LaTeX string for math mode
            label = Tex(f"${l}_{{{n + 1}}}$")
            label.set_height(0.3 * neuron.get_height())
            label.move_to(neuron)
            self.output_labels.add(label)
        self.add(self.output_labels)

    def label_outputs(self, l):
        self.output_labels = VGroup()
        for n, neuron in enumerate(self.layers[-1].neurons):
            # Add $...$ around the LaTeX string for math mode
            label = Tex(f"${l}_{{{n + 1}}}$")
            label.set_height(0.4 * neuron.get_height())
            label.move_to(neuron)
            self.output_labels.add(label)
        self.add(self.output_labels)

    def label_outputs_text(self, outputs):
        self.output_labels = VGroup()
        for n, neuron in enumerate(self.layers[-1].neurons):
            label = Tex(outputs[n])
            label.set_height(0.75 * neuron.get_height())
            label.move_to(neuron)
            label.shift((neuron.get_width() + label.get_width() / 2) * RIGHT)
            self.output_labels.add(label)
        self.add(self.output_labels)

# Manim Scene
class NeuralNetworkScene(Scene):
    def construct(self):
        # Define the neural network structure
        architecture = [3, 5, 2]

        # Create a neural network object
        nn = NeuralNetworkMobject(architecture)

        # Optionally, customize the neural network
        nn.CONFIG["neuron_radius"] = 0.2
        nn.CONFIG["neuron_fill_color"] = BLUE

        # Position and add the neural network to the scene
        nn.move_to(ORIGIN)
        self.play(Create(nn))

        # Label input and output neurons
        nn.label_inputs("x")
        nn.label_outputs("y")

        self.wait(2)
