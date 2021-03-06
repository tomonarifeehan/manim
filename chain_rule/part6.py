from manimlib import *


# Constants
small_font = 40


# LaTeX Expressions
latexOne = "$$g(x) = sin^3(x)$$"
latexTwo = "$$=[\\hspace{.05cm}sin(x)\\hspace{.05cm}]^3$$"
latexThree = "$$g\\hspace{.1cm}'(x) = 3\\hspace{.05cm}[\\hspace{.05cm}sin(x)\\hspace{.05cm}]^2$$"
latexFour = "$$\\boldsymbol{\\cdot}\\hspace{.1cm}cos(x)$$"
latexFive = "$$= 3\\hspace{.1cm}sin^2(x)\\hspace{.05cm}cos(x)$$"


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

        # Title Box
        title = create_textbox(height = 1, width = 6, color = "#E5C6BB", string = "")
        self.add(title)
        title.shift(3 * UP + 3.5 * LEFT)

        titleText = TexText("Example 4", font_size = small_font, color = BLACK)
        self.add(titleText)
        titleText.shift(3 * UP + 5 * LEFT)


class Content(Scene):  
    def construct(self):

        textboxOne = create_textbox(height = 5, width = 13, color = "#E5C6BB", string = "")
        self.add(textboxOne)
        textboxOne.shift(1 * DOWN)

        # g(x) = sin^3(x)
        equationOne_partOne = TexText(latexOne, font_size = small_font, color = BLACK)
        equationOne_partOne.shift(0.5 * UP + 4.6 * LEFT)

        equationOne_partTwo = TexText(latexTwo, font_size = small_font, color = BLACK)
        equationOne_partTwo.shift(0.5 * UP + 2.2 * LEFT)

        # g'(x) = 3 * sin^2(x) * cos(x)
        equationTwo_partOne = TexText(latexThree, font_size = small_font, color = BLACK)
        equationTwo_partOne.shift(0.75 * DOWN + 4.2 * LEFT)

        equationTwo_partTwo = TexText(latexFour, font_size = small_font, color = BLACK)
        equationTwo_partTwo.shift(0.75 * DOWN + 1.7 * LEFT)

        equationThree = TexText(latexFive, font_size = small_font, color = BLACK)
        equationThree.shift(1.75 * DOWN + 3.2 * LEFT)

        self.wait(1)

        self.play(Write(equationOne_partOne), run_time = 3)
        self.play(Write(equationOne_partTwo), run_time = 3)

        self.play(Write(equationTwo_partOne), run_time = 3)
        self.play(Write(equationTwo_partTwo), run_time = 3)

        self.play(Write(equationThree), run_time = 3)
        

# Final Animation
class FinalAnimation(Scene):
    def construct(self):
        Title.construct(self)
        Content.construct(self)