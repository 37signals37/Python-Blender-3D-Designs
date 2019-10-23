import bpy
from math import cos, sin, tan, sqrt, atan

def makeMotorMimic():
    
    motorMimicL = 0.875 #last 1.10
    motorMimicW = 0.49 #last 0.45, 0.5
    motorMimicPnchShift = 0.375 #0.4
            
    bpy.ops.mesh.primitive_cylinder_add(radius=motorMimicW, depth=motorMimicL, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    mtrMmc = bpy.context.active_object
    mtrMmc.name = "mtrMmc"   
                
    bpy.ops.mesh.primitive_cube_add(view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    mtrMmcPnch = bpy.context.active_object
    mtrMmcPnch.name = "mtrMmcPnch"
    bpy.ops.transform.translate(value=(0, 1+motorMimicPnchShift, 0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
             
    subtractObj(mtrMmc, mtrMmcPnch)
    bpy.ops.transform.translate(value=(0, -2*(1+motorMimicPnchShift), 0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    subtractObj(mtrMmc, mtrMmcPnch)
    deleteObj(mtrMmcPnch) 

def SideMotorMount():

    colletR = 0.25 
    axleShieldL = 1.33 #1
    axleR = 0.065 #0.05, 0.1, 0.075

    motorMimicW = 0.66 #last 0.72   For large Motor
    motorMimicL = 1.35

    axleShieldR = colletR * 1.25

    bpy.ops.mesh.primitive_cylinder_add(radius=motorMimicW * 1.25, depth=motorMimicL, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    motorFrame = bpy.context.active_object
    motorFrame.name = "motorFrame"

    bpy.ops.mesh.primitive_cylinder_add(radius=motorMimicW, depth=motorMimicL + 0.01, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    motorPunch = bpy.context.active_object
    motorPunch.name = "motorPunch"
    bpy.ops.transform.translate(value=(0, 0, motorFrame.dimensions.z/10), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    #makeMotorMimic()
#    motorFrame = bpy.context.active_object
#    motorFrame.name = "motorFrame"
#    bpy.data.objects['motorFrame'].select = True
#    bpy.ops.transform.resize(value=(1.25, 1.25, 1.25), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
#    bpy.data.objects['motorFrame'].select = False

#    makeMotorMimic()
#    motorPunch = bpy.context.active_object
#    motorPunch.name = "motorPunch"
#    bpy.data.objects['motorPunch'].select = True
#    bpy.ops.transform.resize(value=(0, 0, 1.25), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
#    bpy.ops.transform.translate(value=(0, 0, motorFrame.dimensions.z/10), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
#    bpy.data.objects['motorFrame'].select = False
    
    subtractObj(motorFrame, motorPunch)
    deleteObj(motorPunch)
    
    bpy.ops.mesh.primitive_cylinder_add(radius=axleShieldR, depth=axleShieldL, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    axleShield = bpy.context.active_object
    axleShield.name = "axleShield"
    
    bpy.ops.mesh.primitive_cylinder_add(radius=colletR, depth=axleShieldL*2, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    colletPunch = bpy.context.active_object
    colletPunch.name = "colletPunch"
#    bpy.ops.transform.translate(value=(0, 0, axleShield.dimensions.z/10), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        
    subtractObj(axleShield, colletPunch)
    
    bpy.data.objects['colletPunch'].select = True
    bpy.ops.transform.translate(value=(0, 0, -colletPunch.dimensions.z/2), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.data.objects['colletPunch'].select = False

    subtractObj(motorFrame, colletPunch)
    deleteObj(colletPunch)
   
    bpy.ops.mesh.primitive_cylinder_add(radius=axleR, depth=10, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    axlePunch = bpy.context.active_object
    axlePunch.name = "axlePunch"

    subtractObj(axleShield, axlePunch)

    bpy.ops.mesh.primitive_uv_sphere_add(size=colletR, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    domePunch = bpy.context.active_object
    domePunch.name = "domePunch"
    
    bpy.ops.mesh.primitive_cube_add(view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    domePunch1 = bpy.context.active_object
    domePunch1.name = "domePunch1"
    bpy.ops.transform.translate(value=(0, 0, domePunch1.dimensions.z/2), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    
    bpy.ops.mesh.primitive_uv_sphere_add(size=axleShieldR, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    dome = bpy.context.active_object
    dome.name = "dome"
    
    subtractObj(dome, domePunch)
    deleteObj(domePunch)
    subtractObj(dome, domePunch1)
    deleteObj(domePunch1)
    subtractObj(dome, axlePunch)
    deleteObj(axlePunch)
    
    


def AxelCatch():

    baseL = 0.6
    baseW = 0.45
    baseH = 0.15

    standL = 0.2
    standW = 0.2
    standH = 1

    basePunchR = 0.1
    standPunchR = 0.04
    standPunchL = 0.2
    standPunchH = 1.75
        
    bpy.ops.mesh.primitive_cube_add(radius=1, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    base = bpy.context.active_object
    base.name = "base"
    bpy.ops.transform.resize(value=(baseL, baseW, baseH), constraint_axis=(True, True, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.translate(value=(0, 0, baseH), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    bpy.ops.mesh.primitive_cube_add(radius=1, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    stand = bpy.context.active_object
    stand.name = "stand"
    bpy.ops.transform.resize(value=(standL,standW,standH), constraint_axis=(True, True, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.translate(value=(0, baseW - standW, standH), constraint_axis=(False, True, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    
    bpy.ops.mesh.primitive_cylinder_add(radius=basePunchR, depth=2, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    basePunch = bpy.context.active_object
    basePunch.name = "basePunch"
    bpy.ops.transform.translate(value=(baseL - basePunchR - baseL/5, baseW - basePunchR - baseW/5, 0), constraint_axis=(True, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    subtractObj(base, basePunch)
    bpy.ops.transform.translate(value=(-2*baseL + 2 * basePunchR + 2 * baseL/5, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    subtractObj(base, basePunch)
    bpy.ops.transform.translate(value=(0, -2 * baseW + 2 * basePunchR + 2 * baseW/5, 0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    subtractObj(base, basePunch)
    bpy.ops.transform.translate(value=(2*baseL - 2 * basePunchR - 2 * baseL/5, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    subtractObj(base, basePunch)
    deleteObj(basePunch)
    
    bpy.ops.mesh.primitive_cylinder_add(radius=standPunchR, depth=standPunchL, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    standPunch = bpy.context.active_object
    standPunch.name = "standPunch"
    bpy.ops.transform.rotate(value=1.5708, axis=(1, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.translate(value=(0, baseW - standPunchL/2 + 0.01, standPunchH), constraint_axis=(False, True, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    subtractObj(stand, standPunch)
    deleteObj(standPunch)

    bpy.data.objects['base'].select = True
    bpy.data.objects['stand'].select = True
    bpy.ops.object.join()

def makeRodConnector():
    bpy.ops.mesh.primitive_cylinder_add(radius=engHolePnchR1, depth=engHolePnchL, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    engHolePnch1 = bpy.context.active_object
    engHolePnch1.name = "engHolePnch1"
    bpy.ops.transform.rotate(value=1.5708, axis=(1, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.translate(value=(0, -engHolePnchL/2, 0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    bpy.ops.mesh.primitive_cylinder_add(radius=engHolePnchR2, depth=engHolePnchL, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    engHolePnch2 = bpy.context.active_object
    engHolePnch2.name = "engHolePnch2"
    bpy.ops.transform.rotate(value=1.5708, axis=(1, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.translate(value=(0, engHolePnchL/2, 0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    
    bpy.ops.mesh.primitive_cylinder_add(radius=rodXtrR, depth=rodXtrL, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    rodXtr = bpy.context.active_object
    rodXtr.name = "rodXtr"
    bpy.ops.transform.rotate(value=1.5708, axis=(1, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)    
    subtractObj(rodXtr,engHolePnch1)
    subtractObj(rodXtr,engHolePnch2)
        
    deleteObj(engHolePnch1)
    deleteObj(engHolePnch2)       

def makeMotorMimic1(motorMimicW, motorMimicL):
    bpy.ops.mesh.primitive_cylinder_add(radius=motorMimicW, depth=motorMimicL, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    mtrMmc = bpy.context.active_object
    mtrMmc.name = "mtrMmc"

def makeMotorMount1():

    motorMimicW = 0.66 
    motorMimicL = 1.35
    mountW = 1.5 #1.25

    screwBlockL = 0.4
    screwBlockW = mountW * 0.6

    extraSpacePunchR = 1
    extraSpacePunchL = 1

    screwR = 0.06

    makeMotorMimic1(motorMimicW, 10)
    mtrMmc = bpy.context.active_object
           
    makeMotorMimic1(motorMimicW + 0.15, motorMimicL)
    mtrShld = bpy.context.active_object
    mtrShld.name = "mtrShld"
           
    subtractObj(mtrShld, mtrMmc)
                      
    bpy.ops.mesh.primitive_uv_sphere_add(size=mountW, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    mount = bpy.context.active_object
    mount.name = "mount"
            
    bpy.ops.mesh.primitive_cube_add(view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    mountPunch = bpy.context.active_object
    mountPunch.name = "mountPunch"
    bpy.ops.transform.resize(value=(mountW, mountW, mountW), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    bpy.ops.transform.translate(value=(0, 0, -mountPunch.dimensions.z/2), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    
    subtractObj(mount, mountPunch)
    deleteObj(mountPunch)
    subtractObj(mount, mtrMmc)
    deleteObj(mtrMmc)    

    bpy.ops.mesh.primitive_cylinder_add(radius=extraSpacePunchR, depth=extraSpacePunchL, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    extraSpacePunch = bpy.context.active_object
    extraSpacePunch.name = "extraSpacePunch"
    subtractObj(mount, extraSpacePunch)
    deleteObj(extraSpacePunch)

    screwDriverPunchW = 0.5
    screwDriverPunchD = 5

    bpy.ops.mesh.primitive_cylinder_add(radius=screwDriverPunchW, depth=screwDriverPunchD, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    screwDriverPunch = bpy.context.active_object
    screwDriverPunch.name = "screwDriverPunch"
    bpy.ops.transform.rotate(value=1.5708, axis=(0, 1, 0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.translate(value=(screwDriverPunch.dimensions.z/2, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    subtractObj(mount, screwDriverPunch)
    deleteObj(screwDriverPunch)


    bpy.ops.mesh.primitive_cylinder_add(radius=screwR, depth=motorMimicL + 0.01, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    screwDriverHolePunch = bpy.context.active_object
    screwDriverHolePunch.name = "screwDriverHolePunch"
    bpy.ops.transform.translate(value=(-(motorMimicW - mount.dimensions.x)/2, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
    bpy.ops.transform.rotate(value=0.785398, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    for i in range(0,7):
        subtractObj(mount, screwDriverHolePunch)        
        bpy.ops.transform.rotate(value=0.785398, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    deleteObj(screwDriverHolePunch)

    screwDriverPunchW = 2
    screwDriverPunchD = 5
    screwDriverPunchHeightMove = 0.75

    bpy.ops.mesh.primitive_cylinder_add(radius=screwR * 3, depth=motorMimicL + 0.01, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    screwDriverHolePunch1 = bpy.context.active_object
    screwDriverHolePunch1.name = "screwDriverHolePunch1"
    bpy.ops.transform.translate(value=(-(motorMimicW - mount.dimensions.x)/2, 0, screwDriverHolePunch1.dimensions.z/2 + screwDriverPunchHeightMove), constraint_axis=(True, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
    bpy.ops.transform.rotate(value=0.785398, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    for i in range(0,7):
        subtractObj(mount, screwDriverHolePunch1)        
        bpy.ops.transform.rotate(value=0.785398, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    deleteObj(screwDriverHolePunch1)

                          
   
def makeMotorMount():
    makeMotorMimic()
    bpy.data.objects['mtrMmc'].select = True
    bpy.ops.transform.rotate(value=1.5708, axis=(1, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.mesh.primitive_cube_add(view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))    
 #   bpy.ops.transform.resize(value=(0.2,0.2,motorMntBoxH), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.resize(value=(motorMntBoxL,motorMntBoxW,motorMntBoxH), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.translate(value=(0, 0,motorMntBoxH), constraint_axis=(False,False,True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

def makeVerticalMotorMount1():
    mountW = 1
    
    makeMotorMimic1(motorMimicW, motorMimicL*2)        
    mtrMmc = bpy.context.active_object
    bpy.data.objects['mtrMmc'].select = True   
    bpy.ops.transform.translate(value=(0, 0,mtrMmc.dimensions.z/2 + wallWdth/2), constraint_axis=(False,False,True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.data.objects['mtrMmc'].select = False
                
    bpy.ops.mesh.primitive_cube_add(view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    mtrFrm = bpy.context.active_object
    mtrFrm.name = "mtrFrm"
#    bpy.ops.transform.resize(value=(motorMimicW+wallWdth,motorMimicL/2,motorMimicW), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)    
    bpy.ops.transform.resize(value=(motorMimicW+wallWdth,motorMimicL/2,motorMimicW*2), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)    
    bpy.ops.transform.translate(value=(0, 0,mtrFrm.dimensions.z/2), constraint_axis=(False,False,True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    subtractObj(mtrFrm,mtrMmc)
    deleteObj(mtrMmc)
        
    bpy.ops.mesh.primitive_cylinder_add(radius=engHolePnchR1, depth=2, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    frmPnch = bpy.context.active_object
    frmPnch.name = "frmPnch"
    subtractObj(mtrFrm,frmPnch)
    deleteObj(frmPnch)


def makeVerticalMotorMount():
    mmcW = 0.68 #0.66
    mmcL = 1.35 #1.75a
    frmBffr = 0.05 #last 0.25
    
    lidBffr = 0.20 #last 0.1, 0.15
    lidHght = 0.5
    lidShft = 0.4
    
    cnntPnchDst = 0.45 #last 0.34, 0.4
    cnntPnchR = 0.15
    
    axlPnchR = 0.3 #last 0.225

    airPnchR = 0.05
    concR = 0.2
        
    makeXTRMale()
    XTRmale = bpy.context.active_object
    XTRmale.name = "XTRmale"    

    bpy.ops.mesh.primitive_cylinder_add(radius=XTRmale.dimensions.x/2, depth=mmcL + frmBffr, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    mtrFrm = bpy.context.active_object
    mtrFrm.name = "mtrFrm"
    bpy.ops.transform.translate(value=(0,0,XTRmale.dimensions.z + mtrFrm.dimensions.z/2), constraint_axis=(False,False,True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    bpy.ops.mesh.primitive_cylinder_add(radius=XTRmale.dimensions.x/2 + lidBffr, depth=lidHght, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    frmLid = bpy.context.active_object
    frmLid.name = "frmLid"
    bpy.ops.transform.translate(value=(0,0,XTRmale.dimensions.z + lidHght/2 + mtrFrm.dimensions.z - lidShft), constraint_axis=(False,False,True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    subtractObj(frmLid, mtrFrm)
    bpy.ops.transform.resize(value=(1.005, 1.005, 1.005), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    bpy.ops.mesh.primitive_cylinder_add(radius=cnntPnchR, depth=mmcL + frmBffr, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    cnntPnch = bpy.context.active_object
    cnntPnch.name = "cnntPnch"
    bpy.ops.transform.translate(value=(0,cnntPnchDst,XTRmale.dimensions.z + mtrFrm.dimensions.z/2 + cnntPnch.dimensions.z/2), constraint_axis=(False,True,True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    subtractObj(frmLid, cnntPnch)
    bpy.ops.transform.translate(value=(0,-2*cnntPnchDst,0), constraint_axis=(False,True,False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    subtractObj(frmLid, cnntPnch)
    deleteObj(cnntPnch)
    
    bpy.ops.mesh.primitive_cylinder_add(radius=0.35, depth=mmcL + frmBffr, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    cntrPnch = bpy.context.active_object
    cntrPnch.name = "cntrPnch"
    bpy.ops.transform.translate(value=(0,0,XTRmale.dimensions.z + mtrFrm.dimensions.z/2 + cntrPnch.dimensions.z/2), constraint_axis=(False,True,True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    subtractObj(frmLid, cntrPnch)
    deleteObj(cntrPnch)
    
    bpy.ops.mesh.primitive_cylinder_add(radius=airPnchR, depth=mmcL + frmBffr, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    airPnch = bpy.context.active_object
    airPnch.name = "airPnch"
    bpy.ops.transform.translate(value=(0,concR,XTRmale.dimensions.z + mtrFrm.dimensions.z/2 + cntrPnch.dimensions.z/2), constraint_axis=(False,True,True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    raise Exception()


#    for j in range(0,3):
#        for i in range(0,18):
            
    


    makeMotorMimic1(mmcW, mmcL + 0.01)
    mtrMmc = bpy.context.active_object
    mtrMmc.name = "mtrMmc"
    bpy.ops.transform.translate(value=(0,0,XTRmale.dimensions.z + mtrMmc.dimensions.z/2 + frmBffr + 0.01), constraint_axis=(False,False,True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    bpy.ops.mesh.primitive_cylinder_add(radius=0.31, depth=0.21 + 0.01, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    mtrMmcAttc = bpy.context.active_object
    mtrMmcAttc.name = "mtrMmcAttc"
    bpy.ops.transform.translate(value=(0,0,XTRmale.dimensions.z + (frmBffr - mtrMmcAttc.dimensions.z) + mtrMmcAttc.dimensions.z/2 + 0.01), constraint_axis=(False,False,True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    subtractObj(mtrFrm,mtrMmc)
    deleteObj(mtrMmc)
    subtractObj(mtrFrm,mtrMmcAttc)
    deleteObj(mtrMmcAttc)

    makeCupPunch()
    cupPunch = bpy.context.active_object
    cupPunch.name = "cupPunch" 
    
    bpy.ops.mesh.primitive_cube_add(radius=cupPunch.dimensions.z, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    cubePnch = bpy.context.active_object
    cubePnch.name = "cubePnch"    
    bpy.ops.transform.translate(value=(0,0,XTRmale.dimensions.z + cubePnch.dimensions.z/2), constraint_axis=(False,False,True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    subtractObj(cupPunch, cubePnch)
    deleteObj(cubePnch)
            
    bpy.ops.mesh.primitive_cylinder_add(radius=axlPnchR, depth=2, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    axlPnch = bpy.context.active_object
    axlPnch.name = "axlPnch"
    subtractObj(mtrFrm,axlPnch)
    
    subtractObj(cupPunch,axlPnch)
    deleteObj(axlPnch)
    deleteObj(XTRmale)

#    bpy.data.objects['XTRmale'].select = True   
    bpy.data.objects['cupPunch'].select = True   
    bpy.data.objects['mtrFrm'].select = True   
    bpy.ops.object.join()

def makeRotor():    

    #bpy.ops.mesh.primitive_gear(number_of_teeth=12, radius=0.4, addendum=0.1, dedendum=0.1, angle=0.785398, base=0.2, width=rotorGearL, skew=0, conangle=0, crown=0)
    #bpy.ops.transform.translate(value=(0, 0,rotorGearL), constraint_axis=(False,False,True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)    
    bpy.ops.mesh.primitive_worm_gear(number_of_teeth=6, number_of_rows=80, radius=0.25, addendum=0.2, dedendum=0.1, angle=0.349066, row_height=0.05, skew=0.19635, crown=0.03)

    makeRodConnector()   
    bpy.data.objects['rodXtr'].select = True
    bpy.ops.transform.rotate(value=1.5708, axis=(1, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.translate(value=(0, 0,rodXtrL/2), constraint_axis=(False,False,True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)   
    bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
    #bpy.ops.transform.resize(value=(0,0,motorMntBoxH), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    
    engPnch = bpy.data.objects['engHolePnch1']
    deleteObj(engPnch)
    engPnch = bpy.data.objects['engHolePnch2']
    deleteObj(engPnch)

def makeScrewRotor():
    bpy.ops.object.empty_add(type='PLAIN_AXES', view_align=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    empty = bpy.context.active_object
    empty.name = "empty"
    bpy.data.objects['empty'].select = False

    mesh = bpy.data.meshes.new("e")
    screw = bpy.data.objects.new("screw",mesh)
     
    #set mesh location
    screw.location = bpy.context.scene.cursor_location
    bpy.context.scene.objects.link(screw)
    
    # mesh arrays
    verts = []  # the vertex array
    faces = []  # the face array
    
    verts.append((0,1,0))
    verts.append((1,-1,0))
    verts.append((-1,-1,0))
    verts.append((0,-1,0))

    faces.append((0,2,3,1))

    mesh.from_pydata(verts,[],faces)
    mesh.update(calc_edges=True)
    
    bpy.ops.object.select_all(action='TOGGLE')
    edge = bpy.context.active_object
    bpy.ops.transform.rotate(value=1.5708, axis=(0, 1, 0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.translate(value=(0, 4, 0), constraint_axis=(False,True,False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    bpy.data.objects['screw'].select = True
    bpy.ops.object.modifier_add(type='SCREW')
    bpy.context.object.modifiers["Screw"].object = bpy.data.objects["empty"]
    bpy.context.object.modifiers["Screw"].use_normal_calculate = True

def makeThinWiskRotor():

    cntrHght = 0.01

    wiskHght = 0.01
    wiskLngth = 0.4
    wiskCnt = 48
    
    for i in range(0, wiskCnt):
        bpy.ops.mesh.primitive_cube_add(view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
        wisk = bpy.context.active_object
        wisk.name = "wisk" + str(i)
        bpy.ops.transform.resize(value=(wiskLngth,wiskHght,wiskHght), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)    
        bpy.ops.transform.translate(value=(wisk.dimensions.x/2 + engHolePnchR1*0.8, 0, wisk.dimensions.z/2), constraint_axis=(True,False,True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
        bpy.ops.transform.rotate(value=2*pi/wiskCnt * i, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    
    bpy.ops.object.select_all(action='TOGGLE')
    bpy.ops.object.select_all(action='TOGGLE')
    bpy.ops.object.join()

def ThinWiskBall():

    ctOffHght = 0.75
    cntrHght = 0.02

    wiskHght = 0.02
    wiskWdth = 0.025
    wiskLngth = 0.25 #last 0.3, 0.35, 0.25
    wiskCnt = 12

    bladeLayers = 12
                    
    wiskExtTheta = pi/4                    
                    
    for j in range(0,bladeLayers):
        for i in range(0, wiskCnt):
#    for j in range(0,12):
#        for i in range(0, wiskCnt):
            bpy.ops.mesh.primitive_cube_add(view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
            wisk = bpy.context.active_object
            wisk.name = "wisk" + str(i)
            bpy.ops.transform.resize(value=(wiskLngth * 1,wiskWdth,wiskHght), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)    
            bpy.ops.transform.translate(value=(wisk.dimensions.x/2, 0, 0), constraint_axis=(True,False,False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
            bpy.ops.object.origin_set(type='ORIGIN_CURSOR')           
            bpy.ops.transform.rotate(value=-pi/180 * 80/bladeLayers * j, axis=(0, 1, 0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
            bpy.ops.transform.translate(value=(engHolePnchR1, 0, wisk.dimensions.z/2 + j * wisk.dimensions.z), constraint_axis=(True,False,True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)                         
            bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
            bpy.ops.transform.rotate(value=2*pi/wiskCnt * i + 2*pi/wiskCnt/bladeLayers * j + pi/wiskCnt * sin(pi/2*j), axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
            
            bpy.ops.mesh.primitive_cube_add(view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))            
            wiskExt = bpy.context.active_object
            wiskExt.name = "wiskExt" + str(i)
            bpy.ops.transform.resize(value=(wiskLngth*2,wiskWdth,wiskHght), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
            bpy.ops.transform.rotate(value=-pi/2, axis=(0, 1, 0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)       
            bpy.ops.transform.translate(value=(0, 0, wiskExt.dimensions.x/2), constraint_axis=(False,False,True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)                         
            bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
            bpy.ops.transform.rotate(value= -wiskExtTheta, axis=(1, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)       
            bpy.ops.transform.rotate(value= 2*pi/wiskCnt * i + 2*pi/wiskCnt/bladeLayers * j + pi/wiskCnt * sin(pi/2*j), axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)       
            bpy.ops.transform.translate(value=(getMaxFaceLocation(wisk, 0), getMaxFaceLocation(wisk, 1), getMaxFaceLocation(wisk, 2)), constraint_axis=(True,True,True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)                         

    bpy.ops.object.select_all(action='TOGGLE')
    bpy.ops.object.select_all(action='TOGGLE')
    bpy.ops.object.join()   
    rotor = bpy.context.active_object
    rotor.name = "rotor"

    makeRodConnector()   
    rodXtr = bpy.data.objects['rodXtr']
    bpy.data.objects['rodXtr'].select = True
    bpy.ops.transform.rotate(value=1.5708, axis=(1, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.resize(value=(0,0,0.5), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)    
    bpy.ops.transform.translate(value=(0, 0,rodXtr.dimensions.z/2), constraint_axis=(False,False,True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)   
    bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
                        
    bpy.ops.mesh.primitive_cube_add(view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    ctOff = bpy.context.active_object
    ctOff.name = "ctOff"                        
    bpy.ops.transform.resize(value=(2,2,2), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.translate(value=(0, 0, ctOff.dimensions.z/2 + ctOffHght), constraint_axis=(False,False,True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    
    subtractObj(rotor,ctOff)
    deleteObj(ctOff)                                                      
                                                     
def ThinFan():

    XTRrad = 0.125
    axelPunchR = 0.075
    shieldThickness = 0.025

    cntrHght = 0.02

    wiskHght = 0.01 #last 0.01
#    wiskWdth = 0.02
    wiskWdth = 0.04
    wiskLngth = 0.3 #last 0.25,
    wiskCnt = 3

    bladeLayers = 64
                    
    for j in range(0,bladeLayers):
        for i in range(0, wiskCnt):
#           #bpy.ops.mesh.primitive_cylinder_add(radius=wiskLngth, depth=wiskHght, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
#            wisk = bpy.context.active_object
#            wisk.name = "wisk"
#            bpy.ops.transform.translate(value=(0, 0, wisk.dimensions.z/2), constraint_axis=(False,False,True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    
#            bpy.ops.mesh.primitive_cylinder_add(radius=wiskLngth, depth=wiskHght + 0.01, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
#            wiskPunch = bpy.context.active_object
#            wiskPunch.name = "wiskPunch"
#            bpy.ops.transform.translate(value=(0, wiskWdth, wiskPunch.dimensions.z/2), constraint_axis=(False,True,True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    
#            subtractObj(wisk, wiskPunch)
#            deleteObj(wiskPunch)

#            wiskA = bpy.context.active_object
#            wiskA.name = "wiskA" + str(i) + str(j)
#            bpy.data.objects["wiskA" + str(i) + str(j)].select = True
#            bpy.ops.transform.translate(value=(wisk.dimensions.x/2 + axelPunchR, 0, wiskA.dimensions.z/2 + j * wiskA.dimensions.z), constraint_axis=(True,False,True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
#            bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
#            bpy.ops.transform.rotate(value=2*pi/wiskCnt * i - pi*2/360 * 2 * j, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
#            bpy.data.objects["wiskA" + str(i) + str(j)].select = False

            bpy.ops.mesh.primitive_cube_add(view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
            wisk = bpy.context.active_object
            wisk.name = "wisk" + str(i)
            bpy.ops.transform.resize(value=(wiskLngth,wiskWdth,wiskHght), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)    
            bpy.ops.transform.translate(value=(wisk.dimensions.x/2 + axelPunchR, 0, wisk.dimensions.z/2 + j * wisk.dimensions.z), constraint_axis=(True,False,True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
            bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
            bpy.ops.transform.rotate(value=2*pi/wiskCnt * i + pi*2/360 * 2 * j, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
                
    bpy.ops.object.select_all(action='TOGGLE')
    bpy.ops.object.select_all(action='TOGGLE')
    bpy.ops.object.join()   
    blades = bpy.context.active_object
    blades.name = "blades"
        
    bpy.ops.mesh.primitive_cylinder_add(radius=XTRrad, depth=blades.dimensions.z, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    xtr = bpy.context.active_object
    xtr.name = "xtr"
    bpy.ops.transform.translate(value=(0, 0, xtr.dimensions.z/2), constraint_axis=(False,False,True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    bpy.ops.mesh.primitive_cylinder_add(radius=axelPunchR, depth=blades.dimensions.z+0.01, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    axelPunch = bpy.context.active_object
    axelPunch.name = "axelPunch"
    bpy.ops.transform.translate(value=(0, 0, axelPunch.dimensions.z/2), constraint_axis=(False,False,True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    
    subtractObj(xtr, axelPunch)
    deleteObj(axelPunch)
    
    bpy.ops.mesh.primitive_cylinder_add(radius=axelPunchR + wiskLngth*2, depth=blades.dimensions.z, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    shield = bpy.context.active_object
    shield.name = "shield"
    bpy.ops.transform.translate(value=(0, 0, shield.dimensions.z/2), constraint_axis=(False,False,True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    bpy.ops.mesh.primitive_cylinder_add(radius=axelPunchR + wiskLngth*2-shieldThickness, depth=blades.dimensions.z+0.01, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    shieldPunch = bpy.context.active_object
    shieldPunch.name = "shieldPunch"
    bpy.ops.transform.translate(value=(0, 0, shieldPunch.dimensions.z/2), constraint_axis=(False,False,True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    
    subtractObj(shield, shieldPunch)
    deleteObj(shieldPunch)