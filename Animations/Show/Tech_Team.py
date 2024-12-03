from manim import *


class introTitle(Scene):
    def construct(self):
        Logo = Text("Nittany Ai")
        Logo.to_edge(UP)  # Position the title at the top edge of the screen

        self.play(Write(Logo),run_time=2)