import bpy
from math import cos, sin, tan, sqrt, atan

def makeMistStout():
    mtrFrmHght = 2
    stHght = 1.875
  
    def makeCylinderWalls():
            
        makeXTRMale()
        XTRmale = bpy.context.active_object
        XTRmale.name = "XTRmale"
        
        for i in range(0,3):
            bpy.ops.mesh.primitive_cube_add(radius=1, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
            bpy.ops.transform.resize(value=((innerR + outerR)/4,wallWdth/3,wallWdth), constraint_axis=(True, True, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
            spndlHndl = bpy.context.active_object
            spndlHndl.name = "spndlHndl" + str(i)
            bpy.ops.transform.translate(value=(spndlHndl.dimensions.x/2, 0, spndlHndl.dimensions.z/2), constraint_axis=(True, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
            bpy.ops.object.origin_set(type='ORIGIN_CURSOR')        
            bpy.ops.transform.rotate(value=2.09439 * i, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    
        for i in range(0,3):
            bpy.data.objects["spndlHndl" + str(i)].select = True
            
        bpy.ops.object.join()        
        triSpk = bpy.context.active_object
        triSpk.name = "triSpk"      
    
        bpy.ops.mesh.primitive_uv_sphere_add(size=1, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
        axlCnnt = bpy.context.active_object
        axlCnnt.name = "axlCnnt"       
        bpy.ops.transform.resize(value=(0.2, 0.2, spndlHndl.dimensions.z), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        bpy.ops.transform.translate(value=(0, 0, spndlHndl.dimensions.z), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

#        last radius =: 0.15        
        bpy.ops.mesh.primitive_cube_add(radius=axlCnnt.dimensions.x, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))       
        axlCnntPnch = bpy.context.active_object
        axlCnntPnch.name = "axlCnntPnch"       
        bpy.ops.transform.translate(value=(0, 0, axlCnntPnch.dimensions.z/2 + axlCnnt.dimensions.z/2), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    
        subtractObj(axlCnnt, axlCnntPnch)
        deleteObj(axlCnntPnch)
                
#        last radius =: 0.15
        bpy.ops.mesh.primitive_uv_sphere_add(size=0.125, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
        axlCnntPnch = bpy.context.active_object
        axlCnntPnch.name = "axlCnntPnch"       
        bpy.ops.transform.translate(value=(0, 0, axlCnntPnch.dimensions.z/2 + axlCnnt.dimensions.z/2), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    
        subtractObj(triSpk, axlCnntPnch)        
        subtractObj(axlCnnt, axlCnntPnch)
        deleteObj(axlCnntPnch)
                
        bpy.ops.object.select_all(action='TOGGLE')
        bpy.ops.object.join()
        spndlCnnt = bpy.context.active_object
        spndlCnnt.name = "spndlCnnt" 
        bpy.data.objects["spndlCnnt"].select = False
    
        #Making the walls from cylinders
        #last Z: 2.0
        bpy.ops.mesh.primitive_cylinder_add(radius=spndlCnnt.dimensions.x/2, depth=2.5, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
        MSwalls = bpy.context.active_object
        MSwalls.name = "MSwalls"       
        bpy.ops.transform.translate(value=(0, 0, MSwalls.dimensions.z/2 + axlCnnt.dimensions.z/2), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        
        bpy.ops.mesh.primitive_cylinder_add(radius=(spndlCnnt.dimensions.x  - wallWdth/2)/2, depth=MSwalls.dimensions.z + 0.01, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
        MSwallsPnch = bpy.context.active_object
        MSwallsPnch.name = "MSwallsPnch"
        bpy.ops.transform.translate(value=(0, 0, MSwallsPnch.dimensions.z/2 + axlCnnt.dimensions.z/2), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        
        subtractObj(MSwalls, MSwallsPnch)
        deleteObj(MSwallsPnch)
                     
    makeCylinderWalls()                     
    MSwalls = bpy.context.active_object
    MSwalls.name = "MSwalls"                         

    raise Exception()
                                            
    #last MSwalls.dimensions.x - wallWdth)/2 - :0.02
    bpy.ops.mesh.primitive_uv_sphere_add(size=(MSwalls.dimensions.x - wallWdth)/2 -0.06, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)) 
    fanFrm = bpy.context.active_object
    fanFrm.name = "fanFrm"
    bpy.data.objects['fanFrm'].select = False
        
    #bpy.ops.mesh.primitive_uv_sphere_add(size=(MSwalls.dimensions.x - wallWdth)/2, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    #bpy.ops.transform.resize(value=(stInnrDiam + stThknss,stInnrDiam + stThknss,stInnrDiam + stThknss), constraint_axis=(True, True, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    
    bpy.ops.mesh.primitive_cube_add(radius=fanFrm.dimensions.x, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    fanFrmPnch = bpy.context.active_object
    fanFrmPnch.name = "fanFrmPnch"
    bpy.ops.transform.translate(value=(0, 0, -fanFrmPnch.dimensions.z/2), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)    
    subtractObj(fanFrm, fanFrmPnch)
    deleteObj(fanFrmPnch)
    
    ventCnt = 12

    for i in range(0,ventCnt):
        #last radius =: 0.2
        bpy.ops.mesh.primitive_cylinder_add(radius=0.15, depth=3, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
        ventPnch = bpy.context.active_object
        ventPnch.name = "ventPnch" + str(i)
        bpy.ops.transform.translate(value=((fanFrm.dimensions.x - ventPnch.dimensions.x)/2 + 0.01, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)         
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
        bpy.ops.transform.rotate(value=2*pi/ventCnt * i, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    for i in range(0,ventCnt):
        bpy.data.objects["ventPnch" + str(i)].select = True
        
    bpy.ops.object.join()
    ventPnch = bpy.context.active_object
    ventPnch.name = "ventPnch"
    
    subtractObj(fanFrm, ventPnch)
    #deleteObj(ventPnch)
              
    bpy.ops.mesh.primitive_cylinder_add(radius=fanFrm.dimensions.x/2, depth=motorMimicL, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    fanFrm1 = bpy.context.active_object
    fanFrm1.name = "fanFrm1"
    bpy.ops.transform.translate(value=(0, 0, -fanFrm1.dimensions.z/2), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        
#    last: * 1.18, 1.23, 1.28
    makeMotorMimic1(motorMimicW * 1.24, motorMimicL*2)   
    fanFrmPnch = bpy.context.active_object
    fanFrmPnch.name = "fanFrmPnch"
    bpy.data.objects['fanFrmPnch'].select = True
    
#   last: -0.2, -0.5
    bpy.ops.transform.translate(value=(0, 0, -fanFrmPnch.dimensions.z/2 - 0.3), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)      
    subtractObj(fanFrm1, fanFrmPnch)
    deleteObj(fanFrmPnch)        
    
    makeMotorMimic1(motorMimicW, motorMimicL*2)   
    fanFrmPnch = bpy.context.active_object
    fanFrmPnch.name = "fanFrmPnch"
    bpy.data.objects['fanFrmPnch'].select = True   
    bpy.ops.transform.translate(value=(0, 0, -fanFrmPnch.dimensions.z/2), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)      
    subtractObj(fanFrm1, fanFrmPnch)
    deleteObj(fanFrmPnch)  
            
    subtractObj(fanFrm1,ventPnch)        
    deleteObj(ventPnch)
    
    #last radius = rodXtrR * : 1.00
    bpy.ops.mesh.primitive_cylinder_add(radius=rodXtrR * 1.25, depth=rodXtrL, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    rodXtr = bpy.context.active_object
    rodXtr.name = "rodXtr"
    bpy.data.objects['rodXtr'].select = True   
    bpy.ops.transform.translate(value=(0, 0, rodXtr.dimensions.z/2), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)      
    subtractObj(fanFrm, rodXtr)
    deleteObj(rodXtr)  

#    last: * 1.00, 1.15
    bpy.ops.mesh.primitive_cylinder_add(radius=engHolePnchR1* 1.2, depth=10, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    engHolePnch = bpy.context.active_object
    engHolePnch.name = "engHolePnch"
    bpy.data.objects['engHolePnch'].select = True   
    subtractObj(fanFrm, engHolePnch)
    deleteObj(engHolePnch)  
       
    raise Exception() 
    
                                



        

            
    bpy.ops.mesh.primitive_uv_sphere_add(size=(cnntChmbr.dimensions.x+wallWdth)/2, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    dome = bpy.context.active_object
    dome.name = "dome"

    bpy.ops.mesh.primitive_uv_sphere_add(size=(dome.dimensions.x-wallWdth)/2, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    domePnch = bpy.context.active_object
    domePnch.name = "domePnch"
    subtractObj(dome, domePnch)
    deleteObj(domePnch)

    bpy.ops.mesh.primitive_cube_add(radius=dome.dimensions.x/2, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    domePnch = bpy.context.active_object
    domePnch.name = "domePnch"
    bpy.ops.transform.translate(value=(0, 0, -domePnch.dimensions.z/2), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    subtractObj(dome, domePnch)
    deleteObj(domePnch)    

    bpy.data.objects['dome'].select = True
    bpy.ops.transform.translate(value=(0, 0, fanFrm.dimensions.z), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.data.objects['dome'].select = False

    deleteObj(MSwalls)
    deleteObj(spndlCnnt)
    raise Exception()

    #last engHolePnchR1: 1
    bpy.ops.mesh.primitive_cylinder_add(radius=engHolePnchR1 *1.03, depth=rodXtrL*3, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    engHolePnch = bpy.context.active_object
    engHolePnch.name = "engHolePnch"
    subtractObj(dome,engHolePnch)
    deleteObj(engHolePnch)
    


    
    raise Exception()
    
    axlPnch = makeCylinder(engHolePnchR1,cnntChmbrPnch.dimensions.z + 0.01,"axlPnch")
    
    
              
                  
              



    bpy.ops.transform.translate(value=(0, 0, spndlCnnt.dimensions.z + MSwalls.dimensions.z), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)             
    

    
    
#    makeVerticalMotorMount()
        
#    mtrFrm = bpy.context.active_object
#    mtrFrm.name = "mtrFrm"
#    bpy.data.objects['mtrFrm'].select = True
#    bpy.ops.transform.translate(value=(0, 0, mtrFrmHght), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
#    bpy.data.objects['mtrFrm'].select = False
     
    bpy.ops.mesh.primitive_cylinder_add(radius=stInnrDiam + stThknss, depth=stHght, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    stWlls = bpy.context.active_object
    stWlls.name = "stWlls"
    
    bpy.ops.mesh.primitive_cylinder_add(radius=stInnrDiam, depth=stHght, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    stWllsPnch = bpy.context.active_object
    stWllsPnch.name = "stWllsPnch"
    
    subtractObj(stWlls,stWllsPnch)
     
    bpy.data.objects['stWlls'].select = True
    bpy.ops.transform.translate(value=(0, 0, stHght/2), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.data.objects['stWlls'].select = False
        
    bpy.ops.mesh.primitive_uv_sphere_add(size=1, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    bpy.ops.transform.resize(value=(stInnrDiam + stThknss,stInnrDiam + stThknss,stInnrDiam + stThknss), constraint_axis=(True, True, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    domeCnnct = bpy.context.active_object
    domeCnnct.name = "domeCnnct"
    bpy.data.objects['domeCnnct'].select = False

    bpy.data.objects['stWllsPnch'].select = True
        
    bpy.ops.transform.translate(value=(0, 0, -stWllsPnch.dimensions.z/2), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.data.objects['stWllsPnch'].select = False
    subtractObj(domeCnnct, stWllsPnch)
    deleteObj(stWllsPnch)

    bpy.ops.mesh.primitive_uv_sphere_add(size=1, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    bpy.ops.transform.resize(value=(stInnrDiam,stInnrDiam,stInnrDiam), constraint_axis=(True, True, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    domeCnnctPnch = bpy.context.active_object
    domeCnnctPnch.name = "domeCnnctPnch"

    subtractObj(domeCnnct, domeCnnctPnch)
    deleteObj(domeCnnctPnch)

    bpy.ops.mesh.primitive_cube_add(radius=1, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    bpy.ops.transform.resize(value=(stInnrDiam + stThknss,stInnrDiam + stThknss,stInnrDiam + stThknss), constraint_axis=(True, True, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    domeCnnctPnch = bpy.context.active_object
    domeCnnctPnch.name = "domeCnnctPnch"
    bpy.ops.transform.translate(value=(0, 0, -domeCnnctPnch.dimensions.z/2), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    subtractObj(domeCnnct, domeCnnctPnch)
    deleteObj(domeCnnctPnch)
    
    bpy.data.objects['domeCnnct'].select = True
    bpy.ops.transform.translate(value=(0, 0, stHght), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.data.objects['domeCnnct'].select = False
        
    bpy.ops.object.select_all(action='TOGGLE')
    bpy.ops.object.join()

