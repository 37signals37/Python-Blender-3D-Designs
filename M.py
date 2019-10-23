import bpy
from math import cos, sin, tan, sqrt, atan

pi = 3.14159

def Bracket():
    raise Exception()

def deleteObj(obj1):
    for obj in bpy.data.objects:
        obj.select = False
        
    obj1.select = True
    bpy.ops.object.delete(use_global=False)

def subtractObj(obj1, obj2):    
    bpy.context.scene.objects.active = bpy.data.objects[obj1.name]      
    bpy.ops.object.modifier_add(type='BOOLEAN')
    bpy.context.object.modifiers["Boolean"].operation = 'DIFFERENCE'
    bpy.context.object.modifiers["Boolean"].object = bpy.data.objects[obj2.name]
    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")

def subsurf(obj1, levels):
    bpy.context.scene.objects.active = bpy.data.objects[obj1.name]      
    bpy.ops.object.modifier_add(type='SUBSURF')
    bpy.context.object.modifiers["Subsurf"].levels = levels
    bpy.context.object.modifiers["Subsurf"].render_levels = levels
    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Subsurf")


def intersectObj(obj1, obj2):    
    bpy.context.scene.objects.active = bpy.data.objects[obj1.name]      
    bpy.ops.object.modifier_add(type='BOOLEAN')
    bpy.context.object.modifiers["Boolean"].operation = 'INTERSECT'
    print(obj2.name)
    bpy.context.object.modifiers["Boolean"].object = bpy.data.objects[obj2.name]
    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")
      
def remeshObj(obj1, octree_depth):
    bpy.context.scene.objects.active = bpy.data.objects[obj1.name]
    bpy.ops.object.modifier_add(type='REMESH')
    bpy.context.object.modifiers["Remesh"].octree_depth = octree_depth
    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Remesh")

def decimateObj(obj1, decimateRatio):
    bpy.context.scene.objects.active = bpy.data.objects[obj1.name]
    bpy.ops.object.modifier_add(type='DECIMATE')
    bpy.context.object.modifiers["Decimate"].ratio = decimateRatio
    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Decimate")

def deleteEverything():
    bpy.ops.object.select_all(action='TOGGLE')
    bpy.ops.object.delete(use_global=False)


