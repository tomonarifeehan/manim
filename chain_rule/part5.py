from manimlib import *


# Constants
small_font = 40


# LaTeX Expressions
latexOne = "$$g(x) = sin(x^2 + 3x + 4)$$"
latexTwo = "$$g\\hspace{.1cm}'(x) = cos(x^2 + 3x + 4)$$"
latexThree = "$$\\boldsymbol{\\cdot}\\hspace{.1cm}(\\hspace{1.1cm})$$"
latexFour = "$$2x$$"
latexFive = "$$+\\hspace{.1cm}3$$"
latexSix = "$$=2x\\hspace{.1cm}cos(x^2 + 3x + 4)$$"
latexSeven = "$$+\\hspace{.1cm}3\\hspace{.1cm}cos(x^2 + 3x + 4)$$"


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

        titleText = TexText("Example 3", font_size = small_font)
        self.add(titleText)
        titleText.shift(3 * UP + 5 * LEFT)


class Content(Scene):  
    def construct(self):

        textboxOne = create_textbox(height = 5, width = 13, color = TEAL_B, string = "")
        self.add(textboxOne)
        textboxOne.shift(1 * DOWN)

        # g(x) = sin(x^2 + 3x + 4)
        equationOne = TexText(latexOne, font_size = small_font)
        equationOne.shift(0.5 * UP + 4 * LEFT)

        # g'(x) = cos(x^2 + 3x + 4) * (2x + 3)
        equationTwo_partOne = TexText(latexTwo, font_size = small_font)
        equationTwo_partOne.shift(0.75 * DOWN + 3.9 * LEFT)

        equationTwo_partTwo = TexText(latexThree, font_size = small_font)
        equationTwo_partTwo.shift(0.75 * DOWN + 0.7 * LEFT)

        equationTwo_partThree = TexText(latexFour, font_size = small_font)
        equationTwo_partThree.shift(0.75 * DOWN + 0.9 * LEFT)

        equationTwo_partFour = TexText(latexFive, font_size = small_font)
        equationTwo_partFour.shift(0.75 * DOWN + 0.3 * LEFT)

        # g'(x) = 2x * cos(x^2 + 3x + 4) + 3 * cos(x^2 + 3x + 4)
        equationThree_partOne = TexText(latexSix, font_size = small_font)
        equationThree_partOne.shift(1.75 * DOWN + 3.1 * LEFT)

        equationThree_partTwo = TexText(latexSeven, font_size = small_font)
        equationThree_partTwo.shift(1.75 * DOWN + 0.7 * RIGHT)

        self.wait(1)

        self.play(Write(equationOne), run_time = 3)

        self.play(Write(equationTwo_partOne), run_time = 3)
        self.play(Write(equationTwo_partTwo), run_time = 3)
        self.play(Write(equationTwo_partThree), run_time = 3)
        self.play(Write(equationTwo_partFour), run_time = 3)

        self.play(Write(equationThree_partOne), run_time = 3)
        self.play(Write(equationThree_partTwo), run_time = 3)


# Final Animation
class FinalAnimation(Scene):
    def construct(self):
        Title.construct(self)
        Content.construct(self)