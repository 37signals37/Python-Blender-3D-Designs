#Repertier multiplier 21.3
import bpy
from math import cos, sin, tan, sqrt, atan

filename = "e:/Blender Scripts/BlenderScripts/M.py"
exec(compile(open(filename).read(), filename, 'exec'))
filename = "e:/Blender Scripts/BlenderScripts/Cup.py"
exec(compile(open(filename).read(), filename, 'exec'))
filename = "e:/Blender Scripts/BlenderScripts/PumpBox.py"
#exec(compile(open(filename).read(), filename, 'exec'))
filename = "e:/Blender Scripts/BlenderScripts/MistingChamber.py"
exec(compile(open(filename).read(), filename, 'exec'))
filename = "e:/Blender Scripts/BlenderScripts/MotorMount.py"
exec(compile(open(filename).read(), filename, 'exec'))
filename = "e:/Blender Scripts/BlenderScripts/VerticalMotorMount.py"
exec(compile(open(filename).read(), filename, 'exec'))
filename = "e:/Blender Scripts/BlenderScripts/FanChamber.py"
exec(compile(open(filename).read(), filename, 'exec'))
filename = "e:/Blender Scripts/BlenderScripts/FanChamberPt1.py"
exec(compile(open(filename).read(), filename, 'exec'))
filename = "e:/Blender Scripts/BlenderScripts/FanChamberPt2.py"
exec(compile(open(filename).read(), filename, 'exec'))
filename = "e:/Blender Scripts/BlenderScripts/WateringLine.py"
exec(compile(open(filename).read(), filename, 'exec'))
filename = "e:/Blender Scripts/BlenderScripts/MistingStout.py"
exec(compile(open(filename).read(), filename, 'exec'))
filename = "e:/Blender Scripts/BlenderScripts/MistingFan.py"
exec(compile(open(filename).read(), filename, 'exec'))

#SideMotorMount()          #MotorMount

#ThinWiskBall()          #MistingFan
#ThinFan()              #MotorMount
#MistingFan()           #MistingFan
#HorizontalMistingFan()     #MistingFan
#TwirlMistingFan()           #MistingFan
#FanWithMistingBlades()      #MistingFan
#AxleCoverWithMistingFanBlades()   #MistingFan
#AxleFanBlades()
#AxleFanBladesHolder()

#makeBox()              #Pump Box
#makeLid()              #Pump Box

#makeCup()              #Cup
#makeCupBody()          #Cup
#makeCupTop()           #Cup
#makeInteriorWalls()    #Cup
#makeCentralVent()      #Cup
#makePunchHoles()       #Cup

#makeXTRMale()
#makeXTRfemale()

#makeRootHolders()

#makeRotor()
#makeRodConnector()
#Collet()                    #VerticalMotorMount
#SilverScrewCollet()         #VerticalMotorMount

#mstngChmbr = bpy.context.active_object
#bpy.ops.transform.translate(value=(lidHolePunchX, lidHolePunchY, lidHolePunchZ), constraint_axis=(True, True, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
#bpy.ops.transform.rotate(value=3*pi/4, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

#makeThinWiskRotor()

#makeVerticalMotorMount()
#makeVerticalMotorMountLid()
#makeMotorMount()
#makeMotorMount1()

#makeMotorMount()
#bpy.data.objects["rodXtr"].select = True
#mstngChmbr = bpy.context.active_object

#bpy.ops.transform.translate(value=(lidHolePunchX, lidHolePunchY, lidHolePunchZ), constraint_axis=(True, True, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
#bpy.ops.transform.rotate(value=pi/2 - engHolePnchTheta, axis=(1, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
#bpy.ops.transform.rotate(value=3*pi/4, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
#bpy.ops.transform.rotate(value=3*pi/4, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
