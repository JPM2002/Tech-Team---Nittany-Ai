# manim -pql example.py

from manim import *
from manim_ml.neural_network import Convolutional2DLayer, FeedForwardLayer, NeuralNetwork

class BasicScene(ThreeDScene):
    def construct(self):

        nn = NeuralNetwork([
            FeedForwardLayer(num_nodes=3),
            FeedForwardLayer(num_nodes=5),
            FeedForwardLayer(num_nodes=3)
        ])
        self.add(nn)
