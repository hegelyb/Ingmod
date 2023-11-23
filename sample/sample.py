#!/usr/bin/env python 

import os
from math import log
from math import exp
#from Constants import R
# IPython log file

R=8.314 # J/(molK)
Tk = 273.15 # K
F=96485.0 # C/mol

#Tx=12.0 # fokC
#ccu=0.03 # M
#cfe=0.05 # M
#dEdT=-4.7*10**(-4.0) # V/K
#K=9.798*10**(24.0) # -

string=os.environ['INGMOD_Tx']
Tx=float(string) # fokC
string=os.environ['INGMOD_ccu']
ccu=float(string) # M
string=os.environ['INGMOD_cfe']
cfe=float(string) # M
string=os.environ['INGMOD_dEdT']
dEdT=float(string) # V/K
string=os.environ['INGMOD_K']
K=float(string) # -

z=2.0
Tx=Tx+Tk # K

E=R*Tx/(z*F)*(log(K)-log(cfe/ccu)) # V
drG=-z*F*E # J/mol
#print'dEdT = ',dEdT,' V/K'
drS=z*F*dEdT # J/(molK)
drH=drG+Tx*drS # J/mol

drG=drG/1000.0 # kJ/mol
drH=drH/1000.0 # kJ/mol
invK=1.0/K

# unformatted print for manual use
#print 'E = ',E,' V'
#print 'drG = ',drG,' kJ/mol'
#print 'drS = ',drS,' J/molK'
#print 'drH = ',drH,' kJ/mol'

# formatted outfor for IngMod
print("E=%-25.20f" %(E))
print("drG=%-25.20f" %(drG))
print("drS=%-25.20f" %(drS))
print("drH=%-25.20f" %(drH))
print("invK=%-35.30f" %(invK))
