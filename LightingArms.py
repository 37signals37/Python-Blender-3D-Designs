import bpy
from math import cos, sin, tan, sqrt, atan, radians, floor

filename = "c:/Users/BeckyBot/Desktop/Botnyst/Prototype Models/Scripts/M.py"
exec(compile(open(filename).read(), filename, 'exec'))

shellR = 1
shellD = 2
shellT = 0.05

collarR = shellR + 0.25
collarD = shellT

mainBlockL = 1.3 #1.3 #1.25
mainBlockW = 1.5
mainBlockH = 0.15 #0.2
mainBlockT = 0.33 #0.3
slotPnchT = 0.1 #0.06
slotPnchD = 0.085 #0.15
leadR = 0.09 #0.11 #0.12 #0.1
cornerPnchR = 0.3
screwPnchR = 0.1

armsL = 0.3
armsW = 0.6
armsH = 0.03
connectSpacer = 0.01

def arm():

    bpy.ops.mesh.primitive_cylinder_add(radius=collarR, depth=collarD, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    collar = bpy.context.active_object
    collar.name = "collar"
    bpy.ops.transform.translate(value=(0, 0, collarD/2), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    bpy.ops.mesh.primitive_cylinder_add(radius=shellR, depth=shellD, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    shell = bpy.context.active_object
    shell.name = "shell"
    
    subtractObj(collar, shell)
    
    bpy.ops.transform.translate(value=(0, 0, shellD/2), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
           
def armHolder():
    bpy.ops.mesh.primitive_uv_sphere_add(view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))

def LEDHolder():
    #bpy.ops.mesh.primitive_cylinder_add(radius = mainBlockL/2, depth = mainBlockH, vertices=32, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    bpy.ops.mesh.primitive_cube_add(view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    mainBlock = bpy.context.active_object
    mainBlock.name = "mainBlock"
    bpy.ops.transform.resize(value=(mainBlockL/2, mainBlockW/2, mainBlockH), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    bpy.ops.mesh.primitive_cylinder_add(radius = (mainBlockL-mainBlockT)/2, vertices=32, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    mainBlockPnch = bpy.context.active_object
    mainBlockPnch.name = "mainBlockPnch"

    subtractObj(mainBlock, mainBlockPnch)
    deleteObj(mainBlockPnch)

    bpy.ops.mesh.primitive_cube_add(radius = mainBlockL/2, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))    
    mainBlockPnch = bpy.context.active_object
    mainBlockPnch.name = "mainBlockPnch"
    bpy.ops.transform.translate(value=(0, 3*mainBlockL/4, 0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    subtractObj(mainBlock, mainBlockPnch)
    deleteObj(mainBlockPnch)

    bpy.ops.mesh.primitive_cylinder_add(radius = (mainBlockL - mainBlockT + slotPnchT)/2, depth = slotPnchD, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    slotPnch = bpy.context.active_object
    slotPnch.name = "slotPnch"
    subtractObj(mainBlock, slotPnch)
    deleteObj(slotPnch)    

    bpy.ops.mesh.primitive_cube_add(view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))    
    slotPnch = bpy.context.active_object
    slotPnch.name = "slotPnch"
    bpy.ops.transform.resize(value=((mainBlockL - mainBlockT + slotPnchT)/2, (mainBlockL - mainBlockT + slotPnchT)/2, slotPnchD/2), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.translate(value=(0, (mainBlockL - mainBlockT + slotPnchT)/2, 0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    subtractObj(mainBlock, slotPnch)
    deleteObj(slotPnch)    
     
    bpy.ops.mesh.primitive_cylinder_add(radius=leadR, depth=mainBlockL/2, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    leadPnch = bpy.context.active_object
    leadPnch.name = "leadPnch"
    bpy.ops.transform.rotate(value=1.5708, axis=(0, 1, 0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.translate(value=(mainBlockL/2, 0, slotPnchD/2), constraint_axis=(True, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
    bpy.ops.transform.rotate(value=-pi/3, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    subtractObj(mainBlock, leadPnch)
    bpy.ops.transform.rotate(value=-pi/3, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    subtractObj(mainBlock, leadPnch)
    deleteObj(leadPnch)

    bpy.ops.mesh.primitive_cylinder_add(radius=cornerPnchR, depth=mainBlockH*2, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    cornerPnch = bpy.context.active_object
    cornerPnch.name = "cornerPnch"
    #bpy.ops.transform.rotate(value=1.5708, axis=(1, 0, 0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.translate(value=(mainBlockL/2, -mainBlockW/2, 0), constraint_axis=(True, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    subtractObj(mainBlock, cornerPnch)
    bpy.ops.transform.translate(value=(-mainBlockL, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    subtractObj(mainBlock, cornerPnch)
    deleteObj(cornerPnch)

    bpy.ops.mesh.primitive_uv_sphere_add(size=cornerPnchR, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    hinge = bpy.context.active_object
    hinge.name = "hinge"
    bpy.ops.transform.translate(value=(0, -mainBlockW/2, 0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    bpy.data.objects['hinge'].select = True
    bpy.data.objects['mainBlock'].select = True
    bpy.ops.object.join()

    raise Exception()

    bpy.ops.mesh.primitive_cylinder_add(radius=(mainBlockL - 2 * cornerPnchR)/2, depth=mainBlockH*2, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    hinge = bpy.context.active_object
    hinge.name = "hinge"

    bpy.ops.mesh.primitive_cube_add(view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    hingePnch = bpy.context.active_object
    hingePnch.name = "hingePnch"
    bpy.ops.transform.translate(value=(0, 1, 0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)    
    subtractObj(hinge, hingePnch)
    deleteObj(hingePnch)
    
    bpy.data.objects['hinge'].select = True
    bpy.ops.transform.translate(value=(0, -mainBlockW/2, 0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)    
    bpy.data.objects['hinge'].select = False
       
    bpy.ops.mesh.primitive_cylinder_add(radius=screwPnchR, depth=mainBlockH*2, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    screwPnch = bpy.context.active_object
    screwPnch.name = "screwPnch"
#    bpy.ops.transform.translate(value=(0, -mainBlockW/2 + (mainBlockW/2 - (mainBlockL-mainBlockT)/2)/2, 0), constraint_axis=(True, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.translate(value=(0, -mainBlockW/2, 0), constraint_axis=(True, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    subtractObj(mainBlock, screwPnch)
    subtractObj(hinge, screwPnch)
    deleteObj(screwPnch)

def LEDHolderConnect():

    bpy.ops.mesh.primitive_cube_add(view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    bottomArm = bpy.context.active_object
    bottomArm.name = "bottomArm"
    bpy.ops.transform.resize(value=(armsL, armsW, armsH), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.translate(value=(0, -mainBlockW/2 - armsW/2, -armsH - mainBlockH - connectSpacer), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    bpy.ops.mesh.primitive_cube_add(view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    topArm = bpy.context.active_object
    topArm.name = "topArm"
    bpy.ops.transform.resize(value=(armsL, armsW, armsH), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.translate(value=(0, -mainBlockW/2 - armsW/2, armsH + mainBlockH + connectSpacer), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    bpy.ops.mesh.primitive_cube_add(view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    backArm = bpy.context.active_object
    backArm.name = "backArm"
    bpy.ops.transform.resize(value=(armsL, 2 * armsH + connectSpacer + mainBlockH, armsH), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.rotate(value=1.5708, axis=(1, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.translate(value=(0, -mainBlockW/2 - 3*armsW/2 + armsL, 0), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    bpy.ops.mesh.primitive_cylinder_add(radius=screwPnchR, depth=mainBlockH*4, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    screwPnch = bpy.context.active_object
    screwPnch.name = "screwPnch"
    bpy.ops.transform.rotate(value=1.5708, axis=(0, 1, 0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)    
    bpy.ops.transform.translate(value=(0, -mainBlockW/2 - 3*armsW/2 + armsL, 0), constraint_axis=(True, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)    
    
    subtractObj(backArm, screwPnch)
    deleteObj(screwPnch)

    bpy.data.objects['topArm'].select = True
    bpy.data.objects['bottomArm'].select = True
    bpy.data.objects['backArm'].select = True
    bpy.ops.object.join()

def LEDHolderConnect1():

    hingeR = 0.3
    bridgeL = 0.3
    bridgeW = 0.5
    bridgeH = 0.05 #0.04 #0.03
    bridgeOffset = 0.275 #0.25 #0.2

    bpy.ops.mesh.primitive_uv_sphere_add(size=hingeR, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    leftHinge = bpy.context.active_object
    leftHinge.name = "leftHinge"
    bpy.ops.transform.translate(value=(0, -bridgeW + hingeR, 0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    
#    bpy.ops.mesh.primitive_uv_sphere_add(size=hingeR, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
#    rightHinge = bpy.context.active_object
#    rightHinge.name = "rightHinge"
#    bpy.ops.transform.translate(value=(0, bridgeW - hingeR, 0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    
    bpy.ops.mesh.primitive_cube_add(view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    bottomArm = bpy.context.active_object
    bottomArm.name = "bottomArm"
    bpy.ops.transform.resize(value=(bridgeL, bridgeW, bridgeH), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.translate(value=(0, 0, -bridgeOffset), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    bpy.ops.mesh.primitive_cube_add(view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    topArm = bpy.context.active_object
    topArm.name = "topArm"
    bpy.ops.transform.resize(value=(bridgeL, bridgeW, bridgeH), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.translate(value=(0, 0, bridgeOffset), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    bpy.ops.mesh.primitive_cube_add(view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    armBridge = bpy.context.active_object
    armBridge.name = "armBridge"
    bpy.ops.transform.resize(value=(bridgeL, bridgeW/3, bridgeOffset), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.translate(value=(0, bridgeW - bridgeW/3, 0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    

    subtractObj(bottomArm, leftHinge)
    subtractObj(topArm, leftHinge)
#    subtractObj(bottomArm, rightHinge)
    deleteObj(leftHinge)
#    deleteObj(rightHinge)

    
#    bpy.ops.transform.translate(value=(0, -mainBlockW/2 - armsW + cornerPnchR, cornerPnchR), constraint_axis=(False, True, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
#    bpy.ops.transform.translate(value=(0, -mainBlockW/2 - 3*armsW/2 + armsL, -armsH/2), constraint_axis=(False, True, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)    
        

def extendingArm():
    bottomR = 1
    topR = 0.95
    depth = 2
    thcknss = 0.03
    iterations = 4
    heightIncrementor = 0
    
    for i in range(0,iterations):

        bpy.ops.mesh.primitive_cone_add(radius1=bottomR, radius2=topR, depth=depth, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
        outer = bpy.context.active_object
        outer.name = "outer" + str(i)

        bpy.ops.mesh.primitive_cone_add(radius1=topR - thcknss, radius2=bottomR - thcknss, depth=depth, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
        inner = bpy.context.active_object
        inner.name = "inner"
                        
        subtractObj(outer, inner)
        deleteObj(inner)
        print(heightIncrementor)
        heightIncrementor = heightIncrementor + depth     
        print(heightIncrementor)
        print("---")
        
        bpy.data.objects['outer' + str(i)].select = True        
        bpy.ops.transform.translate(value=(0, 0,  heightIncrementor), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        bpy.data.objects['outer' + str(i)].select = False

        bottomR = topR
        topR = topR - 0.05

#arm()
#LEDHolder()
#LEDHolderConnect1()
extendingArm()