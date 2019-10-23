#Repertier multiplier 12
import bpy
from math import cos, sin, tan, sqrt, atan

filename = "c:/BlenderScripts/M.py"
exec(compile(open(filename).read(), filename, 'exec'))
filename = "c:/BlenderScripts/Cup.py"
exec(compile(open(filename).read(), filename, 'exec'))


def makeBox():

    #Adding the pump box
    bpy.ops.mesh.primitive_cube_add(radius=1, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    box = bpy.context.active_object 
    box.name = "Box"
    bpy.ops.transform.resize(value=(pmpBxXYZRszFctr, pmpBxXYZRszFctr, pmpBxXYZRszFctr), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.translate(value=(0, 0, pmpBxXYZSz/2), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    
    #Adding the pump box punch
    bpy.ops.mesh.primitive_cube_add(radius=1, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    boxPunch = bpy.context.active_object 
    boxPunch.name = "BoxPunch"
    bpy.ops.transform.resize(value=(pmpBxPunchXYRszFctr, pmpBxPunchXYRszFctr, pmpBxPunchZRszFctr), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.translate(value=(0, 0, pmpBxXYZSz/2 + pmpBxThcknss/2 + 0.01), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        
    subtractObj(box, boxPunch)
    deleteObj(boxPunch)

    bpy.ops.mesh.primitive_cube_add(radius=1, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    boxPunch = bpy.context.active_object 
    boxPunch.name = "BoxPunch"
    bpy.ops.transform.resize(value=(pmpBxPunchXYRszFctr, pmpBxPunchXYRszFctr*2, pmpBxThcknss), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.translate(value=(0, 0, pmpBxXYZSz - pmpBxThcknss + 0.01), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        
    subtractObj(box, boxPunch)
    deleteObj(boxPunch)

def makeLid():

    #Adding the lid
    bpy.ops.mesh.primitive_cube_add(radius=1, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    bpy.ops.transform.resize(value=(pmpBxXYZRszFctr-pmpBxThcknss, pmpBxXYZRszFctr-pmpBxThcknss/4, lidThcknssRszFct), constraint_axis=(True, True, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)    
    lid = bpy.context.active_object 
    lid.name = "Lid"
    bpy.ops.transform.translate(value=(0, 0, lid.dimensions.z/2), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.data.objects['Lid'].select = False
    
    bpy.ops.mesh.primitive_uv_sphere_add(size=pmpBxXYZRszFctr-pmpBxThcknss, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    pmpBxDome = bpy.context.active_object   
    pmpBxDome.name = "pmpBxDome"
    
    bpy.ops.mesh.primitive_uv_sphere_add(size=pmpBxXYZRszFctr-pmpBxThcknss-wallWdth, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    pmpBxDomePnch = bpy.context.active_object   
    pmpBxDomePnch.name = "pmpBxDomePnch"

    bpy.ops.mesh.primitive_cube_add(radius=1, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    bpy.ops.transform.resize(value=(pmpBxXYZRszFctr, pmpBxXYZRszFctr, pmpBxXYZRszFctr), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.translate(value=(0, 0, -pmpBxXYZRszFctr), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    boxPnch = bpy.context.active_object 
    boxPnch.name = "boxPnch"

    subtractObj(pmpBxDome,pmpBxDomePnch)
    subtractObj(pmpBxDome,boxPnch)
    subtractObj(lid,pmpBxDomePnch)
    deleteObj(pmpBxDomePnch)
    deleteObj(boxPnch)    
                      
    makeCupPunch()
    cupPunch = bpy.context.active_object 
    bpy.ops.transform.translate(value=(0, 0, -0.15 + sqrt((pmpBxXYZRszFctr-pmpBxThcknss-wallWdth)**2-outerR**2)), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.data.objects['cupPunch'].select = False
    subtractObj(pmpBxDome, cupPunch)
    deleteObj(cupPunch)
    
    axlR = 0.085 #last 0.05, 0.07, 0.08
    
    bpy.ops.mesh.primitive_cube_add(radius=1, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    bpy.ops.transform.resize(value=(pmpBxXYZRszFctr-pmpBxThcknss, axlR, lidThcknssRszFct/3), constraint_axis=(True, True, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)    
    axlSppt1 = bpy.context.active_object 
    axlSppt1.name = "axlSppt1"
    bpy.ops.transform.translate(value=(0, 0, axlSppt1.dimensions.z/2), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    
    bpy.ops.mesh.primitive_cube_add(radius=1, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    bpy.ops.transform.resize(value=(pmpBxXYZRszFctr-pmpBxThcknss, axlR, lidThcknssRszFct/3), constraint_axis=(True, True, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)    
    axlSppt2 = bpy.context.active_object 
    axlSppt2.name = "axlSppt2"
    bpy.ops.transform.rotate(value=1.5708, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.translate(value=(0, 0, axlSppt1.dimensions.z/2), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    bpy.ops.mesh.primitive_cylinder_add(radius=axlR, depth=2, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    axlPnch = bpy.context.active_object 
    axlPnch.name = "axlPnch"

    bpy.ops.mesh.primitive_cylinder_add(radius=axlR*2.5, depth=axlSppt1.dimensions.z, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    axlSupport = bpy.context.active_object 
    axlSupport.name = "axlSupport"
    bpy.ops.transform.translate(value=(0, 0, axlSupport.dimensions.z/2), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    
    subtractObj(axlSppt1,axlPnch)
    subtractObj(axlSppt2,axlPnch)
    subtractObj(axlSupport,axlPnch)
    deleteObj(axlPnch)
        
    bpy.ops.mesh.primitive_cylinder_add(radius=(sqrt(2 * (pmpBxDome.dimensions.y/2)**2) - pmpBxDome.dimensions.x/2)/2.5, depth=2, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    temp = bpy.context.active_object 
    temp.name = "temp"
    bpy.ops.transform.translate(value=(1.68642, -1.7757, 0), constraint_axis=(True, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    subtractObj(lid,temp)
    bpy.ops.transform.translate(value=(0, 3.5931, 0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    subtractObj(lid,temp)
    bpy.ops.transform.translate(value=(-3.3545, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    subtractObj(lid,temp)    
    bpy.ops.transform.translate(value=(0, -3.60714, 0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    subtractObj(lid,temp)
    deleteObj(temp)

    bpy.data.objects['Lid'].select = True   
    bpy.data.objects['axlSppt1'].select = True   
    bpy.data.objects['axlSppt2'].select = True
    bpy.data.objects['axlSupport'].select = True
    bpy.data.objects['pmpBxDome'].select = True
    bpy.ops.object.join()


