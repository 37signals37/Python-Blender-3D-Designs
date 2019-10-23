import bpy
from math import cos, sin, tan, sqrt, atan

drive = "e"
filename = drive + ":/M.py"
exec(compile(open(filename).read(), filename, 'exec'))

def HorizontalMistingFan():
    wiskHght = 0.05
    wiskWdth = 0.015
    wiskLngth = 0.3
    wiskCnt = 16
    XTRheight = 0.2
    XTRrad = 0.2
    axelPunchR = 0.059055 #0.0975, 0.101, 0.0675 ::: 0.0675 for 2mm stainless steel rod
    wskLngthMult = 0.1
    incrementFactor = 2
    # For coat hanger wire axelPunchR = 0.055 #0.0575 #0.06 #0.0625 #0.0525
    
    bpy.ops.mesh.primitive_cylinder_add(radius=XTRrad, depth=XTRheight, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    xtr = bpy.context.active_object
    xtr.name = "xtr"
    bpy.ops.transform.translate(value=(0, 0, xtr.dimensions.z/2), constraint_axis=(False,False,True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
         
    bpy.ops.mesh.primitive_cylinder_add(radius=axelPunchR, depth=1, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    axelPunch = bpy.context.active_object
    axelPunch.name = "axelPunch"   
    
    subtractObj(xtr,axelPunch)
    deleteObj(axelPunch)
    
    inc = 0
    
    for i in range(0, wiskCnt):
#        if(inc == 4): 
#            inc = 0
        bpy.ops.mesh.primitive_cube_add(view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
#       bpy.ops.transform.resize(value=(wiskLngth + inc * wskLngthMult,wiskWdth,wiskHght), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)    
        bpy.ops.transform.resize(value=(wiskLngth,wiskWdth,wiskHght), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)    
        wisk = bpy.context.active_object
        wisk.name = "wisk" + str(i)
        inc = inc + 1
        bpy.ops.transform.translate(value=(wisk.dimensions.x/2 + axelPunchR, 0, wisk.dimensions.z/2), constraint_axis=(True,False,True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR')           
        bpy.ops.transform.rotate(value=-2*pi/wiskCnt * i, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    bpy.ops.object.select_all(action='TOGGLE')
    bpy.ops.object.select_all(action='TOGGLE')
    bpy.ops.object.join()   

def MistingFan():
    
    wiskHght = 0.1
    wiskWdth = 0.05
    wiskLngth = 0.3
    wiskCnt = 12
    
    XTRrad = 0.125
    axelPunchR = 0.075
    
    coneLength = 1
    coneTheta = -pi/8
    conePhi = -pi/4
    numberOfConesPerSpike = 3
    coneRadius2 = wiskWdth/2
    coneSpaceDistance = (wiskLngth*2 - axelPunchR - wiskWdth)/numberOfConesPerSpike
    
    for i in range(0, wiskCnt):
        bpy.ops.mesh.primitive_cube_add(view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
        wisk = bpy.context.active_object
        wisk.name = "wisk" + str(i)
        bpy.ops.transform.resize(value=(wiskLngth,wiskWdth,wiskHght), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)    
        bpy.ops.transform.translate(value=(wisk.dimensions.x/2 + axelPunchR, 0, 0), constraint_axis=(True,False,False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR')           
        bpy.ops.transform.rotate(value=-2*pi/wiskCnt * i, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        
        for j in range(0,numberOfConesPerSpike+1):        
            bpy.ops.mesh.primitive_cone_add(radius1=wiskWdth, radius2=coneRadius2, depth=coneLength, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
            bpy.ops.transform.translate(value=(0, 0, coneLength/2), constraint_axis=(False,False,True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)            
            bpy.ops.object.origin_set(type='ORIGIN_CURSOR') 
            bpy.ops.transform.rotate(value=coneTheta, axis=(1, 0, 0), constraint_axis=(True,False,False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
            bpy.ops.transform.rotate(value=-conePhi, axis=(0, 1, 0), constraint_axis=(False,True,False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1) 
            bpy.ops.transform.translate(value=(axelPunchR + wiskWdth + coneSpaceDistance * j, 0, 0), constraint_axis=(True,False,False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
            bpy.ops.object.origin_set(type='ORIGIN_CURSOR') 
            bpy.ops.transform.rotate(value=-2*pi/wiskCnt * i, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    bpy.ops.object.select_all(action='TOGGLE')
    bpy.ops.object.select_all(action='TOGGLE')
    bpy.ops.object.join()   
    mister = bpy.context.active_object
    mister.name = "mister"

    bpy.ops.mesh.primitive_cylinder_add(radius=XTRrad, depth=wiskHght, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    xtr = bpy.context.active_object
    xtr.name = "xtr"
    bpy.ops.transform.translate(value=(0, 0, xtr.dimensions.z/2), constraint_axis=(False,False,True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
         
    bpy.ops.mesh.primitive_cylinder_add(radius=axelPunchR, depth=1, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    axelPunch = bpy.context.active_object
    axelPunch.name = "axelPunch"   
    
    subtractObj(xtr,axelPunch)
    deleteObj(axelPunch)
    bpy.ops.object.select_all(action='TOGGLE')
    bpy.ops.object.join()  
    
def TwirlMistingFan():
    wiskR = 0.1
    wiskDistance = 0.25
    coneTheta = pi/6
    conePhi = pi/6
    wisksPerArm = 3
    wishTheta = pi/8
    armCount = 6
    
    XTRrad = 0.3
    XTRHeight = 0.25
    axelPunchR = 0.075
    
    bpy.ops.object.empty_add(type='PLAIN_AXES', view_align=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))

    for j in range(0,armCount):    
        for i in range(1,wisksPerArm+1):
            bpy.ops.mesh.primitive_plane_add(radius=wiskR, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
            wisk = bpy.context.active_object
            wisk.name = "wisk" + str(i) + str (j)
            bpy.ops.transform.rotate(value=pi/2, axis=(0, 1, 0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
            bpy.ops.transform.rotate(value=pi/4, axis=(1, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
            bpy.ops.transform.translate(value=(0, wiskDistance*i, 0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
            bpy.ops.object.modifier_add(type='SCREW')
            bpy.context.object.modifiers["Screw"].object = bpy.data.objects["Empty"]
            bpy.context.object.modifiers["Screw"].angle = 3.14159
            bpy.context.object.modifiers["Screw"].screw_offset = 2
            bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Screw")
            bpy.ops.transform.translate(value=(0,wiskR*2 + wiskDistance*i, 0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
            bpy.ops.object.origin_set(type='ORIGIN_CURSOR') 
            bpy.ops.transform.rotate(value=wishTheta * i, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
            bpy.ops.transform.rotate(value=-2*pi/armCount * j, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    
    bpy.ops.object.select_all(action='TOGGLE')
    bpy.ops.object.select_all(action='TOGGLE')
    bpy.ops.object.join()   
    wisks = bpy.context.active_object
    wisks.name = "wisks"     
    
#    bpy.ops.object.modifier_add(type='DECIMATE')
#    bpy.context.object.modifiers["Decimate"].decimate_type = 'DISSOLVE'
#    bpy.context.object.modifiers["Decimate"].angle_limit = 0.436332
#    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Decimate")

       
    bpy.ops.mesh.primitive_cylinder_add(radius=axelPunchR, depth=1, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    axelPunch = bpy.context.active_object
    axelPunch.name = "axelPunch"   
    
    bpy.ops.mesh.primitive_cylinder_add(radius=XTRrad, depth=XTRHeight, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    xtr = bpy.context.active_object
    xtr.name = "xtr"   

    subtractObj(xtr, axelPunch)
    deleteObj(axelPunch)          

    bpy.data.objects['xtr'].select = True  
    bpy.ops.transform.translate(value=(0, 0, wisks.dimensions.z + XTRHeight/2), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)                    

    
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

def AxleFanBladesHolder():
    #Repetier Multiplier 4
    holderR = 2
    holderL = 0.35
    
    axleR = 0.39 #0.5, 0.45, 0.33

    slitWidth = 0.125 #0.05, 0.1, 0.15
    slitBuffer = 0.25
    
    slitCount = 12
        
    bpy.ops.mesh.primitive_cylinder_add(radius=holderR, depth=holderL, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    holder = bpy.context.active_object
    holder.name = "holder"
       
    for i in range(0, slitCount):
        bpy.ops.mesh.primitive_cube_add(view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))   
        slitPunch = bpy.context.active_object
        slitPunch.name = "slitPunch"
        bpy.ops.transform.resize(value=(slitWidth,1,holderL), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        bpy.ops.transform.translate(value=(0, slitPunch.dimensions.y/2 + axleR + slitBuffer, 0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)    
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
        bpy.ops.transform.rotate(value=2*pi/slitCount * i, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        subtractObj(holder, slitPunch)
        
    bpy.ops.mesh.primitive_cylinder_add(radius=axleR, depth=holderL+0.01, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    axlePunch = bpy.context.active_object
    axlePunch.name = "axlePunch"
    
    subtractObj(holder, axlePunch)
    deleteObj(axlePunch)

def AxleFanBlades():

    coverR = 0.1
    coverL = 4
    
    axleR = 0.05
        
    prongThcknss = 0.01
    prongLength = 50

    prongCnt = 40

    coverProngBuffer = coverL/15
    prongGrpSpcng =((coverL - 2 * coverProngBuffer) / (prongCnt))

    bpy.ops.mesh.primitive_cube_add(view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))   
    bar = bpy.context.active_object
    bar.name = "bar"
    bpy.ops.transform.resize(value=(coverL/2,0.02,prongThcknss *2), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.translate(value=(0, -bar.dimensions.y/2, bar.dimensions.z/2), constraint_axis=(False, True, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

               
    for i in range(0, prongCnt):
        bpy.ops.mesh.primitive_cube_add(radius=prongThcknss, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
        prong = bpy.context.active_object
        prong.name = "prong" + str(i)
        bpy.ops.transform.resize(value=(0,prongLength,0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        bpy.ops.transform.translate(value=(-coverL/2 + coverProngBuffer + prongGrpSpcng * i, -prong.dimensions.y/2, prong.dimensions.z/2), constraint_axis=(True,True,True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    
        bpy.ops.mesh.primitive_cube_add(radius=prongThcknss, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
        prongT = bpy.context.active_object
        prongT.name = "prongT"
        bpy.ops.transform.resize(value=(0,prongLength * 0.9,0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        bpy.ops.transform.translate(value=(-coverL/2 + coverProngBuffer + prongGrpSpcng * i, -prongT.dimensions.y/2, 3/2*prongT.dimensions.z), constraint_axis=(True,True,True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    
def AxleCoverWithMistingFanBlades():

    coverR = 0.1
    coverL = 1.5
    
    axleR = 0.05
        
    prongThcknss = 0.01
    prongLength = 50

    prongGroupsCnt = 7
    prongCnt = 5

    coverProngBuffer = coverL/5
    prongGrpSpcng =((coverL - 2 * coverProngBuffer) / (prongCnt+1))
    
    bpy.ops.mesh.primitive_cylinder_add(radius=coverR, depth=coverL, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    cover = bpy.context.active_object
    cover.name = "cover"
    bpy.ops.transform.rotate(value=1.5708, axis=(1, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    bpy.ops.mesh.primitive_cube_add(radius=coverL/2 + 0.01, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    coverPunch = bpy.context.active_object
    coverPunch.name = "coverPunch"                
    bpy.ops.transform.translate(value=(0, 0, -coverL/2 - 0.005), constraint_axis=(False,False,True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    subtractObj(cover, coverPunch)
    deleteObj(coverPunch)

    bpy.ops.mesh.primitive_cylinder_add(radius=axleR, depth=coverL + 0.01, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    axlePunch = bpy.context.active_object
    axlePunch.name = "axlePunch"
    bpy.ops.transform.rotate(value=1.5708, axis=(1, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    
    subtractObj(cover, axlePunch)
    deleteObj(axlePunch)
    
    for j in range(0,prongGroupsCnt):
        for i in range(0, prongCnt+1):
            bpy.ops.mesh.primitive_cube_add(radius=prongThcknss, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
            prong = bpy.context.active_object
            prong.name = "prong" + str(j) + str(i)
            bpy.ops.transform.resize(value=(prongLength,0,0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
            bpy.ops.transform.translate(value=(prong.dimensions.x/2 + coverR - 0.01, -coverL/2 + coverProngBuffer + prongGrpSpcng * j, 0), constraint_axis=(True,True,False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
            bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
            bpy.ops.transform.rotate(value=-pi/prongCnt * i, axis=(0, 1, 0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        

    
def FanWithMistingBlades():
    XTRrad = 0.2 #0.125
    axelPunchR = 0.095 #0.1 #0.055 #0.09
    shieldThickness = 0.025

    cntrHght = 0.02

    wiskHght = 0.01 #last 0.01
    wiskWdth = 0.03 #0.04
    wiskLngth = 0.75 #0.7
    wiskCnt = 16

    bladeLayers = 6

    mistTeeth = 16
    toothWidth = 0.05
    toothLength = 0.5

    
    bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(0, 0, 0), "constraint_axis":(False, False, False), "constraint_orientation":'GLOBAL', "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "texture_space":False, "remove_on_cancel":False, "release_confirm":False})
                    
    for j in range(0,bladeLayers):
        for i in range(0, wiskCnt):
            bpy.ops.mesh.primitive_cube_add(view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
            wisk = bpy.context.active_object
            wisk.name = "wisk" + str(i)
            bpy.ops.transform.resize(value=(wiskLngth,wiskWdth,wiskHght), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)    
            bpy.ops.transform.translate(value=(wisk.dimensions.x/2 + axelPunchR, 0, wisk.dimensions.z/2 + j * wisk.dimensions.z/2), constraint_axis=(True,False,True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
            bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
            bpy.ops.transform.rotate(value=-2*pi/wiskCnt * i - pi*2/360 * 1.5 * j, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
                                    
    bpy.ops.object.select_all(action='TOGGLE')
    bpy.ops.object.select_all(action='TOGGLE')
    bpy.ops.object.join()   
    blades = bpy.context.active_object
    blades.name = "blades"
        
        
    bpy.ops.mesh.primitive_uv_sphere_add(size=XTRrad, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))           
    xtr = bpy.context.active_object
    xtr.name = "xtr"

    bpy.ops.mesh.primitive_cube_add(radius=XTRrad, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    xtrPnch = bpy.context.active_object
    xtrPnch.name = "xtrPnch"    
    bpy.ops.transform.translate(value=(0, 0, -XTRrad), constraint_axis=(False,False,True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    subtractObj(xtr, xtrPnch)
    deleteObj(xtrPnch)

    bpy.ops.mesh.primitive_cylinder_add(radius=axelPunchR, depth=blades.dimensions.z * 5 + 0.01, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    axelPunch = bpy.context.active_object
    axelPunch.name = "axelPunch"
    bpy.ops.transform.translate(value=(0, 0, axelPunch.dimensions.z/2), constraint_axis=(False,False,True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    
    subtractObj(xtr, axelPunch)
    deleteObj(axelPunch)

    bpy.ops.object.select_all(action='TOGGLE')
    bpy.ops.object.join()   
    blades = bpy.context.active_object
    blades.name = "blades"

    raise Exception()            
    
    bpy.ops.mesh.primitive_cylinder_add(radius=blades.dimensions.x/2, depth=blades.dimensions.z, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    shield = bpy.context.active_object
    shield.name = "shield"
    bpy.ops.transform.translate(value=(0, 0, shield.dimensions.z/2), constraint_axis=(False,False,True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    bpy.ops.mesh.primitive_cylinder_add(radius=blades.dimensions.x/2-shieldThickness, depth=blades.dimensions.z+0.01, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    shieldPunch = bpy.context.active_object
    shieldPunch.name = "shieldPunch"
    bpy.ops.transform.translate(value=(0, 0, shieldPunch.dimensions.z/2), constraint_axis=(False,False,True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    
    subtractObj(shield, shieldPunch)
    deleteObj(shieldPunch)
    
    for i in range(0,mistTeeth):
        bpy.ops.mesh.primitive_cone_add(radius1=toothWidth, radius2=0, depth=toothLength, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
        tooth = bpy.context.active_object
        tooth.name = "tooth" + str(i)
        bpy.ops.transform.rotate(value=pi, axis=(1, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        bpy.ops.transform.translate(value=(tooth.dimensions.x/2 + wiskLngth*2, 0, -tooth.dimensions.z/2), constraint_axis=(True,False,True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)               
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
        bpy.ops.transform.rotate(value=-pi/4, axis=(1, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR')       
        bpy.ops.transform.rotate(value=2*pi/mistTeeth * i, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        
    bpy.ops.object.select_all(action='TOGGLE')
    bpy.ops.object.select_all(action='TOGGLE')
    bpy.ops.object.join()


HorizontalMistingFan()        