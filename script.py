from browser import window as p


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
def mousePressed():
    p.background(0)


p.p5.new()
