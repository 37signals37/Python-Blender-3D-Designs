import bpy
from math import cos, sin, tan, sqrt, atan, radians, floor

filename = "c:/BlenderScripts/M.py"
exec(compile(open(filename).read(), filename, 'exec'))

barL = 2
barW = 0.5
barH = 0.25

def bar():
    
    bpy.ops.mesh.primitive_cube_add(view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    xtrPnch = bpy.context.active_object
    xtrPnch.name = "xtrPnch"
    bpy.ops.transform.resize(value=(0.386136, 0.386136, 0.386136), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
