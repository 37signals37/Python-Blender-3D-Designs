import bpy
from math import cos, sin, tan, sqrt, atan, radians

filename = "c:/Users/BeckyBot/Desktop/Botnyst/Prototype Models/Scripts/2nd Prototype/M.py"
exec(compile(open(filename).read(), filename, 'exec'))

KISSslicerMult = 27.75 #27.5, 26.667, 40

baseR = 3.5
baseD = 1
baseT = 0.1

podiumR = 0.5
podiumD = 3

tankR = 3
tankD = 1
tankT = 0.1

drainR = 0.25
drainD = 2
drainT = 0.1

railsR = drainR + 2 * drainT
railsD = podiumD - drainD
railsT = 0.1

slitL = railsR*2
slitW = 0.25
slitH = railsD

floatBallR = 0.275
floatBallT = 0.03

def floatTrapDesigns():
    
    bpy.ops.mesh.primitive_uv_sphere_add(size=floatBallR, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    ball = bpy.context.active_object
    ball.name = "ball"
    #bpy.ops.transform.translate(value=(0, 0, podiumD - drainD), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    
    #subtractObj(drain, ball)

    bpy.ops.mesh.primitive_uv_sphere_add(size=floatBallR - floatBallT, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    ballPnch = bpy.context.active_object
    ballPnch.name = "ballPnch"
#    bpy.ops.transform.translate(value=(0, 0, podiumD - drainD), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    bpy.ops.mesh.primitive_cube_add(radius=floatBallR, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    ballPnchHalver = bpy.context.active_object
    ballPnchHalver.name = "ballPnchHalver"
    bpy.ops.transform.translate(value=(0, 0, -floatBallR), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
#    raise Exception()
    subtractObj(ball, ballPnchHalver)
    bpy.ops.transform.translate(value=(0, 0, floatBallT), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)    
    subtractObj(ballPnch, ballPnchHalver)
    subtractObj(ball, ballPnch)    
    deleteObj(ballPnch)
    deleteObj(ballPnchHalver)

#    subtractObj(drain, ball)
#    subtractObj(rails, ball)

    bpy.ops.object.select_all(action='TOGGLE')
    bpy.ops.transform.resize(value=(KISSslicerMult, KISSslicerMult, KISSslicerMult), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    raise Exception() 
    
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
    
    bpy.data.objects['podium1'].select = True
    bpy.data.objects['podium2'].select = True
    bpy.data.objects['podium3'].select = True    
    bpy.ops.object.join()
    podium = bpy.context.active_object
    podium.name = "podium"
    
    bpy.ops.mesh.primitive_cylinder_add(radius=tankR, depth=tankD, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    tank = bpy.context.active_object
    tank.name = "tank"

    bpy.ops.mesh.primitive_cylinder_add(radius=tankR - tankT, depth=tankD - tankT, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    tankPnch = bpy.context.active_object
    tankPnch.name = "tankPnch"
    bpy.ops.transform.translate(value=(0, 0, baseT/2), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        
    subtractObj(tank, tankPnch)
    deleteObj(tankPnch)

    bpy.data.objects['tank'].select = True 
    bpy.ops.transform.translate(value=(0, 0, tankD/2 + podiumD), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)        
    bpy.data.objects['tank'].select = False
    
    bpy.ops.mesh.primitive_cylinder_add(radius=drainR + 2 * drainT, depth=drainD, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    drain = bpy.context.active_object
    drain.name = "drain"
    bpy.ops.transform.translate(value=(0, 0, -drainD/2 + podiumD + baseT), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    bpy.ops.mesh.primitive_cylinder_add(radius=drainR, depth=drainD, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    drainPnch = bpy.context.active_object
    drainPnch.name = "drainPnch"
    bpy.ops.transform.translate(value=(0, 0, -drainD/2 + podiumD + baseT), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        
    subtractObj(tank, drainPnch)
    subtractObj(drain, drainPnch)
    deleteObj(drainPnch)
   
    bpy.ops.mesh.primitive_cylinder_add(radius=railsR, depth=railsD, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    rails = bpy.context.active_object
    rails.name = "rails"
    bpy.ops.transform.translate(value=(0, 0, railsD/2 + baseT), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    
    bpy.ops.mesh.primitive_cylinder_add(radius=railsR - railsT, depth=railsD, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    railsPnch = bpy.context.active_object
    railsPnch.name = "railsPnch"
    bpy.ops.transform.translate(value=(0, 0, railsD/2 + baseT), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    subtractObj(rails, railsPnch)
    deleteObj(railsPnch)
    
    bpy.ops.mesh.primitive_cube_add(radius=1, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    railsPnch = bpy.context.active_object
    railsPnch.name = "railsPnch"
    bpy.ops.transform.resize(value=(slitL/2, slitW/2, slitH/2), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.translate(value=(0, 0, slitH/2), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    for i in range(0,3):
        subtractObj(rails, railsPnch)
        bpy.ops.transform.rotate(value=1.0472, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    deleteObj(railsPnch)
    
    bpy.ops.mesh.primitive_uv_sphere_add(size=floatBallR, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    ball = bpy.context.active_object
    ball.name = "ball"
    bpy.ops.transform.translate(value=(0, 0, podiumD - drainD), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    
    #subtractObj(drain, ball)

    bpy.ops.mesh.primitive_uv_sphere_add(size=floatBallR - floatBallT, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    ballPnch = bpy.context.active_object
    ballPnch.name = "ballPnch"
    bpy.ops.transform.translate(value=(0, 0, podiumD - drainD), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    bpy.ops.mesh.primitive_cube_add(radius=floatBallR, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    ballPnchHalver = bpy.context.active_object
    ballPnchHalver.name = "ballPnchHalver"
    bpy.ops.transform.translate(value=(0, 0, podiumD - drainD - floatBallR), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    subtractObj(ball, ballPnchHalver)
    bpy.ops.transform.translate(value=(0, 0, floatBallT), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)    
    subtractObj(ballPnch, ballPnchHalver)
    subtractObj(ball, ballPnch)    
    deleteObj(ballPnch)
    deleteObj(ballPnchHalver)

#    subtractObj(drain, ball)
#    subtractObj(rails, ball)

    raise Exception() 
    bpy.ops.object.select_all(action='TOGGLE')
    bpy.ops.transform.resize(value=(KISSslicerMult, KISSslicerMult, KISSslicerMult), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

floatTrapDesigns()    
    