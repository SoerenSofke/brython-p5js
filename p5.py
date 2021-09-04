from browser import window as p, load  # pylint: disable=import-error


class P5:
    def __init__(self):
        load("https://cdn.jsdelivr.net/npm/p5@1.4/lib/p5.min.js")

    def createCanvas(self, *arg):
        p.createCanvas(*arg)

    def background(self, *arg):
        p.background(*arg)

    def fill(self, *arg):
        p.fill(*arg)

    def circle(self, *arg):
        p.circle(*arg)

    @property
    def mouseX(self):
        return p.mouseX

    @property
    def mouseY(self):
        return p.mouseY


def export(f):
    p[f.__name__] = f
    return f
