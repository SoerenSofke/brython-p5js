from browser import window

def sketch(p):

    def setup():
        p.createCanvas(400, 400)
        p.background(0)
    
    def draw():
        p.fill(255,255,0,128)
        p.ellipse(p.mouseX, p.mouseY, 50, 50)
    
    def mousePressed():
        p.background(0)
    
    p.setup = setup
    p.draw = draw
    p.mousePressed = mousePressed

myp5 = window.p5.new(sketch)
