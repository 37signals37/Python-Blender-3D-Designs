import bpy
from math import cos, sin, tan, sqrt, atan

def makeCup():
    makeCupBody()
    makeInteriorWalls()       
    makeCupTop()
        
    bpy.context.scene.objects.active = bpy.data.objects["wall"]

    bpy.data.objects['wall'].select = True
    bpy.data.objects['s1'].select = True
    bpy.data.objects['ws'].select = True
    bpy.ops.object.join()
    cup = bpy.context.active_object
    cup.name = "cup"
    
def makeCupBody():
    mesh = bpy.data.meshes.new("wall")
    wall = bpy.data.objects.new("wall",mesh)
     
    #set mesh location
    wall.location = bpy.context.scene.cursor_location
    bpy.context.scene.objects.link(wall)
    
    # mesh arrays
    verts = []  # the vertex array
    faces = []  # the face array
    
    theta = 2*pi/vCnt
    
    #Add the lower circle
    inc = 0
    while inc < 2*pi:   
        verts.append((outerR*cos(inc),outerR*sin(inc),0))
        inc = round((inc + theta),7)
        #print(inc)
    
    inc = 0
    while inc < 2*pi:
        verts.append((innerR*cos(inc),innerR*sin(inc),0))
        inc = round((inc + theta),7)
    
    for i in range (0, vCnt-1):
        faces.append((i,i+vCnt,i+vCnt+1,i+1))
        faces.append((vCnt-1,2*vCnt-1,vCnt,0))
    
    #Add the upper circle
    inc = 0
    while inc < 2*pi:   
        verts.append((outerRUp*cos(inc),outerRUp*sin(inc),hght))
        inc = round((inc + theta),7)
    
    inc = 0
    while inc < 2*pi:
        verts.append((innerRUp*cos(inc),innerRUp*sin(inc),hght))
        inc = round((inc + theta),7)
    
    for i in range (vCnt*2, vCnt*3-1):
        #print(i,"",i+vCnt,"",i+vCnt+1,"",i+1)
        faces.append((i,i+vCnt,i+vCnt+1,i+1))
        
    faces.append((3*vCnt-1,4*vCnt-1,3*vCnt,2*vCnt))
    
    #Connecting the lower and upper circle
    for i in range (0, vCnt-1):
        faces.append((i,2*vCnt+i,2*vCnt+i+1,i+1))
        faces.append((vCnt+i,3*vCnt+i,3*vCnt+i+1,vCnt+i+1))
    
    faces.append((vCnt-1,3*vCnt-1,2*vCnt,0))
    faces.append((vCnt*2-1,4*vCnt-1,3*vCnt,vCnt))

    mesh.from_pydata(verts,[],faces)
    mesh.update(calc_edges=True)
    
