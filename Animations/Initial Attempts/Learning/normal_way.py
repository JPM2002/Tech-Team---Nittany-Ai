from manim import *

class FirstExample(Scene):
    def construct(self):
        # Create a blue circle
        blue_circle = Circle(color=BLUE, fill_opacity=0.5)
        
        # Create a green square
        green_square = Square(color=GREEN, fill_opacity=0.8)
        green_square.next_to(blue_circle, RIGHT)
        
        # Add the shapes to the scene
        self.add(blue_circle, green_square)
