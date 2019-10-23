import bpy
from math import cos, sin, tan, sqrt, atan, radians

#filename = "c:/Users/BeckyBot/Desktop/Botnyst/Prototype Models/Scripts/2nd Prototype/M.py"
filename = "F:/Blender Scripts/Scripts/2nd Prototype/M.py"
exec(compile(open(filename).read(), filename, 'exec'))

KISSslicerMult = 25.62 #27.75 #27.5, 26.667, 40
#motorFrameH = 0.5

basinL = 10
basinW = 5
basinH = 6
basinT = 0.12

degreeOfCurvature = 45

reservoirTopBuffer = 0.5
reservoirBottomBuffer = 2.5
reservoirW = basinW * 0.45
reservoirH = basinH - reservoirTopBuffer - reservoirBottomBuffer
reservoirT = 0.12
degreeOfReservoirCeilingCurvature = 0.2

reservoirCPL = 6
reservoirCPW = 3.5
reservoirCPH = 6

reservoirWaterHolePnchR = 0.175

reservoirHolePnchR = 0.375

reservoirLidBuffer = 0.2

waterTrapBoxL = 0.5
waterTrapBoxW = 0.5
waterTrapBoxH = 0.5
waterLineR = 0.015

motorPnchL = 1.5
motorPnchR = 1.14 #1.09

motorHsngBuffer = 0.4 #Closing the gap with the basin piece
motorPnchBottomBuffer = 2
motorHsngT = 0.05
motorHsngL = motorPnchL + motorHsngT + motorHsngBuffer/2
motorHsngW = motorPnchR + motorHsngT
motorHsngH = reservoirBottomBuffer

#0.085 for motor axle
axlePnchR = 0.065
axlePnchD = 10 
 
ridgeBuffer = 0.5
 
floatTrapCavityAttachmentR = 0.3
floatTrapCavityAttachmentD = 0.35

floatTrapCavityD = 1
floatTrapCavityT = 0.15
floatTrapCavityXShift = 1.8

waterLinePnchR = 0.06
 
