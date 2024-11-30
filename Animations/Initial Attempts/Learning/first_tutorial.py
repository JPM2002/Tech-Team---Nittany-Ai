
# put this in terminal to run:
# manim -ql -p normal_way.py FirstExample

from manim import *

class SecondExample(Scene):
    def construct(self):
        ax = Axes(x_range=(-3,3), y_range=(-3,3))
        curve = ax.plot(lambda x: (x+2)*x*(x-2)/2,color=RED)
        area = ax.get_area(curve,x_range=(-2,0))
        self.play(Create(ax),Create(curve), run_time=3)
        self.play(FadeIn(area))
        self.wait(2)
        #self.add(ax, curve,area)

class SquareToCircle(Scene):
    def construct(self):
        green_square = Square(color=GREEN , fill_opacity=0.5)
        self.play(DrawBorderThenFill(green_square))
        blue_cirlce = Circle(color=BLUE, fill_opacity=0.5)
        self.play(Transform(green_square, blue_cirlce))
        # ReplacementTransform
        self.play(Indicate(blue_cirlce))
        self.play(FadeOut(green_square))
        self.wait(2)
