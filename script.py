from p5 import p, export


@export
def setup():
    p.createCanvas(300, 500)
    p.background(0)


@export
def draw():
    p.fill(255, 255, 0, 128)
    p.circle(p.mouseX, p.mouseY, 20)


@export
def mousePressed(event):
    p.background(0)
