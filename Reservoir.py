filename = "c:/Users/BeckyBot/Desktop/Botnyst/Prototype Models/Scripts/M.py"
exec(compile(open(filename).read(), filename, 'exec'))

def reservoir():

    bpy.ops.mesh.primitive_cube_add(radius=1, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    reservoir = bpy.context.active_object
    reservoir.name = "reservoir"
    bpy.ops.transform.resize(value=(reservoirW/2, reservoirD/2, reservoirH/2), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.translate(value=(0, 0, reservoirH/2), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    bpy.ops.mesh.primitive_cube_add(radius=1, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    reservoirPnch = bpy.context.active_object
    reservoirPnch.name = "reservoirPnch"
    bpy.ops.transform.resize(value=(reservoirW/2 - 2 * plasticT, reservoirD/2 - 2 * plasticT, reservoirH/2 - plantHousingOffset/2 - plasticT/2), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.translate(value=(0, 0, reservoirPnch.dimensions.z/2 + plasticT), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    subtractObj(reservoir, reservoirPnch)
    deleteObj(reservoirPnch)
    
    bpy.ops.mesh.primitive_cube_add(radius=1, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    reservoirPnch = bpy.context.active_object
    reservoirPnch.name = "reservoirPnch"
    bpy.ops.transform.resize(value=(reservoirW/2 - plasticT, reservoirD/2 - plasticT, plantHousingOffset/2), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.translate(value=(0, 0, reservoirPnch.dimensions.z/2 + reservoirH - plantHousingOffset), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    subtractObj(reservoir, reservoirPnch)
    deleteObj(reservoirPnch)