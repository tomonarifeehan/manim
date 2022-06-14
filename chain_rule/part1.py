from manimlib import *


# Constants
small_font = 40
medium_font = 50


# LaTeX Expressions
latexOne = "$h(x) = f\\hspace{.1cm}[ \\hspace{.1cm}g(x)\\hspace{.1cm}]$"
latexTwo_partOne = "$h\\hspace{.1cm}'(x) = f\\hspace{.1cm}'\\hspace{.1cm}[\\hspace{.1cm}g(x)\\hspace{.1cm}]$"
latexTwo_partTwo = "$\\hspace{.1cm}\\boldsymbol{\\cdot}\\hspace{.2cm}g\\hspace{.1cm}'(x)$"


# Helper Functions
def create_textbox(height, width, color, string):
    result = VGroup()
    box = Rectangle(height = height, width = width, fill_color = color, fill_opacity = 0.9, stroke_color = color)
    text = Text(string).move_to(box.get_center())
    result.add(box, text)
    return result


# Content
class Title(Scene):  
    def construct(self):

        textbox = create_textbox(height = 1, width = 5, color = "#E5C6BB", string = "")
        self.add(textbox)
        textbox.shift(3 * UP + 4 * LEFT)

        titleText = TexText("Chain Rule", font_size = medium_font, color = BLACK)
        self.add(titleText)
        titleText.shift(3 * UP + 5 * LEFT)

class Content(Scene):  
    def construct(self):

        textbox = create_textbox(height = 5, width = 10, color = "#E5C6BB", string = "")
        self.add(textbox)

        textbox.shift(1 * DOWN + 1.5 * LEFT)

class ChainRule(Scene):
    def construct(self):
        
        # h(x) = f[g(x)]
        equationOne = TexText(latexOne, font_size = small_font, color = BLACK)
        equationOne.shift(0.5 * UP + 4 * LEFT)
        
        # h'(x) = f'[g(x)] * g'(x)
        equationTwo_partOne = TexText(latexTwo_partOne, font_size = small_font, color = BLACK)
        equationTwo_partOne.shift(1 * DOWN + 3.7 * LEFT)

        equationTwo_partTwo = TexText(latexTwo_partTwo, font_size = small_font, color = BLACK)
        equationTwo_partTwo.shift(1 * DOWN + 1.1 * LEFT)
        
        self.wait(23)

        self.play(Write(equationOne), run_time = 2)

        self.wait(15)
        
        self.play(Write(equationTwo_partOne), run_time = 1)
        self.play(Write(equationTwo_partTwo), run_time = 1)

        self.wait(10)


# Final Animation
class FinalAnimation(Scene):
    def construct(self):
        Title.construct(self)
        Content.construct(self)
        ChainRule.construct(self)