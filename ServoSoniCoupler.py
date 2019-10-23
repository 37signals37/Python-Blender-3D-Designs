import bpy
from math import cos, sin, tan, sqrt, atan, radians

drive = "f"
filename = drive + ":/M.py"
exec(compile(open(filename).read(), filename, 'exec'))
#Repetier Multiplier = 4

bridgeX = 0.85 #0.75 #0.5
bridgeY = 2.5 #4
bridgeZ = 1

screwCatchR = 0.6 #0.625 #0.6 #0.7 #0.8 #0.85 #0.9
screwCatchD = 2
screwCatchHeadOffset = 0.15

screwPnchR = 0.3 #0.35
screwPnchD = 2

legR = 0.4
legD = 0.4 #1.25 #0.5 

def servoSoniCoupler():
            
    bpy.ops.mesh.primitive_cube_add(radius=1, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    bridge = bpy.context.active_object
    bridge.name = "bridge"
    bpy.ops.transform.resize(value=(bridgeX, bridgeY, bridgeZ), constraint_axis=(True, True, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    bpy.ops.mesh.primitive_cylinder_add(radius=screwCatchR, depth=screwCatchD, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    screwCatch = bpy.context.active_object
    screwCatch.name = "screwCatch"
    bpy.ops.transform.rotate(value=1.5708, axis=(0, 1, 0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.translate(value=(screwCatchD/2, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    subtractObj(bridge, screwCatch)
    bpy.ops.transform.translate(value=(-screwCatchD - bridgeX + screwCatchHeadOffset, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    subtractObj(bridge, screwCatch)
    deleteObj(screwCatch)
    
    bpy.ops.mesh.primitive_cylinder_add(radius=screwPnchR, depth=screwPnchD, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    screwPnch = bpy.context.active_object
    screwPnch.name = "screwPnch"
    bpy.ops.transform.rotate(value=1.5708, axis=(0, 1, 0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    subtractObj(bridge, screwPnch)
    deleteObj(screwPnch)    
    
    bpy.ops.mesh.primitive_cylinder_add(radius=legR, depth=legD, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    leftLeg = bpy.context.active_object
    leftLeg.name = "leftLeg"
    bpy.ops.transform.translate(value=(0, bridgeX - bridgeY, -legD/2 - bridgeZ), constraint_axis=(True, True, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    bpy.ops.mesh.primitive_cylinder_add(radius=legR, depth=legD, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    rightLeg = bpy.context.active_object
    rightLeg.name = "rightLeg"
    bpy.ops.transform.translate(value=(0, -bridgeX + bridgeY, -legD/2 - bridgeZ), constraint_axis=(True, True, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    bpy.data.objects['leftLeg'].select = True
    bpy.data.objects['rightLeg'].select = True
    bpy.data.objects['bridge'].select = True
    bpy.ops.object.join()

servoSoniCoupler()