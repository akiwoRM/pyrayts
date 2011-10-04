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
from .. vector import *

class ray:
	def __init__(self, initPos=vector(0,0,0), initUnit=vector(0,0,0)):
		self.pos  = initPos
		self.unit = initUnit
	def __call__(self, val):
		return self.pos + self.unit*val

	def appendDistance(self, outObjects, addObj):
		for idx, obj in enumerate(outObjects):
			if obj.hitDist < addObj.hitDist:
				outObjects.insert(idx, sddObj)
				return 1
		outObjects.append(addObj)
		return 0

	def intersect(self, objects, near, far, myObject=""):
		d=100000
		hitIdx = -1
		hitPos = vector()
		for idx, obj in enumerate(objects):
			if myObject != obj:
				if obj.intersect(self, near, far):
					if d > obj.hitDist:
						hitIdx = idx
						d      = obj.hitDist
						hitPos = obj.hitPos
		return hitIdx, hitPos

