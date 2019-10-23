import bpy
from math import cos, sin, tan, sqrt, atan, radians

filename = "c:/Users/BeckyBot/Desktop/Botnyst/Prototype Models/Scripts/2nd Prototype/M.py"
exec(compile(open(filename).read(), filename, 'exec'))

def reservoir():
    
    bpy.ops.mesh.primitive_cube_add(radius=1, view_align=False, enter_editmode=False, location=(-0.741223, -3.76897, 0.795539), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))

reservoir()