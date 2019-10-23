import bpy
from math import cos, sin, tan, sqrt, atan, radians, floor

filename = "c:/BlenderScripts/M.py"
exec(compile(open(filename).read(), filename, 'exec'))

bottomR = 0.08
topR = 0.08
height = 0.4
bottomPnchR = 0.06#0.045
topPnchR = 0.06#0.045
pnchOffset = -0.01
leadBottomPnchR = 0.02
leadTopPnchR = 0.02
leadPnchOffset = 0.04



def leadConnects():
    bpy.ops.mesh.primitive_cone_add(radius1=bottomR, radius2=topR, depth=height, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    bottom = bpy.context.active_object
    bottom.name = "bottom"
    bpy.ops.transform.translate(value=(0, 0, -height/2), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    bpy.ops.mesh.primitive_cone_add(radius1=bottomPnchR, radius2=topPnchR, depth=height, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    bottomPnch = bpy.context.active_object
    bottomPnch.name = "bottomPnch"
    bpy.ops.transform.translate(value=(pnchOffset, 0, -height/2), constraint_axis=(True, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    bpy.ops.mesh.primitive_cone_add(radius1=leadBottomPnchR, radius2=leadTopPnchR, depth=height, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    leadBottomPnch = bpy.context.active_object
    leadBottomPnch.name = "leadBottomPnch"
    bpy.ops.transform.translate(value=(leadPnchOffset, 0, -height/2), constraint_axis=(True, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    

    subtractObj(bottom, bottomPnch)
    subtractObj(bottom, leadBottomPnch)
    deleteObj(bottomPnch)
    deleteObj(leadBottomPnch)

    raise Exception()

    bpy.ops.mesh.primitive_cone_add(radius1=topR, radius2=bottomR, depth=height, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    top = bpy.context.active_object
    top.name = "top"
    bpy.ops.transform.translate(value=(0, 0, height/2), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    bpy.ops.mesh.primitive_cone_add(radius1=topPnchR, radius2=bottomPnchR, depth=height, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    topPnch = bpy.context.active_object
    topPnch.name = "topPnch"
    bpy.ops.transform.translate(value=(0, 0, height/2), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    subtractObj(top, topPnch)
    deleteObj(topPnch)

    bpy.data.objects['top'].select = True
    bpy.data.objects['bottom'].select = True
    bpy.ops.object.join()

leadConnects()