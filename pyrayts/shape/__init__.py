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
from .. vector  import *
from .. color   import *
from .. shading import *
import math

class uv:
	def __init__(self, u=0, v=0):
		self.u = u
		self.v = v

class shape:
	hitDist = 100000000
	hitPos  = vector()
	shader  = ""
	def classname(self):
		return 'shape'
	def intersect(self):
		pass
	def shading(self):
		pass
	def setShader(self, shd):
		self.shader = shd

class sphere(shape):
	def __init__(self, posv=vector(0,0,0), radiusv=1.0):
		self.pos = posv
		self.radius = radiusv
		self.hitPos = vector()
		self.shader = lambert()
	def intersect(self, eye, nearClip, farClip, isCollision=0):
		xc = eye.pos - self.pos
		xdt = vector.dot(eye.unit,xc)
		de = xdt * xdt - vector.dot(xc,xc) + self.radius *self.radius

		if de < 0:
				
			return 0

		tp = -xdt + math.sqrt(de)
		tm = -xdt - math.sqrt(de)

		tr = 0
		if tp > 0 or tm > 0:
			if tp > 0 and tm > 0:
				if tp < tm:
					tr = tp
				else:
					tr = tm
			elif tp < tm:
				tr = tm
			elif tp > tm:
				tr = tp

			self.hitPos  = eye(tr);
			self.hitDist = tr;
			if tr > nearClip and tr <farClip:
				return 1
		else:
			if isCollision:
				return 1
		return 0

	def shading(self, lights):
		norm = (self.hitPos - self.pos).normalize()
		return self.shader.getDiffuse(lights, norm, self.hitPos)

class particle(shape):
	def __init__(self, posv=vector(0,0,0)):
		self.pos = posv

class plane(shape):
	def __init__(self, y=0, norm=vector(0.0, 1.0, 0.0)):
		self.y = y
		self.normal = norm
	def intersect(self, eye, nearClip, farClip, isCollision=0):
		if eye.unit.y == 0:
			return 0
		if vector.dot(eye.unit.reverse(), self.normal) < 0:
			return 0
		tr = (self.y - eye.pos.y) / eye.unit.y
		if tr <= 0:
			if not isCollision:
				return 0
		self.hitPos  = eye(tr)
		self.hitDist = tr
		if tr > nearClip and tr <farClip:
			return 1
		return 0
	def shading(self, lights):
		return self.shader.getDiffuse(lights, self.normal, self.hitPos)

class polygon3(shape):
	def __init__(self,v0=vector(0,0,0),v1=vector(0,0,0), v2=vector(0,0,0)):
		self.v0=v0
		self.v1=v1
		self.v2=v2
		self.e0 = v1-v0
		self.e1 = v2-v0
		self.uv	= uv()
		self.normal = vector.cross(self.e0, self.e1).normalize()
	def intersect(self, eye, nearClip, farClip, isCollision=0):
		pvec = vector.cross(eye.unit, self.e1)
		det	 = vector.dot(self.e0, pvec)
		tvec = eye.pos - self.v0
		qvec = vector.cross(tvec, self.e0)
		u = vector.dot(tvec,     pvec)
		v = vector.dot(eye.unit, qvec)
		if u < 0 or u   > det:
			return 0
		if v < 0 or u+v > det:
			return 0
		t = vector.dot(self.e1, qvec)
		if t < 0:
			return 0

		det = 1.0/det
		t  *= det
		self.hitPos  = eye(t)
		self.hitDist = t
		if t > nearClip and t <farClip:
			return 1
		return 0
	def shading(self, lights):
		return self.shader.getDiffuse(lights, self.normal, self.hitPos)


class polygon4(polygon3):
	def __init__(self,v0=vector(0,0,0),v1=vector(0,0,0), v2=vector(0,0,0), v3=vector(0,0,0)):
		self.v0=v0
		self.v1=v1
		self.v2=v2
		self.v3=v3
		self.e0 = v1-v0
		self.e1 = v2-v0
		self.e3 = v3-v0
		self.uv	= uv()
		self.normal = (vector.cross(self.e0, self.e1)+vector.cross(self.e0, self.e3)).normalize()
