filename = "c:/Users/BeckyBot/Desktop/Botnyst/Prototype Models/Scripts/M.py"
exec(compile(open(filename).read(), filename, 'exec'))

def PlantHousing():

    #Main Piece
    bpy.ops.mesh.primitive_cone_add(radius1=plntHsngRad1, radius2=plntHsngRad2, depth=plntHsngHght, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))    
    plntHsng = bpy.context.active_object
    plntHsng.name = "plntHsng"
    subdivisionSubsurface(plntHsng, 3, 3) #V:3074
    bpy.ops.transform.translate(value=(0, 0, plntHsng.dimensions.z/2 + reservoirHght), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        
    bpy.ops.mesh.primitive_cone_add(radius1=plntHsngRad1 - plntHsngThcknss, radius2=plntHsngRad2 - plntHsngThcknss, depth=plntHsngHght - plntHsngThcknss, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    plntHsngPnch = bpy.context.active_object
    plntHsngPnch.name = "plntHsngPnch"
    subdivisionSubsurface(plntHsngPnch, 3, 3) #V:6148
    bpy.ops.transform.translate(value=(0, 0, plntHsng.dimensions.z/2 + reservoirHght - plntHsngThcknss/2), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        
    subtractObj(plntHsng, plntHsngPnch)
    deleteObj(plntHsngPnch) #V:182,498
    decimateObj(plntHsng, 0.04)#10,082

    RockwoolPlug() 
    rockWoolPlug = bpy.context.active_object
    rockWoolPlug.name = "rockWoolPlug"
    bpy.ops.transform.rotate(value=pi/2 - plntHsngSlantAngle, axis=(0, 1, 0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.translate(value= ((plntHsngRad1-plntHsngRad2)/(bttmRwsRtWtrDstnc/plntHsngHght), 0, reservoirHght + bttmRwsRtWtrDstnc), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
      
    for i in range (0,numOfRow):
        for j in range (0,numOfRootPlugsPerRow):       
            subtractObj(plntHsng, rockWoolPlug)
            bpy.ops.transform.rotate(value=2*pi/numOfRootPlugsPerRow, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        bpy.ops.transform.translate(value= (-rowSpacing*tan(plntHsngSlantAngle), 0, rowSpacing), constraint_axis=(True, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
        bpy.ops.transform.rotate(value=pi/numOfRootPlugsPerRow, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    
    deleteObj(rockWoolPlug)
    
    #Drainage Collar
    bpy.ops.mesh.primitive_torus_add(rotation=(0, 0, 0), view_align=False, location=(0, 0, 0), minor_segments=40, major_radius=reservoirRad, minor_radius=plntHsngCllrRad, abso_major_rad=1.25, abso_minor_rad=0.75)
    drngCllr = bpy.context.active_object
    drngCllr.name = "drngCllr"
    
    bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(0, 0, 0), "constraint_axis":(False, False, False), "constraint_orientation":'GLOBAL', "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "texture_space":False, "remove_on_cancel":False, "release_confirm":False})
    bpy.data.objects['drngCllr'].select = False
    bpy.data.objects['drngCllr.001'].select = True    
    drngCllrPnch = bpy.context.active_object
    drngCllrPnch.name = "drngCllrPnch"
    bpy.ops.transform.translate(value=(0, 0, -reservoirThcknss), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    
    subtractObj(drngCllr, drngCllrPnch)
    deleteObj(drngCllrPnch)
           
    bpy.ops.mesh.primitive_cone_add(radius1=reservoirRad, radius2=reservoirRad, depth=plntHsngCllrRad*2, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    drngCllrPnch1 = bpy.context.active_object
    drngCllrPnch1.name = "drngCllrPnch1"

    intersectObj(drngCllr, drngCllrPnch1)
    deleteObj(drngCllrPnch1)
           
    bpy.ops.mesh.primitive_cube_add(view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    drngCllrPnch2 = bpy.context.active_object
    drngCllrPnch2.name = "drngCllrPnch2"
    bpy.ops.transform.resize(value=(reservoirRad,reservoirRad,plntHsngCllrRad), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.translate(value=(0, 0, -drngCllrPnch.dimensions.z/2), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        
    subtractObj(drngCllr, drngCllrPnch2)
    deleteObj(drngCllrPnch2)
      
    bpy.data.objects['drngCllr'].select = True
    bpy.ops.transform.resize(value=(0,0,plntHsngCllrHght), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.translate(value=(0, 0, reservoirHght - drngCllr.dimensions.z), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    
    bpy.data.objects['plntHsng'].select = True
    bpy.ops.object.join()
    plntHsng = bpy.context.active_object
    plntHsng.name = "plntHsng"
    
def Frustum():
    #http://mathforum.org/dr.math/faq/formulas/BuildFrustum.html
    t = atan((plntHsngRad1-plntHsngRad2)/plntHsngHght)
    S = plntHsngRad1/sin(t)
    s = S - plntHsngRad2/sin(t)
    T = 2*pi*sin(t)
    
    bpy.ops.mesh.primitive_cone_add(radius1=S, radius2=S, depth=plntHsngThcknss, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    frustum = bpy.context.active_object
    frustum.name = "frustum"

    bpy.ops.mesh.primitive_cube_add(radius=S, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    frustumEdgePnch = bpy.context.active_object
    frustumEdgePnch.name = "frustumEdgePnch"

    bpy.ops.transform.translate(value=(0, S, 0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    subtractObj(frustum,frustumEdgePnch)
    bpy.ops.transform.translate(value=(-S, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
    bpy.ops.transform.rotate(value=pi/2, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    subtractObj(frustum,frustumEdgePnch)
    bpy.ops.transform.rotate(value=pi/2-T, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    subtractObj(frustum,frustumEdgePnch)
    deleteObj(frustumEdgePnch)

    bpy.ops.mesh.primitive_cone_add(radius1=S-s, radius2=S-s, depth=plntHsngThcknss+0.01, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    frustumCirPnch = bpy.context.active_object
    frustumCirPnch.name = "frustumCirPnch"
    subtractObj(frustum,frustumCirPnch)
    deleteObj(frustumCirPnch)

    RockwoolPlug()
    bpy.data.objects['rockwoolPlug'].select = True
    rockwoolPlug = bpy.context.active_object
    rockwoolPlug.name = "rockwoolPlug"    

    for i in range (0,numOfRow):
        bpy.ops.object.origin_set(type='GEOMETRY_ORIGIN')
        bpy.ops.transform.translate(value= (S-s + bttmRwsRtWtrDstnc - rowSpacing * i, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
        bpy.ops.transform.rotate(value= -T/numOfRootPlugsPerRow/4 -T/numOfRootPlugsPerRow/2 * abs(cos(pi/2*i)), axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

        for j in range (0,numOfRootPlugsPerRow):       
            subtractObj(frustum, rockwoolPlug)
            bpy.ops.transform.rotate(value=-T/numOfRootPlugsPerRow, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    deleteObj(rockwoolPlug)
    
def RockwoolPlug():
    bpy.ops.mesh.primitive_cone_add(radius1=rwpRad, radius2=rwpRad, depth=rwpHght, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    rockwoolPlug = bpy.context.active_object
    rockwoolPlug.name = "rockwoolPlug"    