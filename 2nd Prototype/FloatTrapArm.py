import bpy
from math import cos, sin, tan, sqrt, atan, radians

#filename = "c:/Users/BeckyBot/Desktop/Botnyst/Prototype Models/Scripts/2nd Prototype/M.py"
filename = "e:/Blender Scripts/Scripts/2nd Prototype/M.py"
exec(compile(open(filename).read(), filename, 'exec'))

KISSslicerMult = 25.62 #27.5, 26.667, 40

baseR = 2
baseD = 1
baseT = 0.05

podiumR = 0.15
podiumD = 3

tankR = 2
tankD = 1.25
tankT = 0.05

drainR = 0.06 # 0.025
drainD = 2.75
drainT = 0.05

plugR = drainR
plugD = 0.3

domeR = 0.2 + drainR + 2 * drainT
domeT = 0.07
waterHolePnchR = 0.05
waterHolePnchD = 0.1

armL = 1
armW = drainR + drainR * 0.25
armH = 0.1

hingeL = 2 * drainR + 4 * drainT
hingeW = drainR * 3
hingeH = 0.4

hingeR = hingeH/2
hingeD = drainR * 2

hingePnchR = 0.05
hingePnchD = 0.5

boltPnchR = 0.15

floatBallR = 0.5
floatBallT = 0.08 #0.04

#bpy.ops.mesh.bolt_add(bf_Shank_Length=0, bf_Shank_Dia=3, bf_Phillips_Bit_Depth=1.14315, bf_Allen_Bit_Depth=1.5, bf_Allen_Bit_Flat_Distance=2.5, bf_Hex_Head_Height=2, bf_Hex_Head_Flat_Distance=5.5, bf_CounterSink_Head_Dia=6.3, bf_Cap_Head_Height=3, bf_Cap_Head_Dia=5.5, bf_Dome_Head_Dia=5.6, bf_Pan_Head_Dia=5.6, bf_Philips_Bit_Dia=1.82, bf_Thread_Length=6, bf_Major_Dia=3, bf_Pitch=0.7076, bf_Minor_Dia=2.62111, bf_Crest_Percent=10, bf_Root_Percent=10, bf_Hex_Nut_Height=2.4, bf_Hex_Nut_Flat_Distance=5.5)
#bpy.ops.mesh.bolt_add(bf_Model_Type='bf_Model_Bolt', bf_Shank_Length=0, bf_Shank_Dia=3, bf_Phillips_Bit_Depth=1.14315, bf_Allen_Bit_Depth=1.5, bf_Allen_Bit_Flat_Distance=2.5, bf_Hex_Head_Height=2, bf_Hex_Head_Flat_Distance=5.5, bf_CounterSink_Head_Dia=6.3, bf_Cap_Head_Height=3, bf_Cap_Head_Dia=5.5, bf_Dome_Head_Dia=5.6, bf_Pan_Head_Dia=5.6, bf_Philips_Bit_Dia=1.82, bf_Thread_Length=6, bf_Major_Dia=3, bf_Pitch=0.71, bf_Minor_Dia=2.62111, bf_Crest_Percent=10, bf_Root_Percent=10, bf_Hex_Nut_Height=2.4, bf_Hex_Nut_Flat_Distance=5.5)


