from manimlib import *


# LaTeX Expressions
latexOne = "$h(x) = f\\hspace{.1cm}[ \\hspace{.2cm}g(x)\\hspace{.2cm}]$"
latexTwo_partOne = "$h\\hspace{.1cm}'(x) = f\\hspace{.1cm}'\\hspace{.1cm}[\\hspace{.2cm}g(x)\\hspace{.2cm}]$"
latexTwo_partTwo = "$\\hspace{.1cm}\\boldsymbol{\\cdot}\\hspace{.2cm}g\\hspace{.1cm}'(x)$"


# Helper Functions
def create_textbox(height, width, color, string):
    result = VGroup()
    box = Rectangle(height = height, width = width, fill_color = color, fill_opacity = 0.5, stroke_color = color)
    text = Text(string).move_to(box.get_center())
    result.add(box, text)
    return result


# Content
class Title(Scene):  
    def construct(self):

        textbox = create_textbox(height = 1, width = 5, color = TEAL_B, string = " Chain Rule ")
        self.add(textbox)

        textbox.shift(3 * UP + 4 * LEFT)

class Content(Scene):  
    def construct(self):

        textbox = create_textbox(height = 5, width = 10, color = TEAL_B, string = "")
        self.add(textbox)

        textbox.shift(1 * DOWN + 1.5 * LEFT)

class ChainRule(Scene):
    def construct(self):
        
        # h(x) = f[g(x)]
        equationOne = TexText(latexOne, font_size = 40)
        equationOne.shift(0.5 * UP + 4 * LEFT)
        
        # h'(x) = f'[g(x)] * g'(x)
        equationTwo_partOne = TexText(latexTwo_partOne, font_size = 40)
        equationTwo_partOne.shift(1 * DOWN + 3.7 * LEFT)

        equationTwo_partTwo = TexText(latexTwo_partTwo, font_size = 40)
        equationTwo_partTwo.shift(1 * DOWN + 1.1 * LEFT)
        
        self.wait(1)

        self.play(Write(equationOne), run_time = 3)
        self.wait(2)
        
        self.play(Write(equationTwo_partOne), run_time = 3)
        self.wait(1)

        self.play(Write(equationTwo_partTwo), run_time = 1)
        self.wait(5)


# Final Animation
class FinalAnimation(Scene):
    def construct(self):

        self.camera.background_color = WHITE

        Title.construct(self)
        Content.construct(self)
        ChainRule.construct(self)