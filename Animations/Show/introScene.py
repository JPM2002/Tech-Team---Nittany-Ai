# manim -pql introScene.py TeamIntro
# manim -pql introScene.py TeamIntro3D

from manim import *
from manim_neural_network.neural_network import NeuralNetworkMobject

class TeamIntro(Scene):
    def construct(self):


        
        # Create Text objects for the intro
        title = Text("MLB Team", font_size=60, color=BLUE)
        subtitle = Text("Nittany AI Student Society", font_size=40, color=GREEN)
        description = Text("The Power of Manim!", font_size=36, color=YELLOW)

        # Position subtitle below title
        subtitle.next_to(title, DOWN)

        # Display the title and subtitle with animations
        self.play(Write(title))
        self.play(FadeIn(subtitle))
        self.wait(2)

        # Transition to description
        self.play(FadeOut(title, shift=UP), 
                  ReplacementTransform(subtitle, description.move_to(ORIGIN)))
        self.wait(2)

        # Add example text-based animations to show capabilities
        example_1 = Text("Animations are smooth and engaging", font_size=30, color=RED)
        example_2 = Text("Customizable and flexible!", font_size=30, color=PURPLE)

        example_1.next_to(description, DOWN, buff=1)
        example_2.next_to(example_1, DOWN, buff=0.5)

        self.play(FadeIn(example_1, shift=UP))
        self.wait(1)
        self.play(FadeIn(example_2, shift=UP))
        self.wait(2)
        self.play(FadeOut(description))

        # Transition to final message
        final_message = Text("Okay okay. Let me show you what can be done", font_size=40, color=ORANGE)
        eric_approved_message = Text("Eric, you better approve the use of this tool")

        eric_approved_message.next_to(final_message, DOWN, buff=1)

        self.play(
                  FadeOut(example_1, shift=UP), 
                  FadeOut(example_2, shift=UP))
        self.play(Write(final_message))
        self.play(Write(eric_approved_message))
        self.wait(2)

        # Fade out to conclude the scene
        self.play(FadeOut(final_message))
        self.play(FadeOut(eric_approved_message))

        # # Define the neural network structure [Input, Hidden, Output]
        # neural_network = NeuralNetworkMobject([3, 5, 5, 5, 2])
        # neural_network.move_to(ORIGIN)

        # # Animate neuron creation
        # for layer in neural_network.layers:
        #     self.play(FadeIn(layer.neurons), run_time=0.5)
        # self.wait(1)

        # # Animate edge creation
        # for edge_group in neural_network.edge_groups:
        #     self.play(Create(edge_group), run_time=1)
        # self.wait(1)


        # # Label the inputs and outputs AFTER neurons and edges are added
        # neural_network.label_inputs("x")  # Label inputs as x_1, x_2, x_3
        # neural_network.label_outputs("y")  # Label outputs as y_1, y_2

        # # Add the input and output labels explicitly
        # for i, neuron in enumerate(neural_network.layers[0].neurons):
        #     label = MathTex(f"x_{{{i + 1}}}")
        #     label.set_height(0.3)
        #     label.next_to(neuron, LEFT)
        #     self.play(FadeIn((label)))

        # for i, neuron in enumerate(neural_network.layers[-1].neurons):
        #     label = MathTex(f"y_{{{i + 1}}}")
        #     label.set_height(0.3)
        #     label.next_to(neuron, RIGHT)
        #     self.play(FadeIn((label)))

        # # Highlight input and output labels
        # for layer, direction in [(neural_network.layers[0], LEFT), (neural_network.layers[-1], RIGHT)]:
        #     for neuron in layer.neurons:
        #         self.play(Indicate(neuron, color=YELLOW), run_time=0.5)

        # self.wait(2)


        # Define multiple neural network structures
        network_variations = [
            [3, 5, 2],  # Input, Hidden, Output
            [4, 6, 3, 2],
            [3, 5, 5, 5, 2],
            [5, 10, 10, 5, 2],
        ]

        for structure in network_variations:
            # Create a neural network
            neural_network = NeuralNetworkMobject(structure)
            neural_network.move_to(ORIGIN)

            # Generate layer labels dynamically with proper line breaks
            layer_labels = ["Input Layer"] + [f"Hidden\nLayer {i+1}" for i in range(len(structure) - 2)] + ["Output Layer"]

            # Adjust size of hidden layers if more than two
            hidden_layer_size = 0.2 if len(structure) - 2 > 2 else 0.25

            # Add layer labels and keep them visible
            label_objects = VGroup()
            for idx, (layer, label) in enumerate(zip(neural_network.layers, layer_labels)):
                if "Hidden\nLayer" in label:
                    layer_label = Text(label, font_size=hidden_layer_size * 100, color=BLUE)
                else:
                    layer_label = Text(label, font_size=24, color=BLUE)
                layer_label.next_to(layer, UP)
                label_objects.add(layer_label)
            self.play(FadeIn(neural_network.layers), FadeIn(label_objects), run_time=0.8)

            # Initialize all neurons by "shining"
            for layer in neural_network.layers:
                self.play(*[Indicate(neuron, color=YELLOW) for neuron in layer.neurons], run_time=0.5)

            # Connect layers simultaneously
            for layer_idx in range(len(neural_network.layers) - 1):
                edge_group = neural_network.edge_groups[layer_idx]
                self.play(Create(edge_group), run_time=0.5)

            self.wait(0.5)  # Brief pause for visibility

            # Fade out the entire network
            self.play(FadeOut(neural_network), FadeOut(label_objects), run_time=0.8)

        # Final wait to transition to the next scene
        self.wait(2)

        dot = Dot(ORIGIN)
        arrow = Arrow(ORIGIN, [2, 2, 0], buff=0)
        numberplane = NumberPlane()
        origin_text = Text('(0, 0)').next_to(dot, DOWN)
        tip_text = Text('(2, 2)').next_to(arrow.get_end(), RIGHT)

        self.play(FadeIn(numberplane), FadeIn(dot), FadeIn(arrow), FadeIn(origin_text), FadeIn(tip_text))
        self.wait(2)
        self.play(FadeOut(numberplane), FadeOut(dot), FadeOut(arrow), FadeOut(origin_text), FadeOut(tip_text))

        text = MathTex(
            "\\frac{d}{dx}f(x)g(x)=","f(x)\\frac{d}{dx}g(x)","+",
            "g(x)\\frac{d}{dx}f(x)"
        )
        self.play(Write(text))
        framebox1 = SurroundingRectangle(text[1], buff=0.1)
        framebox2 = SurroundingRectangle(text[3], buff=0.1)
        self.play(Create(framebox1))
        self.wait(1)
        self.play(ReplacementTransform(framebox1, framebox2))
        self.wait(1)
        self.play(FadeOut(text), FadeOut(framebox2))

        # Add concluding text
        concluding_text_1 = Text("Hope we can use this during the semester,", font_size=30, color=WHITE)
        concluding_text_2 = Text("I am developing a library for using this more easily.", font_size=30, color=WHITE)

        concluding_text_1.to_edge(UP, buff=1)
        concluding_text_2.next_to(concluding_text_1, DOWN, buff=0.5)

        # Animate the concluding text
        self.play(FadeIn(concluding_text_1))
        self.wait(1)
        self.play(FadeIn(concluding_text_2))
        self.wait(2)

        # Fade out concluding text
        self.play(FadeOut(concluding_text_1), FadeOut(concluding_text_2))
        self.wait(3)

