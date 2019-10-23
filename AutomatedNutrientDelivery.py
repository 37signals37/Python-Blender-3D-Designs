import bpy
from math import cos, sin, tan, sqrt, atan

filename = "c:/Users/BeckyBot/Desktop/Botnyst/Prototype Models/Scripts/M.py"
exec(compile(open(filename).read(), filename, 'exec'))

#1 Input Unit = 0.040625"

def KeyChain():
    frameW = 35
    frameL = 35
    frameH = 6.25

    framePW = 20
    framePL = 28
    framePH = 5
    framePoffset = 10
    
    slitPnchW = 6.25
    slitPnchL = 28
    slitPnchH = frameH+0.01
    slitPoffset = -20
    
    keyPW = 20
    keyPL = 7.81
    keyPH = 3.5
    keyPOffset = 20
    
    bpy.ops.mesh.primitive_cube_add(radius=1, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    frame = bpy.context.active_object
    frame.name = "frame"
    bpy.ops.transform.resize(value=(frameW, frameL, frameH), constraint_axis=(True, True, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    bpy.ops.mesh.primitive_cube_add(radius=1, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    framePnch = bpy.context.active_object
    framePnch.name = "framePnch"
    bpy.ops.transform.resize(value=(framePW, framePL, framePH), constraint_axis=(True, True, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.translate(value=(framePoffset, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    subtractObj(frame, framePnch)
    deleteObj(framePnch)
    
    bpy.ops.mesh.primitive_cube_add(radius=1, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    slitPnch = bpy.context.active_object
    slitPnch.name = "slitPnch"
    bpy.ops.transform.resize(value=(slitPnchW, slitPnchL, slitPnchH), constraint_axis=(True, True, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.translate(value=(slitPoffset, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    subtractObj(frame, slitPnch)
    deleteObj(slitPnch)

    bpy.ops.mesh.primitive_cube_add(radius=1, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    keyPnch = bpy.context.active_object
    keyPnch.name = "keyPnch"
    bpy.ops.transform.resize(value=(keyPW, keyPL, keyPH), constraint_axis=(True, True, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.translate(value=(keyPOffset, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    subtractObj(frame, keyPnch)
    deleteObj(keyPnch)

def ANDSbase():
    
    middleWidth = 15.63
    
    StepperMotorMount()        
    sm_turner = bpy.context.active_object
    sm_turner.name = "sm_turner"    
    bpy.data.objects['sm_turner'].select = True    
    bpy.ops.transform.rotate(value=-1.5708, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.translate(value=(-sm_turner.dimensions.y/2 - middleWidth/2, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    bpy.ops.mesh.primitive_cube_add(radius=1, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    middle = bpy.context.active_object
    middle.name = "middle"
    bpy.ops.transform.resize(value=(middleWidth/2, sm_turner.dimensions.x/2, sm_turner.dimensions.z/2), constraint_axis=(True, True, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    StepperMotorMount()        
    sm_elevator = bpy.context.active_object
    sm_elevator.name = "sm_elevator"
    bpy.data.objects['sm_elevator'].select = True
    bpy.ops.transform.rotate(value=-1.5708, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.translate(value=(sm_turner.dimensions.y/2 + middleWidth/2, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    bpy.data.objects['sm_turner'].select = True
    bpy.data.objects['middle'].select = True
    bpy.data.objects['sm_elevator'].select = True
    bpy.ops.object.join()
    ANDS_base = bpy.context.active_object
    ANDS_base.name = "ANDS_base"



def BaseSupport1():

    basePlateRad = 35 #27.5
    basePlateHght = 9 #3
    ten_mL_NozzlePunchRad = 3 #2.8, 2.2, 1.92, 2.4
    ten_mL_PunchRad = 8.5 #8.75, 9, 5.5
    sixty_mL_NozzlePunchRad = 2.35 #2.1, 1.92, 2.3
    sixty_mL_PunchRad = 16.2 #16 #15.75, 15, 13.75
    stepperPunchRad = 2.83 #2.73, 2.63, 2.88
    stepperSquarePunchTrans = 2.2 #2, 1.75
    frmThcknss = 1 #0.5
    frmHght = 30
    pnchOffset = basePlateRad/15
    
    bpy.ops.mesh.primitive_cylinder_add(radius=basePlateRad, depth=basePlateHght, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    base_plate = bpy.context.active_object
    base_plate.name = "base_plate"

    bpy.ops.mesh.primitive_cylinder_add(radius=stepperPunchRad, depth=basePlateHght+1, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    stepperPunch = bpy.context.active_object
    stepperPunch.name = "stepperPunch"

    bpy.ops.mesh.primitive_cube_add(radius=basePlateHght+2, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    stepperPunchSqur = bpy.context.active_object
    stepperPunchSqur.name = "stepperPunchSqur"
    bpy.ops.transform.resize(value=(1, 1, 10), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.translate(value=(0, stepperPunchSqur.dimensions.y/2 + stepperSquarePunchTrans, 0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    subtractObj(stepperPunch,stepperPunchSqur)
    bpy.ops.transform.translate(value=(0, -stepperPunchSqur.dimensions.y - 2 * stepperSquarePunchTrans, 0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    subtractObj(stepperPunch,stepperPunchSqur)
    deleteObj(stepperPunchSqur)
    subtractObj(base_plate, stepperPunch)
    deleteObj(stepperPunch)

    bpy.ops.mesh.primitive_cylinder_add(radius=sixty_mL_NozzlePunchRad, depth=basePlateHght+1, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    sixty_mL_punch = bpy.context.active_object
    sixty_mL_punch.name = "sixty_mL_punch"
    bpy.ops.transform.translate(value=(0, basePlateRad - sixty_mL_punch.dimensions.y/2 - pnchOffset, 0), constraint_axis=(True, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    subtractObj(base_plate, sixty_mL_punch)
    bpy.ops.transform.translate(value=(0, -2 * basePlateRad + 2 * sixty_mL_punch.dimensions.y/2 + 2 * pnchOffset, 0), constraint_axis=(True, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    subtractObj(base_plate, sixty_mL_punch)
    deleteObj(sixty_mL_punch)

    bpy.ops.mesh.primitive_cylinder_add(radius=ten_mL_NozzlePunchRad, depth=frmHght+1, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    ten_mL_punch = bpy.context.active_object
    ten_mL_punch.name = "ten_mL_punch"
    
    bpy.ops.mesh.primitive_cylinder_add(radius=ten_mL_PunchRad, depth=frmHght, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    ten_mL_bigPunch = bpy.context.active_object
    ten_mL_bigPunch.name = "ten_mL_bigPunch"
    bpy.ops.transform.translate(value=(0, 0, basePlateHght), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    bpy.ops.mesh.primitive_cylinder_add(radius=ten_mL_PunchRad + frmThcknss, depth=frmHght, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    ten_mL_frm = bpy.context.active_object
    ten_mL_frm.name = "ten_mL_frm"
    subtractObj(ten_mL_frm, ten_mL_bigPunch)
    deleteObj(ten_mL_bigPunch)
    subtractObj(ten_mL_frm, ten_mL_punch)

    bpy.data.objects['ten_mL_punch'].select = True    
    bpy.ops.transform.translate(value=(0, basePlateRad - ten_mL_punch.dimensions.y/2 - pnchOffset, 0), constraint_axis=(True, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
    bpy.ops.transform.rotate(value=1.5708, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    subtractObj(base_plate, ten_mL_punch)
    bpy.ops.transform.rotate(value=-3.14159, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    subtractObj(base_plate, ten_mL_punch)
    deleteObj(ten_mL_punch)

    bpy.data.objects['ten_mL_frm'].select = True
    bpy.ops.transform.translate(value=(0, basePlateRad - pnchOffset - ten_mL_NozzlePunchRad, ten_mL_frm.dimensions.z/2 - base_plate.dimensions.z/2), constraint_axis=(False, True, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(0, 0, 0), "constraint_axis":(False, False, False), "constraint_orientation":'GLOBAL', "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "texture_space":False, "remove_on_cancel":False, "release_confirm":False})
    bpy.ops.transform.translate(value=(0, -2*basePlateRad + 2 * pnchOffset + 2 * ten_mL_NozzlePunchRad, 0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    bpy.ops.mesh.primitive_cylinder_add(radius=sixty_mL_PunchRad, depth=frmHght+1, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    sixty_mL_bigPunch = bpy.context.active_object
    sixty_mL_bigPunch.name = "sixty_mL_bigPunch"

    bpy.ops.mesh.primitive_cylinder_add(radius=sixty_mL_PunchRad + frmThcknss, depth=frmHght, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    sixty_mL_frm = bpy.context.active_object
    sixty_mL_frm.name = "sixty_mL_frm"
    subtractObj(sixty_mL_frm, sixty_mL_bigPunch)
    deleteObj(sixty_mL_bigPunch)

    bpy.data.objects['sixty_mL_frm'].select = True
    bpy.ops.transform.translate(value=(basePlateRad - sixty_mL_frm.dimensions.x/2, 0, sixty_mL_frm.dimensions.z/2), constraint_axis=(True, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(0, 0, 0), "constraint_axis":(False, False, False), "constraint_orientation":'GLOBAL', "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "texture_space":False, "remove_on_cancel":False, "release_confirm":False})
    bpy.ops.transform.translate(value=(- 2 * basePlateRad + 2 * sixty_mL_frm.dimensions.x/2, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    bpy.ops.object.select_all(action='TOGGLE')
    bpy.ops.object.select_all(action='TOGGLE')
    bpy.ops.object.join()
    
def BaseSupport2():

    Ten_mL_NozzlePunchDiam = 3.6 #3.84
    Ten_mL_NozzlePunchDiam = 5.5

def StepperMotorMount():
    
    mountL = 43.75
    mountW = 41
    mountH = 21.88
    
    mtrPnchR = 14.5 #13.28
    mtrPnchH = 18.75
    mtrPnchOffset = mountH - mtrPnchH
    
    mtrPnchAL = 18 #17.19
    mtrPnchAW = 6.25
    mtrPnchAH = 18.75
    mtrPnchYOffset = mtrPnchR
    mtrPnchZOffset = mountH - mtrPnchH
    
    wrPnchW = 6.25
    wrPnchL = 3.13
    wrPnchZ = 4.69
    wrPnchOffestY = 18 #17.5
    
    bpy.ops.mesh.primitive_cube_add(radius=1, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    motorMount = bpy.context.active_object
    motorMount.name = "motorMount"
    bpy.ops.transform.resize(value=(mountL/2, mountW/2, mountH/2), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    bpy.ops.mesh.primitive_cone_add(radius1=mtrPnchR, radius2=mtrPnchR, depth=mtrPnchH, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    motorMountPnch = bpy.context.active_object
    motorMountPnch.name = "motorMountPnch"
    bpy.ops.transform.translate(value=(0, 0, mtrPnchOffset/2), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    subtractObj(motorMount, motorMountPnch)
    deleteObj(motorMountPnch)

    bpy.ops.mesh.primitive_cube_add(radius=1, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    motorMountPnchA = bpy.context.active_object
    motorMountPnchA.name = "motorMountPnchA"
    bpy.ops.transform.resize(value=(mtrPnchAL/2, mtrPnchAW/2, mtrPnchAH/2), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.translate(value=(0, mtrPnchYOffset, mtrPnchZOffset/2), constraint_axis=(False, True, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)    
    
    subtractObj(motorMount, motorMountPnchA)
    deleteObj(motorMountPnchA)

    bpy.ops.mesh.primitive_cube_add(radius=1, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    wrPnch = bpy.context.active_object
    wrPnch.name = "wrPnch"
    bpy.ops.transform.resize(value=(wrPnchW/2, wrPnchL/2, wrPnchZ/2), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.translate(value=(0, wrPnchOffestY, -wrPnch.dimensions.z/2 + motorMount.dimensions.z/2), constraint_axis=(False, True, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    subtractObj(motorMount, wrPnch)
    deleteObj(wrPnch)

    
#BaseSupport1()
#StepperMotorMount()
ANDSbase()
#KeyChain()