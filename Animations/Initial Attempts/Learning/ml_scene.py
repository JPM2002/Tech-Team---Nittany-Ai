
from manim import *


class CombinedScenes(Scene):
    def construct(self):
        # Add Dial elements
        circle = Circle(radius=0.5).set_fill(BLUE, opacity=0.5).set_stroke(YELLOW, width=4)
        pointer = Line(start=[0, 0, 0], end=[0, 0.4, 0], color=WHITE).shift(UP * 0.1).rotate(PI / 4)
        group = VGroup(circle, pointer)
        self.add(group)
        self.play(pointer.animate.rotate(-PI / 2), run_time=2)
        self.wait()

        # Add MachineWithDials elements
        box = Rectangle(height=2, width=3).set_stroke(WHITE, width=2)
        dials = VGroup(
            *[Circle(radius=0.2).set_fill(GREEN, opacity=0.6).set_stroke(WHITE, 1) for _ in range(5)]
        ).arrange_in_grid(rows=1, buff=0.3).move_to(box.get_center())
        machine = VGroup(box, dials)
        self.add(machine)
        for dial in dials:
            self.play(dial.animate.scale(1.2), run_time=0.3)
            self.play(dial.animate.scale(0.8), run_time=0.3)
        self.wait()

        # Add NeuralNetwork elements
        layer_1 = VGroup(*[Circle(radius=0.3).set_fill(TEAL, opacity=0.8) for _ in range(5)]).arrange(DOWN, buff=0.5)
        layer_2 = VGroup(*[Circle(radius=0.3).set_fill(PURPLE, opacity=0.8) for _ in range(3)]).arrange(DOWN, buff=0.5)
        layer_3 = VGroup(*[Circle(radius=0.3).set_fill(ORANGE, opacity=0.8) for _ in range(4)]).arrange(DOWN, buff=0.5)
        layers = VGroup(layer_1, layer_2, layer_3).arrange(RIGHT, buff=1.5)
        self.add(layers)

        connections = VGroup()
        for neuron1 in layer_1:
            for neuron2 in layer_2:
                connections.add(Line(start=neuron1.get_center(), end=neuron2.get_center(), stroke_width=1))
        for neuron2 in layer_2:
            for neuron3 in layer_3:
                connections.add(Line(start=neuron2.get_center(), end=neuron3.get_center(), stroke_width=1))
        self.add(connections)
        self.play(Create(connections), run_time=3)
        self.play(layer_2[1].animate.set_fill(YELLOW, opacity=1))
        self.wait()

        # Add DeepLearningHierarchy elements
        dl_box = Rectangle(height=2, width=4, color=BLUE).set_fill(TEAL, opacity=0.2)
        ml_box = Rectangle(height=3, width=5, color=GREEN).set_fill(GREEN, opacity=0.1)
        ai_box = Rectangle(height=4, width=6, color=RED).set_fill(RED, opacity=0.05)
        dl_text = Text("Deep Learning", font_size=36).move_to(dl_box.get_center())
        ml_text = Text("Machine Learning", font_size=36).move_to(ml_box.get_center())
        ai_text = Text("Artificial Intelligence", font_size=36).move_to(ai_box.get_center())
        group = VGroup(ai_box, ml_box, dl_box, ai_text, ml_text, dl_text).arrange(DOWN, buff=0.5)
        self.add(group)
        self.play(Create(ai_box), Write(ai_text))
        self.wait()
        self.play(Create(ml_box), Write(ml_text))
        self.wait()
        self.play(Create(dl_box), Write(dl_text))
        self.wait()

        # Add LinearRegression elements
        axes = Axes(x_range=[0, 10, 1], y_range=[0, 10, 1], axis_config={"include_numbers": True})
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")
        m, y_intercept = 0.5, 2
        regression_line = axes.plot(lambda x: m * x + y_intercept, color=YELLOW)
        scatter_points = VGroup(*[Dot(axes.c2p(x, m * x + y_intercept + np.random.normal(0, 0.5))) for x in range(1, 9)])
        self.play(Create(axes), Write(axes_labels))
        self.play(Create(scatter_points))
        self.play(Create(regression_line))
        self.wait()

        # Add SoftmaxFunction elements
        bars = BarChart([0.1, 0.5, 0.2, 0.7], bar_colors=[RED, BLUE, GREEN, YELLOW])
        labels = VGroup(*[Text(f"Class {i+1}", font_size=24).next_to(bar, DOWN) for i, bar in enumerate(bars.bars)])
        self.play(Create(bars))
        self.play(FadeIn(labels))
        self.wait()
        text = Text("Softmax ensures these sum to 1", font_size=30).to_edge(UP)
        self.play(Write(text))
        self.wait()

