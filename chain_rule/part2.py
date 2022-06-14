from manimlib import *


# Constants
small_font = 40


# LaTeX Expressions
latexOne = "$g(x) = sin(x)$"
latexTwo = "$g\\hspace{.1cm}'(x) = cos(x)$"
latexThree = "$g(x) = sin(f(x))$"
latexFour = "$g\\hspace{.1cm}'(x) = cos(f(x))$"
latexFive = "$\\boldsymbol{\\cdot}\\hspace{.1cm}f\\hspace{.1cm}'(x)$"


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

        # Title 1 Box
        titleOne = create_textbox(height = 1, width = 6, color = "#E5C6BB", string = "")
        self.add(titleOne)
        titleOne.shift(3 * UP + 3.5 * LEFT)

        # Derivative of sin(x)
        titleOneText = TexText("Derivative of $sin(x)$", font_size = small_font, color = BLACK)
        self.add(titleOneText)
        titleOneText.shift(3 * UP + 4.2 * LEFT)

        # Title 2 Box
        titleTwo = create_textbox(height = 1, width = 6, color = "#E5C6BB", string = "")
        self.add(titleTwo)
        titleTwo.shift(3 * UP + 3.5 * RIGHT)

class Content(Scene):  
    def construct(self):
        
        textboxOne = create_textbox(height = 5, width = 6, color = "#E5C6BB", string = "")
        self.add(textboxOne)
        textboxOne.shift(1 * DOWN + 3.5 * LEFT)

        textboxTwo = create_textbox(height = 5, width = 6, color = "#E5C6BB", string = "")
        self.add(textboxTwo)
        textboxTwo.shift(1 * DOWN + 3.5 * RIGHT)

        # g(x) = sin(x)
        equationOne = TexText(latexOne, font_size = small_font, color = BLACK)
        equationOne.shift(0.5 * UP + 4.7 * LEFT)

        # g'(x) = cos(x)
        equationTwo = TexText(latexTwo, font_size = small_font, color = BLACK)
        equationTwo.shift(1 * DOWN + 4.6 * LEFT)

        # Derivative of sin(f(x))
        titleTwoText = TexText("Derivative of $sin(f(x))$", font_size = small_font, color = BLACK)
        titleTwoText.shift(3 * UP + 3 * RIGHT)

        # g(x) = sin(f(x))
        equationThree = TexText(latexThree, font_size = small_font, color = BLACK)
        equationThree.shift(0.5 * UP + 2.6  * RIGHT)

        # g'(x) = cos(f(x)) * f'(x)
        equationFour_partOne = TexText(latexFour, font_size = small_font, color = BLACK)
        equationFour_partOne.shift(1 * DOWN + 2.7  * RIGHT)

        equationFour_partTwo = TexText(latexFive, font_size = small_font, color = BLACK)
        equationFour_partTwo.shift(1 * DOWN + 5.1  * RIGHT)

        self.wait(1)

        self.play(Write(equationOne), run_time = 3)

        self.play(Write(equationTwo), run_time = 3)

        self.play(Write(titleTwoText), run_time = 3)

        self.play(Write(equationThree), run_time = 3)

        self.play(Write(equationFour_partOne), run_time = 3)
        self.play(Write(equationFour_partTwo), run_time = 3)


# Final Animation
class FinalAnimation(Scene):
    def construct(self):
        Title.construct(self)
        Content.construct(self)