def makeCupTop():     
    s1 = bpy.ops.mesh.primitive_uv_sphere_add
    s1(location=(0,0,0))
    s1 = bpy.context.active_object 
    s1.name = "s1"
    bpy.ops.transform.resize(value=(outerRUp, outerRUp, outerRUp), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)    
    
    s2 = bpy.ops.mesh.primitive_uv_sphere_add
    s2(location=(0,0,0))
    s2 = bpy.context.active_object 
    s2.name = "s2"
    bpy.ops.transform.resize(value=(innerRUp, innerRUp, innerRUp), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    
    c1 = bpy.ops.mesh.primitive_cube_add
    c1(location=(0,0,0))
    c1 = bpy.context.active_object 
    c1.name = "c1"
    bpy.ops.transform.resize(value=(outerRUp, outerRUp, outerRUp), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.translate(value=(0, 0, -outerRUp), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        
    #Adding the plug holes
    #####
    zInc = 0
    ph = 0
    for i in range(0,plugHoleCnt):
        bpy.ops.mesh.primitive_cylinder_add(radius=plugHoleR, depth=plugHolelngth, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
        temp = bpy.context.active_object
        temp.name = "ph" + str(ph)
        bpy.ops.transform.rotate(value=(pi/2 - plugHoleRot), axis=(1, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        bpy.ops.transform.translate(value=(0, -plugHoleDist*cos(plugHoleDistTheta), hght+plugHoleDist*sin(plugHoleDistTheta)), constraint_axis=(False, True, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
        bpy.ops.transform.rotate(value=zInc, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        zInc = zInc + plugHoleZtheta
    
        ph = ph + 1
    
    for i in range (0, ph):
        bpy.data.objects["ph" + str(i)].select = True
    
    bpy.ops.object.join()
    ph = bpy.context.active_object
    ph.name = "ph"
              
    makeCupPunch()
    cupPunch = bpy.context.active_object 
    bpy.ops.transform.translate(value=(0, 0, hght + domePunchHght), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.data.objects['cupPunch'].select = False
                                    
    subtractObj(s1, c1)
    subtractObj(s1, s2)
    
    bpy.data.objects['s1'].select = True
    bpy.ops.transform.translate(value=(0, 0, hght), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    
    subtractObj(s1, cupPunch)
    subtractObj(s1, ph)
    
    deleteObj(s2)
    deleteObj(ph)
    deleteObj(cupPunch)
    deleteObj(c1)

def makeCupPunch():
        #Adding the dome hole punch
    bpy.ops.mesh.primitive_cylinder_add(view_align=False, enter_editmode=False, location=(0, 0, 1), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    cupPunch = bpy.context.active_object 
    cupPunch.name = "cupPunch"
    
    bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
    bpy.ops.transform.resize(value=(domePunchMult, domePunchMult, hght/2*domePunchMult), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=0)
    
    mesh = cupPunch.data
    for i in range(0, len(mesh.vertices)):
        if mesh.vertices[i].co.z > 0.0:       
            mesh.vertices[i].co.x = mesh.vertices[i].co.x * outerRUp * domePunchMult
            mesh.vertices[i].co.y = mesh.vertices[i].co.y * outerRUp * domePunchMult
        
def makeInteriorWalls():
    zInc = 0
    w = 0
    for i in range(0,plugHoleCnt):
        bpy.ops.mesh.primitive_cube_add(view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
        temp = bpy.context.active_object
        temp.name = "w" + str(w)        
        bpy.ops.transform.resize(value=(wallWdth/2, (outerRUp - stInnrDiam - stThknss)/2 - 0.075, (hght + outerRUp)/2), constraint_axis=(True, True, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)                                   
        bpy.ops.transform.translate(value=(0, outerRUp - temp.dimensions.y/2 - 0.1, (hght+outerRUp)/2), constraint_axis=(False, True, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)                
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR')                
        bpy.ops.transform.rotate(value=zInc, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        zInc = zInc + plugHoleZtheta    
        w = w + 1    
    
    for i in range (0, w):
        bpy.data.objects["w" + str(i)].select = True
    
    bpy.ops.object.join()
    ws = bpy.context.active_object
    ws.name = "ws"
        
    makeCupPunch()
        
    s1 = bpy.ops.mesh.primitive_uv_sphere_add
    s1(location=(0,0,0))
    s1 = bpy.context.active_object 
    s1.name = "s1"
    bpy.ops.transform.resize(value=(outerRUp, outerRUp, outerRUp), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    c1 = bpy.ops.mesh.primitive_cube_add
    c1(location=(0,0,0))
    c1 = bpy.context.active_object 
    c1.name = "c1"
    bpy.ops.transform.resize(value=(outerRUp, outerRUp, outerRUp), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.translate(value=(0, 0, -outerRUp), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    
    subtractObj(s1,c1)
        
    deleteObj(c1)
    bpy.data.objects["s1"].select = True
    bpy.ops.transform.translate(value=(0, 0, hght), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    bpy.data.objects["cupPunch"].select = True
    bpy.ops.object.join()
    s1 = bpy.context.active_object            
    intersectObj(ws, s1)
    deleteObj(s1)
    
    makeCupPunch()
    cupPunch = bpy.context.active_object 
    bpy.ops.transform.translate(value=(0, 0, hght + domePunchHght - intWlsCupPnchOffset), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    subtractObj(ws,cupPunch)
    deleteObj(cupPunch)

    bpy.ops.mesh.primitive_cylinder_add(view_align=False, enter_editmode=False, location=(0, 0, 1), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    cntrPunch = bpy.context.active_object 
    bpy.ops.transform.resize(value=(intWlsCntrPnchR, intWlsCntrPnchR, hght+domePunchHght), constraint_axis=(True, True, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=0)
    bpy.ops.transform.translate(value=(0, 0, (hght + domePunchHght)/2), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    subtractObj(ws,cntrPunch)    
    deleteObj(cntrPunch)    

def makePunchHoles():
    
    zInc = 0
    ph = 0
    for i in range(0,plugHoleCnt):
        bpy.ops.mesh.primitive_cylinder_add(radius=plugHoleR, depth=plugHolelngth, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
        temp = bpy.context.active_object
        temp.name = "ph" + str(ph)
        bpy.ops.transform.rotate(value=(pi/2 - plugHoleRot), axis=(1, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        bpy.ops.transform.translate(value=(0, -plugHoleDist*cos(plugHoleDistTheta), hght+plugHoleDist*sin(plugHoleDistTheta)), constraint_axis=(False, True, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
        bpy.ops.transform.rotate(value=zInc, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        zInc = zInc + plugHoleZtheta
    
        ph = ph + 1
    
    for i in range (0, ph):
        bpy.data.objects["ph" + str(i)].select = True
    
    bpy.ops.object.join()
    ph = bpy.context.active_object
    ph.name = "ph"
    
def makeCentralVent():
    bpy.ops.mesh.primitive_cylinder_add(radius=innerR + wallWdth, depth=hght + outerRUp, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    cntrlVnt = bpy.context.active_object
    cntrlVnt.name = "cntrlVnt"
    bpy.ops.transform.translate(value=(0,0,cntrlVnt.dimensions.z/2), constraint_axis=(False,False,True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    
    bpy.ops.mesh.primitive_cylinder_add(radius=innerR, depth=hght + outerRUp + 0.01, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    cntrlVntPnch = bpy.context.active_object
    cntrlVntPnch.name = "cntrlVntPnch"
    bpy.ops.transform.translate(value=(0,0,cntrlVntPnch.dimensions.z/2), constraint_axis=(False,False,True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    
    makeCupPunch()
    cupPunch = bpy.context.active_object
    cupPunch.name = "cupPunch"
    bpy.ops.transform.translate(value=(0, 0, hght + domePunchHght - intWlsCupPnchOffset), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    subtractObj(cntrlVnt, cupPunch)
    deleteObj(cupPunch)
    
    subtractObj(cntrlVnt, cntrlVntPnch)
    deleteObj(cntrlVntPnch)
            
    mistHoleR = 0.1
    mistHoleDepth = 1
    
    zInc = 0
    ph = 0
    
    bpy.ops.mesh.primitive_cylinder_add(radius=mistHoleR, depth=mistHoleDepth, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    temp = bpy.context.active_object
    temp.name = "temp"
    bpy.ops.transform.translate(value=(0, cntrlVnt.dimensions.y/2 - temp.dimensions.y/2 - wallWdth/2, temp.dimensions.z/2), constraint_axis=(False, True, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.context.scene.cursor_location = (0.0,innerR,0.0)
    bpy.ops.object.origin_set(type='ORIGIN_CURSOR')    
    bpy.ops.transform.rotate(value=(-cupWallAngle), axis=(1, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.context.scene.cursor_location = (0.0,0.0,0.0)
    bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
    bpy.ops.transform.rotate(value=2*pi/plugHoleCnt/4, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    for j in range(0,3):
        for i in range(0,plugHoleCnt):
            bpy.ops.transform.rotate(value=2*pi/plugHoleCnt/2, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
            subtractObj(cntrlVnt,temp)
            bpy.ops.transform.rotate(value=2*pi/plugHoleCnt/2, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
            subtractObj(cntrlVnt,temp) 
        bpy.ops.transform.translate(value=(0, 0, cntrlVnt.dimensions.z/3), constraint_axis=(False, True, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)    

    deleteObj(temp)
    
    