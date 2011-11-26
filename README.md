Pyrayts
=============

Pyrayts is ray tracer package by python.

Code license
-------

New BSD License

System require
-------

* OS on intel CPU(powerPC not supported)
* python 2.5 or later
* wxPython (if you use preview function)
* pypy (if you wanna rendering more faster)

Installation
-------

Move "pyrayts" folder into PYTHONPATH.


How to use
------------

if you want to try soon, you can execurate test rendering by next command.

    python main.py

General procedure of using pyrayts as python module is described below:

1. import pyrayts package and create scene instance.

        import pyrayts
        renderScene = pyrayts.scene()

2. set output image buffer in the scene instance and define image size(width and height).

        renderScene.setImageBuffer(width=320, height=240)

3. add camera object ,light object ,shape object and shader object in the scene instance.
(require minimum 4 objects)

        cam = pyrayts.camera()
        lit = pyrayts.directionalLight()
        shp = pyrayts.sphere()
        lmb = pyrayts.lambert()
        shp.setShader(lmb)
        renderScene.setCamera(cam)
        renderScene.append(lit)
        renderScene.append(shp)

4. execurate render method

        renderScene.render()

    if you want to check rendered image, you can use preview method.(wxPython module required)

        renderScene.preview()

5. export rendered image. (only BMP format)

        import pyrayts.bmpLib 
        outbmp = pyrayts.bmpLib.bmpLib("./test.bmp", 320, 240)
        outbmp.save(renderScene.imageBuffer)

if you want to know more, analyze in 'main.py'
