from browser import window, load  # pylint: disable=import-error

load("https://cdn.jsdelivr.net/npm/p5@1.4/lib/p5.min.js")


class P5:
    def createCanvas(self, *arg):
        window.createCanvas(*arg)

    def background(self, *arg):
        window.background(*arg)

    def fill(self, *arg):
        window.fill(*arg)

    def circle(self, *arg):
        window.circle(*arg)

    @property
    def mouseX(self):
        return window.mouseX

    @property
    def mouseY(self):
        return window.mouseY


def export(f):
    window[f.__name__] = f
    return f


p5 = P5()
