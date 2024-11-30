from manim import *
import itertools as it
import numpy as np

class EpicManimDemo(Scene):
    def construct(self):
        # 1. Cosmic Particle Swirl Intro
        self.play_title_intro()

        # 2. Neural Network Propagation
        self.play_neural_network_firing()

        # 3. Machine Learning in Action
        self.play_machine_learning_visualization()

        # 4. Grand Finale with Logo
        self.play_logo_outro()

    def play_title_intro(self):
        # Generate swirling particles
        particles = VGroup(*[
            Dot(radius=0.05, color=BLUE)
            for _ in range(200)
        ])
        for particle in particles:
            particle.move_to(np.random.uniform(-6, 6, size=3))

        # Animate swirl
        swirl = particles.animate.rotate(PI * 4, about_point=ORIGIN).scale(0.5)
        self.play(swirl, run_time=4, rate_func=smooth)

        # Title reveal
        title = Text("The Power of Manim", font_size=72, gradient=(BLUE, PURPLE))
        subtitle = Text("Grandiose Visuals with Python", font_size=36, color=GREY)
        subtitle.next_to(title, DOWN)

        self.play(FadeIn(title, shift=UP), Write(subtitle))
        self.wait(1)
        self.play(FadeOut(particles), FadeOut(title), FadeOut(subtitle))

    def play_neural_network_firing(self):
        # Define neural network layers
        nn_structure = [6, 10, 7, 3]
        layers = self.create_neural_network(nn_structure)
        layers.move_to(ORIGIN)

        # Neural network creation animation
        self.play(Create(layers), run_time=3)

        # Simulate firing
        for layer in layers:
            self.fire_neurons(layer)
        
        # Highlight output layer
        output_layer = layers[-1]
        self.play(*[n.animate.set_fill(RED, opacity=0.9) for n in output_layer], run_time=1.5)
        self.wait(1)

    def play_machine_learning_visualization(self):
        # Create dataset points
        points = VGroup(*[
            Dot3D(point=(x, y, z), color=BLUE)
            for x, y, z in np.random.uniform(-3, 3, (100, 3))
        ])
        self.play(FadeIn(points, shift=DOWN), run_time=2)

        # Apply clustering colors
        clusters = [RED, GREEN, BLUE]
        for point in points:
            point.set_color(np.random.choice(clusters))

        self.play(points.animate.scale(1.2), run_time=2)

        # Rotate dataset to show in 3D
        self.play(Rotate(points, angle=PI/2, axis=RIGHT), run_time=3)
        self.play(FadeOut(points), run_time=2)

    def play_logo_outro(self):
        # Glowing logo
        logo = Text("Manim Magic", font_size=64, gradient=(BLUE, YELLOW))
        ring = Annulus(inner_radius=0.5, outer_radius=1.5, color=WHITE)
        glow = SurroundingRectangle(logo, color=YELLOW, buff=0.5).set_opacity(0.2)

        self.play(Write(logo), Create(ring), FadeIn(glow, scale=2))
        self.play(ring.animate.rotate(PI * 2), run_time=3)
        self.play(FadeOut(logo, scale=2), FadeOut(ring), FadeOut(glow))

    def create_neural_network(self, structure):
        layers = VGroup()
        for size in structure:
            layer = VGroup(*[
                Circle(radius=0.2, fill_color=BLACK, fill_opacity=1, stroke_color=WHITE)
                for _ in range(size)
            ])
            layer.arrange(DOWN, buff=0.5)
            layers.add(layer)
        layers.arrange(RIGHT, buff=1)
        return layers

    def fire_neurons(self, layer):
        self.play(
            AnimationGroup(*[
                neuron.animate.set_fill(YELLOW, opacity=0.8).set_stroke(RED, width=2)
                for neuron in layer
            ], lag_ratio=0.1),
            run_time=2
        )
        self.play(
            AnimationGroup(*[
                neuron.animate.set_fill(BLACK, opacity=1).set_stroke(WHITE, width=1)
                for neuron in layer
            ], lag_ratio=0.1),
            run_time=1
        )
