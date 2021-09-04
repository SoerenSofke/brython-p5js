from browser import window as p, load

load("https://cdn.jsdelivr.net/npm/p5@1.4/lib/p5.min.js")


def export(f):
    p[f.__name__] = f
    return f


@export
def setup():
    p.createCanvas(400, 400)
    p.background(0)


@export
def draw():
    p.fill(255, 255, 0, 128)
    p.ellipse(p.mouseX, p.mouseY, 50, 50)


@export
def mousePressed(event):
    p.background(0)
