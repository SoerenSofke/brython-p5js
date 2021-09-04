from p5 import P5, export
p5 = P5()


@export
def setup():
    p5.createCanvas(300, 500)
    p5.background(0)


@export
def draw():
    p5.fill(255, 255, 0, 128)
    p5.circle(p5.mouseX, p5.mouseY, 20)


@export
def mousePressed(event):
    p5.background(0)
