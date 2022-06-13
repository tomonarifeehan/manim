from manimlib import *


# Constants
small_font = 40

# LaTeX Expressions
latexOne = "$$g(x) = 4\\hspace{.1cm}\\boldsymbol{\\cdot}\\hspace{.1cm}sin(2x^5)$$"
latexTwo = "$$g\\hspace{.1cm}'(x) = 4\\hspace{.1cm}\\boldsymbol{\\cdot}\\hspace{.1cm}[\\hspace{2.6cm}]$$"
latexThree = "$$cos(2x^5)$$"
latexFour = "$$\\boldsymbol{\\cdot}\\hspace{.1cm}10x^4$$"
latexFive = "$$ = 40\\hspace{.05cm}x^4\\hspace{.05cm}cos(2x^5)$$"


# Helper Functions
def create_textbox(height, width, color, string):
    result = VGroup()
    box = Rectangle(height = height, width = width, fill_color = color, fill_opacity = 0.1, stroke_color = color)
    text = Text(string).move_to(box.get_center())
    result.add(box, text)
    return result

# Content
class Title(Scene):  
    def construct(self):

        # Title Box
        title = create_textbox(height = 1, width = 6, color = TEAL_B, string = "")
        self.add(title)
        title.shift(3 * UP + 3.5 * LEFT)

        titleText = TexText("Example 2", font_size = small_font)
        self.add(titleText)
        titleText.shift(3 * UP + 5 * LEFT)


class Content(Scene):  
    def construct(self):

        textboxOne = create_textbox(height = 5, width = 13, color = TEAL_B, string = "")
        self.add(textboxOne)
        textboxOne.shift(1 * DOWN)

        # g(x) = 4 * sin(2x^5)
        equationOne = TexText(latexOne, font_size = small_font)
        equationOne.shift(0.5 * UP + 4 * LEFT)

        # g'(x) = 4 * cos(2x^5) * 10x^4
        equationTwo_partOne = TexText(latexTwo, font_size = small_font)
        equationTwo_partOne.shift(0.75 * DOWN + 3 * LEFT)

        equationTwo_partTwo = TexText(latexThree, font_size = small_font)
        equationTwo_partTwo.shift(0.75 * DOWN + 2.5  * LEFT)

        equationTwo_partThree = TexText(latexFour, font_size = small_font)
        equationTwo_partThree.shift(0.75 * DOWN + 1.1 * LEFT)

        # g'(x) = 40 * x^4  * cos(2x^5)
        equationThree = TexText(latexFive, font_size = small_font)
        equationThree.shift(1.75 * DOWN + 3.2 * LEFT)

        self.wait(1)

        self.play(Write(equationOne), run_time = 3)
        self.play(Write(equationTwo_partOne), run_time = 3)
        self.play(Write(equationTwo_partTwo), run_time = 3)
        self.play(Write(equationTwo_partThree), run_time = 3)
        self.play(Write(equationThree), run_time = 3)
        
        

# Final Animation
class FinalAnimation(Scene):
    def construct(self):
        Title.construct(self)
        Content.construct(self)