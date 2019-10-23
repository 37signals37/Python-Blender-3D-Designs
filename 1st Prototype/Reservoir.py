filename = "c:/Users/BeckyBot/Desktop/Botnyst/Prototype Models/Scripts/M.py"
exec(compile(open(filename).read(), filename, 'exec'))

def importPump():
    full_path_to_file = "C://Users//BeckyBot//Desktop//Botnyst//Prototype Models//Parts//HJ-1142 pump.STL"
    file_name = "HJ-1142 pump.STL"
    file_directory = "C://Users//BeckyBot//Desktop//Botnyst//Prototype Models//Parts"
    bpy.ops.import_mesh.stl(filepath=full_path_to_file, filter_glob="*.stl",  files=[{"name":file_name, "name":file_name}], directory=file_directory)        
    pump = bpy.context.active_object
    pump.name = "pump"
    decimateObj(pump, 0.1)

def reservoir():
    
    bpy.ops.mesh.primitive_cone_add(radius1=reservoirRad, radius2=reservoirRad, depth=reservoirHght, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    reservoir = bpy.context.active_object
    reservoir.name = "reservoir"

    #Double check outcome of wall thickness    
    bpy.ops.mesh.primitive_cone_add(radius1=reservoirRad - reservoirThcknss, radius2=reservoirRad - reservoirThcknss, depth=reservoirHght - reservoirThcknss, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    reservoirPnch = bpy.context.active_object
    reservoirPnch.name = "reservoirPnch"

    subtractObj(reservoir, reservoirPnch)
    deleteObj(reservoirPnch)

    bpy.ops.mesh.primitive_cone_add(radius1=collarRad, radius2=collarRad, depth=reservoirHght, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    collarPnch = bpy.context.active_object
    collarPnch.name = "collarPnch"
    bpy.ops.transform.translate(value=(0, 0, reservoirThcknss + 0.01), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    subtractObj(reservoir, collarPnch)
    deleteObj(collarPnch)

    if(rotatingModel):
        bpy.ops.mesh.primitive_cone_add(radius1=brngPnchRad, radius2=brngPnchRad, depth=reservoirHght, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
        bearingPnch = bpy.context.active_object
        bearingPnch.name = "bearingPnch"
        bpy.ops.transform.translate(value=(reservoirRad - collarWdth/2, 0, reservoirThcknss), constraint_axis=(True, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR')

        for i in range(0, numOfBrngs):
            subtractObj(reservoir, bearingPnch)
            bpy.ops.transform.rotate(value=2*pi/numOfBrngs, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        
        deleteObj(bearingPnch)
        
    if(spinMisterModel):
        bpy.ops.mesh.primitive_cube_add(view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
        misterMotorCage = bpy.context.active_object
        misterMotorCage.name = "misterMotorCage"        
        bpy.ops.transform.resize(value=(misterMotorCageX/2, misterMotorCageY/2, misterMotorCageZ/2), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        bpy.ops.object.modifier_add(type='BEVEL')
        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Bevel")
        bpy.ops.transform.translate(value=(misterMotorCageXO, misterMotorCageYO, 0), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        bpy.ops.transform.rotate(value=misterMotorCageZA, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        subtractObj(reservoir, misterMotorCage)
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
        bpy.ops.object.origin_set(type='GEOMETRY_ORIGIN')
        bpy.ops.transform.rotate(value=-misterMotorCageZA, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

        #Double check outcome of wall thickness
        bpy.ops.mesh.primitive_cube_add(view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
        misterMotorCagePnch = bpy.context.active_object
        misterMotorCagePnch.name = "misterMotorCagePnch"
        bpy.ops.transform.resize(value=((misterMotorCageX - misterMotorCageT)/2, (misterMotorCageY - misterMotorCageT)/2, (misterMotorCageZ - misterMotorCageT)/2), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        bpy.ops.object.modifier_add(type='BEVEL')
        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Bevel")
        subtractObj(misterMotorCage, misterMotorCagePnch)
        bpy.ops.transform.translate(value=(0, misterMotorCageYO/2, 0), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        subtractObj(misterMotorCage, misterMotorCagePnch)
        deleteObj( misterMotorCagePnch)
        
        #Find exact length of punch based on  misterMotorCage thickness
        #Find exact YO offest for misterMotorCagePnchA
        bpy.ops.mesh.primitive_cone_add(radius1=misterMotorCageAxlePnchRad, radius2=misterMotorCageAxlePnchRad, depth=reservoirThcknss*10, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
        misterMotorCagePnchA = bpy.context.active_object
        misterMotorCagePnchA.name = "misterMotorCagePnchA"
        bpy.ops.transform.rotate(value=1.5708, axis=(1, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        bpy.ops.transform.translate(value=(0, -misterMotorCageYO/2, misterMotorCageAxlePnchZO), constraint_axis=(False, True, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        subtractObj(misterMotorCage, misterMotorCagePnchA)
        deleteObj(misterMotorCagePnchA)
        
        bpy.data.objects['misterMotorCage'].select = True
        bpy.ops.transform.translate(value=(misterMotorCageXO, misterMotorCageYO, 0), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        bpy.ops.transform.rotate(value=misterMotorCageZA, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    bpy.ops.mesh.primitive_cone_add(radius1=stirrerMotorR + reservoirThcknss, radius2=stirrerMotorR + reservoirThcknss, depth=stirrerMotorZ + reservoirThcknss, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    stirrerMotorCage = bpy.context.active_object
    stirrerMotorCage.name = "stirrerMotorCage"
        
    bpy.ops.mesh.primitive_cone_add(radius1=stirrerMotorR, radius2=stirrerMotorR, depth=stirrerMotorZ, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    stirrerMotorCagePnch = bpy.context.active_object
    stirrerMotorCagePnch.name = "stirrerMotorCagePnch"

    subtractObj(stirrerMotorCage, stirrerMotorCagePnch)
    bpy.ops.transform.translate(value=(0, 0, -stirrerMotorZ/2), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    subtractObj(stirrerMotorCage, stirrerMotorCagePnch)

    bpy.ops.transform.translate(value=(stirrerMotorCageXO, stirrerMotorCageYO, stirrerMotorZ/2-reservoirHght/2), constraint_axis=(True, True, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    subtractObj(reservoir, stirrerMotorCagePnch)    
    deleteObj(stirrerMotorCagePnch)

    bpy.ops.mesh.primitive_cone_add(radius1=stirrerMotorAxlePnchR, radius2=stirrerMotorAxlePnchR, depth=stirrerMotorAxlePnchZ, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    stirrerMotorCagePnchA = bpy.context.active_object
    stirrerMotorCagePnchA.name = "stirrerMotorCagePnchA"
    subtractObj(stirrerMotorCage,stirrerMotorCagePnchA)
    deleteObj(stirrerMotorCagePnchA)

    bpy.data.objects['stirrerMotorCage'].select = True
    bpy.ops.transform.translate(value=(stirrerMotorCageXO, stirrerMotorCageYO, stirrerMotorZ/2 - reservoirHght/2 + reservoirThcknss), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    
    #SonicatorCage
    bpy.ops.mesh.primitive_cylinder_add(radius=1, depth=sonicatorCageZ, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    sonicatorCage = bpy.context.active_object
    sonicatorCage.name = "sonicatorCage"    
    bpy.ops.transform.resize(value=(sonicatorCageX/2, sonicatorCageY/2, 0), constraint_axis=(True, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
       
    bpy.ops.mesh.primitive_cylinder_add(radius=1, depth=sonicatorCageZ*2, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    sonicatorCagePnch = bpy.context.active_object
    sonicatorCagePnch.name = "sonicatorCagePnch"
    bpy.ops.transform.resize(value=((sonicatorCageX - reservoirThcknss)/2, (sonicatorCageY - reservoirThcknss)/2, 0), constraint_axis=(True, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    subtractObj(sonicatorCage,sonicatorCagePnch)
    deleteObj(sonicatorCagePnch)
    
    bpy.data.objects['sonicatorCage'].select = True
    bpy.ops.transform.translate(value=(sonicatorCageXO, sonicatorCageYO, sonicatorCageZ/2 - reservoirHght/2), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.rotate(value=sonicatorCageZA, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    bpy.ops.mesh.primitive_cone_add(radius1=sonicatorCordPnchR, radius2=sonicatorCordPnchR, depth=sonicatorCordPnchZ, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    sonicatorCordPnch = bpy.context.active_object
    sonicatorCordPnch.name = "sonicatorCordPnch"
    bpy.ops.transform.translate(value=(sonicatorCordPnchXO, sonicatorCordPnchYO, 0), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    subtractObj(reservoir, sonicatorCordPnch)
    deleteObj(sonicatorCordPnch)

    bpy.data.objects['misterMotorCage'].select = True
    bpy.data.objects['sonicatorCage'].select = True
    bpy.data.objects['stirrerMotorCage'].select = True
    bpy.data.objects['reservoir'].select = True
    bpy.ops.object.join()
    bpy.ops.transform.translate(value=(0, 0, reservoirHght/2), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.data.objects['reservoir'].select = False

def stirrer():

   bpy.ops.mesh.primitive_cone_add(radius1=strrrMtrCnnctRad, radius2=strrrMtrCnnctRad, depth=strrrMtrCnnctHght, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
   motorConnect = bpy.context.active_object
   motorConnect.name = "motorConnect"
        
   #bpy.ops.mesh.primitive_cone_add(radius1=strrrMtrAxlPnchRad, radius2=strrrMtrAxlPnchRad, depth=strrrMtrCnnctHght*2, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
   #motorConnectAxlePnch = bpy.context.active_object
   #motorConnectAxlePnch.name = "motorConnectAxlePnch"

#   subtractObj(motorConnect, motorConnectAxlePnch)
#   deleteObj(motorConnectAxlePnch)    
               
   bpy.ops.mesh.primitive_cube_add(radius=1, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
   strrrArmA = bpy.context.active_object
   strrrArmA.name = "strrrArmA"
   bpy.ops.transform.resize(value=(strrrArmW, strrrArmL, strrrArmH), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
   bpy.ops.transform.translate(value=(strrrArmA.dimensions.x/2 + strrrMtrAxlPnchRad, 0, (motorConnect.dimensions.z - strrrArmA.dimensions.z)/2), constraint_axis=(True, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

   bpy.ops.mesh.primitive_cube_add(radius=1, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
   strrrArmB = bpy.context.active_object
   strrrArmB.name = "strrrArmB"
   bpy.ops.transform.resize(value=(strrrArmW, strrrArmL, strrrArmH), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
   bpy.ops.transform.translate(value=(-strrrArmB.dimensions.x/2 - strrrMtrAxlPnchRad, 0, (motorConnect.dimensions.z - strrrArmB.dimensions.z)/2), constraint_axis=(True, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

   bpy.ops.mesh.primitive_cone_add(radius1=strrrWngsRad, radius2=strrrWngsRad, depth=strrrWngsHght, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
   strrrWngA = bpy.context.active_object
   strrrWngA.name = "strrrWngA"

   bpy.ops.mesh.primitive_cone_add(radius1=strrrWngsRad, radius2=strrrWngsRad, depth=strrrWngsHght, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
   strrrWngPnch = bpy.context.active_object
   strrrWngPnch.name = "strrrWngPnch"
   bpy.ops.transform.translate(value=(0, strrrWngsPnchOffset, 0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

   subtractObj(strrrWngA, strrrWngPnch)

   bpy.ops.mesh.primitive_cone_add(radius1=strrrWngsRad, radius2=strrrWngsRad, depth=strrrWngsHght, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
   strrrWngB = bpy.context.active_object
   strrrWngB.name = "strrrWngB"
   subtractObj(strrrWngB, strrrWngPnch)
   
   deleteObj(strrrWngPnch)

   bpy.data.objects['strrrWngA'].select = True
   bpy.ops.transform.rotate(value=-3.14159, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
   bpy.ops.transform.resize(value=(3, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
   bpy.ops.transform.translate(value=(-strrrWngA.dimensions.x/2 + strrrMtrAxlPnchRad + strrrArmW * 2, 0, -strrrWngA.dimensions.z/2 + strrrMtrCnnctHght/2), constraint_axis=(True, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
   bpy.data.objects['strrrWngA'].select = False

   bpy.data.objects['strrrWngB'].select = True
   bpy.ops.transform.resize(value=(3, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
   bpy.ops.transform.translate(value=(strrrWngB.dimensions.x/2 - strrrMtrAxlPnchRad - strrrArmW * 2, 0, -strrrWngB.dimensions.z/2 + strrrMtrCnnctHght/2), constraint_axis=(True, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
   bpy.data.objects['strrrWngB'].select = False

   bpy.data.objects['strrrArmA'].select = True
   bpy.data.objects['strrrArmB'].select = True
   bpy.data.objects['strrrWngA'].select = True
   bpy.data.objects['strrrWngB'].select = True
   bpy.data.objects['motorConnect'].select = True
   bpy.ops.object.join()

   stirrer = bpy.context.active_object
   stirrer.name = "stirrer"

   bpy.ops.transform.rotate(value=-3.14159, axis=(1, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)