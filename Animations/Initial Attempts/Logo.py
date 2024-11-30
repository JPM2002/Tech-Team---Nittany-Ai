from manim import *
import itertools as it

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
        "include_output_labels": False,
        "arrow": False,
    }

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

    def get_layer(self, size, index=-1):
        layer = VGroup()
        neurons = VGroup(*[
            Circle(
                radius=self.CONFIG["neuron_radius"],
                stroke_color=WHITE,
                stroke_width=self.CONFIG["neuron_stroke_width"],
                fill_color=BLACK,
                fill_opacity=1,
            )
            for x in range(size)
        ])
        neurons.arrange_submobjects(
            DOWN, buff=self.CONFIG["neuron_to_neuron_buff"]
        )
        for neuron in neurons:
            neuron.edges_in = VGroup()
            neuron.edges_out = VGroup()
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
                    stroke_color=GREY,
                    stroke_width=self.CONFIG["edge_stroke_width"]
                )
                edge_group.add(edge)
                n1.edges_out.add(edge)
                n2.edges_in.add(edge)
            self.edge_groups.add(edge_group)
        self.add_to_back(self.edge_groups)

class MachineLearningBootcamp(Scene):
    def construct(self):
        # 1. Title Introduction
        title = Text("Machine Learning Bootcamp", font_size=48, color=BLUE)
        subtitle = Text("By Nittany AI", font_size=32, color=GREY)
        subtitle.next_to(title, DOWN)

        self.play(FadeIn(title, shift=UP), Write(subtitle))
        self.wait(2)
        self.play(FadeOut(title, shift=UP), FadeOut(subtitle, shift=UP))

        # 2. Neural Network Animation
        nn_structure = [5, 8, 8, 3]  # Neural network layers
        nn = NeuralNetworkMobject(nn_structure).move_to(ORIGIN)
        self.play(Create(nn))

        # Highlight neuron firing
        firing_animation = AnimationGroup(*[
            neuron.animate.set_fill(GREEN, opacity=0.5).set_stroke(YELLOW)
            for layer in nn.layers
            for neuron in layer.neurons
        ], lag_ratio=0.05)
        self.play(firing_animation)

        # Highlight output layer
        output_layer = nn.layers[-1]
        self.play(*[neuron.animate.set_fill(RED, opacity=0.8) for neuron in output_layer.neurons])
        self.wait(1)

        # 3. Final Logo Reveal
        self.play(FadeOut(nn))
        logo = Text("Nittany AI", font_size=64, color=BLUE).to_edge(UP)
        closing_text = Text("Empowering Machine Learning", font_size=36, color=WHITE)
        closing_text.next_to(logo, DOWN)

        self.play(Write(logo), FadeIn(closing_text))
        self.wait(2)
