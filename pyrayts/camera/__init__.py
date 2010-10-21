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
import math
from .. transform import *
from .. vector    import *
from .. color     import *
class camera(transform):
	def __init__(self, **args):
		self.angle  = 35
		self.translate = vector(0,0,-5)
		self.aimPos = vector(0,0,0)
		self.nearClip = 0.001
		self.farClip  = 100000

		self.a = vector()
		self.b = vector()
		self.c = vector()
		self.c_pos = vector()
		self.bg_color = color(0.5,0.5,0.5)
		
		for key, val in args:
			self.__dict__[key] = val
			
	def initAxis(self, width):
		z_vec = (self.aimPos - self.translate).normalize()
		d = width*0.5/math.tan(self.angle*0.5/180*3.141952);
		#d = width*0.5/math.tan(self.angle*0.5);
		self.c_pos  = self.translate + z_vec*d

		dA = math.sqrt(z_vec.x*z_vec.x+z_vec.z*z_vec.z)
		sinA = z_vec.x/dA
		cosA = z_vec.z/dA
		sinB = z_vec.y
		cosB = dA
		sinC = 0
		cosC = 1
		
		self.a.x = cosA*cosC+sinA*sinB*sinC
		self.a.y = cosA*sinC-sinA*sinB*cosC
		self.a.z = sinA*cosB
		self.b.x = sinC*cosB
		self.b.y = cosB*cosC
		self.b.z = sinB
		self.c.x = sinA*cosC-cosA*sinB*sinC
		self.c.y = sinA*sinC+cosA*sinB*cosC
		self.c.z = cosA*cosB

	def axisConv(self, p):
		r = vector()
		r.x =  p.x*self.a.x+p.y*self.a.y+p.z*self.a.z+self.c_pos.x
		r.y = -p.x*self.b.x+p.y*self.b.y+p.z*self.b.z+self.c_pos.y
		r.z = -p.x*self.c.x-p.y*self.c.y+p.z*self.c.z+self.c_pos.z
		return (r - self.translate).normalize()
