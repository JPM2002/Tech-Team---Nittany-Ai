from manim import *

class Positioning(Scene):
    def construct(self):
        plane= NumberPlane()
        self.add(plane)

        red_dot = Dot(color=RED)
        green_dot = Dot(color=GREEN)
        green_dot.next_to(red_dot, RIGHT + UP)
        self.add(red_dot, green_dot)

        #Shift

        s= Square(color=ORANGE)
        s.shift(2*UP + 4*RIGHT)
        self.add(s)

        # move_to

        c = Circle(color=PURPLE)
        c.move_to([-2,-2,0])
        self.add(c)

        #align_to

        c2 = Circle(radius=0.5, color=RED, fill_opacity=0.5)
        c3 = c2.copy().set_color(YELLOW)
        c4 = c2.copy().set_color(ORANGE)
        c2.align_to(s,UP) #align so the border matches the border of the square\
        c3.align_to(s, RIGHT)
        self.add(c2,c3)

class CriticalPoints(Scene):
    def construct(self):
        c = Circle(color=GREEN, fill_opacity=0.5)
        self.add(c)

        for d in [(0,0,0), UP, UR, RIGHT, DR, DOWN, DL,LEFT, UL]:
            self.add(Cross(scale_factor=0.2).move_to(c.get_critical_point(d)))

        s = Square(color=RED, fill_opacity = 0.5)
        s.move_to([1,0,0], aligned_edge=LEFT)

from manim.utils.unit import Percent, Pixels

class UsefulUnits(Scene):
    def construct(self):
        for perc in range(5,51,5):
            self.add(Circle(radius=perc * Percent(X_AXIS)))
            self.add(Square(side_length=2*perc*Percent(Y_AXIS)))

            d = Dot()
            d.shift(100 * Pixels * RIGHT)
            self.add(d)

class Grouping(Scene):
    def construct(self):
        red_dot = Dot(color=RED)
        green_dot = Dot(color=GREEN).next_to(red_dot,RIGHT)
        blue_dot = Dot(color=BLUE).next_to(red_dot, UP)
        dot_group = VGroup(red_dot, green_dot, blue_dot)
        dot_group.to_edge(RIGHT)
        self.add(dot_group)

        circles = VGroup(*[Circle(radius=0.2)for _ in range(10)])
        circles.arrange(UP) # if wanted we could buff=0.5 which is in essence spacing
        self.add(circles)

        stars = VGroup(*[Star(color=YELLOW, fill_opacity=1).scale(0.5) for _ in range(20)])
        stars.arrange_in_grid(4,5, buff=0.2)
        self.add(stars)

#class 

class NittanyAI(Scene):
    def construct(self):
        text = Text("Nittany Ai")
        
        self.play(Create(text),run_time=9)
        self.wait(4)



