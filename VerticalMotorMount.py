import bpy
from math import cos, sin, tan, sqrt, atan

mmcW = 0.66 #0.66, 0.68
mmcL = 1.35 #1.75a
frmBffr = 0.05 #last 0.25
    
lidBffr = 0.10 #last 0.1, 0.15
lidHght = 0.5
lidShft = 0.4
    
cnntPnchDst = 0.45 #last 0.34, 0.4
cnntPnchR = 0.15
    
axlPnchR = 0.3 #last 0.225

airPnchR = 0.05625 #last 0.05, 0.075, 0625
concR = 0.5

def Collet():
    
    inwrdSlitDst = 0.225  #last 0.15, 0.25, 0.2, 0.35, 0.25, 0.28
    
    XTRrad = 0.28 #0.3, 0.32, 0.28, 0.26 
    XTRlength = 1 #last 1.25    
    
    cntrPnchLngth = 1    
    cntrPnchR = 0.08 #0.07, 0.06 0.093

    screwRad = 0.07 #0.3 0.15
    screwPnchL = XTRrad*2 + 0.01
    screwHeadR = 0.4 #0.32 0.27 0.23, 0.18
    screwHeadOffset  = 0 #0.06
    screwHeadH = 0.18 #0.15 0.3
    
    #axelConeR1 = 0.113 #For ScrubBrush
    axelConeR1 = 0.08
    #axelConeR2 = 0.093  #last 0.65,

    bpy.ops.mesh.primitive_cylinder_add(radius=cntrPnchR, depth=XTRlength*2, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    centerPunch = bpy.context.active_object
    centerPunch.name = "centerPunch"
    bpy.ops.transform.rotate(value=1.5708, axis=(1, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)    
    bpy.ops.transform.translate(value=(0, -XTRlength + 0.01, 0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    bpy.ops.mesh.primitive_cylinder_add(radius=axelConeR1, depth=XTRlength*2, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    centerPunch1 = bpy.context.active_object
    centerPunch1.name = "centerPunch1"
    bpy.ops.transform.rotate(value=1.5708, axis=(1, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)    
    bpy.ops.transform.translate(value=(0, XTRlength, 0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    bpy.ops.mesh.primitive_cylinder_add(radius=XTRrad, depth=XTRlength, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    collet = bpy.context.active_object
    collet.name = "collet"
    bpy.ops.transform.rotate(value=1.5708, axis=(1, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)    

    subtractObj(collet,centerPunch)
    subtractObj(collet,centerPunch1)
    subtractObj(collet,centerPunch)    
    deleteObj(centerPunch)

    remeshObj(collet, 6)
#ScrewPunch   
    bpy.ops.mesh.primitive_cylinder_add(radius=screwRad, depth=screwPnchL, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    screwPunch = bpy.context.active_object
    screwPunch.name = "screwPunch"
    bpy.ops.transform.translate(value=(0, XTRlength/4, 0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    subtractObj(collet,screwPunch)
    bpy.ops.transform.translate(value=(0, -XTRlength/2, 0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    subtractObj(collet,screwPunch)
      
    #bpy.ops.mesh.primitive_cone_add(radius1=screwRad, radius2=screwHeadR, depth=XTRrad/2, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    bpy.ops.mesh.primitive_cone_add(view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    bpy.ops.transform.resize(value=(screwHeadR, screwHeadR, screwHeadH), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    screwPunchHead = bpy.context.active_object
    screwPunchHead.name = "screwPunchHead"
    bpy.ops.transform.rotate(value=-3.14159, axis=(1, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.translate(value=(0, -XTRlength/4, XTRrad + screwHeadOffset), constraint_axis=(False, True, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    subtractObj(collet, screwPunchHead)
    bpy.ops.transform.translate(value=(0, XTRlength/2, 0), constraint_axis=(False, True, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    subtractObj(collet, screwPunchHead)
    bpy.ops.transform.rotate(value=-3.14159, axis=(1, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)  
    bpy.ops.transform.translate(value=(0, 0, -2 * XTRrad - 2 * screwHeadOffset), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    subtractObj(collet, screwPunchHead)
    bpy.ops.transform.translate(value=(0, -XTRlength/2, 0), constraint_axis=(False, True, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    subtractObj(collet, screwPunchHead)
    
    decimateObj(collet, 0.04)
    
    deleteObj(screwPunch)
    deleteObj(screwPunchHead)
    deleteObj(centerPunch1)

def SilverScrewCollet():
        
    XTRrad = 0.32 #0.3, 0.32, 0.28, 0.26 
    XTRlength = 2 #last 1.45, 1
    
    cntrPnchLngth = 1    
    cntrPnchR = 0.078 #0.08, 0.07

#    screwRad = 0.0925 #0.09, 0.095, 0.08, 0.07
    screwRad = 0.0875 #0.0925
    screwPnchL = XTRrad*2 + 0.01
    
    #axelConeR1 = 0.113 #For ScrubBrush
    axelConeR1 = 0.08
    #axelConeR2 = 0.093  #last 0.65,

    bpy.ops.mesh.primitive_cylinder_add(radius=cntrPnchR, depth=XTRlength*2, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    centerPunch = bpy.context.active_object
    centerPunch.name = "centerPunch"
    bpy.ops.transform.rotate(value=1.5708, axis=(1, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)    
    bpy.ops.transform.translate(value=(0, -XTRlength + 0.01, 0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    bpy.ops.mesh.primitive_cylinder_add(radius=axelConeR1, depth=XTRlength*2, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    centerPunch1 = bpy.context.active_object
    centerPunch1.name = "centerPunch1"
    bpy.ops.transform.rotate(value=1.5708, axis=(1, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)    
    bpy.ops.transform.translate(value=(0, XTRlength, 0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    bpy.ops.mesh.primitive_cylinder_add(radius=XTRrad, depth=XTRlength, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    collet = bpy.context.active_object
    collet.name = "collet"
    bpy.ops.transform.rotate(value=1.5708, axis=(1, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)    

    subtractObj(collet,centerPunch)
    subtractObj(collet,centerPunch1)
    subtractObj(collet,centerPunch)    
    deleteObj(centerPunch)

    remeshObj(collet, 7)
#ScrewPunch   
    bpy.ops.mesh.primitive_cylinder_add(radius=screwRad, depth=screwPnchL, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    screwPunch = bpy.context.active_object
    screwPunch.name = "screwPunch"
    bpy.ops.transform.translate(value=(0, XTRlength/4, 0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    subtractObj(collet,screwPunch)
    bpy.ops.transform.translate(value=(0, -XTRlength/2, 0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    subtractObj(collet,screwPunch)
          
    deleteObj(screwPunch)
    deleteObj(centerPunch1)
    decimateObj(collet, 0.1)
    
def makeMotorMimic1(motorMimicW, motorMimicL):
    bpy.ops.mesh.primitive_cylinder_add(radius=motorMimicW, depth=motorMimicL, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    mtrMmc = bpy.context.active_object
    mtrMmc.name = "mtrMmc"

def makeVerticalMotorMountLid():
    
    makeXTRMale()
    XTRmale = bpy.context.active_object
    XTRmale.name = "XTRmale"
    
    bpy.ops.mesh.primitive_cylinder_add(radius=XTRmale.dimensions.x/2, depth=mmcL + frmBffr, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    mtrFrm = bpy.context.active_object
    mtrFrm.name = "mtrFrm"
    bpy.ops.transform.translate(value=(0,0,XTRmale.dimensions.z + mtrFrm.dimensions.z/2), constraint_axis=(False,False,True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    
    XTRmaleR = XTRmale.dimensions.x/2
    lidZ = XTRmale.dimensions.z + mtrFrm.dimensions.z
    
    deleteObj(XTRmale)
    
    bpy.ops.mesh.primitive_cylinder_add(radius= XTRmaleR + lidBffr, depth=lidHght, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    frmLid = bpy.context.active_object
    frmLid.name = "frmLid"
    bpy.ops.transform.translate(value=(0,0,lidZ + lidHght/2 - lidShft), constraint_axis=(False,False,True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    subtractObj(frmLid, mtrFrm)
    #last 1.005, 1.01
    bpy.ops.transform.resize(value=(1.015, 1.015, 1.015), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    deleteObj(mtrFrm)

    bpy.ops.mesh.primitive_cylinder_add(radius=cnntPnchR, depth=mmcL + frmBffr, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    cnntPnch = bpy.context.active_object
    cnntPnch.name = "cnntPnch"
    bpy.ops.transform.translate(value=(0,cnntPnchDst,lidZ + (mmcL + frmBffr)/2), constraint_axis=(False,True,True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    subtractObj(frmLid, cnntPnch)
    bpy.ops.transform.translate(value=(0,-2*cnntPnchDst,0), constraint_axis=(False,True,False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    subtractObj(frmLid, cnntPnch)
    deleteObj(cnntPnch)
    
    bpy.ops.mesh.primitive_cylinder_add(radius=0.35, depth=mmcL + frmBffr, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    cntrPnch = bpy.context.active_object
    cntrPnch.name = "cntrPnch"
    bpy.ops.transform.translate(value=(0,0,lidZ + (mmcL + frmBffr)/2), constraint_axis=(False,True,True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    subtractObj(frmLid, cntrPnch)
    deleteObj(cntrPnch)
    
    bpy.ops.mesh.primitive_cylinder_add(radius=airPnchR, depth=mmcL + frmBffr, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    airPnch = bpy.context.active_object
    airPnch.name = "airPnch"
    bpy.ops.transform.translate(value=(0,concR,lidZ + (mmcL + frmBffr)/2), constraint_axis=(False,True,True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
    for j in range(0,3):
        for i in range(0,18):
            bpy.ops.transform.rotate(value=0.349066, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
            subtractObj(frmLid,airPnch)
        bpy.ops.transform.translate(value=(0,concR/2,0), constraint_axis=(False,True,False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)            
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
        bpy.ops.transform.rotate(value=0.349066/2, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    deleteObj(airPnch)

def makeVerticalMotorMount():

    brthrSpc = 0.2
    brthrSpcZ = 0.3
        
    makeXTRMale()
    XTRmale = bpy.context.active_object
    XTRmale.name = "XTRmale"    

    makeCupPunch()
    base = bpy.context.active_object
    base.name = "base" 
    
    bpy.ops.mesh.primitive_cube_add(radius=base.dimensions.z, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    cubePnch = bpy.context.active_object
    cubePnch.name = "cubePnch"    
    bpy.ops.transform.translate(value=(0,0,XTRmale.dimensions.z + cubePnch.dimensions.z/2), constraint_axis=(False,False,True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    subtractObj(base, cubePnch)
    deleteObj(cubePnch)
    deleteObj(XTRmale)

    bpy.ops.mesh.primitive_cylinder_add(radius=base.dimensions.x/2, depth=mmcL + frmBffr, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    mtrFrm = bpy.context.active_object
    mtrFrm.name = "mtrFrm"
    bpy.ops.transform.translate(value=(0,0,base.dimensions.z + mtrFrm.dimensions.z/2), constraint_axis=(False,False,True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
             
    bpy.ops.mesh.primitive_cylinder_add(radius=base.dimensions.x/2 - brthrSpc, depth=mmcL + frmBffr, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    airBrthr = bpy.context.active_object
    airBrthr.name = "airBrthr"
    bpy.ops.transform.translate(value=(0,0,base.dimensions.z + mtrFrm.dimensions.z/2 + brthrSpcZ), constraint_axis=(False,False,True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)                          

#radius = 0.18, 0.26, 0.22  depth = 0.33
    bpy.ops.mesh.primitive_cylinder_add(radius=0.24, depth=0.16 + 0.01, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    mtrMmcAttc = bpy.context.active_object
    mtrMmcAttc.name = "mtrMmcAttc"
    bpy.ops.transform.translate(value=(0,0,mtrMmcAttc.dimensions.z/2 - 0.01), constraint_axis=(False,False,True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    makeMotorMimic1(mmcW, mmcL + 0.01)
    mtrMmc = bpy.context.active_object
    mtrMmc.name = "mtrMmc"
    bpy.ops.transform.translate(value=(0,0,mtrMmc.dimensions.z/2 + mtrMmcAttc.dimensions.z - 0.01), constraint_axis=(False,False,True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    subtractObj(mtrFrm,airBrthr)
    subtractObj(mtrFrm,mtrMmc)
    subtractObj(base,mtrMmc)
    deleteObj(mtrMmc)
    deleteObj(airBrthr)

    subtractObj(mtrFrm,mtrMmcAttc)
    subtractObj(base,mtrMmcAttc)
    deleteObj(mtrMmcAttc)

    bpy.data.objects['base'].select = True   
    bpy.data.objects['mtrFrm'].select = True   
    bpy.ops.object.join()

