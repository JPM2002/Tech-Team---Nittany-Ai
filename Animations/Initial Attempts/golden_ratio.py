from manim import *

class GoldenRatioVisualization(Scene):
    def construct(self):
        # Title
        title = Text("The Golden Ratio (φ)", font_size=48, color=YELLOW)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        
        # Definition
        definition = MathTex(r"\phi = \frac{1 + \sqrt{5}}{2} \approx 1.618", font_size=36)
        definition.next_to(title, DOWN, buff=0.5)
        self.play(Write(definition))
        
        # Geometric representation
        # Step 1: Draw initial rectangle
        golden_rect = Rectangle(height=2, width=3.236, color=BLUE)  # Approximates the Golden Ratio
        golden_rect.shift(LEFT * 1.5)
        
        square = Square(side_length=2, color=GREEN)
        square.next_to(golden_rect.get_left(), RIGHT, buff=0)
        
        self.play(Create(golden_rect), Create(square))
        
        # Subdivide the rectangle into a square and smaller golden rectangle
        smaller_rect = Rectangle(height=2, width=1.236, color=RED)
        smaller_rect.next_to(square, RIGHT, buff=0)
        self.play(Create(smaller_rect))
        
        # Add labels
        side_label = MathTex("1", font_size=24).next_to(square, DOWN, buff=0.2)
        phi_label = MathTex(r"\phi", font_size=24).next_to(smaller_rect, DOWN, buff=0.2)
        self.play(Write(side_label), Write(phi_label))
        
        # Repeated subdivision
        current_rect = smaller_rect
        for _ in range(3):  # Repeat subdivision 3 more times
            new_square = Square(side_length=current_rect.height, color=GREEN)
            new_square.move_to(current_rect.get_corner(UL))
            self.play(Create(new_square))
            
            new_rect = Rectangle(height=new_square.height, width=current_rect.width - new_square.height, color=RED)
            new_rect.next_to(new_square, RIGHT, buff=0)
            self.play(Create(new_rect))
            
            current_rect = new_rect  # Update the current rectangle
        
        # Draw Golden Spiral
        arc_start = golden_rect.get_corner(DR)
        for _ in range(4):
            arc = ArcBetweenPoints(start=arc_start, end=golden_rect.get_corner(DL), angle=TAU / 4, color=ORANGE)
            self.play(Create(arc))
            golden_rect.scale(0.618)  # Shrink to next segment
            arc_start = golden_rect.get_corner(DR)
        
        # Applications Text
        applications = Text("Applications: Nature, Art, Architecture", font_size=28)
        applications.to_edge(DOWN, buff=0.5)
        self.play(Write(applications))
        
        self.wait(3)
