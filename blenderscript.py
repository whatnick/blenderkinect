#!/usr/bin/env python
import sys

from freenect import *

from Blender import *
import Blender, meshtools

import numpy as np

def drawmesh(mesh):
    Blender.NMesh.PutRaw(mesh,"obj",1)
    Blender.Redraw()

def display(data):
    data -= np.min(data.ravel())
    mesh = Blender.NMesh.GetRaw()
    for y in range(0,480,5):
        for x in range(0,640,5):
            zz = data[y,x]
            if(zz<1000):
                xx = (x-320)*(zz-10)*0.0021 #This 'calibration' copied using Zephod's windows software - because it 'just works'
                yy = (y-240)*(zz-10)*0.0021
                zz-=200
                mesh.verts.append(NMesh.Vert(xx, yy, -zz))
    drawmesh(mesh)
    
display(sync_get_depth()[0])
