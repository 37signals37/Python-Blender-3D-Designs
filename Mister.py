#Repetier Multiplier 21.3
import bpy
from math import cos, sin, tan, sqrt, atan

filename = "e:/Blender Scripts/Scripts/M.py"
exec(compile(open(filename).read(), filename, 'exec'))

def mister():
    wiskHght = 0.03 #0.015
    wiskWdth = 0.015 #0.01
    wiskLngth = 0.6 #0.45
    wiskCnt = 48 #40
    XTRheight = 0.06 #0.03
    XTRrad = 0.25 #0.2, 0.15    
    axelPunchR = 0.0875 #0.101, 0.0675 ::: 0.0675 for 2mm stainless steel rod
    wskLngthMult = 0.1
    # For coat hanger wire axelPunchR = 0.055 #0.0575 #0.06 #0.0625 #0.0525
    
    bpy.ops.mesh.primitive_cylinder_add(radius=XTRrad, depth=XTRheight, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    xtr = bpy.context.active_object
    xtr.name = "xtr"
    bpy.ops.transform.translate(value=(0, 0, xtr.dimensions.z/2), constraint_axis=(False,False,True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
         
    bpy.ops.mesh.primitive_cylinder_add(radius=axelPunchR, depth=1, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    axelPunch = bpy.context.active_object
    axelPunch.name = "axelPunch"   
    
    subtractObj(xtr,axelPunch)
#    deleteObj(axelPunch)
    
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
        subtractObj(wisk,axelPunch)

    deleteObj(axelPunch)

    bpy.ops.object.select_all(action='TOGGLE')
    bpy.ops.object.join()       

mister()