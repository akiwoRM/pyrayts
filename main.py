# -*- coding: utf-8 -*-
#
# Copyright (c) 2010, Tatsuya Akagi
# All rights reserved.
#
# Redistribution and use in source and binary forms,
# with or without modification,
# are permitted provided that the following conditions are met:
#
#  * Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
#  * Neither the name of the RedM Studio nor the names of its contributors may be used to endorse
#    or promote products derived from this software without specific prior written permission.
#
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES,
# INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
# IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY,
# OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
import pyrayts
import pyrayts.bmpLib as bl
import pyrayts.tools.statistics
import time

def main():
	msg = pyrayts.tools.statistics.statistics()
	outputFile = "./test.bmp"

	# Initialize output images
	#width  = 160
	#height = 120
	width  = 320
	height = 240

	msg.trace("pyrayts render...","{","Start")
	msg.separator()
	msg.trace("image size: %s x %s"%(width, height))
	stTime = time.time()

	# Initialize render scene
	renderScene = pyrayts.scene()
	renderScene.setImageBuffer(width, height)

	# render objects
	# create shader

	sphereShader  = pyrayts.lambert(diffuseColor=pyrayts.color(0.6,0.6,0.98))
	lmtGray = pyrayts.lambert(diffuseColor=pyrayts.color(0.95,0.95,0.95))
	lmtR = pyrayts.lambert(diffuseColor=pyrayts.color(0.85,0.1,0.1))
	lmtG = pyrayts.lambert(diffuseColor=pyrayts.color(0.2,0.7,0.2))

	# create rendered objects
	sph  = pyrayts.sphere(pyrayts.vector( 0, 0.5, 0), 0.5)
	sph.setShader(sphereShader)
	renderScene.append(sph)

	#sph2 = pyrayts.sphere(pyrayts.vector( 0, 1.0, 0), 1.0)
	#sph2.setShader(lmtR)
	#renderScene.append(sph2)

	polyFront1 = pyrayts.polygon3( pyrayts.vector(1,2,1),
					 pyrayts.vector(1, 0, 1),
					 pyrayts.vector(-1,  0, 1))
	polyFront1.setShader(lmtGray)
	renderScene.append(polyFront1)

	polyFront2 = pyrayts.polygon3( pyrayts.vector(-1, 2, 1),
				   pyrayts.vector( 1, 2, 1),
				   pyrayts.vector(-1, 0, 1))
	polyFront2.setShader(lmtGray)
	renderScene.append(polyFront2)

	polyTop1 = pyrayts.polygon3( pyrayts.vector(1,2,-1),
					 pyrayts.vector(1, 2, 1),
					 pyrayts.vector(-1,  2, 1))
	polyTop1.setShader(lmtGray)
	renderScene.append(polyTop1)

	polyTop2 = pyrayts.polygon3( pyrayts.vector(-1, 2, 1),
				   pyrayts.vector( -1, 2, -1),
				   pyrayts.vector( 1, 2, -1))
	polyTop2.setShader(lmtGray)
	renderScene.append(polyTop2)

	polyLeft1 = pyrayts.polygon3( pyrayts.vector(1,2,1),
					 pyrayts.vector(1, 2, -1),
					 pyrayts.vector(1, 0, -1))
	polyLeft1.setShader(lmtG)
	renderScene.append(polyLeft1)

	polyLeft2 = pyrayts.polygon3( pyrayts.vector(1, 2, 1),
				   pyrayts.vector( 1, 0, -1),
				   pyrayts.vector( 1, 0, 1))
	polyLeft2.setShader(lmtG)
	renderScene.append(polyLeft2)

	polyRight1 = pyrayts.polygon3( pyrayts.vector(-1,2,1),
					 pyrayts.vector(-1, 0, -1),
					 pyrayts.vector(-1, 2, -1))
	polyRight1.setShader(lmtR)
	renderScene.append(polyRight1)

	polyRight2 = pyrayts.polygon3( pyrayts.vector(-1, 2, 1),
				   pyrayts.vector( -1, 0, 1),
				   pyrayts.vector( -1, 0, -1))
	polyRight2.setShader(lmtR)
	renderScene.append(polyRight2)

	pl = pyrayts.plane(y=0)
	pl.setShader(lmtGray)
	renderScene.append(pl)

	#plTop = pyrayts.plane(y=2, norm=pyrayts.vector(0, -1, 0))
	#plTop.setShader(lmtGray)
	#renderScene.append(plTop)

	# render lights
	#lit = directionalLight()
	lit = pyrayts.pointLight()
	lit.intencity = 0.75
	lit.isShadow  = True
	lit.translate =  pyrayts.vector(-0.5, 1.2, -0.7)
	renderScene.append(lit)

	"""
	lit2 = pyrayts.directionalLight()
	lit.intencity = 0.5
	lit2.isShadow  = False
	renderScene.append(lit2)
	"""

	# render camera
	cam = pyrayts.camera()
	cam.translate   = pyrayts.vector(0, 1.0, -4.0)
	cam.aimPos      = pyrayts.vector(0, 1.0,    0)
	cam.angle       = 50.0
	renderScene.setCamera(cam)

	renderScene.render()

	edTime = time.time()
	msg.trace("Render Time : %.6ss"%(edTime - stTime))

	# create preview window
	if not renderScene.preview():
		msg.trace("Don't use preview function for nothing 'wx' module.", "=","Warning")

	# output bmp File
	outbmp = bl.bmpLib(outputFile, width, height)
	outbmp.save(renderScene.imageBuffer)

	msg.separator()
	msg.trace("pyrayts render","}","Finish")
	msg.trace("output image:"+outputFile)

if __name__ == "__main__":
	main()