def floatTrapDesigns():
    bpy.ops.mesh.primitive_cylinder_add(radius=baseR, depth=baseD, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    base = bpy.context.active_object
    base.name = "base"
    
    bpy.ops.mesh.primitive_cylinder_add(radius=baseR - baseT, depth=baseD - baseT, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    basePnch = bpy.context.active_object
    basePnch.name = "basePnch"
    bpy.ops.transform.translate(value=(0, 0, baseT/2), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    subtractObj(base, basePnch)
    deleteObj(basePnch)

    bpy.data.objects['base'].select = True 
    bpy.ops.transform.translate(value=(0, 0, baseD/2), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)        
    bpy.data.objects['base'].select = False

    bpy.ops.mesh.primitive_uv_sphere_add(size=domeR, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    dome = bpy.context.active_object
    dome.name = "dome"
    bpy.ops.transform.resize(value=(1, 1, 2), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    
    bpy.ops.mesh.primitive_uv_sphere_add(size=domeR - domeT, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    domePnch = bpy.context.active_object
    domePnch.name = "domePnch"
    bpy.ops.transform.resize(value=(1, 1, 2), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    
    bpy.ops.mesh.primitive_cube_add(radius=domeR, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    domeHalfPnch = bpy.context.active_object
    domeHalfPnch.name = "domeHalfPnch"
    bpy.ops.transform.translate(value=(0, 0, -domeR), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    subtractObj(dome, domeHalfPnch)
    subtractObj(domePnch, domeHalfPnch)
    deleteObj(domeHalfPnch)
    
    bpy.data.objects['domePnch'].select = True 
    bpy.ops.transform.translate(value=(0, 0, domeT/2), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)        
    bpy.data.objects['domePnch'].select = False
    subtractObj(dome, domePnch)
    deleteObj(domePnch)

    bpy.ops.mesh.primitive_cylinder_add(radius=waterHolePnchR, depth=waterHolePnchD, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    waterHolePnch = bpy.context.active_object
    waterHolePnch.name = "waterHolePnch"
    bpy.ops.transform.rotate(value=1.5708, axis=(0, 1, 0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)


    raise Exception()

    bpy.data.objects['dome'].select = True 
    bpy.ops.transform.translate(value=(0, 0, baseT), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)        
    bpy.data.objects['dome'].select = False      
   
    bpy.ops.mesh.primitive_cylinder_add(radius=podiumR, depth=podiumD, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    podium1 = bpy.context.active_object
    podium1.name = "podium1"
    bpy.ops.transform.translate(value=(baseR/2, baseR/2, podiumD/2), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    bpy.ops.mesh.primitive_cylinder_add(radius=podiumR, depth=podiumD, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    podium2 = bpy.context.active_object
    podium2.name = "podium2"
    bpy.ops.transform.translate(value=(-baseR/2, baseR/2, podiumD/2), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    
    bpy.ops.mesh.primitive_cylinder_add(radius=podiumR, depth=podiumD, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    podium3 = bpy.context.active_object
    podium3.name = "podium3"
    bpy.ops.transform.translate(value=(-baseR/2, -baseR/2, podiumD/2), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    
    bpy.ops.mesh.primitive_cylinder_add(radius=podiumR, depth=podiumD, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    podium4 = bpy.context.active_object
    podium4.name = "podium4"
    bpy.ops.transform.translate(value=(baseR/2, -baseR/2, podiumD/2), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    
    bpy.data.objects['podium1'].select = True
    bpy.data.objects['podium2'].select = True
    bpy.data.objects['podium3'].select = True    
    bpy.data.objects['podium4'].select = True    
    bpy.ops.object.join()
    podium = bpy.context.active_object
    podium.name = "podium"
    
    bpy.ops.mesh.primitive_cylinder_add(radius=tankR, depth=tankD, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    tank = bpy.context.active_object
    tank.name = "tank"

    bpy.ops.mesh.primitive_cylinder_add(radius=tankR - tankT, depth=tankD - tankT, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    tankPnch = bpy.context.active_object
    tankPnch.name = "tankPnch"
    bpy.ops.transform.translate(value=(0, 0, baseT), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        
    subtractObj(tank, tankPnch)
    deleteObj(tankPnch)

    bpy.data.objects['tank'].select = True 
    bpy.ops.transform.translate(value=(0, 0, tankD/2 + podiumD -baseT), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)        
    bpy.data.objects['tank'].select = False
    subtractObj(tank, podium)
    
    bpy.ops.mesh.bolt_add(bf_Model_Type='bf_Model_Nut', bf_Shank_Length=0, bf_Shank_Dia=3, bf_Phillips_Bit_Depth=1.14315, bf_Allen_Bit_Depth=1.5, bf_Allen_Bit_Flat_Distance=2.5, bf_Hex_Head_Height=2, bf_Hex_Head_Flat_Distance=5.5, bf_CounterSink_Head_Dia=6.3, bf_Cap_Head_Height=3, bf_Cap_Head_Dia=5.5, bf_Dome_Head_Dia=5.6, bf_Pan_Head_Dia=5.6, bf_Philips_Bit_Dia=1.82, bf_Thread_Length=6, bf_Major_Dia=3, bf_Pitch=0.71, bf_Minor_Dia=2.62111, bf_Crest_Percent=10, bf_Root_Percent=10, bf_Hex_Nut_Height=2.4, bf_Hex_Nut_Flat_Distance=5.5)
    nut = bpy.context.active_object
    nut.name = "nut"
    bpy.ops.transform.translate(value=(0, 0, podiumD - 3*tankT/4), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    bpy.ops.mesh.primitive_cylinder_add(radius = boltPnchR, depth = 100, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    boltPnch = bpy.context.active_object
    boltPnch.name = "boltPnch"
    subtractObj(tank, boltPnch)
    deleteObj(boltPnch)


    bpy.ops.mesh.bolt_add(bf_Shank_Length=0, bf_Shank_Dia=3, bf_Phillips_Bit_Depth=1.14315, bf_Allen_Bit_Depth=1.5, bf_Allen_Bit_Flat_Distance=2.5, bf_Hex_Head_Height=2, bf_Hex_Head_Flat_Distance=5.5, bf_CounterSink_Head_Dia=6.3, bf_Cap_Head_Height=3, bf_Cap_Head_Dia=5.5, bf_Dome_Head_Dia=5.6, bf_Pan_Head_Dia=5.6, bf_Philips_Bit_Dia=1.82, bf_Thread_Length=6, bf_Major_Dia=3, bf_Pitch=0.71, bf_Minor_Dia=2.62111, bf_Crest_Percent=10, bf_Root_Percent=10, bf_Hex_Nut_Height=2.4, bf_Hex_Nut_Flat_Distance=5.5)
    bolt = bpy.context.active_object
    bolt.name = "bolt"
    bpy.ops.transform.translate(value=(0, 0, podiumD-tankT), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    bpy.ops.mesh.primitive_cube_add(view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    headPnch = bpy.context.active_object
    headPnch.name = "headPnch"
    bpy.ops.transform.translate(value=(0, 0, 1 + podiumD - 3*tankT/4 + nut.dimensions.z), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    subtractObj(bolt, headPnch)
    deleteObj(headPnch)
        
    bpy.ops.mesh.primitive_cylinder_add(radius=drainR + 2 * drainT, depth=drainD, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    drain = bpy.context.active_object
    drain.name = "drain"
    bpy.ops.transform.translate(value=(0, 0, -drainD/2 + podiumD), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    bpy.ops.mesh.primitive_cylinder_add(radius=drainR, depth=drainD * 2, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    drainPnch = bpy.context.active_object
    drainPnch.name = "drainPnch"
    bpy.ops.transform.translate(value=(0, 0, -drainD/2 + podiumD), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        
    subtractObj(bolt, drainPnch)        
    subtractObj(tank, drainPnch)
    subtractObj(dome, drain)
    raise Exception()
    subtractObj(drain, drainPnch)
    deleteObj(drainPnch)

    raise Exception()

#    bpy.ops.mesh.primitive_cube_add(view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
#    hingePnch = bpy.context.active_object
#    hingePnch.name = "hingePnch"
#    bpy.ops.transform.resize(value=(hingeL/2, hingeW/2, hingeH/2), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
#    bpy.ops.transform.translate(value=(0, 0, podiumD - drainD + hingeH/2), constraint_axis=(True, True, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    
#    subtractObj(drain, hingePnch)
#    deleteObj(hingePnch)
    
    bpy.ops.mesh.primitive_cube_add(view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    leftHinge = bpy.context.active_object
    leftHinge.name = "leftHinge"
    bpy.ops.transform.resize(value=(hingeL, (drain.dimensions.x/2 - hingeW/2)/2, hingeH/2), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.translate(value=(-hingeL + drain.dimensions.x/2, -drain.dimensions.y/2, podiumD - drainD), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    bpy.ops.mesh.primitive_cube_add(view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    rightHinge = bpy.context.active_object
    rightHinge.name = "rightHinge"
    bpy.ops.transform.resize(value=(hingeL, (drain.dimensions.x/2 - hingeW/2)/2, hingeH/2), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.translate(value=(-hingeL + drain.dimensions.x/2, drain.dimensions.y/2, podiumD - drainD), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    bpy.ops.mesh.primitive_cylinder_add(radius=hingePnchR, depth=hingePnchD, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    hingePnch = bpy.context.active_object
    hingePnch.name = "hingePnch"
    bpy.ops.transform.rotate(value=1.5708, axis=(1, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.translate(value=(-hingeL, 0, -hingeH/4 + podiumD - drainD), constraint_axis=(True, True, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    subtractObj(leftHinge, hingePnch)
    subtractObj(rightHinge, hingePnch)
    
    bpy.ops.mesh.primitive_cube_add(view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    arm = bpy.context.active_object
    arm.name = "arm"
    bpy.ops.transform.resize(value=(hingeL*1.5, armW, armH), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.translate(value=(0, 0, podiumD - drainD -armH), constraint_axis=(True, True, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    
    subtractObj(arm, hingePnch)
#    deleteObj(hingePnch)


    bpy.ops.mesh.primitive_uv_sphere_add(size=floatBallR, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    ball = bpy.context.active_object
    ball.name = "ball"
    bpy.ops.transform.resize(value=(1, 1, 0.25), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.translate(value=(armL/2 + floatBallR - floatBallR/5, 0, podiumD - drainD - armH), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)


    bpy.ops.mesh.primitive_uv_sphere_add(size=floatBallR - floatBallT, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    ballPnch = bpy.context.active_object
    ballPnch.name = "ballPnch"
    bpy.ops.transform.resize(value=(1, 1, 0.25), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.translate(value=(armL/2 + floatBallR - floatBallR/5, 0, podiumD - drainD - armH), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
 
    subtractObj(ball, ballPnch)
    deleteObj(ballPnch)          

    bpy.ops.object.select_all(action='TOGGLE')
    bpy.ops.transform.resize(value=(KISSslicerMult, KISSslicerMult, KISSslicerMult), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
                         




    subtractObj(leftHinge, hinge)
    subtractObj(rightHinge, hinge)
    deleteObj(hinge)

    bpy.ops.mesh.primitive_cylinder_add(radius = hingeR, depth = hingeD, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    hinge = bpy.context.active_object
    hinge.name = "hinge"
    bpy.ops.transform.rotate(value=1.5708, axis=(1, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        
    bpy.ops.mesh.primitive_cube_add(view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    arm = bpy.context.active_object
    arm.name = "arm"
    bpy.ops.transform.resize(value=(armL/2, armW, armH/2), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    #bpy.ops.transform.translate(value=(0, 0, armH), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    #bpy.context.scene.cursor_location = (-armL/2,0.0,armH) 
    #bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
    #bpy.ops.transform.rotate(value=-7.5/180 * pi, axis=(0, 1, 0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    #subtractObj(drain, arm)

#    bpy.ops.mesh.primitive_wedge_add(size_x=1.79, size_y=2, size_z = 2 * drainR + 4 * drainT)
#    bpy.ops.transform.rotate(value=1.5708, axis=(1, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)








    bpy.ops.object.select_all(action='TOGGLE')
    bpy.ops.transform.resize(value=(KISSslicerMult, KISSslicerMult, KISSslicerMult), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
                      
                  
floatTrapDesigns()    
    