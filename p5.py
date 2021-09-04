from browser import window as w  # pylint: disable=import-error
from browser import load  # pylint: disable=import-error

load("https://cdn.jsdelivr.net/npm/p5@1.4/lib/p5.min.js")


class P5:
    def createCanvas(self, *arg):
        w.createCanvas(*arg)

    def background(self, *arg):
        w.background(*arg)

    def fill(self, *arg):
        w.fill(*arg)

    def circle(self, *arg):
        w.circle(*arg)

    @property
    def mouseX(self):
        return w.mouseX

    @property
    def mouseY(self):
        return w.mouseY


def export(f):
    w[f.__name__] = f
    return f


p = P5()
