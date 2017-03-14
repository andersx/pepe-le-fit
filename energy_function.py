#!/usr/bin/env python2
#
# MIT License
# 
# Copyright (c) 2017 Anders Steen Christensen
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import numpy as np
from numpy.linalg import norm

class CostFunction:

    def __init__(self, names, work_dir="." dh=0.000001):

        self.dh = dh





    def cost(self, values, verbose=False):

        return

    def jacobian(self, values):

        zenergy = self.cost(values)

        grad = []

        for i, p in enumerate(values):

            dparams = deepcopy(values)

            dh = self.dx

            dparams[i] += dh
            energy_high = self.cost(dparams)

            dparams[i] -= (2.0 * dh)
            energy_low = self.cost(dparams)

            de = energy_high - energy_low

            grad.append(de/(2.0 * dh))

            s = self.names[i]
            # print de
            print "%3i %8s  %15.7f    dE/dP = %22.10f" % \
                    (i+1, s, values[i],  de/dh)

        grad = np.array(grad)

        print "Gradient norm = ", norm(grad)
        print "Gradient RMS  = ", np.sqrt(np.mean(np.square(grad)))

        print
        print " Numpy formatted values at this point:" 
        print "    values = np.array(["
        for v in values:
            print "%20.15f," % v
        print "])"
        print 



        return grad
