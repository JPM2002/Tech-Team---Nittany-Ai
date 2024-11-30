from manim import *


class CreateCircle(Scene):
    def construct(self):
        # Create a circle
        circle = Circle()
        circle.set_fill(PINK, opacity=0.5)
        
        # Create a title
        title = Text("Machine Learning Boot camp 2025")
        title.to_edge(UP)  # Position the title at the top edge of the screen
        
        # Add the title and circle to the scene
        self.play(Write(title))
        self.play(Create(circle))