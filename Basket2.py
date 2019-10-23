import bpy
from math import cos, sin, tan, sqrt, atan

filename = "c:/M.py"
exec(compile(open(filename).read(), filename, 'exec'))

KISSslicerMult = 25.62 

collarR = 0.5
collarT = 0.05

holderR = 0.875/2
holderT = 0.08
holderD = 0.6

domeT = 0.05
plantHoleR = 0.25
flapT = 0.02
flapW = 0.009
numOfFlaps = 7

casingR1 = 0.6 #0.6
casingR2 = 0
casingH = 2
casingT = 0.05
slitWidth = 0.04 #0.01
slitAngle = 30
casingAngle = 30
catchPnchR = 0.4

plantHolePunchYResize = 0.5
domeProtusion = 0.6

def basket2():

    bpy.ops.mesh.primitive_cylinder_add(vertices=32, radius=holderR - holderT, depth=holderD - holderT, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    holderPnch = bpy.context.active_object
    holderPnch.name = "holderPnch"
#    bpy.ops.transform.resize(value=(plantHoleR*2, 1, 1), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    bpy.ops.mesh.primitive_cylinder_add(vertices=32, radius=holderR, depth=holderD, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    holder = bpy.context.active_object
    holder.name = "holder"
    subtractObjCarve(holder, holderPnch)
    bpy.ops.transform.translate(value=(0, 0, -holderT), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    subtractObjCarve(holder, holderPnch)


    bpy.data.objects['holder'].select = True
    bpy.ops.transform.translate(value=(0, 0, holderT), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.data.objects['holder'].select = False

    #### Collar        
    bpy.ops.mesh.primitive_cylinder_add(vertices=64, radius=collarR, depth=collarT, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    collar = bpy.context.active_object
    collar.name = "collar"
    subtractObjCarve(collar, holderPnch)
    bpy.data.objects['collar'].select = True
    bpy.ops.transform.translate(value=(0, 0, holderD/2 - collarT/2), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.data.objects['collar'].select = False
    deleteObj(holderPnch)    

    bpy.ops.mesh.primitive_cylinder_add(vertices=32, radius=plantHoleR, depth=holderD, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    plantHolePnch = bpy.context.active_object
    plantHolePnch.name = "plantHolePnch"
    bpy.ops.transform.translate(value=(0, -holderR + plantHoleR + 1.25*holderT, flapT), constraint_axis=(False, True, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)    
    subtractObjCarve(holder, plantHolePnch)
    deleteObj(plantHolePnch)
   
    bpy.ops.mesh.primitive_cube_add(view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    slitPnch = bpy.context.active_object
    slitPnch.name = "slitPnch"
    bpy.ops.transform.resize(value=(flapW, plantHoleR, casingH), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.translate(value=(0, -holderR + holderT + plantHoleR, 0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    for i in range(0,numOfFlaps):
        subtractObjCarve(holder, slitPnch)
        bpy.ops.transform.rotate(value=pi/numOfFlaps, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    deleteObj(slitPnch)

    waterHolePunchR = 0.05
    numOfWaterHoles_Row = 6
    numOfWaterHoles_Col = 4
    rowSpacing = waterHolePunchR/2
    colSpacing = 2 * waterHolePunchR
    xTrans = 2*waterHolePunchR + rowSpacing
    yTrans = 2*waterHolePunchR + colSpacing
    
    bpy.ops.mesh.primitive_cylinder_add(vertices=32, radius=waterHolePunchR, depth=holderD*2, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    waterHolePnch = bpy.context.active_object
    waterHolePnch.name = "waterHolePnch"
    bpy.ops.transform.rotate(value=1.5708, axis=(1, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.translate(value=(0, holderD, 0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.translate(value=(xTrans * numOfWaterHoles_Row/2 - xTrans/4, 0, numOfWaterHoles_Col * waterHolePunchR), constraint_axis=(True, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
            
    for j in range(0,numOfWaterHoles_Col):
        for i in range(0, numOfWaterHoles_Row):
            subtractObjCarve(holder, waterHolePnch)
            bpy.ops.transform.translate(value=(-xTrans, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
                
        if(j%2 == 0):
            bpy.ops.transform.translate(value=(2.5*numOfWaterHoles_Row*waterHolePunchR + 1*waterHolePunchR, 0, -2*waterHolePunchR), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        else:
            bpy.ops.transform.translate(value=(2.5*(numOfWaterHoles_Row-1)*waterHolePunchR + waterHolePunchR, 0, -0.101387), constraint_axis=(True, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    deleteObj(waterHolePnch)

    bpy.ops.mesh.primitive_uv_sphere_add(size=collarR, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    dome = bpy.context.active_object
    dome.name = "dome"
    bpy.ops.transform.resize(value=(1, 1, domeProtusion), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    bpy.ops.mesh.primitive_uv_sphere_add(size=collarR-domeT, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    domePnch = bpy.context.active_object
    domePnch.name = "domePnch"
    bpy.ops.transform.resize(value=(1, 1, domeProtusion), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    subtractObjCarve(dome, domePnch)
    deleteObj(domePnch)

    bpy.ops.mesh.primitive_cube_add(radius=collarR, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    domePnch = bpy.context.active_object
    domePnch.name = "domePnch"
    bpy.ops.transform.translate(value=(0, 0, -collarR), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    subtractObjCarve(dome, domePnch)
    deleteObj(domePnch)

    bpy.data.objects['dome'].select = True
    bpy.ops.transform.translate(value=(0, 0, holderD/2), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.data.objects['dome'].select = False

    bpy.ops.mesh.primitive_cylinder_add(vertices=32, radius=plantHoleR, depth=holderD*2, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    plantHolePnch = bpy.context.active_object
    plantHolePnch.name = "plantHolePnch"
    bpy.ops.transform.resize(value=(1, plantHolePunchYResize, 1), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.translate(value=(0, 0, holderD), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)    
    bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
    bpy.ops.transform.rotate(value=-0.758135, axis=(1, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    subtractObjCarve(dome, plantHolePnch)
    subtractObjCarve(collar, plantHolePnch)
    subtractObjCarve(holder, plantHolePnch)
    deleteObj(plantHolePnch)

    raise Exception()

    bpy.data.objects['collar'].select = True
    bpy.data.objects['dome'].select = True
    bpy.data.objects['holder'].select = True
    bpy.ops.object.join()
    bpy.ops.transform.resize(value=(KISSslicerMult, KISSslicerMult, KISSslicerMult), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

basket2()
    
 