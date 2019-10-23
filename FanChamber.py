import bpy
from math import cos, sin, tan, sqrt, atan

drnChamberHght = 0.4

fanL = 1.0
fanW = 1.0
fanH = 0.29
fanChamberThcnss = 0.1

def makeFanChamberPt1():
       
    makeXTRMale()

    bpy.ops.mesh.primitive_cylinder_add(radius=fanW+fanChamberThcnss, depth=drnChamberHght, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    drnChamber = bpy.context.active_object
    drnChamber.name = "drnChamber"
    
    bpy.ops.mesh.primitive_cylinder_add(radius=fanW, depth=drnChamberHght, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    c1 = bpy.context.active_object
    c1.name = "c1"
    
    subtractObj(drnChamber, c1)
    deleteObj(c1)
    
    bpy.data.objects['drnChamber'].select = True
    bpy.ops.transform.translate(value=(0, 0,maleXTRHght + drnChamberHght/2), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    bpy.ops.mesh.primitive_cube_add(radius=1, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    fanChmbr = bpy.context.active_object
    fanChmbr.name = "fanChmbr"
    bpy.ops.transform.resize(value=(fanL+fanChamberThcnss, fanW+fanChamberThcnss, fanH+fanChamberThcnss), constraint_axis=(True, True, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
                  
    bpy.ops.mesh.primitive_cube_add(radius=1, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    fanPnch = bpy.context.active_object
    fanPnch.name = "fanPnch"
    bpy.ops.transform.resize(value=(fanL, fanW, fanH + fanChamberThcnss/2 -0.02), constraint_axis=(True, True, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)    

    subtractObj(fanChmbr, fanPnch)
    bpy.ops.transform.translate(value=(0, fanL, 0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    subtractObj(fanChmbr, fanPnch)
    deleteObj(fanPnch)

    bpy.ops.mesh.primitive_cube_add(radius=(fanL+fanChamberThcnss), view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    incline = bpy.context.active_object
    incline.name = "incline"   
    
    bpy.ops.mesh.primitive_cube_add(radius=((fanL+fanChamberThcnss)*2), view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    inclinePnch = bpy.context.active_object
    inclinePnch.name = "inclinePnch"
    bpy.ops.transform.translate(value=(0, 0,-inclinePnch.dimensions.z/2), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)    
    
    subtractObj(incline,inclinePnch)
    bpy.data.objects['inclinePnch'].select = True    
    bpy.ops.transform.translate(value=(0, inclinePnch.dimensions.y/2 - incline.dimensions.y/2, inclinePnch.dimensions.z), constraint_axis=(False, True, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.context.scene.cursor_location = (0.0,-incline.dimensions.y/2,0.0)
    bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
    bpy.context.scene.cursor_location = (0.0,0.0,0.0)
    bpy.ops.transform.rotate(value=atan(incline.dimensions.z/incline.dimensions.y), axis=(1, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    subtractObj(incline, inclinePnch)
    deleteObj(inclinePnch)
    
    bpy.ops.mesh.primitive_cylinder_add(radius=fanW, depth=(incline.dimensions.z + fanH+fanChamberThcnss)*2, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    c1 = bpy.context.active_object
    c1.name = "c1"
    
    subtractObj(fanChmbr, c1)
    deleteObj(c1)

    bpy.data.objects['fanChmbr'].select = True
    bpy.ops.transform.translate(value=(0, 0,maleXTRHght + drnChamberHght + (fanH+fanChamberThcnss)), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    
    sFC = bpy.ops.mesh.primitive_uv_sphere_add
    sFC(location=(0,0,0))
    sFC = bpy.context.active_object 
    sFC.name = "sFC"
    bpy.ops.transform.resize(value=(fanL+fanChamberThcnss, fanL+fanChamberThcnss, fanL+fanChamberThcnss), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
                                      
    s2 = bpy.ops.mesh.primitive_uv_sphere_add
    s2(location=(0,0,0))
    s2 = bpy.context.active_object 
    s2.name = "s2"
    bpy.ops.transform.resize(value=(fanL, fanL, fanL), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    
    bpy.ops.mesh.primitive_cube_add(radius=fanL+fanChamberThcnss, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    c1 = bpy.context.active_object
    c1.name = "c1"
    bpy.ops.transform.translate(value=(0, 0,-(fanL+fanChamberThcnss)), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    subtractObj(sFC,c1)
    deleteObj(c1)
    
    makeXTRfemale()
    XTRFemaleTop = bpy.context.active_object
    XTRFemaleTop.name = "XTRFemaleTop"
    bpy.data.objects['XTRFemaleTop'].select = True
    bpy.ops.transform.translate(value=(0, 0,maleXTRHght + drnChamberHght + (fanH+fanChamberThcnss)*2 + (fanL+fanChamberThcnss) - (fanL+fanChamberThcnss)*0.05 + nzzlAttcHght + nzzleAttcOtrDiam), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    
    makeXTRfemale()
    XTRFemaleBottom = bpy.context.active_object
    XTRFemaleBottom.name = "XTRFemaleBottom"    
    bpy.data.objects['XTRFemaleBottom'].select = True
    bpy.ops.transform.rotate(value=-3.14159, axis=(0, 1, 0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.translate(value=(0, 0,fanChmbr.location.z + fanChmbr.dimensions.z/2 + XTRFemaleBottom.dimensions.z), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.data.objects['XTRFemaleBottom'].select = False

    bpy.data.objects['sFC'].select = True
    bpy.ops.transform.translate(value=(0, 0,maleXTRHght + drnChamberHght + (fanH+fanChamberThcnss)*2), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.data.objects['sFC'].select = False
    
    bpy.data.objects['s2'].select = True
    bpy.ops.transform.translate(value=(0, 0,maleXTRHght + drnChamberHght + (fanH+fanChamberThcnss)*2), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.data.objects['s2'].select = False
    
    bpy.data.objects['incline'].select = True
    bpy.ops.transform.translate(value=(0, 0,XTRFemaleBottom.location.z), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.data.objects['incline'].select = False

    cHght = XTRFemaleTop.location.z - XTRFemaleBottom.location.z
    bpy.ops.mesh.primitive_cylinder_add(radius=XTRFemaleBottom.dimensions.x/2, depth=cHght, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    cWall = bpy.context.active_object
    cWall.name = "cWall"
    bpy.ops.transform.translate(value=(0, 0,XTRFemaleBottom.location.z + cWall.dimensions.z/2), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.data.objects['cWall'].select = False
    
    bpy.ops.mesh.primitive_cylinder_add(radius=XTRFemaleBottom.dimensions.x/2-wallWdth, depth=cHght, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))    
    cWallPnch = bpy.context.active_object
    cWallPnch.name = "cWallPnch"
    bpy.ops.transform.translate(value=(0, 0,XTRFemaleBottom.location.z + cWall.dimensions.z/2), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    
    intersectObj(incline, cWall)
    subtractObj(incline, sFC)

    subtractObj(sFC,s2)
    deleteObj(s2)

    subtractObj(cWall,cWallPnch)
    deleteObj(cWallPnch)
    
    bpy.ops.mesh.primitive_cylinder_add(radius=stInnrDiam + stThknss, depth=maleXTRHght + drnChamberHght + (fanH+fanChamberThcnss)*2 + (fanL+fanChamberThcnss) + 1, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    stoutPunch = bpy.context.active_object
    stoutPunch.name = "stoutPunch"
    bpy.ops.transform.translate(value=(0, 0,(maleXTRHght + drnChamberHght + (fanH+fanChamberThcnss)*2 + (fanL+fanChamberThcnss) + 1)/2), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    
    subtractObj(sFC,stoutPunch)
    deleteObj(stoutPunch)
    
    bpy.ops.mesh.primitive_torus_add(view_align=False, location=(0, 0, 0), rotation=(0, 1.5708, 0), mode='EXT_INT', major_radius=1, minor_radius=0.25, abso_major_rad=0.85, abso_minor_rad=0.60)
    drain = bpy.context.active_object
    drain.name = "drain"
    bpy.ops.transform.translate(value=(0, -0.98545, 1.23), constraint_axis=(False, True, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)    
    
    bpy.ops.mesh.primitive_torus_add(view_align=False, location=(0, 0, 0), rotation=(0, 1.5708, 0), mode='EXT_INT', major_radius=1, minor_radius=0.25, abso_major_rad=0.8, abso_minor_rad=0.65)
    drainPnch = bpy.context.active_object
    drainPnch.name = "drainPnch"
    bpy.ops.transform.translate(value=(0, -0.98545, 1.23), constraint_axis=(False, True, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)    

    subtractObj(cWall,drainPnch)
    subtractObj(drnChamber,drainPnch)
    subtractObj(XTRFemaleBottom,drainPnch)
    subtractObj(drain,drainPnch)
    deleteObj(drainPnch)
    
    bpy.ops.mesh.primitive_cube_add(radius=drain.dimensions.x/2, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    drainPnch = bpy.context.active_object
    drainPnch.name = "drainPnch"
    bpy.ops.transform.translate(value=(0, -0.22934, 0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    subtractObj(drain,drainPnch)
    bpy.ops.transform.translate(value=(0, -0.163808, 1.66538), constraint_axis=(False, True, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)        
    subtractObj(drain,drainPnch)
    deleteObj(drainPnch)    

    makeWateringLine()
    stout = bpy.context.active_object
    bpy.data.objects['stout'].select = True    
    bpy.ops.transform.translate(value=(0, 0,(maleXTRHght + drnChamberHght + (fanH+fanChamberThcnss)*2 + (fanL+fanChamberThcnss) - (fanL+fanChamberThcnss)*0.05)), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)    

    bpy.ops.mesh.primitive_cube_add(radius=stHght, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    c1 = bpy.context.active_object
    c1.name = "c1"
    bpy.ops.transform.translate(value=(0, 0,0.2 + maleXTRHght + drnChamberHght + (fanH+fanChamberThcnss)*2 + (fanL+fanChamberThcnss) - (fanL+fanChamberThcnss)*0.05 + nzzlAttcHght + nzzleAttcOtrDiam + stHght), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    
    subtractObj(stout,c1)
    deleteObj(c1)
    
    bpy.ops.object.select_all(action='TOGGLE')
    bpy.ops.object.join()