def makeCylinder(d,h,name):
    temp = bpy.ops.mesh.primitive_cylinder_add(radius=d/2, depth=h, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    temp.name = name

      
def makeRootHolders():
    #Adding the root holders
    tth = 0
    inc = 0
    
    for i in range(0,rtHldrTthCnt):
        cube = bpy.ops.mesh.primitive_cube_add
        cube(location=(0,0,0))
        c1 = bpy.context.active_object 
        c1.name = "tth" + str(tth)
        bpy.ops.transform.resize(value=(rtHldrTthPnchWdth, rootHolderR+1, rtHldrTthPnchHght), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        bpy.ops.transform.translate(value=(0, 0, plugHolelngth/2), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        bpy.ops.transform.rotate(value=inc, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        inc = inc + rtHldrTthTheta
        tth = tth + 1
    
    for i in range (0, tth):
            bpy.data.objects["tth" + str(i)].select = True
            
    bpy.ops.object.join()
    tth = bpy.context.active_object
    tth.name = "tth"
    
    bpy.ops.mesh.primitive_cylinder_add(radius=rootHolderR-rootHolderWallThck, depth=plugHolelngth+1, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    c7 = bpy.context.active_object
    c7.name = "c7"
    
    #Adding the RootSlot punch
    rs = bpy.ops.mesh.primitive_cube_add
    rs(location=(0,0,0))
    rs = bpy.context.active_object 
    rs.name = "RootSlot"
    bpy.ops.transform.resize(value=(rtHldrTthPnchWdth*2, rootHolderR/2, plugHolelngth/2), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.translate(value=(0, rootHolderR, 0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.rotate(value=inc, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    
    bpy.ops.mesh.primitive_cylinder_add(radius=rootHolderR, depth=plugHolelngth, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    c6 = bpy.context.active_object
    c6.name = "c6"
    
    subtractObj(c6, rs)
    subtractObj(c6, c7)
    subtractObj(c6, tth)
            
    bpy.data.objects['c6'].select = False
    
    bpy.data.objects['tth'].select = True
    bpy.data.objects['RootSlot'].select = True
    bpy.data.objects['c7'].select = True
    bpy.ops.object.delete(use_global=False)    
        
def makeXTRfemale():
    xtrFemale = bpy.ops.mesh.primitive_uv_sphere_add
    xtrFemale(location=(0,0,0))
    xtrFemale = bpy.context.active_object 
    xtrFemale.name = "xtrFemale"
    bpy.ops.transform.resize(value=(outerRUp, outerRUp, outerRUp), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    
    sM2 = bpy.ops.mesh.primitive_uv_sphere_add
    sM2(location=(0,0,0))
    sM2 = bpy.context.active_object 
    sM2.name = "sM2"
    bpy.ops.transform.resize(value=(innerRUp, innerRUp, innerRUp), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    
    c1 = bpy.ops.mesh.primitive_cube_add
    c1(location=(0,0,0))
    c1 = bpy.context.active_object 
    c1.name = "c1"
    bpy.ops.transform.resize(value=(outerRUp, outerRUp, outerRUp), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.translate(value=(0, 0, -outerRUp), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    c2 = bpy.ops.mesh.primitive_cube_add
    c2(location=(0,0,0))
    c2 = bpy.context.active_object 
    c2.name = "c2"
    bpy.ops.transform.resize(value=(outerRUp+1, outerRUp+1, outerRUp), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.translate(value=(0, 0, -outerRUp + domePunchHght), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    makeCupPunch()
    cupPunch = bpy.context.active_object 
    
    subtractObj(xtrFemale, c1)
    subtractObj(xtrFemale, sM2)
    subtractObj(xtrFemale, c2)
    
    deleteObj(sM2)
    deleteObj(c1)
    deleteObj(c2)
    
    bpy.data.objects['cupPunch'].select = True
    bpy.ops.transform.translate(value=(0, 0,domePunchHght), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    
    subtractObj(xtrFemale, cupPunch)
    deleteObj(cupPunch)
    
    bpy.data.objects['xtrFemale'].select = True
    bpy.ops.transform.translate(value=(0, 0,-domePunchHght), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
    bpy.data.objects['xtrFemale'].select = False
    
def makeXTRMale():
    makeCupBody()
#    bpy.context.scene.objects.active = bpy.data.objects[obj1.name]
    xtrMale = bpy.data.objects['wall']
    xtrMale.name = "xtrMale"

    bpy.ops.mesh.primitive_cube_add(radius=1, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    xtrPnch = bpy.context.active_object
    xtrPnch.name = "xtrPnch"
    bpy.ops.transform.resize(value=(outerRUp+1, outerRUp+1, hght/2), constraint_axis=(True, True, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.translate(value=(0, 0,maleXTRHght + hght/2), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    remeshObj(xtrMale, 6)
    subtractObj(xtrMale, xtrPnch)
    deleteObj(xtrPnch)
    decimateObj(xtrMale, 0.1)
    
def getMaxFaceLocation(obj, dmsn):
            
    maxAve = 0
    sum = 0
    maxFace = 0;

    for f in obj.data.polygons:
        
        sum = 0
        
        for idx in f.vertices:
            world_point = obj.matrix_world * obj.data.vertices[idx].co
            sum = sum + world_point[dmsn]

        average = sum/len(f.vertices)                
        
        if(abs(average) > abs(maxAve)):                    
            maxAve = average
                         
    return maxAve
                         
                         
def subdivisionSubsurface(obj, viewLevels, renderLevels):    
    bpy.context.scene.objects.active = bpy.data.objects[obj.name]      
    bpy.ops.object.modifier_add(type='SUBSURF')
    bpy.context.object.modifiers["Subsurf"].subdivision_type = 'SIMPLE'
    bpy.context.object.modifiers["Subsurf"].levels = viewLevels
    bpy.context.object.modifiers["Subsurf"].render_levels = renderLevels
    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Subsurf")

name = "Blank"
            
def makeShape():
    bpy.ops.mesh.primitive_uv_sphere_add(view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    reservoir = bpy.context.active_object
    reservoir.name = name