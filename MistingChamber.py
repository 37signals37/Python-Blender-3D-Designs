import bpy
from math import cos, sin, tan, sqrt, atan

def makeMistingChamber():
    
    makeCupBody()
    wall = bpy.context.active_object

    bpy.ops.mesh.primitive_cylinder_add(radius=engHolePnchR, depth=engHolePnchL, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    engHolePnch = bpy.context.active_object
    engHolePnch.name = "engHolePnch"
    bpy.ops.transform.translate(value=(0, 0, engHolePnchL/2), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
    bpy.ops.transform.translate(value=(0, -innerR, 0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.rotate(value=-engHolePnchTheta, axis=(1, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    
    #Maiking Rod Holder Base
    bpy.ops.mesh.primitive_uv_sphere_add(size=rodHldrR, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    rodHldrBase = bpy.context.active_object
    rodHldrBase.name = "rodHldrBase"

    bpy.ops.mesh.primitive_cube_add(radius=1, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    bpy.ops.transform.translate(value=(0, -1, 0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    cube = bpy.context.active_object
    subtractObj(rodHldrBase, cube)
    deleteObj(cube)    
    
    bpy.data.objects['rodHldrBase'].select = True    
    bpy.ops.transform.rotate(value=wallTheta, axis=(1, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    bpy.ops.mesh.primitive_cube_add(radius=1, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    bpy.ops.transform.translate(value=(0, 0, -1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    cube = bpy.context.active_object
    subtractObj(rodHldrBase, cube)
    deleteObj(cube)

    bpy.data.objects['rodHldrBase'].select = True
    bpy.ops.transform.translate(value=(0, -innerR, 0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)      
    
    #Maiking Rod Holder Top
    bpy.ops.mesh.primitive_uv_sphere_add(size=rodHldrR, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    rodHldrTop = bpy.context.active_object   
    rodHldrTop.name = "rodHldrTop"
    bpy.ops.transform.translate(value=(0, rodHldrTopXSpacer, rodHldrTopHght), constraint_axis=(False, True, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    
    subtractObj(rodHldrBase, engHolePnch)
    subtractObj(rodHldrTop, engHolePnch)
#    subtractObj(wall, engHolePnch)
    
    bpy.data.objects['rodHldrBase'].select = True
    bpy.data.objects['rodHldrTop'].select = True
    bpy.data.objects['wall'].select = True
    bpy.data.objects['engHolePnch'].select = True
    rodHldrTop = bpy.context.active_object
    bpy.ops.object.join()
    bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
