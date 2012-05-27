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

class spacePartitioning:
	bbmax = vector()
	bbmin = vector()
	def _isInclude(self, obj):
		if self.bbmax < obj.bbmax and self.bbmin > obj.bbmin:
			return 1
		return 0
	def __init__(self):
		pass
	def garageIn(self):
		pass
	def intersect(self):
		pass

class grid(spacePartitioning):
	def __init__(self, numOfUnit=-1 ):
		if numOfUnit!=-1:
			self._childs = [grid() for i in range(numOfUnit*numOfUnit*numOfUnit)]
			self.numOfUnit = numOfUnit
	def garageIn(self, objs):
		curMax = vector(-1000000, -1000000, -1000000)
		curMin = vector( 1000000,  1000000,  1000000)
		for obj in objs:
			curMax = vector.max(obj.bbmax, curMax)
			curMin = vector.min(obj.bbmin, curMin)
		unitWidth = (curMax - curMin)*(1.0/self.numOfUnit)

		i = 0
		for x in range(self.numOfUnit):
			for y in range(self.numOfUnit):
				for z in range(self.numOfUnit):
					self._childs[i].bbmin = curMin
					self._childs[i].bbmax = curMin
					i+=1

class octree(spacePartitioning):
	pass

class kdTree(spacePartitioning):
	pass

class bvh(spacePartitioning):
	pass
#a = grid(2)
#print dir(a)