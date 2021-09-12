from browser import window, load  # pylint: disable=import-error

load("https://cdn.jsdelivr.net/npm/p5@1.4/lib/p5.min.js")


class P5:
    # Environment
    def describe(self, *arg):
        return window.describe(*arg)

    def describeElement(self, *arg):
        return window.describeElement(*arg)

    def textOutput(self, *arg):
        return window.textOutput(*arg)

    def gridOutput(self, *arg):
        return window.gridOutput(*arg)

    def print(self, *arg):
        return window.print(*arg)

    @property
    def frameCount(self):
        return window.frameCount

    @property
    def deltaTime(self):
        return window.deltaTime

    @property
    def focused(self):
        return window.focused

    def cursor(self, *arg):
        return window.cursor(*arg)

    def frameRate(self, *arg):
        return window.frameRate(*arg)

    def noCursor(self, *arg):
        return window.noCursor(*arg)

    @property
    def displayWidth(self):
        return window.displayWidth

    @property
    def displayHeight(self):
        return window.displayHeight

    @property
    def windowWidth(self):
        return window.windowWidth

    @property
    def windowHeight(self):
        return window.windowHeight

    def windowResized(self, *arg):
        return window.windowResized(*arg)

    @property
    def width(self):
        return window.width

    @property
    def height(self):
        return window.height

    def fullscreen(self, *arg):
        return window.fullscreen(*arg)

    def pixelDensity(self, *arg):
        return window.pixelDensity(*arg)

    def displayDensity(self, *arg):
        return window.displayDensity(*arg)

    def getURL(self, *arg):
        return window.getURL(*arg)

    def getURLPath(self, *arg):
        return window.getURLPath(*arg)

    def getURLParams(self, *arg):
        return window.getURLParams(*arg)

    # Color
    # Creating & Reading
    def alpha(self, *arg):
        return window.alpha(*arg)

    def blue(self, *arg):
        return window.blue(*arg)

    def brightness(self, *arg):
        return window.brightness(*arg)

    def color(self, *arg):
        return window.color(*arg)

    def green(self, *arg):
        return window.green(*arg)

    def hue(self, *arg):
        return window.hue(*arg)

    def lerpColor(self, *arg):
        return window.lerpColor(*arg)

    def lightness(self, *arg):
        return window.lightness(*arg)

    def red(self, *arg):
        return window.red(*arg)

    def saturation(self, *arg):
        return window.saturation(*arg)

    # Setting
    def background(self, *arg):
        return window.background(*arg)

    def clear(self, *arg):
        return window.clear(*arg)

    def colorMode(self, *arg):
        return window.colorMode(*arg)

    def fill(self, *arg):
        return window.fill(*arg)

    def noFill(self, *arg):
        return window.noFill(*arg)

    def noStroke(self, *arg):
        return window.noStroke(*arg)

    def stroke(self, *arg):
        return window.stroke(*arg)

    def erase(self, *arg):
        return window.erase(*arg)

    def noErase(self, *arg):
        return window.noErase(*arg)

    # Shape
    # 2D Primitives
    def arc(self, *arg):
        return window.arc(*arg)

    def ellipse(self, *arg):
        return window.ellipse(*arg)

    def circle(self, *arg):
        return window.circle(*arg)

    def line(self, *arg):
        return window.line(*arg)

    def point(self, *arg):
        return window.point(*arg)

    def quad(self, *arg):
        return window.quad(*arg)

    def rect(self, *arg):
        return window.rect(*arg)

    def square(self, *arg):
        return window.square(*arg)

    def triangle(self, *arg):
        return window.triangle(*arg)

    # Attributes
    def ellipseMode(self, *arg):
        return window.ellipseMode(*arg)

    def noSmooth(self, *arg):
        return window.noSmooth(*arg)

    def rectMode(self, *arg):
        return window.rectMode(*arg)

    def smooth(self, *arg):
        return window.smooth(*arg)

    def strokeCap(self, *arg):
        return window.strokeCap(*arg)

    def strokeJoin(self, *arg):
        return window.strokeJoin(*arg)

    def strokeWeight(self, *arg):
        return window.strokeWeight(*arg)

    # Curves
    def bezier(self, *arg):
        return window.bezier(*arg)

    def bezierDetail(self, *arg):
        return window.bezierDetail(*arg)

    def bezierPoint(self, *arg):
        return window.bezierPoint(*arg)

    def bezierTangent(self, *arg):
        return window.bezierTangent(*arg)

    def curve(self, *arg):
        return window.curve(*arg)

    def curveDetail(self, *arg):
        return window.curveDetail(*arg)

    def curveTightness(self, *arg):
        return window.curveTightness(*arg)

    def curvePoint(self, *arg):
        return window.curvePoint(*arg)

    def curveTangent(self, *arg):
        return window.curveTangent(*arg)

    # Vertex
    def beginContour(self, *arg):
        return window.beginContour(*arg)

    def beginShape(self, *arg):
        return window.beginShape(*arg)

    def bezierVertex(self, *arg):
        return window.bezierVertex(*arg)

    def curveVertex(self, *arg):
        return window.curveVertex(*arg)

    def endContour(self, *arg):
        return window.endContour(*arg)

    def endShape(self, *arg):
        return window.endShape(*arg)

    def quadraticVertex(self, *arg):
        return window.quadraticVertex(*arg)

    def vertex(self, *arg):
        return window.vertex(*arg)

    def normal(self, *arg):
        return window.normal(*arg)

    # 3D Primitives
    def plane(self, *arg):
        return window.plane(*arg)

    def box(self, *arg):
        return window.box(*arg)

    def sphere(self, *arg):
        return window.sphere(*arg)

    def cylinder(self, *arg):
        return window.cylinder(*arg)

    def cone(self, *arg):
        return window.cone(*arg)

    def ellipsoid(self, *arg):
        return window.ellipsoid(*arg)

    def torus(self, *arg):
        return window.torus(*arg)

    # 3D Models
    def loadModel(self, *arg):
        return window.loadModel(*arg)

    def model(self, *arg):
        return window.model(*arg)

    # Constants
    # HALF_PI
    # PI
    # QUARTER_PI
    # TAU
    # TWO_PI
    # DEGREES
    # RADIANS
    # Structure
    def preload(self, *arg):
        return window.preload(*arg)

    def setup(self, *arg):
        return window.setup(*arg)

    def draw(self, *arg):
        return window.draw(*arg)

    def remove(self, *arg):
        return window.remove(*arg)

    @property
    def disableFriendlyErrors(self):
        return window.disableFriendlyErrors

    def noLoop(self, *arg):
        return window.noLoop(*arg)

    def loop(self, *arg):
        return window.loop(*arg)

    def isLooping(self, *arg):
        return window.isLooping(*arg)

    def push(self, *arg):
        return window.push(*arg)

    def pop(self, *arg):
        return window.pop(*arg)

    def redraw(self, *arg):
        return window.redraw(*arg)

    def p5(self, *arg):
        return window.p5(*arg)

    # DOM
    def select(self, *arg):
        return window.select(*arg)

    def selectAll(self, *arg):
        return window.selectAll(*arg)

    def removeElements(self, *arg):
        return window.removeElements(*arg)

    def changed(self, *arg):
        return window.changed(*arg)

    def input(self, *arg):
        return window.input(*arg)

    def createDiv(self, *arg):
        return window.createDiv(*arg)

    def createP(self, *arg):
        return window.createP(*arg)

    def createSpan(self, *arg):
        return window.createSpan(*arg)

    def createImg(self, *arg):
        return window.createImg(*arg)

    def createA(self, *arg):
        return window.createA(*arg)

    def createSlider(self, *arg):
        return window.createSlider(*arg)

    def createButton(self, *arg):
        return window.createButton(*arg)

    def createCheckbox(self, *arg):
        return window.createCheckbox(*arg)

    def createSelect(self, *arg):
        return window.createSelect(*arg)

    def createRadio(self, *arg):
        return window.createRadio(*arg)

    def createColorPicker(self, *arg):
        return window.createColorPicker(*arg)

    def createInput(self, *arg):
        return window.createInput(*arg)

    def createFileInput(self, *arg):
        return window.createFileInput(*arg)

    def createVideo(self, *arg):
        return window.createVideo(*arg)

    def createAudio(self, *arg):
        return window.createAudio(*arg)

    # VIDEO
    # AUDIO
    def createCapture(self, *arg):
        return window.createCapture(*arg)

    def createElement(self, *arg):
        return window.createElement(*arg)

    # Rendering
    def createCanvas(self, *arg):
        return window.createCanvas(*arg)

    def resizeCanvas(self, *arg):
        return window.resizeCanvas(*arg)

    def noCanvas(self, *arg):
        return window.noCanvas(*arg)

    def createGraphics(self, *arg):
        return window.createGraphics(*arg)

    def blendMode(self, *arg):
        return window.blendMode(*arg)

    @property
    def drawingContext(self):
        return window.drawingContext

    def setAttributes(self, *arg):
        return window.setAttributes(*arg)

    # Foundation
    @property
    def let(self):
        return window.let

    @property
    def const(self):
        return window.const

    # ===
    # >
    # >=
    # <
    # <=

    # JSON
    @property
    def console(self):
        return window.console

    # Transform
    def applyMatrix(self, *arg):
        return window.applyMatrix(*arg)

    def resetMatrix(self, *arg):
        return window.resetMatrix(*arg)

    def rotate(self, *arg):
        return window.rotate(*arg)

    def rotateX(self, *arg):
        return window.rotateX(*arg)

    def rotateY(self, *arg):
        return window.rotateY(*arg)

    def rotateZ(self, *arg):
        return window.rotateZ(*arg)

    def scale(self, *arg):
        return window.scale(*arg)

    def shearX(self, *arg):
        return window.shearX(*arg)

    def shearY(self, *arg):
        return window.shearY(*arg)

    def translate(self, *arg):
        return window.translate(*arg)

    # Data
    # LocalStorage
    def storeItem(self, *arg):
        return window.storeItem(*arg)

    def getItem(self, *arg):
        return window.getItem(*arg)

    def clearStorage(self, *arg):
        return window.clearStorage(*arg)

    def removeItem(self, *arg):
        return window.removeItem(*arg)

    # Dictionary
    def createStringDict(self, *arg):
        return window.createStringDict(*arg)

    def createNumberDict(self, *arg):
        return window.createNumberDict(*arg)

    # Array Functions
    def append(self, *arg):
        return window.append(*arg)

    def arrayCopy(self, *arg):
        return window.arrayCopy(*arg)

    def concat(self, *arg):
        return window.concat(*arg)

    def reverse(self, *arg):
        return window.reverse(*arg)

    def shorten(self, *arg):
        return window.shorten(*arg)

    def shuffle(self, *arg):
        return window.shuffle(*arg)

    def sort(self, *arg):
        return window.sort(*arg)

    def splice(self, *arg):
        return window.splice(*arg)

    def subset(self, *arg):
        return window.subset(*arg)

    # Conversion
    def float(self, *arg):
        return window.float(*arg)

    def int(self, *arg):
        return window.int(*arg)

    def str(self, *arg):
        return window.str(*arg)

    def boolean(self, *arg):
        return window.boolean(*arg)

    def byte(self, *arg):
        return window.byte(*arg)

    def char(self, *arg):
        return window.char(*arg)

    def unchar(self, *arg):
        return window.unchar(*arg)

    def hex(self, *arg):
        return window.hex(*arg)

    def unhex(self, *arg):
        return window.unhex(*arg)

    # String Functions
    def join(self, *arg):
        return window.join(*arg)

    def match(self, *arg):
        return window.match(*arg)

    def matchAll(self, *arg):
        return window.matchAll(*arg)

    def nf(self, *arg):
        return window.nf(*arg)

    def nfc(self, *arg):
        return window.nfc(*arg)

    def nfp(self, *arg):
        return window.nfp(*arg)

    def nfs(self, *arg):
        return window.nfs(*arg)

    def split(self, *arg):
        return window.split(*arg)

    def splitTokens(self, *arg):
        return window.splitTokens(*arg)

    def trim(self, *arg):
        return window.trim(*arg)

    # Events
    # Acceleration
    @property
    def deviceOrientation(self):
        return window.deviceOrientation

    @property
    def accelerationX(self):
        return window.accelerationX

    @property
    def accelerationY(self):
        return window.accelerationY

    @property
    def accelerationZ(self):
        return window.accelerationZ

    @property
    def pAccelerationX(self):
        return window.pAccelerationX

    @property
    def pAccelerationY(self):
        return window.pAccelerationY

    @property
    def pAccelerationZ(self):
        return window.pAccelerationZ

    @property
    def rotationX(self):
        return window.rotationX

    @property
    def rotationY(self):
        return window.rotationY

    @property
    def rotationZ(self):
        return window.rotationZ

    @property
    def pRotationX(self):
        return window.pRotationX

    @property
    def pRotationY(self):
        return window.pRotationY

    @property
    def pRotationZ(self):
        return window.pRotationZ

    @property
    def turnAxis(self):
        return window.turnAxis

    def setMoveThreshold(self, *arg):
        return window.setMoveThreshold(*arg)

    def setShakeThreshold(self, *arg):
        return window.setShakeThreshold(*arg)

    def deviceMoved(self, *arg):
        return window.deviceMoved(*arg)

    def deviceTurned(self, *arg):
        return window.deviceTurned(*arg)

    def deviceShaken(self, *arg):
        return window.deviceShaken(*arg)

    # Keyboard
    @property
    def keyIsPressed(self):
        return window.keyIsPressed

    @property
    def key(self):
        return window.key

    @property
    def keyCode(self):
        return window.keyCode

    def keyPressed(self, *arg):
        return window.keyPressed(*arg)

    def keyReleased(self, *arg):
        return window.keyReleased(*arg)

    def keyTyped(self, *arg):
        return window.keyTyped(*arg)

    def keyIsDown(self, *arg):
        return window.keyIsDown(*arg)

    # Mouse
    @property
    def movedX(self):
        return window.movedX

    @property
    def movedY(self):
        return window.movedY

    @property
    def mouseX(self):
        return window.mouseX

    @property
    def mouseY(self):
        return window.mouseY

    @property
    def pmouseX(self):
        return window.pmouseX

    @property
    def pmouseY(self):
        return window.pmouseY

    @property
    def winMouseX(self):
        return window.winMouseX

    @property
    def winMouseY(self):
        return window.winMouseY

    @property
    def pwinMouseX(self):
        return window.pwinMouseX

    @property
    def pwinMouseY(self):
        return window.pwinMouseY

    @property
    def mouseButton(self):
        return window.mouseButton

    @property
    def mouseIsPressed(self):
        return window.mouseIsPressed

    def mouseMoved(self, *arg):
        return window.mouseMoved(*arg)

    def mouseDragged(self, *arg):
        return window.mouseDragged(*arg)

    def mousePressed(self, *arg):
        return window.mousePressed(*arg)

    def mouseReleased(self, *arg):
        return window.mouseReleased(*arg)

    def mouseClicked(self, *arg):
        return window.mouseClicked(*arg)

    def doubleClicked(self, *arg):
        return window.doubleClicked(*arg)

    def mouseWheel(self, *arg):
        return window.mouseWheel(*arg)

    def requestPointerLock(self, *arg):
        return window.requestPointerLock(*arg)

    def exitPointerLock(self, *arg):
        return window.exitPointerLock(*arg)

    # Touch
    @property
    def touches(self):
        return window.touches

    def touchStarted(self, *arg):
        return window.touchStarted(*arg)

    def touchMoved(self, *arg):
        return window.touchMoved(*arg)

    def touchEnded(self, *arg):
        return window.touchEnded(*arg)

    # Image
    def createImage(self, *arg):
        return window.createImage(*arg)

    def saveCanvas(self, *arg):
        return window.saveCanvas(*arg)

    def saveFrames(self, *arg):
        return window.saveFrames(*arg)

    # Loading & Displaying
    def loadImage(self, *arg):
        return window.loadImage(*arg)

    def image(self, *arg):
        return window.image(*arg)

    def tint(self, *arg):
        return window.tint(*arg)

    def noTint(self, *arg):
        return window.noTint(*arg)

    def imageMode(self, *arg):
        return window.imageMode(*arg)

    # Pixels
    @property
    def pixels(self):
        return window.pixels

    def blend(self, *arg):
        return window.blend(*arg)

    def copy(self, *arg):
        return window.copy(*arg)

    def filter(self, *arg):
        return window.filter(*arg)

    def get(self, *arg):
        return window.get(*arg)

    def loadPixels(self, *arg):
        return window.loadPixels(*arg)

    def set(self, *arg):
        return window.set(*arg)

    def updatePixels(self, *arg):
        return window.updatePixels(*arg)

    # IO
    # Input
    def loadJSON(self, *arg):
        return window.loadJSON(*arg)

    def loadStrings(self, *arg):
        return window.loadStrings(*arg)

    def loadTable(self, *arg):
        return window.loadTable(*arg)

    def loadXML(self, *arg):
        return window.loadXML(*arg)

    def loadBytes(self, *arg):
        return window.loadBytes(*arg)

    def httpGet(self, *arg):
        return window.httpGet(*arg)

    def httpPost(self, *arg):
        return window.httpPost(*arg)

    def httpDo(self, *arg):
        return window.httpDo(*arg)

    # Output
    def createWriter(self, *arg):
        return window.createWriter(*arg)

    def save(self, *arg):
        return window.save(*arg)

    def saveJSON(self, *arg):
        return window.saveJSON(*arg)

    def saveStrings(self, *arg):
        return window.saveStrings(*arg)

    def saveTable(self, *arg):
        return window.saveTable(*arg)

    # Table
    # Time & Date
    def day(self, *arg):
        return window.day(*arg)

    def hour(self, *arg):
        return window.hour(*arg)

    def minute(self, *arg):
        return window.minute(*arg)

    def millis(self, *arg):
        return window.millis(*arg)

    def month(self, *arg):
        return window.month(*arg)

    def second(self, *arg):
        return window.second(*arg)

    def year(self, *arg):
        return window.year(*arg)

    # Math
    # Calculation
    def abs(self, *arg):
        return window.abs(*arg)

    def ceil(self, *arg):
        return window.ceil(*arg)

    def constrain(self, *arg):
        return window.constrain(*arg)

    def dist(self, *arg):
        return window.dist(*arg)

    def exp(self, *arg):
        return window.exp(*arg)

    def floor(self, *arg):
        return window.floor(*arg)

    def lerp(self, *arg):
        return window.lerp(*arg)

    def log(self, *arg):
        return window.log(*arg)

    def mag(self, *arg):
        return window.mag(*arg)

    def map(self, *arg):
        return window.map(*arg)

    def max(self, *arg):
        return window.max(*arg)

    def min(self, *arg):
        return window.min(*arg)

    def norm(self, *arg):
        return window.norm(*arg)

    def pow(self, *arg):
        return window.pow(*arg)

    def round(self, *arg):
        return window.round(*arg)

    def sq(self, *arg):
        return window.sq(*arg)

    def sqrt(self, *arg):
        return window.sqrt(*arg)

    def fract(self, *arg):
        return window.fract(*arg)

    # Vector
    def createVector(self, *arg):
        return window.createVector(*arg)

    # Noise
    def noise(self, *arg):
        return window.noise(*arg)

    def noiseDetail(self, *arg):
        return window.noiseDetail(*arg)

    def noiseSeed(self, *arg):
        return window.noiseSeed(*arg)

    # Random
    def randomSeed(self, *arg):
        return window.randomSeed(*arg)

    def random(self, *arg):
        return window.random(*arg)

    def randomGaussian(self, *arg):
        return window.randomGaussian(*arg)

    # Trigonometry
    def acos(self, *arg):
        return window.acos(*arg)

    def asin(self, *arg):
        return window.asin(*arg)

    def atan(self, *arg):
        return window.atan(*arg)

    def atan2(self, *arg):
        return window.atan2(*arg)

    def cos(self, *arg):
        return window.cos(*arg)

    def sin(self, *arg):
        return window.sin(*arg)

    def tan(self, *arg):
        return window.tan(*arg)

    def degrees(self, *arg):
        return window.degrees(*arg)

    def radians(self, *arg):
        return window.radians(*arg)

    def angleMode(self, *arg):
        return window.angleMode(*arg)

    # Typography
    # Attributes
    def textAlign(self, *arg):
        return window.textAlign(*arg)

    def textLeading(self, *arg):
        return window.textLeading(*arg)

    def textSize(self, *arg):
        return window.textSize(*arg)

    def textStyle(self, *arg):
        return window.textStyle(*arg)

    def textWidth(self, *arg):
        return window.textWidth(*arg)

    def textAscent(self, *arg):
        return window.textAscent(*arg)

    def textDescent(self, *arg):
        return window.textDescent(*arg)

    def textWrap(self, *arg):
        return window.textWrap(*arg)

    # Loading & Displaying
    def loadFont(self, *arg):
        return window.loadFont(*arg)

    def text(self, *arg):
        return window.text(*arg)

    def textFont(self, *arg):
        return window.textFont(*arg)

    # Lights, Camera
    # Interaction
    def orbitControl(self, *arg):
        return window.orbitControl(*arg)

    def debugMode(self, *arg):
        return window.debugMode(*arg)

    def noDebugMode(self, *arg):
        return window.noDebugMode(*arg)

    # Lights
    def ambientLight(self, *arg):
        return window.ambientLight(*arg)

    def specularColor(self, *arg):
        return window.specularColor(*arg)

    def directionalLight(self, *arg):
        return window.directionalLight(*arg)

    def pointLight(self, *arg):
        return window.pointLight(*arg)

    def lights(self, *arg):
        return window.lights(*arg)

    def lightFalloff(self, *arg):
        return window.lightFalloff(*arg)

    def spotLight(self, *arg):
        return window.spotLight(*arg)

    def noLights(self, *arg):
        return window.noLights(*arg)

    # Material
    def loadShader(self, *arg):
        return window.loadShader(*arg)

    def createShader(self, *arg):
        return window.createShader(*arg)

    def shader(self, *arg):
        return window.shader(*arg)

    def resetShader(self, *arg):
        return window.resetShader(*arg)

    def texture(self, *arg):
        return window.texture(*arg)

    def textureMode(self, *arg):
        return window.textureMode(*arg)

    def textureWrap(self, *arg):
        return window.textureWrap(*arg)

    def normalMaterial(self, *arg):
        return window.normalMaterial(*arg)

    def ambientMaterial(self, *arg):
        return window.ambientMaterial(*arg)

    def emissiveMaterial(self, *arg):
        return window.emissiveMaterial(*arg)

    def specularMaterial(self, *arg):
        return window.specularMaterial(*arg)

    def shininess(self, *arg):
        return window.shininess(*arg)

    # Camera
    def camera(self, *arg):
        return window.camera(*arg)

    def perspective(self, *arg):
        return window.perspective(*arg)

    def ortho(self, *arg):
        return window.ortho(*arg)

    def frustum(self, *arg):
        return window.frustum(*arg)

    def createCamera(self, *arg):
        return window.createCamera(*arg)

    def setCamera(self, *arg):
        return window.setCamera(*arg)


def export(f):
    window[f.__name__] = f
    return f


p5 = P5()
