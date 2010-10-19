Pyrayts
=============

Pyrayts is ray tracer package by python.

System require
-------

* OS on intel CPU(powerPC not supported)
* python 2.5 or later


Installation
-------

Move "pyrayts" folder into PYTHONPATH.


How to use
------------

if you want to try soon, you can test rendering by next command.

    python main.py

 pyrayts module way
you analyze in 'main.py'
Flow

1. import pyrayts package and create scene instance.

    import pyrayts
    renderScene = pyrayts.scene()

2. set output image buffer in the scene instance.

    renderScene.setImageBuffer(320, 240)

3. add camera object ,light object and shape object in the scene instance.
(require minimum these 3 objects)

    cam = pyrayts.camera()
    lit = pyrayts.directionalLight()
    shp = pyrayts.sphere()
    renderScene.setCamera(cam)
    renderScene.append(lit)
    renderScene.append(shp)

4. execurate render method

    renderScene.render()

5. export rendered image. (only BMP format)

    import pyrayts.bmpLib 
    outbmp = pyrayts.bmpLib.bmpLib(o"./test.bmp", 320, 240)
    outbmp.save(renderScene.imageBuffer)
