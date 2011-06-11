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
from light     import *
from vector    import *
from color     import *
from camera    import *
from shape     import *
from shading   import *
from ray       import *
from baseImage import *

try:
	import wx
	from preview import *
except:
	WXPYTHON = False
else:
	WXPYTHON = True

class scene:
	def __init__(self):
		self.width   = 320
		self.height  = 240
		self.objects = []
		self.lights  = []
		self.camera  = camera()
		self.bgCol   = color()

	def append(self, obj):
		if   obj.classname()=='shape':
			self.objects.append(obj)
		elif obj.classname()=='light':
			self.lights.append(obj)

	def setColor(self, i, j):
		camUnit = self.camera.axisConv(vector(i-self.imageBuffer.width*0.5, self.imageBuffer.height*0.5 - j,0))
		eye = ray(self.camera.translate, camUnit)

		hitIdx, hitPos = eye.intersect(self.objects, self.camera.nearClip, self.camera.farClip )
		
		if hitIdx != -1:
			shadowFlag = 0
			for lt in self.lights:
				if not lt.isShadow:
					continue
				shadow_eye = ray(hitPos, (lt.translate-hitPos).normalize())
				shadowRet = shadow_eye.intersect(self.objects, 0, 200, self.objects[hitIdx])
				if shadowRet[0] != -1:
					self.imageBuffer.setColor(i, j, color(0,0,0))
					shadowFlag = 1
					break
			if not shadowFlag:
				self.imageBuffer.setColor(i, j, self.objects[hitIdx].shading(self.lights))
		else:
			self.imageBuffer.setColor(i, j, self.bgCol)

	def setCamera(self, cam):
		self.camera = cam 
		self.camera.initAxis(self.imageBuffer.width)
		self.bgCol = cam.bg_color;

	def setImageBuffer(self, width, height):
		self.imageBuffer = baseImage(width, height)
		self.width  = width
		self.height = height

	def render(self):
		for j in range(self.height):
			for i in range(self.width):
				self.setColor(i, j)
	def preview(self):	
		if WXPYTHON:
			app   = wx.App(False)
			frame = PreviewWindow(None, -1, "Render Preview", self.imageBuffer)
			frame.Show(True)
			app.MainLoop()
		else:
			return 0
		return 1
