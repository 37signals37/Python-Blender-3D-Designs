import bpy
from math import cos, sin, tan, sqrt, atan

filename = "c:/Users/BeckyBot/Desktop/Botnyst/Prototype Models/Scripts/2nd Prototype/M.py"
exec(compile(open(filename).read(), filename, 'exec'))

KISSslicerMult = 27.75 #27.5, 26.667, 40
#25.62 by calibration
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

    bpy.ops.object.select_all(action='TOGGLE')
    bpy.ops.transform.resize(value=(KISSslicerMult, KISSslicerMult, KISSslicerMult), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)


SilverScrewCollet()    