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

class vector:
	def __init__(self, *argv):
		if argv == ():
			self.x = 0
			self.y = 0
			self.z = 0
		else:
			self.x = argv[0]
			self.y = argv[1]
			self.z = argv[2]
		self.d = 0
	def __add__(self, vec):
		return vector(self.x + vec.x, self.y + vec.y, self.z + vec.z)
	def __sub__(self, vec):
		return vector(self.x - vec.x, self.y - vec.y, self.z - vec.z)
	def __mul__(self, vec):
		if type(vec) == type(vector()):
			return vector(self.x * vec.x, self.y * vec.y, self.z * vec.z)
		else:
			return vector(self.x * vec, self.y * vec, self.z * vec)
	def length(self):
		self.d = math.sqrt(self.x*self.x+self.y*self.y+self.z*self.z)
		return self.d
	def reverse(self):
		return vector(self.x*-1, self.y*-1, self.z*-1)
	def display(self):
		print ("(%s, %s, %s)"%(self.x, self.y, self.z))
	def getList(self):
		return [self.x, self.y, self.z]
	def normalize(self):
		if self.d == 0:
			self.d = 1.0 / self.length()
		return vector(self.x*self.d, self.y*self.d, self.z*self.d)

	@classmethod
	def dot(cls, vec1, vec2):
		return vec1.x*vec2.x+vec1.y*vec2.y+vec1.z*vec2.z
	
	@classmethod
	def reflection(cls, vec1, norm):
		return (vec1 - (norm * 2 * cls.dot(vec1, norm))).normalize()

	@classmethod
	def cross(cls, vec1, vec2):
		return vector(vec1.y * vec2.z - vec1.z * vec2.y, vec1.z * vec2.x - vec1.x * vec2.z, vec1.x*vec2.y - vec1.y * vec2.x)
