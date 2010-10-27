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
	width  = 160 
	height = 120
	#width  = 320 
	#height = 240

	msg.trace("pyrayts render...","{","Start")
	msg.separator()
	msg.trace("image size: %s x %s"%(width, height))
	stTime = time.time()
	
	# Initialize render scene
	renderScene = pyrayts.scene()
	renderScene.setImageBuffer(width, height)

	# render objects
	# create shader

	lmt  = pyrayts.lambert(diffuseColor=pyrayts.color(0.6,0.6,0.98))
	lmtR = pyrayts.lambert(diffuseColor=pyrayts.color(0.7,0.2,0.2))

	# create rendered objects
	#sph  = pyrayts.sphere(pyrayts.vector( 0, 1, 0), 1.0)
	#sph.setShader(lmt)
	#renderScene.append(sph)

	#sph2 = pyrayts.sphere(pyrayts.vector( 0, 1.0, 0), 1.0)
	#sph2.setShader(lmtR)
	#renderScene.append(sph2)

	poly = pyrayts.polygon3( pyrayts.vector(0,1,0),
					 pyrayts.vector(0.7, 0, 0),
					 pyrayts.vector(-0.7, 0, 0))
	poly.setShader(lmtR)
	renderScene.append(poly)

	poly = pyrayts.polygon3( pyrayts.vector(    0, 1.0, 0),
				   pyrayts.vector( 0.7, 0.0, 0.0),
				   pyrayts.vector(-0.7, 0.0, 0.0))
	poly.setShader(lmtR)
	renderScene.append(poly)

	pl = pyrayts.plane(y=0)
	pl.setShader(lmt)
	renderScene.append(pl)
	
	# render lights
	#lit = directionalLight()
	lit = pyrayts.pointLight()
	lit.intencity = 1.0
	lit.translate =  pyrayts.vector(-1.5, 2, -1.5)
	renderScene.append(lit)
	
	# render camera
	cam = pyrayts.camera()
	cam.translate   = pyrayts.vector(0, 1.5, -7.0)
	cam.aimPos      = pyrayts.vector(0, 0.5,    0)
	cam.angle       = 35.0
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
