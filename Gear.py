import bpy
from math import cos, sin, tan, sqrt, atan, radians, floor

drive = "f"
filename = drive + ":/M.py"
exec(compile(open(filename).read(), filename, 'exec'))

xtrPnchR = 0.07 #0.095
wiskerW = 0.3
wiskerL = 2
wiskR1 = 0.1
wiskR2 = 0.02
wiskL = 1
numWiskPerRow = 8
numRow = floor(wiskerL/wiskR1) - 1

gearW = 0.3 #1.25
gearD = 0.225
numOfTeeth = 9
teethL = 0.6
teethW = 0.15
XTRrad = 0.1 #0.095 for axle

baseL = 2.25
baseW = 0.5
baseD = 0.3
armL = 0.3
armW = baseW
armD = 0.6
axlePnchR = 0.1

holderW = 0.375
holderL = 1
stopEndW = 0.4
stopEndD = 0.125

boxL = 2
boxW = 1
boxH = 1
boxT = 0.1

def wisker():
    bpy.ops.mesh.primitive_cylinder_add(radius=wiskerW/2, depth=wiskerL, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    wisker = bpy.context.active_object
    wisker.name = "wisker"
    bpy.ops.transform.translate(value=(0, 0, wiskerL/2), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    bpy.ops.mesh.primitive_cylinder_add(radius=xtrPnchR, depth=wiskerL * 2, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    xtrPnch = bpy.context.active_object
    xtrPnch.name = "xtrPnch"
    bpy.ops.transform.translate(value=(0, 0, wiskerL/2), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    subtractObj(wisker, xtrPnch)
    deleteObj(xtrPnch)

    bpy.ops.mesh.primitive_cone_add(radius1=wiskR1, radius2=wiskR2, depth=wiskL, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    bpy.ops.transform.rotate(value=-1.5708, axis=(1, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.translate(value=(0, wiskerW/2 + wiskL/2 - xtrPnchR/2, wiskR1), constraint_axis=(False, True, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
          
    for j in range(0, numRow):
        if j%2==0:
            bpy.ops.transform.rotate(value=pi/numWiskPerRow, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        else:
            bpy.ops.transform.rotate(value=-pi/numWiskPerRow, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)            
        for i in range(0, numWiskPerRow):
            bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(0, 0, 0), "constraint_axis":(False, False, False), "constraint_orientation":'GLOBAL', "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "texture_space":False, "remove_on_cancel":False, "release_confirm":False})
            bpy.ops.transform.rotate(value=2*pi/numWiskPerRow, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        bpy.ops.transform.translate(value=(0, 0, wiskR1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

            
 
def gear():
    bpy.ops.mesh.primitive_cylinder_add(radius=gearW/2, depth=gearD, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    gear = bpy.context.active_object
    gear.name = "gear"
    
    bpy.ops.mesh.primitive_cylinder_add(radius=xtrPnchR, depth=wiskerL * 2, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    xtrPnch = bpy.context.active_object
    xtrPnch.name = "xtrPnch"
    subtractObj(gear, xtrPnch)
    deleteObj(xtrPnch)
    
    #bpy.ops.mesh.primitive_cube_add(radius=1, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    bpy.ops.mesh.primitive_cone_add(radius1=teethW, radius2=0, depth=teethL, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    tooth = bpy.context.active_object
    tooth.name = "tooth"
    bpy.ops.transform.rotate(value=1.5708, axis=(0, 1, 0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.translate(value=(gearW/2 + teethL/3, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
       
    for i in range(0,numOfTeeth):
        bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(0, 0, 0), "constraint_axis":(False, False, False), "constraint_orientation":'GLOBAL', "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "texture_space":False, "remove_on_cancel":False, "release_confirm":False})
        bpy.ops.transform.rotate(value=2*pi/numOfTeeth, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    deleteObj(tooth)

    bpy.ops.object.select_all(action='TOGGLE')
    bpy.ops.object.join()     

def shaftHolder():
    bpy.ops.mesh.primitive_cube_add(view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    base = bpy.context.active_object
    base.name = "base"
    bpy.ops.transform.resize(value=(baseL, baseW, baseD), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.translate(value=(0, 0, baseD), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    bpy.ops.mesh.primitive_cube_add(view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    leftArm = bpy.context.active_object
    leftArm.name = "leftArm"
    bpy.ops.transform.resize(value=(armL, armW, armD), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.translate(value=(-baseL + armL, 0, armD + 2 * baseD), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    bpy.ops.mesh.primitive_cube_add(view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    rightArm = bpy.context.active_object
    rightArm.name = "leftArm"
    bpy.ops.transform.resize(value=(armL, armW, armD), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.translate(value=(baseL - armL, 0, armD + 2 * baseD), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    bpy.ops.object.select_all(action='TOGGLE')
    bpy.ops.object.select_all(action='TOGGLE')
    bpy.ops.object.join()   

    bpy.ops.mesh.primitive_cylinder_add(view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    axlePnch = bpy.context.active_object
    axlePnch.name = "axlePnch"
    bpy.ops.transform.resize(value=(axlePnchR, axlePnchR, 2 * baseL), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.rotate(value=1.5708, axis=(0, 1, 0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

def shaftHolder2():
    bpy.ops.mesh.primitive_cube_add(view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    box = bpy.context.active_object
    box.name = "box"
    bpy.ops.transform.resize(value=(boxL, boxW, boxH), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

def beltHolder():
    
    bpy.ops.mesh.primitive_cylinder_add(radius=xtrPnchR, depth=wiskerL * 2, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    xtrPnch = bpy.context.active_object
    xtrPnch.name = "xtrPnch"
    
    bpy.ops.mesh.primitive_cylinder_add(radius=gearW/2, depth=gearD, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    gear = bpy.context.active_object
    gear.name = "gear"

    subtractObj(gear, xtrPnch)

#    bpy.ops.mesh.primitive_cube_add(radius=1, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
#    tooth = bpy.context.active_object
#    tooth.name = "tooth"
#    bpy.ops.transform.resize(value=(teethL/2, teethW/2, gearD/2), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

#    bpy.ops.transform.translate(value=(gearW/2, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
#    bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
    
#    for i in range(0,numOfTeeth):
#        bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(0, 0, 0), "constraint_axis":(False, False, False), "constraint_orientation":'GLOBAL', "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "texture_space":False, "remove_on_cancel":False, "release_confirm":False})
#        bpy.ops.transform.rotate(value=2*pi/numOfTeeth, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

#    deleteObj(tooth)
    deleteObj(xtrPnch)
    bpy.ops.object.select_all(action='TOGGLE')
    bpy.ops.object.join()
    gear = bpy.context.active_object
    gear.name = "gear"
    
#    bpy.ops.mesh.primitive_cylinder_add(radius=stopEndW, depth=stopEndD, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
#    stopEndTop = bpy.context.active_object
#    stopEndTop.name = "stopEndTop"
#    bpy.ops.transform.translate(value=(0, 0, stopEndTop.dimensions.z/2 + gear.dimensions.z/2), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    bpy.ops.mesh.primitive_cylinder_add(radius=stopEndW, depth=stopEndD, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    stopEndBottom = bpy.context.active_object
    stopEndBottom.name = "stopEndBottom"
    bpy.ops.transform.translate(value=(0, 0, -stopEndBottom.dimensions.z/2 - gear.dimensions.z/2), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    bpy.ops.mesh.primitive_cylinder_add(radius=xtrPnchR, depth=wiskerL * 2, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    xtrPnch = bpy.context.active_object
    xtrPnch.name = "xtrPnch"
      
#    subtractObj(stopEndTop, xtrPnch)
    subtractObj(stopEndBottom, xtrPnch)
    deleteObj(xtrPnch)
  
    bpy.ops.object.select_all(action='TOGGLE')
    bpy.ops.object.join()     


#beltHolder()
#wisker()
gear()
#shaftHolder2()