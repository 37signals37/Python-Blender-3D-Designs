#Repertier multiplier = 6.9
import bpy

holeHght = 3.2394
holeDiam = 0.0273 #last 0.0375, 0.05, 0.075,1,0.0875,0.08125
holeCnt = 8

holeSetCnt = 6
holeHeightIncr = 0.1620 #last 0.3

stOtrDiam = stInnrDiam + stThknss

pi = 3.14159
theta = 2*pi/holeCnt
holeSetTheta = theta/holeSetCnt
    
def makeWateringLine():

    bpy.ops.mesh.primitive_cylinder_add(radius=nzzlAttcDiam, depth=nzzlAttcHght + 1, view_align=False, enter_editmode=False, location=(0, 0, nzzlAttcHght/2), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    c1 = bpy.context.active_object
    c1.name = "c1"
    
    bpy.ops.mesh.primitive_cylinder_add(radius=nzzleAttcOtrDiam, depth=nzzlAttcHght, view_align=False, enter_editmode=False, location=(0, 0, nzzlAttcHght/2), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    nzzleAttc = bpy.context.active_object
    nzzleAttc.name = "nzzlAttc"
    
    subtractObj(nzzleAttc, c1)
    deleteObj(c1)
        
    #Adding the dome connector
    #####    
    s2 = bpy.ops.mesh.primitive_uv_sphere_add
    s2(location=(0,0,0))
    s2 = bpy.context.active_object 
    s2.name = "s2"
    bpy.ops.transform.resize(value=(nzzlAttcDiam, nzzlAttcDiam, nzzlAttcDiam), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=0)
    
    cube = bpy.ops.mesh.primitive_cube_add
    cube(location=(0,0,0))
    c1 = bpy.context.active_object 
    c1.name = "c1"
    bpy.ops.transform.resize(value=(nzzleAttcOtrDiam, nzzleAttcOtrDiam, nzzleAttcOtrDiam), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=0)
    bpy.ops.transform.translate(value=(0, 0, -nzzleAttcOtrDiam), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=0)
    
    #Adding the stout hole
    bpy.ops.mesh.primitive_cylinder_add(radius=stInnrDiam, depth=nzzlAttcHght+nzzlAttcDiam+stHght+stHght, view_align=False, enter_editmode=False, location=(0, 0, nzzlAttcHght/2), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    c4 = bpy.context.active_object
    c4.name = "c4"
    bpy.ops.transform.translate(value=(0, 0, stHght/2 + nzzlAttcHght/2 + nzzlAttcDiam/2), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    #nzzlAttcDiam = radius of innerSphere used to hollow out connecting dome
    bpy.data.objects['c4'].select = False
    
    sWL = bpy.ops.mesh.primitive_uv_sphere_add
    sWL(location=(0,0,0))
    sWL = bpy.context.active_object
    sWL.name = "sWL"
    bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
    bpy.ops.transform.resize(value=(nzzleAttcOtrDiam, nzzleAttcOtrDiam, nzzleAttcOtrDiam), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=0)
        
    subtractObj(sWL, c1)
    subtractObj(sWL, c4)
    subtractObj(sWL, s2)
            
    deleteObj(s2)
    deleteObj(c1)    
        
    bpy.data.objects['sWL'].select = True
    bpy.ops.transform.translate(value=(0, 0, nzzlAttcHght), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        
    #Adding the stout
    #####
        
    #Adding the spray holes
    
    holeSetHght = holeDiam
    
    wh = 0
    
    for i in range(0,holeSetCnt):
    
        inc = i * holeSetTheta
        
        while inc < 2*pi:       
            inc = round((inc + theta),7)
            bpy.ops.mesh.primitive_cylinder_add(radius=holeDiam, depth=stOtrDiam, view_align=False, enter_editmode=False, location=(0, stOtrDiam, holeSetHght), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
            temp = bpy.context.active_object
            temp.name = "wh" + str(wh)
            bpy.ops.transform.rotate(value=1.5708, axis=(1, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
            bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
            bpy.ops.transform.rotate(value=inc, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
            wh = wh + 1
    
        for i in range (0, wh):
            bpy.data.objects["wh" + str(i)].select = True
        
        holeSetHght = holeSetHght + holeHeightIncr
        
    bpy.ops.object.join()
    wh = bpy.context.active_object
    wh.name = "wh"
    bpy.ops.transform.translate(value=(0, 0, holeHght), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    
    bpy.ops.mesh.primitive_cylinder_add(radius=stOtrDiam, depth=stHght, view_align=False, enter_editmode=False, location=(0, 0, stHght/2), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    stout = bpy.context.active_object
    stout.name = "stout"
    bpy.ops.transform.translate(value=(0, 0, nzzlAttcHght + nzzlAttcDiam), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.data.objects["stout"].select = False
    #nzzlAttcDiam = radius of innerSphere used to hollow out connecting dome

    subtractObj(stout, c4)
    subtractObj(stout, wh)
    
    deleteObj(c4)
    deleteObj(wh)
        
    bpy.data.objects['nzzlAttc'].select = True
    bpy.data.objects['sWL'].select = True
    bpy.data.objects['stout'].select = True
    bpy.ops.object.join()
    
    cup = bpy.context.active_object
    
    decimateObj(cup, 0.4)
    
    bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
    bpy.data.objects['stout'].select = False
    