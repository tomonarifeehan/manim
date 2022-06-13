from manimlib import *


# Constants
small_font = 40

# LaTeX Expressions
latexOne = "$g(x) = sin(x^3)$"
latexTwo = "$g\\hspace{.1cm}'(x) = cos(x^3)$"
latexThree = "$$\\boldsymbol{\\cdot}\\hspace{.1cm}3x^2$$"
latexFour = "$$ = 3x^2\\boldsymbol{\\cdot}\\hspace{.1cm}cos(x^3)$$"


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

        titleText = TexText("Example 1", font_size = small_font)
        self.add(titleText)
        titleText.shift(3 * UP + 5 * LEFT)


class Content(Scene):  
    def construct(self):

        textboxOne = create_textbox(height = 5, width = 13, color = TEAL_B, string = "")
        self.add(textboxOne)
        textboxOne.shift(1 * DOWN)

        # g(x) = sin(x^3)
        equationOne = TexText(latexOne, font_size = small_font)
        equationOne.shift(0.5 * UP + 4.7 * LEFT)

        # g'(x) = cos(x^3) * 3x^2
        equationTwo = TexText(latexTwo, font_size = small_font)
        equationTwo.shift(1 * DOWN + 4.6 * LEFT)

        equationThree = TexText(latexThree, font_size = small_font)
        equationThree.shift(1 * DOWN + 2.6  * LEFT)

        # = 3x^2 * cos(x^3)
        equationFour = TexText(latexFour, font_size = small_font)
        equationFour.shift(2 * DOWN + 3.5  * LEFT)

        self.wait(1)

        self.play(Write(equationOne), run_time = 3)
        self.play(Write(equationTwo), run_time = 3)
        self.play(Write(equationThree), run_time = 3)
        self.play(Write(equationFour), run_time = 3)
        

# Final Animation
class FinalAnimation(Scene):
    def construct(self):
        Title.construct(self)
        Content.construct(self)