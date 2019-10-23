import bpy
from math import cos, sin, tan, sqrt, atan, radians

filename = "c:/Users/BeckyBot/Desktop/Botnyst/Prototype Models/Scripts/M.py"
exec(compile(open(filename).read(), filename, 'exec'))
filename = "c:/Users/BeckyBot/Desktop/Botnyst/Prototype Models/Scripts/Lighting.py"
exec(compile(open(filename).read(), filename, 'exec'))
filename = "c:/Users/BeckyBot/Desktop/Botnyst/Prototype Models/Scripts/Mister.py"
exec(compile(open(filename).read(), filename, 'exec'))
filename = "c:/Users/BeckyBot/Desktop/Botnyst/Prototype Models/Scripts/PlantHousing.py"
exec(compile(open(filename).read(), filename, 'exec'))
filename = "c:/Users/BeckyBot/Desktop/Botnyst/Prototype Models/Scripts/Reservoir.py"
exec(compile(open(filename).read(), filename, 'exec'))
filename = "c:/Users/BeckyBot/Desktop/Botnyst/Prototype Models/Scripts/WaterReserveAndOverflowTanks.py"
exec(compile(open(filename).read(), filename, 'exec'))

#Add motors/wiring/boards/LEDs/bearings
#Create Materials
  #Plastic
  #Logo
  #Water
  #Anodized Steel
  #LED
#Construct Reservoir
#Construct Plant Housing
  #Attributes: height, thcknss, collar outer diameter, collar inner diameter, neck height, neck diameter
  #Behaviors: rotate, floatUp, turnTransparent
#Construct LED arm
#Construct Automated Dispensing System
#Construct Water Reserve Tank/Overflow Tank

rotatingModel = True
spinMisterModel = True

reservoirRad = 5
reservoirHght = 4
reservoirThcknss = 0.09
collarWdth = 1.5
collarRad = reservoirRad - collarWdth
brngPnchRad = 0.25
numOfBrngs = 5

wv_rad = 8
wv_Hght = reservoirHght * 1.61
wvPnch_rad = 10
wvPnch_offset = 2

axleZO = 1.2

misterMotorCageX = 2.5
misterMotorCageY = 3.5
misterMotorCageZ = reservoirHght
misterMotorCageT = 0.09
misterMotorCageXO = 4
misterMotorCageYO = 4
misterMotorCageZA = -0.4
misterMotorCageAxlePnchRad = 0.25
misterMotorCageAxlePnchZO = axleZO

stirrerMotorR = 0.5
stirrerMotorZ = 1
stirrerMotorCageXO = -2
stirrerMotorCageYO = -2
stirrerMotorAxlePnchR = 0.15
stirrerMotorAxlePnchZ = stirrerMotorZ * 2

strrrMtrCnnctRad = 0.5
strrrMtrCnnctHght = 0.55
strrrArmW = 1.25
strrrArmL = 0.2
strrrArmH = 0.2
strrrWngsRad = strrrArmL
strrrWngsHght = 2.5
strrrWngsPnchOffset = 0.1
strrrMtrAxlPnchRad = 0.1

sonicatorCageX = 3.75
sonicatorCageY = 6
sonicatorCageZ = 1
sonicatorCageXO = 2
sonicatorCageYO = -0.5
sonicatorCageZA = misterMotorCageZA

sonicatorCordPnchR = 0.125
sonicatorCordPnchZ = reservoirHght * 2
sonicatorCordPnchXO = 3
sonicatorCordPnchYO = 1


plntHsngHght = 20
plntHsngRad1 = reservoirRad
plntHsngRad2 = 3
plntHsngThcknss = 0.09
plntHsngCllrRad = collarWdth
plntHsngCllrHght = 0.5
rwpRad = 0.5
rwpHght = 1
bttmRwsRtWtrDstnc = 10
plntHsngSlantAngle = atan((plntHsngRad1 - plntHsngRad2)/plntHsngHght)#1.47181
numOfRootPlugsPerRow = 8
numOfRow = 3
rowSpacing = (plntHsngHght - bttmRwsRtWtrDstnc)/numOfRow

#Lighting
lghtngArmX = 1
lghtngArmY = 1
lghtngArmZ = plntHsngHght + reservoirHght
lghtngArmZA = radians(120)

numOfLightingRods = 8
rodLngth = 12
rodRad = 0.125

#Mister.py
mister()

#PlantHousing.py
#PlantHousing()
#Frustum()
#rockwoolPlug()

#Reservior.py
#reservoir()
#stirrer()

#Lighting.py
#LightingArm()
#LightingRods()

#WaterReserveAndOverflowTanks.py
#reserveAndOverflowTank()




