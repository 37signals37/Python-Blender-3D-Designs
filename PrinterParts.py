#Repetier multiplier 4
import bpy
from math import cos, sin, tan, sqrt, atan

filename = "c:/BlenderScripts/M.py"
exec(compile(open(filename).read(), filename, 'exec'))

mainL = 7
mainW = 0.9 #last 0.5, 65
mainH = 1.25 #last 0.85,1

mainPnchL = 2
mainPnchW = 0.55 #last 0.4
mainPnchH = 0.75

mainPnchX = -5.5 #last -4.5
mainPnchZ = 1.35 #last 1.15

screwPnchR = 0.6 #last 0.45
screwPnchL = 3 * mainW

screwPnchX1 = 4
screwPnchX2 = 2

stageHeight = punchHeight = 0.85 #last 1, 0.88

supportLength = 2
supportWidth = 1
supportHeight = 1.33

nutL = 0.55 #last 0.5, 0.6
nutW = 0.3
nutH = nutL * 12/7

thcknss = 0.5

wedgeL = 3.75 #last 3,4, 3.5
wedgeW = mainW
wedgeH = mainH + thcknss

wedgeBffr = 0.45 #last 0.15, 0.4

stgHght = 1 #last 1.25

def makeRod():
    bpy.ops.mesh.primitive_cube_add(radius=1, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    main = bpy.context.active_object
    main.name = "main"
    bpy.ops.transform.resize(value=(mainL, mainW, mainH), constraint_axis=(True, True, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    
    bpy.ops.mesh.primitive_cube_add(radius=1, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    mainPnch = bpy.context.active_object
    mainPnch.name = "mainPnch"
    bpy.ops.transform.resize(value=(mainPnchL, mainPnchW, mainPnchH), constraint_axis=(True, True, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.rotate(value=1.5708, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.translate(value=(mainPnchX, 0, mainPnchZ), constraint_axis=(True, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    subtractObj(main,mainPnch)
    bpy.ops.transform.translate(value=(0, 0, -2*mainPnchZ), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    subtractObj(main,mainPnch)
    deleteObj(mainPnch)
    
    bpy.ops.mesh.primitive_cylinder_add(radius=screwPnchR, depth=screwPnchL, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    screwPnch = bpy.context.active_object
    screwPnch.name = "screwPnch"
    bpy.ops.transform.rotate(value=1.5708, axis=(1, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.translate(value=(screwPnchX1, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    subtractObj(main,screwPnch)
    bpy.ops.transform.translate(value=(screwPnchX2, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    subtractObj(main,screwPnch)
    deleteObj(screwPnch)
    
    for i in range(0,3):
        bpy.ops.mesh.primitive_cube_add(radius=1, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
        nutPnch = bpy.context.active_object
        nutPnch.name = "nutPnch" + str(i)
        bpy.ops.transform.resize(value=(nutL, nutW, nutH), constraint_axis=(True, True, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)        
        bpy.ops.transform.rotate(value=1.0472 * i, axis=(0, 1, 0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    for i in range(0,3):
        bpy.data.objects['nutPnch' + str(i)].select = True

    bpy.ops.object.join()
    nutPnch = bpy.context.active_object
    nutPnch.name = "nutPnch"        
    bpy.ops.transform.translate(value=(screwPnchX1, (main.dimensions.y-nutPnch.dimensions.y)/2, 0), constraint_axis=(True, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    subtractObj(main, nutPnch)
    deleteObj(nutPnch)

def ScrewSupport():
    bpy.ops.mesh.primitive_cube_add(radius=1, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    main = bpy.context.active_object
    main.name = "main"
    bpy.ops.transform.resize(value=(supportLength, supportWidth, supportHeight), constraint_axis=(True, True, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        
    bpy.ops.mesh.primitive_cube_add(radius=1, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    punch = bpy.context.active_object
    punch.name = "punch"
    bpy.ops.transform.resize(value=(supportLength + 0.01,supportWidth + 0.01, stageHeight), constraint_axis=(True, True, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)        
    bpy.ops.transform.translate(value=(0, supportHeight - stageHeight, 0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    subtractObj(main, punch)
    bpy.ops.transform.rotate(value=1.5708, axis=(0, 1, 0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    subtractObj(main, punch)
    deleteObj(punch)

    bpy.ops.mesh.primitive_wedge_add()
    wedge = bpy.context.active_object
    wedge.name = "wedge"
    bpy.ops.transform.rotate(value=-1.5708, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)


def Spring():
    print()
    
def Wedge():
    bpy.ops.mesh.primitive_cube_add(radius=1, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    main = bpy.context.active_object
    main.name = "main"
    bpy.ops.transform.resize(value=(mainL, mainW + wedgeBffr, mainH + wedgeBffr), constraint_axis=(True, True, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        
    bpy.ops.mesh.primitive_cube_add(radius=1, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    wedge = bpy.context.active_object
    wedge.name = "wedge"
    bpy.ops.transform.resize(value=(wedgeL + wedgeBffr, wedgeW, wedgeH + wedgeBffr), constraint_axis=(True, True, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.rotate(value=1.5708, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.translate(value=(0,wedgeL - mainW - thcknss,0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        
    subtractObj(wedge, main)
    deleteObj(main)

    bpy.ops.mesh.primitive_cube_add(radius=1, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    stgPnch = bpy.context.active_object
    stgPnch.name = "stgPnch"      
    bpy.ops.transform.resize(value=(wedgeW+0.1, wedgeL, stgHght), constraint_axis=(True, True, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)    
    bpy.ops.transform.translate(value=(0,wedgeL + mainW + wedgeBffr + thcknss,0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)    
    subtractObj(wedge, stgPnch)    
    bpy.ops.transform.translate(value=(0,0,stgHght * 2 + thcknss), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)    
    subtractObj(wedge, stgPnch)
    bpy.ops.transform.translate(value=(0,0,-2 * (stgHght * 2 + thcknss)), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)    
    subtractObj(wedge, stgPnch)    
    deleteObj(stgPnch)

def YArmSupportTensionor():
        
    frameWidth = 2
    frameLength = 6
    frameHeight = 0.8

    postWidth = 0.8
    postHeight = 1.8
    postDistance = 3

    punchHeight = 1.25

    bpy.ops.mesh.primitive_cube_add(radius=1, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    frame = bpy.context.active_object
    frame.name = "frame"      
    bpy.ops.transform.resize(value=(frameWidth,frameLength,frameHeight), constraint_axis=(True, True, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)    
    bpy.ops.transform.translate(value=(0,0,frameHeight), constraint_axis=(False,False,True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)    
    
    bpy.ops.mesh.primitive_cube_add(radius=1, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    leftPost = bpy.context.active_object
    leftPost.name = "leftPost"      
    bpy.ops.transform.resize(value=(frameWidth,postWidth,postHeight), constraint_axis=(True, True, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)    
    bpy.ops.transform.translate(value=(0,-postDistance,frameHeight * 2 + postHeight), constraint_axis=(False, True,True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)    
    
    bpy.ops.mesh.primitive_cube_add(radius=1, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    rightPost = bpy.context.active_object
    rightPost.name = "rightPost"      
    bpy.ops.transform.resize(value=(frameWidth,postWidth,postHeight), constraint_axis=(True, True, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)    
    bpy.ops.transform.translate(value=(0,postDistance,frameHeight * 2 + postHeight), constraint_axis=(False, True,True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)    
    
    bpy.ops.mesh.primitive_cylinder_add(radius=screwPnchR, depth=frameLength*2, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    screwPunch = bpy.context.active_object
    screwPunch.name = "screwPunch"
    bpy.ops.transform.rotate(value=1.5708, axis=(1, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.translate(value=(0, 0, frameHeight *2 + screwPnchR + punchHeight), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        
    for i in range(0,3):
        bpy.ops.mesh.primitive_cube_add(radius=1, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
        nutPnch = bpy.context.active_object
        nutPnch.name = "nutPnch" + str(i)
        bpy.ops.transform.resize(value=(nutL, nutW, nutH), constraint_axis=(True, True, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)        
        bpy.ops.transform.rotate(value=1.0472 * i, axis=(0, 1, 0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    for i in range(0,3):
        bpy.data.objects['nutPnch' + str(i)].select = True
    
    bpy.ops.object.join()
    nutPunch = bpy.context.active_object
    nutPunch.name = "nutPunch"        
    bpy.ops.transform.translate(value=(0,-postDistance + nutPnch.dimensions.y, frameHeight * 2 + screwPnchR + punchHeight), constraint_axis=(False,True, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    subtractObj(leftPost,screwPunch)
    subtractObj(leftPost,nutPunch)
    subtractObj(rightPost,screwPunch)
    
#makeRod()    
#Wedge()    
#ScrewSupport()
#Spring()
YArmSupportTensionor()