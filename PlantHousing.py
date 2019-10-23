filename = "c:/Users/BeckyBot/Desktop/Botnyst/Prototype Models/Scripts/M.py"
exec(compile(open(filename).read(), filename, 'exec'))

def plantHousing():
    bpy.ops.mesh.primitive_cube_add(radius=1, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    inset = bpy.context.active_object
    inset.name = "inset"
    bpy.ops.transform.resize(value=(reservoirW/2 - plasticT, reservoirD/2 - plasticT, plantHousingOffset/2), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.translate(value=(0, 0, inset.dimensions.z/2 + reservoirH - plantHousingOffset), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    bpy.ops.mesh.primitive_cube_add(radius=1, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    insetPnch = bpy.context.active_object
    insetPnch.name = "insetPnch"
    bpy.ops.transform.resize(value=(reservoirW/2 - 2 * plasticT, reservoirD/2 - 2 * plasticT, plantHousingOffset/2), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.translate(value=(0, 0, insetPnch.dimensions.z/2 + reservoirH - plantHousingOffset), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    
    subtractObj(inset, insetPnch)
    deleteObj(insetPnch)
    
    bpy.ops.mesh.primitive_wedge_add(size_x=plantHousingH, size_y=plantHousingD - plantHousingSquareIn, size_z=2 * plasticT)
    leftWall = bpy.context.active_object
    leftWall.name = "leftWall"
    bpy.ops.transform.rotate(value=-1.5708, axis=(0, 1, 0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.rotate(value=-3.14159, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.translate(value=(-reservoirW/2 + plasticT, -plantHousingSquareIn/2, leftWall.dimensions.x/2 + reservoirH), constraint_axis=(True, True, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    bpy.ops.mesh.primitive_wedge_add(size_x=plantHousingH, size_y=plantHousingD - plantHousingSquareIn, size_z=2 * plasticT)
    rightWall = bpy.context.active_object
    rightWall.name = "rightWall"
    bpy.ops.transform.rotate(value=-1.5708, axis=(0, 1, 0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.rotate(value=-3.14159, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.translate(value=(reservoirW/2 - plasticT, -plantHousingSquareIn/2, leftWall.dimensions.x/2 + reservoirH), constraint_axis=(True, True, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)        

    bpy.ops.mesh.primitive_cube_add(radius=1, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    frontWall = bpy.context.active_object
    frontWall.name = "frontWall"
    bpy.ops.transform.resize(value=(reservoirW/2, sqrt(plantHousingH**2 + (reservoirD-plantHousingSquareIn)**2)/2, plasticT), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    #Hole Punch
    
    bpy.ops.mesh.primitive_cylinder_add(radius=rockWoolPnchD/2, depth=2, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    holePnch = bpy.context.active_object
    holePnch.name = "holePnch"
    bpy.ops.transform.translate(value=(-frontWall.dimensions.x/2 + 1.5 * rockWoolSpacingX,frontWall.dimensions.y/2 - 2 * rockWoolSpacingY, 0), constraint_axis=(True, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    for j in range(0,6):
        for i in range(0,4):
            subtractObj(frontWall,holePnch)
            bpy.ops.transform.translate(value=(rockWoolPnchD + rockWoolSpacingX,0,0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        bpy.ops.transform.translate(value=(-frontWall.dimensions.x,-rockWoolPnchD - 2 * rockWoolSpacingY, 0), constraint_axis=(True, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    bpy.ops.transform.translate(value=((rockWoolSpacingX + rockWoolPnchD)/2,6 * (rockWoolPnchD + 2 * rockWoolSpacingY) - rockWoolPnchD,0), constraint_axis=(True, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    for j in range(0,5):
        for i in range(0,3):
            subtractObj(frontWall,holePnch)
            bpy.ops.transform.translate(value=(rockWoolPnchD + rockWoolSpacingX,0,0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        bpy.ops.transform.translate(value=(-3 * (rockWoolPnchD + rockWoolSpacingX) ,-rockWoolPnchD - 2 * rockWoolSpacingY, 0), constraint_axis=(True, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    
    deleteObj(holePnch)       
    
    bpy.data.objects['frontWall'].select = True
    bpy.ops.transform.rotate(value=atan(plantHousingH/(plantHousingD-plantHousingSquareIn)), axis=(1, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.translate(value=(0, -plantHousingSquareIn/2, plantHousingH/2 + reservoirH), constraint_axis=(True, True, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)        
    bpy.ops.transform.translate(value=(0, plasticT * sin(atan(plantHousingH/(plantHousingD-plantHousingSquareIn))), 0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)        
    bpy.ops.transform.translate(value=(0, 0, -plasticT * cos(atan(plantHousingH/(plantHousingD-plantHousingSquareIn)))), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)        

    bpy.ops.mesh.primitive_cube_add(radius=1, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    frontWallPnch = bpy.context.active_object
    frontWallPnch.name = "frontWallPnch"
    bpy.ops.transform.resize(value=(reservoirW/2, reservoirD/2, 0), constraint_axis=(True, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.translate(value=(0, 0, -frontWallPnch.dimensions.z/2 + reservoirH), constraint_axis=(True, True, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)        
    subtractObj(frontWall, frontWallPnch)
    deleteObj(frontWallPnch)

    bpy.ops.mesh.primitive_cube_add(radius=1, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    frontWallPnch = bpy.context.active_object
    frontWallPnch.name = "frontWallPnch"
    bpy.ops.transform.resize(value=(plantHousingW/2, plantHousingD/2, 0), constraint_axis=(True, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.translate(value=(0, 2 * plantHousingD/2 - plantHousingSquareIn, -frontWallPnch.dimensions.z/2 + reservoirH + plantHousingH), constraint_axis=(True, True, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)        
    subtractObj(frontWall, frontWallPnch)
    deleteObj(frontWallPnch)

    bpy.ops.mesh.primitive_cube_add(radius=1, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    plantHousingCube = bpy.context.active_object
    plantHousingCube.name = "plantHousingCube"
    bpy.ops.transform.resize(value=(plantHousingW/2, plantHousingSquareIn/2, plantHousingH/2), constraint_axis=(True, True, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.translate(value=(0, reservoirD/2-plantHousingSquareIn/2, plantHousingH/2 + reservoirH), constraint_axis=(True, True, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    bpy.ops.mesh.primitive_cube_add(radius=1, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    plantHousingCubePnch = bpy.context.active_object
    plantHousingCubePnch.name = "plantHousingCubePnch"
    bpy.ops.transform.resize(value=(plantHousingW/2 - 2 * plasticT, plantHousingSquareIn/2 - plasticT, plantHousingH/2 - plasticT), constraint_axis=(True, True, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.translate(value=(0, reservoirD/2-plantHousingSquareIn/2 - plasticT, plantHousingH/2 + reservoirH - plasticT), constraint_axis=(True, True, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    subtractObj(plantHousingCube, plantHousingCubePnch)
    deleteObj(plantHousingCubePnch)

    bpy.data.objects['frontWall'].select = True
    bpy.data.objects['leftWall'].select = True
    bpy.data.objects['rightWall'].select = True
    bpy.data.objects['plantHousingCube'].select = True
    bpy.data.objects['inset'].select = True
    bpy.ops.object.join()