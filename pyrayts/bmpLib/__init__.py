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
import struct
import sys
from .. baseImage.clamp import *

class bmpLib(object):
	def __init__(self, *args):
		self.filename = args[0]
		self.width    = args[1] 
		self.height   = args[2]
		self.bitDepth = 3

	def setHeader(self, fp):
		# BITMAPFILEHEADER
		if sys.version_info[0] > 2:
			header = b"BM"
		else:
			header = "BM"
		fp.write(header)
		fsize = 54 + self.width * self.height * 3
		fp.write(struct.pack("I",fsize))
		fp.write(struct.pack("H",0))
		fp.write(struct.pack("H",0))
		fp.write(struct.pack("I",54))

		#BITMAPINFOHEADER
		fp.write(struct.pack("I",40))
		fp.write(struct.pack("I",self.width))
		fp.write(struct.pack("I",self.height))
		fp.write(struct.pack("H",1))
		fp.write(struct.pack("H",8*self.bitDepth))
		fp.write(struct.pack("I",0))
		fp.write(struct.pack("I",0))
		fp.write(struct.pack("I",3780))
		fp.write(struct.pack("I",3780))
		fp.write(struct.pack("I",0))
		fp.write(struct.pack("I",0))

	def save(self, buf):
		fp = open(self.filename, "wb")
		self.setHeader(fp)
		#for b in buf:
		#	fp.write(struct.pack("B",clamp(b*255)))
		for h in reversed(range(1, self.height+1)):
			for w in range(0, self.width):
				fp.write(struct.pack("B", int(clamp(buf.col[self.width*(h-1)+w].b * 255))))
				fp.write(struct.pack("B", int(clamp(buf.col[self.width*(h-1)+w].g * 255))))
				fp.write(struct.pack("B", int(clamp(buf.col[self.width*(h-1)+w].r * 255))))
		fp.close()