def basin():
    
    bpy.ops.mesh.primitive_uv_sphere_add(view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    basin = bpy.context.active_object
    basin.name = "basin"
    subsurf(basin, 2)
    bpy.ops.transform.resize(value=(basinL/basin.dimensions.x, basinW/basin.dimensions.y, basinH/basin.dimensions.z), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    bpy.ops.mesh.primitive_cube_add(radius=1, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    basinPnch = bpy.context.active_object
    basinPnch.name = "basinPnch"
    bpy.ops.transform.resize(value=(basinL/2, basinW/2, basinH/2), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.translate(value=(0, 0, basinH/2), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    subtractObj(basin, basinPnch)
    bpy.ops.transform.translate(value=(0, 0, -basinH/2 * sin((degreeOfCurvature/180 * pi)) - 2 * basinH/2), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    subtractObj(basin, basinPnch)
    deleteObj(basinPnch)    

    bpy.data.objects['basin'].select = True
    bpy.ops.transform.resize(value=(basinL/basin.dimensions.x, basinW/basin.dimensions.y, basinH/basin.dimensions.z), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(0, 0, 0), "constraint_axis":(False, False, False), "constraint_orientation":'GLOBAL', "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "texture_space":False, "remove_on_cancel":False, "release_confirm":False})
    basinPnch = bpy.context.active_object
    basinPnch.name = "basinPnch"
    bpy.ops.transform.resize(value=((basinL-basinT)/basinL, (basinW-basinT)/basinW, (basinH-basinT/2)/basinH), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)    
    bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(0, 0, 0), "constraint_axis":(False, False, False), "constraint_orientation":'GLOBAL', "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "texture_space":False, "remove_on_cancel":False, "release_confirm":False})
    reservoir = bpy.context.active_object
    reservoir.name = "reservoir"
    subtractObj(basin, basinPnch)

    bpy.ops.mesh.primitive_cube_add(radius=basinL/2, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    reservoirPnch = bpy.context.active_object
    reservoirPnch.name = "reservoirPnch"
    bpy.ops.transform.translate(value=(0, 0, basinL/2-reservoirTopBuffer), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    subtractObj(reservoir, reservoirPnch)
    bpy.ops.transform.translate(value=(0, 0, -reservoirH), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    intersectObj(reservoir, reservoirPnch)
    deleteObj(reservoirPnch)

    bpy.ops.mesh.primitive_uv_sphere_add(view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    reservoirCurver = bpy.context.active_object
    reservoirCurver.name = "reservoirCurver"
    subsurf(reservoirCurver, 1)
    bpy.ops.transform.resize(value=(basinL/2, basinW/2, degreeOfReservoirCeilingCurvature), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.translate(value=(0, 0, -reservoirTopBuffer), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    subtractObj(reservoir, reservoirCurver)
    deleteObj(reservoirCurver)

    bpy.data.objects['reservoir'].select = True
    bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(0, 0, 0), "constraint_axis":(False, False, False), "constraint_orientation":'GLOBAL', "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "texture_space":False, "remove_on_cancel":False, "release_confirm":False})
    reservoirHollowPnch = bpy.context.active_object
    reservoirHollowPnch.name = "reservoirHollowPnch"
    bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
    bpy.ops.transform.resize(value=((reservoir.dimensions.x - reservoirT)/reservoir.dimensions.x, (reservoir.dimensions.y - reservoirT)/reservoir.dimensions.y, (reservoir.dimensions.z - reservoirT)/reservoir.dimensions.z), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)    
#    bpy.ops.transform.resize(value=((reservoir.dimensions.x - 2 * reservoirT)/reservoir.dimensions.x, (reservoir.dimensions.y - 2 * reservoirT)/reservoir.dimensions.y, (reservoir.dimensions.z - reservoirT)/reservoir.dimensions.z), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)    

    ###
    bpy.ops.mesh.bolt_add(bf_Model_Type='bf_Model_Nut', bf_Shank_Length=0, bf_Shank_Dia=3, bf_Phillips_Bit_Depth=1.14315, bf_Allen_Bit_Depth=1.5, bf_Allen_Bit_Flat_Distance=2.5, bf_Hex_Head_Height=2, bf_Hex_Head_Flat_Distance=5.5, bf_CounterSink_Head_Dia=6.3, bf_Cap_Head_Height=3, bf_Cap_Head_Dia=5.5, bf_Dome_Head_Dia=5.6, bf_Pan_Head_Dia=5.6, bf_Philips_Bit_Dia=1.82, bf_Thread_Length=6, bf_Major_Dia=3, bf_Pitch=0.71, bf_Minor_Dia=2.62111, bf_Crest_Percent=10, bf_Root_Percent=10, bf_Hex_Nut_Height=2.4, bf_Hex_Nut_Flat_Distance=5.5)
    reservoirNut = bpy.context.active_object
    reservoirNut.name = "reservoirNut"
    bpy.ops.transform.translate(value=(basinL/2 - floatTrapCavityXShift, 0, -reservoirH - reservoirTopBuffer), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.rotate(value=0.523599, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    bpy.ops.mesh.primitive_cylinder_add(radius = reservoirWaterHolePnchR, depth = reservoirT * 5, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    reservoirWaterHolePnch = bpy.context.active_object
    reservoirWaterHolePnch.name = "reservoirWaterHolePnch"
    bpy.ops.transform.translate(value=(basinL/2 - floatTrapCavityXShift, 0, -reservoirH - reservoirTopBuffer), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    bpy.ops.mesh.primitive_cylinder_add(radius=1, depth=2, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    reservoirCentralPnch = bpy.context.active_object
    reservoirCentralPnch.name = "reservoirCentralPnch"
    bpy.ops.transform.resize(value=(reservoirCPL/2, reservoirCPW/2, reservoirCPH), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)      
    intersectObj(reservoirCentralPnch, reservoir)
    bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(0, 0, 0), "constraint_axis":(False, False, False), "constraint_orientation":'GLOBAL', "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "texture_space":False, "remove_on_cancel":False, "release_confirm":False})
    reservoirCentralHollowPnch = bpy.context.active_object
    reservoirCentralHollowPnch.name = "reservoirCentralHollowPnch"
    bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
    bpy.ops.transform.resize(value=((reservoirCPL/2 - reservoirT)/(reservoirCPL/2), (reservoirCPW/2 - reservoirT)/(reservoirCPW/2), 1.01), constraint_axis=(True, True, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    subtractObj(reservoir, reservoirHollowPnch)
    deleteObj(reservoirHollowPnch)

    subtractObj(reservoir, reservoirWaterHolePnch)
    subtractObj(reservoirNut, reservoirCentralHollowPnch)
    subtractObj(reservoir, reservoirCentralHollowPnch)
    subtractObj(reservoirCentralPnch, reservoirCentralHollowPnch)

#    deleteObj(reservoirCentralHollowPnch)
    deleteObj(reservoirWaterHolePnch)
       
    bpy.data.objects['reservoir'].select = True
    bpy.data.objects['reservoirCentralPnch'].select = True
    bpy.data.objects['reservoirNut'].select = True
    bpy.ops.object.join()    
    reservoir = bpy.context.active_object
    reservoir.name = "reservoir"
    bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(0, 0, 0), "constraint_axis":(False, False, False), "constraint_orientation":'GLOBAL', "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "texture_space":False, "remove_on_cancel":False, "release_confirm":False})
#    bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(0, 0, 0), "constraint_axis":(False, False, False), "constraint_orientation":'GLOBAL', "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False})
    reservoirLid = bpy.context.active_object
    reservoirLid.name = "reservoirLid"

    raise Exception()

    bpy.ops.mesh.primitive_cube_add(radius=1, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    reservoirLidPnch = bpy.context.active_object
    reservoirLidPnch.name = "reservoirLidPnch"
    bpy.ops.transform.resize(value=(basinL/2, basinW/2, basinH/2), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.translate(value=(0, 0, basinH/2 - reservoirTopBuffer - reservoirLidBuffer), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    subtractObj(reservoir, reservoirLidPnch)
    intersectObj(reservoirLid, reservoirLidPnch)
    deleteObj(reservoirLidPnch)
            
    bpy.ops.mesh.primitive_cube_add(radius=1, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    motorHousing = bpy.context.active_object
    motorHousing.name = "motorHousing"
    bpy.ops.transform.resize(value=(motorHsngL/2, motorHsngW/2, motorHsngH/2), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.translate(value=(-basin.dimensions.x/2 + motorHsngL - motorHsngBuffer, 0, -basinH + motorHsngH/2), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    bpy.ops.mesh.primitive_cylinder_add(radius = axlePnchR, depth = axlePnchD, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    axlePnch = bpy.context.active_object
    axlePnch.name = "axlePnch"
    bpy.ops.transform.rotate(value=1.5708, axis=(0, 1, 0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.translate(value=(-basin.dimensions.x/2 + motorHsngL - motorHsngT - motorHsngBuffer, 0, -basinH - motorPnchR/2 + motorPnchBottomBuffer), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    bpy.ops.mesh.primitive_cylinder_add(view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    motorHousingPnch = bpy.context.active_object
    motorHousingPnch.name = "motorHousingPnch"
    bpy.ops.transform.rotate(value=1.5708, axis=(0, 1, 0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.resize(value=(motorPnchL/2, motorPnchR/2, motorPnchR/2), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.translate(value=(-basin.dimensions.x/2 + motorHsngL - motorHsngT - motorHsngBuffer, 0, -basinH - motorPnchR/2 + motorPnchBottomBuffer), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
              
    subtractObj(motorHousing, motorHousingPnch)
    subtractObj(motorHousing, axlePnch)
    intersectObj(motorHousing, basinPnch)
    bpy.ops.transform.translate(value=(-motorPnchL/2, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    subtractObj(basin, motorHousingPnch)

    deleteObj(axlePnch)
    deleteObj(basinPnch)
    deleteObj(motorHousingPnch)

    bpy.data.objects['basin'].select = True    
    bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(0, 0, 0), "constraint_axis":(False, False, False), "constraint_orientation":'GLOBAL', "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "texture_space":False, "remove_on_cancel":False, "release_confirm":False})
    basinRidgePnch = bpy.context.active_object
    basinRidgePnch.name = "basinRidgePnch"    
    bpy.ops.transform.resize(value=((basinL - basinT/2)/basinRidgePnch.dimensions.x, (basinW - basinT/2)/basinRidgePnch.dimensions.y, 1), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    bpy.ops.mesh.primitive_cube_add(radius = basinL/2, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    ridgePnch = bpy.context.active_object
    ridgePnch.name = "ridgePnch"
    bpy.ops.transform.translate(value=(0, 0, basinL/2 - ridgeBuffer), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    intersectObj(basinRidgePnch, ridgePnch)
    deleteObj(ridgePnch)   

    subtractObj(basin, basinRidgePnch)
    deleteObj(basinRidgePnch)

    bpy.ops.object.select_all(action='TOGGLE')  
    bpy.ops.object.select_all(action='DESELECT')

    bpy.data.objects['reservoirCentralHollowPnch'].select = True
    bpy.context.scene.objects.active = bpy.data.objects["reservoirCentralHollowPnch"]
    bpy.data.objects['reservoirCentralHollowPnch']
    lidClip = bpy.context.active_object
    lidClip.name = "lidClip"
    bpy.ops.transform.resize(value=(1, 1, 0.1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(0, 0, 0), "constraint_axis":(False, False, False), "constraint_orientation":'GLOBAL', "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False})
    lidClipPnch = bpy.context.active_object
    lidClipPnch.name = "lidClipPnch"
    bpy.ops.transform.resize(value=((lidClip.dimensions.x - reservoirT/2)/lidClip.dimensions.x, (lidClip.dimensions.y - reservoirT/2)/lidClip.dimensions.y, 1), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    subtractObj(lidClip, lidClipPnch)
    deleteObj(lidClipPnch)
    
    
#    bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(0, 0, 0), "constraint_axis":(False, False, False), "constraint_orientation":'GLOBAL', "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False})

#    bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False, "mode":'TRANSLATION'}, TRANSFORM_OT_resize={"value":(0.438426, 0.438426, 0.438426), "constraint_axis":(False, False, False), "constraint_orientation":'GLOBAL', "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False})

#    bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False, "mode":'TRANSLATION'}, TRANSFORM_OT_resize={"value":((reservoirCentralHollowPnch.dimensions.x - reservoirT)/reservoirCentralHollowPnch.dimensions.x, 0.745292, 0.745292), "constraint_axis":(False, False, False), "constraint_orientation":'GLOBAL', "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False})


#    basinRidgePnch = bpy.context.active_object
    

#    bpy.ops.object.select_all(action='TOGGLE')
#    bpy.ops.transform.resize(value=(KISSslicerMult, KISSslicerMult, KISSslicerMult), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    raise Exception()

    bpy.ops.mesh.primitive_cylinder_add(radius=floatTrapCavityR - floatTrapCavityT/2, depth=floatTrapCavityD - floatTrapCavityT/2, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    floatTrapCavityPnch = bpy.context.active_object
    floatTrapCavityPnch.name = "floatTrapCavityPnch"   
    bpy.ops.transform.translate(value=(0, 0, floatTrapCavityD - floatTrapCavityT), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    subtractObj(floatTrapCavity, floatTrapCavityPnch)
    deleteObj(floatTrapCavityPnch)
 
    bpy.ops.mesh.primitive_cylinder_add(radius=waterLinePnchR, depth=floatTrapCavityR, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    waterLinePnch = bpy.context.active_object
    waterLinePnch.name = "waterLinePnch"   
    bpy.ops.transform.rotate(value=1.5708, axis=(0, 1, 0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.translate(value=(-floatTrapCavityR, 0, -floatTrapCavityD/2 + waterLinePnchR/2 + 3*floatTrapCavityT/4), constraint_axis=(True, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    subtractObj(floatTrapCavity, floatTrapCavityPnch)
    deleteObj(floatTrapCavityPnch)

    bpy.ops.mesh.primitive_cylinder_add(radius=floatTrapCavityR - floatTrapCavityT, depth=floatTrapCavityD - floatTrapCavityT, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    floatTrapCavityPnch = bpy.context.active_object
    floatTrapCavityPnch.name = "floatTrapCavityPnch"   
    
    subtractObj(floatTrapCavity, floatTrapCavityPnch)
    deleteObj(floatTrapCavityPnch)


    bpy.ops.transform.translate(value=(0, 0, basinH/2 - (basinH-motorHousingH)), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    subtractObj(motorHousing, motorHousingPnch)
    bpy.ops.transform.translate(value=(motorHousingL, 0, -basinH + (basinH-motorHousingH)), constraint_axis=(True, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    subtractObj(motorHousing, motorHousingPnch)
    deleteObj(motorHousingPnch)

def basinRoof():
    bpy.ops.transform.translate(value=(0, 0, basinH/2 - (basinH-motorHousingH)), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    

def floatChamber():

    bpy.ops.mesh.primitive_cylinder_add(radius=1, depth=2*reservoirBottomBuffer, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    floatChamber = bpy.context.active_object
    floatChamber.name = "floatChamber"

    bpy.ops.mesh.primitive_cylinder_add(radius=1-reservoirT, depth=2*reservoirBottomBuffer-2*reservoirT, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    floatChamberPnch = bpy.context.active_object
    floatChamberPnch.name = "floatChamberPnch"

    bpy.ops.mesh.primitive_cube_add(view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    floatChamberHalver = bpy.context.active_object
    floatChamberHalver.name = "floatChamberHalver"
    bpy.ops.transform.resize(value=(1, 1, reservoirBottomBuffer), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.translate(value=(0, 0, -reservoirBottomBuffer), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    subtractObj(floatChamber, floatChamberHalver)
    subtractObj(floatChamberPnch, floatChamberHalver)
    deleteObj(floatChamberHalver)
    
    bpy.data.objects['floatChamberPnch'].select = True
    bpy.ops.transform.translate(value=(0, 0, reservoirT/2), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)    
    bpy.data.objects['floatChamberPnch'].select = False

    subtractObj(floatChamber, floatChamberPnch)
    deleteObj(floatChamberPnch)

    bpy.data.objects['floatChamber'].select = True
    bpy.ops.transform.translate(value=(0, 0, -basinH), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)    
    bpy.data.objects['floatChamber'].select = False

def prototype():
    basin()


#floatChamber()
prototype()
