def reserveAndOverflowTank():

    bpy.ops.mesh.primitive_cylinder_add(view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    wv_backPlatePnch = bpy.context.active_object
    wv_backPlatePnch.name = "wv_backPlatePnch"
    bpy.ops.transform.resize(value=(wvPnch_rad, wvPnch_rad, wv_Hght), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.translate(value=(0, wvPnch_offset, wv_backPlatePnch.dimensions.z/2), constraint_axis=(False, True, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    bpy.ops.mesh.primitive_cylinder_add(view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    wv_backPlate = bpy.context.active_object
    wv_backPlate.name = "wv_backPlate"
    bpy.ops.transform.resize(value=(wv_rad, wv_rad, wv_Hght), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.translate(value=(0, wv_rad, wv_backPlate.dimensions.z/2), constraint_axis=(False, True, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    subtractObj(wv_backPlate, wv_backPlatePnch)
    deleteObj(wv_backPlatePnch)