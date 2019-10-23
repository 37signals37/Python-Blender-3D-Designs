import bpy
from math import cos, sin, tan, sqrt, atan, radians, floor

filename = "c:/Users/BeckyBot/Desktop/Botnyst/Prototype Models/Scripts/M.py"
exec(compile(open(filename).read(), filename, 'exec'))

collarWidth = 0.875 #0.25
collarThcknss = 0.03 #0.05    
casingR1 = 0.6 #0.6
casingR2 = 0
casingH = 2
casingThcknss = 0.05
slitWidth = 0.04 #0.01
slitAngle = 30
casingAngle = 30
catchPnchR = 0.4

def basket1():


    bpy.ops.mesh.primitive_cylinder_add(vertices=64, radius=collarWidth, depth=collarThcknss, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    collar = bpy.context.active_object
    collar.name = "collar"    
    
    bpy.ops.mesh.primitive_cone_add(radius1=casingR1, radius2=casingR2, depth=casingH, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    casing = bpy.context.active_object
    casing.name = "casing"
    bpy.ops.transform.translate(value=(0, 0, casingH/2), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    bpy.ops.mesh.primitive_cone_add(radius1=casingR1 - casingThcknss, radius2=casingR2 - casingThcknss, depth=casingH, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    casingPnch = bpy.context.active_object
    casingPnch.name = "casingPnch"
    bpy.ops.transform.translate(value=(0, 0, casingH/2), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    subtractObj(casing, casingPnch)
    deleteObj(casingPnch)
    
    bpy.ops.mesh.primitive_cube_add(view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    slitPnch = bpy.context.active_object
    slitPnch.name = "slitPnch"
    bpy.ops.transform.resize(value=(1, slitWidth, casingH), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.translate(value=(0, 0, casingH), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
            
    for i in range(0, 3):
        subtractObj(casing, slitPnch)
        bpy.ops.transform.rotate(value=slitAngle/90 * pi, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    deleteObj(slitPnch)
    
    bpy.data.objects['casing'].select = True
    bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
    bpy.ops.transform.rotate(value=casingAngle/180*pi, axis=(0, 1, 0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.translate(value=(0, 0, -casingR1 * sin(casingAngle/180 * pi)), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

#    bpy.ops.mesh.primitive_cone_add(radius1=casingR1 - casingThcknss, radius2=casingR2 - casingThcknss, depth=casingH, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
#    collarPnch = bpy.context.active_object
#    collarPnch.name = "collarPnch"
#    bpy.ops.transform.translate(value=(0, 0, casingH/2), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
#    bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
#    bpy.ops.transform.rotate(value=casingAngle/180*pi, axis=(0, 1, 0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
#    bpy.ops.transform.translate(value=(0, 0, -casingR1 * sin(casingAngle/180 * pi)), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

#    subtractObj(collar, collarPnch)
#    deleteObj(collarPnch)
    
    bpy.ops.mesh.primitive_cube_add(view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    casingPnch = bpy.context.active_object
    casingPnch.name = "casingPnch"
    bpy.ops.transform.translate(value=(0, 0, -1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    subtractObj(casing, casingPnch)
    deleteObj(casingPnch)

#    bpy.ops.mesh.primitive_cylinder_add(vertices=64, radius=collarWidth, depth=collarThcknss, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
#    catch = bpy.context.active_object
#    catch.name = "catch"
    
    bpy.ops.mesh.primitive_cylinder_add(vertices=64, radius=catchPnchR, depth=collarThcknss*2, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    catchPnch = bpy.context.active_object
    catchPnch.name = "catchPnch"
        
#    subtractObj(catch, catchPnch)
    subtractObj(collar, catchPnch)
    deleteObj(catchPnch)
        
    bpy.data.objects['casing'].select = True
#    bpy.data.objects['catch'].select = True
    bpy.data.objects['collar'].select = True
    bpy.ops.object.join()




    
basket1()
    
 