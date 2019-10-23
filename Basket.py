import bpy
from math import cos, sin, tan, sqrt, atan, radians, floor

drive = "f"
filename = drive + ":/M.py"
exec(compile(open(filename).read(), filename, 'exec'))

basketTopR = 0.7
basketBottomR = 0.65
basketH = 1.2
basketThcknss = 0.05 #0.075 #0.1
basketHolesR = 0.25
holeSpacing = 0.1 #0.05
numRows = round(basketH/(2 * basketHolesR + holeSpacing))
collarWidth = 0.175 #0.25
collarThcknss = 0.03 #0.05

def basket():
    
    bpy.ops.mesh.primitive_cone_add(radius1=basketBottomR, radius2=basketTopR, depth=basketH, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    basket = bpy.context.active_object
    basket.name = "basket"
    bpy.ops.transform.translate(value=(0, 0, basket.dimensions.z/2), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    
    bpy.ops.mesh.primitive_cone_add(radius1=basketBottomR - basketThcknss, radius2=basketTopR - basketThcknss, depth=basketH + 0.01, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    basketPnch = bpy.context.active_object
    basketPnch.name = "basketPnch"
    bpy.ops.transform.translate(value=(0, 0, basket.dimensions.z/2), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    bpy.ops.mesh.primitive_cylinder_add(radius=basketTopR + collarWidth, depth=collarThcknss, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    collar = bpy.context.active_object
    collar.name = "collar"
    bpy.ops.transform.translate(value=(0, 0,basketH - collarThcknss), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    subtractObj(basket, basketPnch)       

    bpy.ops.mesh.primitive_uv_sphere_add(size=basketBottomR, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    cap = bpy.context.active_object
    cap.name = "cap"
    
    bpy.ops.mesh.primitive_uv_sphere_add(size=basketBottomR - basketThcknss, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    capPnch = bpy.context.active_object
    capPnch.name = "capPnch"
    subtractObj(cap, capPnch)
    deleteObj(capPnch)
    
    bpy.ops.mesh.primitive_cube_add(radius=basketBottomR, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    capPnch = bpy.context.active_object
    capPnch.name = "capPnch"
    bpy.ops.transform.translate(value=(0, 0, basketBottomR), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    subtractObj(cap, capPnch)
    deleteObj(capPnch)

    subtractObj(collar, basketPnch)
    deleteObj(basketPnch)

    bpy.ops.mesh.primitive_cylinder_add(radius=basketHolesR, depth=basketBottomR, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    holePnch = bpy.context.active_object
    holePnch.name = "holePnch"
    bpy.ops.transform.translate(value=(0, 0, -basketBottomR), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    subtractObj(cap, holePnch)
    bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
    bpy.ops.transform.rotate(value=1.0472, axis=(0, 1, 0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    capHoles = 5
    for i in range(0,capHoles):
        subtractObj(cap, holePnch)
        bpy.ops.transform.rotate(value=2*pi/capHoles, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

#    bpy.ops.transform.rotate(value=0.523599, axis=(0, 1, 0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
#    bpy.ops.transform.rotate(value=pi/capHoles, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
#    capHoles = 9
#    for i in range(0,capHoles):
#        subtractObj(cap, holePnch)
#        bpy.ops.transform.rotate(value=2*pi/capHoles, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    deleteObj(holePnch)
                                        
#    bpy.ops.mesh.primitive_cylinder_add(radius=basketHolesR, depth=basketTopR, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
#    holePnch = bpy.context.active_object
#    holePnch.name = "holePnch"    
#    bpy.ops.transform.rotate(value=1.5708, axis=(1, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
#    bpy.ops.transform.translate(value=(0, basketTopR, basketH - basketHolesR - holeSpacing), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
#    bpy.ops.transform.translate(value=(0, basketTopR, basketH - 3 * basketHolesR - holeSpacing), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
#    bpy.ops.object.origin_set(type='ORIGIN_CURSOR')

#    for i in range(1,numRows):
#        currentH = basketH - i * (2 * basketHolesR + holeSpacing)
#        currentR = basketBottomR + (basketTopR - basketBottomR) * currentH/basketH
#        numPnchsPerRow = round((2 * pi * currentR)/(2 * basketHolesR + holeSpacing))

#        for j in range(0, numPnchsPerRow):
#            subtractObj(basket, holePnch)
#            bpy.ops.transform.rotate(value=2 * pi / numPnchsPerRow, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
#        bpy.ops.transform.rotate(value=pi / numPnchsPerRow, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)        
#        bpy.ops.transform.translate(value=(0, 0, -2 * basketHolesR - holeSpacing), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

#    deleteObj(holePnch)                    
    
    bpy.data.objects['basket'].select = True
    bpy.data.objects['cap'].select = True
    bpy.data.objects['collar'].select = True
    bpy.ops.object.join()
#    basket = bpy.context.active_object
#    basket.name = "basket" 
    
basket()    
    
 