from manimlib import *


# Constants
small_font = 40


# LaTeX Expressions
latexOne = "$$g(x)=sin^7(x^5+4x^4)$$"
latexTwo = "$$=[\\hspace{.05cm}sin(x^5+4x^4)\\hspace{.05cm}]^7$$"
latexThree = "$$g'(x)=7\\hspace{.05cm}[\\hspace{2.2cm}]^6$$"
latexFour = "$$sin(x^5+4x^4)$$"
latexFive = "$$\\boldsymbol{\\cdot}\\hspace{.1cm}cos(x^5+4x^4)$$"
latexSix = "$$\\boldsymbol{\\cdot}\\hspace{.1cm}(5x^4+16x^3)$$"


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

        titleText = TexText("Example 5", font_size = small_font)
        self.add(titleText)
        titleText.shift(3 * UP + 5 * LEFT)


class Content(Scene):  
    def construct(self):

        textboxOne = create_textbox(height = 5, width = 13, color = TEAL_B, string = "")
        self.add(textboxOne)
        textboxOne.shift(1 * DOWN)

        # g(x) = sin^7(x^5 + 4x^4)
        equationOne_partOne = TexText(latexOne, font_size = small_font)
        equationOne_partOne.shift(0.5 * UP + 4 * LEFT)

        equationOne_partTwo = TexText(latexTwo, font_size = small_font)
        equationOne_partTwo.shift(0.5 * UP + 0.3 * LEFT)

        # g'(x) = 7 * sin^6(x^5 + 4x^4) * cos(x^5 + 4x^4) * (5x^4 + 16x^3)
        equationTwo_partOne = TexText(latexThree, font_size = small_font)
        equationTwo_partOne.shift(0.75 * DOWN + 3.6 * LEFT)

        equationTwo_partTwo = TexText(latexFour, font_size = small_font)
        equationTwo_partTwo.shift(0.75 * DOWN + 2.85 * LEFT)

        equationTwo_partThree = TexText(latexFive, font_size = small_font)
        equationTwo_partThree.shift(0.75 * DOWN + 0.2 * RIGHT)

        equationTwo_partFour = TexText(latexSix, font_size = small_font)
        equationTwo_partFour.shift(0.75 * DOWN + 2.9 * RIGHT)

        self.wait(1)

        self.play(Write(equationOne_partOne), run_time = 3)
        self.play(Write(equationOne_partTwo), run_time = 3)

        self.play(Write(equationTwo_partOne), run_time = 3)
        self.play(Write(equationTwo_partTwo), run_time = 3)
        self.play(Write(equationTwo_partThree), run_time = 3)
        self.play(Write(equationTwo_partFour), run_time = 3)
        

# Final Animation
class FinalAnimation(Scene):
    def construct(self):
        Title.construct(self)
        Content.construct(self)