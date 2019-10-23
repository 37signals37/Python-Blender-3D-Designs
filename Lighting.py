import bpy
from math import cos, sin, tan, sqrt, atan, radians

filename = "c:/Users/BeckyBot/Desktop/Botnyst/Prototype Models/Scripts/M.py"
exec(compile(open(filename).read(), filename, 'exec'))

def LightingArm():
    
    bpy.ops.mesh.primitive_cone_add(radius1=lghtngArmZ/2, radius2=lghtngArmZ/2, depth=lghtngArmY, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    lightingArm = bpy.context.active_object
    lightingArm.name = "lightingArm"
    
    bpy.ops.mesh.primitive_cone_add(radius1=lghtngArmZ/2 - lghtngArmX, radius2=lghtngArmZ/2 - lghtngArmX, depth=lghtngArmY, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    lightingArmPnch = bpy.context.active_object
    lightingArmPnch.name = "lightingArmPnch"
    
    subtractObj(lightingArm, lightingArmPnch)
    deleteObj(lightingArmPnch)
    
    bpy.ops.mesh.primitive_cube_add(radius=lghtngArmZ/2, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    lightingArmPnchA = bpy.context.active_object
    lightingArmPnchA.name = "lightingArmPnchA"
    bpy.ops.transform.translate(value=(-lghtngArmZ/2, -lghtngArmZ/2, 0), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    subtractObj(lightingArm, lightingArmPnchA)
    
    acc = radians(270)
    bpy.data.objects['lightingArmPnchA'].select = False
    bpy.data.objects['lightingArm'].select = True
    
    while (acc/lghtngArmZA > 1.0001):        
        bpy.ops.transform.rotate(value=radians(1), axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        acc = acc - radians(1)
        subtractObj(lightingArm, lightingArmPnchA)
    
    deleteObj(lightingArmPnchA)
    
    bpy.data.objects['lightingArm'].select = True
    bpy.ops.transform.rotate(value=1.5708, axis=(1, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

def LightingRods():
    for i in range(0, numOfLightingRods):
        bpy.ops.mesh.primitive_cone_add(radius1=rodRad, radius2=rodRad, depth=rodLngth, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
        lightingRod = bpy.context.active_object
        lightingRod.name = "lightingRod + string(i)"
        bpy.ops.transform.rotate(value=1.5708, axis=(0, 1, 0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        bpy.ops.transform.translate(value=(rodLngth/2 + plntHsngRad2, 0, reservoirHght + plntHsngHght), constraint_axis=(True, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
        bpy.ops.transform.rotate(value=2*pi/numOfLightingRods * i, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        
        
