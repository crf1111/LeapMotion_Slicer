#-*- coding:utf-8 -*-

import os

print 'current file path = ', os.path.abspath(__file__)

with open('/tmp/SlicerLeapMotion.log','w') as f:
    f.write('current file path = %s' % os.path.abspath(__file__))

print 'end'


import sys

sys.path.insert(0,'../lib')

import Leap

with open('/tmp/SlicerLeapMotion.log','a') as f:
    f.write('\n\n\nLeap %s \n\n' % Leap.__name__)
print 'leap = ', Leap.__name__
print 'Done'