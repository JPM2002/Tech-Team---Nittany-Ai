from manim import *
import itertools as it

# A customizable Sequential Neural Network
class NeuralNetworkMobject(VGroup):
    def __init__(self, neural_network, **kwargs):
        super().__init__(**kwargs)
        self.layer_sizes = neural_network
        self.neuron_radius = 0.15
        self.neuron_to_neuron_buff = 0.2
        self.layer_to_layer_buff = 1.0
        self.output_neuron_color = WHITE
        self.input_neuron_color = WHITE
        self.hidden_layer_neuron_color = WHITE
        self.neuron_stroke_width = 2
        self.neuron_fill_opacity = 1
        self.edge_color = LIGHT_GREY
        self.edge_stroke_width = 2
        self.add_neurons()
        self.add_edges()
        self.add_to_back(self.layers)

    def add_neurons(self):
        layers = VGroup(*[
            self.get_layer(size, index)
            for index, size in enumerate(self.layer_sizes)
        ])
        layers.arrange(RIGHT, buff=self.layer_to_layer_buff)
        self.layers = layers

    def get_nn_fill_color(self, index):
        if index == 0:
            return self.input_neuron_color
        elif index == len(self.layer_sizes) - 1:
            return self.output_neuron_color
        else:
            return self.hidden_layer_neuron_color

    def get_layer(self, size, index=-1):
        layer = VGroup()
        neurons = VGroup(*[
            Circle(
                radius=self.neuron_radius,
                stroke_color=self.get_nn_fill_color(index),
                stroke_width=self.neuron_stroke_width,
                fill_color=BLACK,
                fill_opacity=self.neuron_fill_opacity,
            )
            for _ in range(size)
        ])
        for neuron in neurons:
            neuron.z_index = 1  # Ensure neurons are in front of edges
        neurons.arrange(DOWN, buff=self.neuron_to_neuron_buff)
        layer.neurons = neurons
        layer.add(neurons)
        return layer


    def add_edges(self):
        self.edge_groups = VGroup()
        for l1, l2 in zip(self.layers[:-1], self.layers[1:]):
            edge_group = VGroup()
            for n1, n2 in it.product(l1.neurons, l2.neurons):
                edge = Line(
                    n1.get_center(),
                    n2.get_center(),
                    stroke_color=self.edge_color,
                    stroke_width=self.edge_stroke_width,
                )
                edge.z_index = 0  # Set edges to a lower z-index
                edge_group.add(edge)
            self.edge_groups.add(edge_group)
        self.add(self.edge_groups)  # Add edges first



    def label_inputs(self, label):
        for i, neuron in enumerate(self.layers[0].neurons):
            text = MathTex(f"{label}_{{{i + 1}}}")
            text.set_height(0.3)
            text.next_to(neuron, LEFT)
            self.add(text)

    def label_outputs(self, label):
        for i, neuron in enumerate(self.layers[-1].neurons):
            text = MathTex(f"{label}_{{{i + 1}}}")
            text.set_height(0.3)
            text.next_to(neuron, RIGHT)
            self.add(text)


class SequentialNeuralNetworkScene(Scene):
    def construct(self):
        # Define a simple neural network structure [Input, Hidden, Output]
        neural_network = NeuralNetworkMobject([3, 5, 5, 5,  2])

        # Center the neural network on the screen
        neural_network.move_to(ORIGIN)

        # Animate the creation of neurons first
        for layer in neural_network.layers:
            self.play(FadeIn(layer.neurons), run_time=.5)

        self.wait(1)

        # Animate the edges after the neurons
        for edge_group in neural_network.edge_groups:
            self.play(Create(edge_group), run_time=1)

        self.wait(2)

class ExampleScene(Scene):
    def construct(self):
        neural_network = NeuralNetworkMobject([3, 5, 2])
        neural_network.move_to(ORIGIN)

        self.play(FadeIn(neural_network))
        self.wait(1)