class TeamIntro3D(ThreeDScene):
    def construct(self):
        # Set up 3D axes and heatmap surface plot
        resolution_fa = 24
        self.set_camera_orientation(phi=75 * DEGREES, theta=-30 * DEGREES)

        def param_gauss(u, v):
            x = u
            y = v
            sigma, mu = 0.4, [0.0, 0.0]
            d = np.linalg.norm(np.array([x - mu[0], y - mu[1]]))
            z = -np.exp(-(d ** 2 / (2.0 * sigma ** 2)))  # Negative Z-axis
            return np.array([x, y, z])

        # Define 3D axes
        axes = ThreeDAxes(
            x_range=[-2, 2, 1],
            y_range=[-2, 2, 1],
            z_range=[-1, 0, 0.2],  # Adjusted for the Gaussian surface range
        )

        # Create a heatmap-like surface
        gauss_plane = Surface(
            param_gauss,
            resolution=(resolution_fa, resolution_fa),
            v_range=[-2, +2],
            u_range=[-2, +2],
        )

        gauss_plane.scale(2, about_point=ORIGIN)
        gauss_plane.set_style(fill_opacity=1)
        gauss_plane.set_fill_by_checkerboard(ORANGE, BLUE, opacity=0.5)

        self.add(axes, gauss_plane)

        # Simulate a ball falling along the surface
        ball = Sphere(radius=0.15, color=RED)
        start_point = param_gauss(1.8, 1.8)
        ball.move_to(start_point)
        self.add(ball)

        # Highlight the start point
        start_label = Text("Start", font_size=24, color=YELLOW).next_to(ball, UP)
        self.play(FadeIn(start_label), GrowFromCenter(ball))
        self.wait(1)

        # Gradient descent trajectory
        trajectory = [
            param_gauss(1.8, 1.8),
            param_gauss(1.5, 1.5),
            param_gauss(1.0, 1.0),
            param_gauss(0.5, 0.5),
            param_gauss(0.2, 0.2),
            np.array([0.0, 0.0, -1.0]),  # True minimum
        ]

        # Show trajectory with glowing path
        trajectory_lines = VGroup()
        for i in range(len(trajectory) - 1):
            line = Line(trajectory[i], trajectory[i + 1], stroke_width=3, color=YELLOW)
            trajectory_lines.add(line)

        self.play(Create(trajectory_lines), run_time=2)

        # Animate the ball moving along the gradient descent path
        for idx, point in enumerate(trajectory):
            self.play(ball.animate.move_to(point), run_time=1.5)
            if idx == len(trajectory) - 2:
                min_label = Text("Minimum", font_size=24, color=GREEN).next_to(point, DOWN)
                self.play(FadeIn(min_label))

        # Transition to top-down view
        self.set_camera_orientation(phi=0 * DEGREES, theta=270 * DEGREES)
        self.wait(2)

        # Highlight trajectory in top-down view
        self.play(Indicate(trajectory_lines, color=RED), run_time=2)
        self.wait(2)

        # Fade out elements
        self.play(FadeOut(ball), FadeOut(trajectory_lines), FadeOut(axes), FadeOut(gauss_plane))

