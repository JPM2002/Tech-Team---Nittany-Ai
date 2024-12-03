from manim import *
from manim_neural_network.neural_network import NeuralNetworkMobject

#manim -pql neural_network_1.py SequentialNeuralNetworkScene

def label_layers(self, labels, input_size=0.4, hidden_size=0.25, output_size=0.4):
    """
    Adds labels above each layer to describe its role, with specific sizes for input, hidden, and output layers.
    Default values are used if no specific size is provided.
    """
    label_objects = VGroup()  # Group all labels to manage them together
    for i, (label_text, layer) in enumerate(zip(labels, self.layers)):
        label = Text(label_text)
        
        # Set the size based on the layer type
        if i == 0:  # Input layer
            label.scale(input_size)
        elif i == len(self.layers) - 1:  # Output layer
            label.scale(output_size)
        else:  # Hidden layers
            label.scale(hidden_size)
        
        label.next_to(layer, UP)  # Place the label above the layer
        label_objects.add(label)  # Add the label to the group

    self.add(label_objects)  # Add the group of labels to the scene
    return label_objects  # Return the labels for further animation if needed


# Attach the method dynamically to NeuralNetworkMobject
NeuralNetworkMobject.label_layers = label_layers




class ExampleScene(Scene):
    def construct(self):
        neural_network = NeuralNetworkMobject([3, 5, 2])
        neural_network.move_to(ORIGIN)

        self.play(FadeIn(neural_network))
        self.wait(1)

# manim -pql neural_network_1.py ExampleScene

class SequentialNeuralNetworkScene(Scene):
    def construct(self):
        # Define the neural network structure [Input, Hidden, Output]
        neural_network = NeuralNetworkMobject([3, 5, 5, 5, 2])
        neural_network.move_to(ORIGIN)

        # Animate neuron creation
        for layer in neural_network.layers:
            self.play(FadeIn(layer.neurons), run_time=0.5)
        self.wait(1)

        # Animate edge creation
        for edge_group in neural_network.edge_groups:
            self.play(Create(edge_group), run_time=1)
        self.wait(1)

        # Add and animate layer labels
        layer_labels = ["Input Layer", "Hidden Layer 1", "Hidden Layer 2", "Hidden Layer 3", "Output Layer"]
        labels = neural_network.label_layers(layer_labels)  # Add the labels
        self.play(FadeIn(labels), run_time=1)  # Animate the labels' appearance

        # Label the inputs and outputs AFTER neurons and edges are added
        neural_network.label_inputs("x")  # Label inputs as x_1, x_2, x_3
        neural_network.label_outputs("y")  # Label outputs as y_1, y_2

        # Add the input and output labels explicitly
        for i, neuron in enumerate(neural_network.layers[0].neurons):
            label = MathTex(f"x_{{{i + 1}}}")
            label.set_height(0.3)
            label.next_to(neuron, LEFT)
            self.play(FadeIn((label)))

        for i, neuron in enumerate(neural_network.layers[-1].neurons):
            label = MathTex(f"y_{{{i + 1}}}")
            label.set_height(0.3)
            label.next_to(neuron, RIGHT)
            self.play(FadeIn((label)))

        # Highlight input and output labels
        for layer, direction in [(neural_network.layers[0], LEFT), (neural_network.layers[-1], RIGHT)]:
            for neuron in layer.neurons:
                self.play(Indicate(neuron, color=YELLOW), run_time=0.5)

        self.wait(2)
