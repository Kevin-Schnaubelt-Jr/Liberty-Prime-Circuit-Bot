import math

''' AC changes in both magnitude and direction.
Z = Impedance : Measure of the opposition that a circuit presents to a current when
a voltage is applied. Z = real number +- imaginary. real number +- imaginary = complex number.

AC
==
V = I*Z
I = V/Z
Z = V/I

Resistors will be represented as real numbers, while capacitors and inductors will be represented as imaginary.

X = reactance

resistor:
R = 100
X = 0
Z = 100 l0o

inductor:
R = 0
Xl = 100 
Z = 100l90o
Z = j100

Capacitor:
R = 0
X = 100
Z = 100l-90o
z = -j100

i * i = -1, j* j = -1
i = sqrt(-1), j = sqrt(-1)

C = sqrt((5 * 2) + (5 * 2))

C * cos(Q) = R
C * sin(Q) = imaginary

"-xj capacitort, +xj inductor


T = Period : Time required to produce one complete cycle of a waveform.

Cycle is one complete positive & negative alternation of the waveform. 

F = Frequency : The number of cycles per second. Measured in hertz (Hz).

F = 1 / T

T = 1 / F

120Vrms @ 60Hz. 
Period = 1/60 

Vp = 0 to max positive peak on sin wave.

Vrms = .707 * Vp



f = 60 #60Hz

t = 1/f

print(t)

'''


#rectangle to polar?
'''

z = 3+4j

c = math.sqrt((z.real * 2) + (z.imag * 2)) # rectangular form, <int>

q = math.degrees(math.atan(z.imag/z.real)) # polar form. Notice the order, in degrees

print(c, q)

'''

#CONVERT TO POLAR
'''
convert_to_polar = complex((math.sqrt(pow(It.real,2) + pow(It.imag, 2))), -math.degrees(math.atan(It.imag / It.real)))
'''


'''
# Z = 4 and L45degrees

z = complex((4 * math.cos(math.radians(45))), (4 * math.sin(math.radians(45))))
print(z) # should be 2.83 + 2.83j
'''



#example 2
'''
Vs = 10 #V
F = 60 #Hz
R = 100 #ohms
C = 10 #mF = .000010F
C = .000010
L = 20 #mh = .020 H
L = .020

#Reactance for capacitors 
Xc = -abs(1 / (2 * math.pi * F * C))
print(f'{Xc=}')

#Reactance for inductors
Xl = 2 * math.pi * F * L
print(f'{Xl=}')

#Total reactance
Xt = Xc + Xl
print(f'{Xt=}')

#Impedance IN SERIES
Zs = math.sqrt(pow(R,2) + pow(Xt,2))
print(f'{Zs=}')

#Impedance IN PARALLEL
Zp =  complex(R, Xt)
print(f'{Zp=}')

#Impedance in parallel RECTANGULAR FORM
rectangular_form = math.sqrt(pow(Zp.real,2) + pow(Zp.imag, 2))
print(f'{rectangular_form=}')

#Impedance in parallel rectangular TO POLAR
polar_form = -abs(math.degrees(math.atan(Zp.imag / Zp.real)))
print(f'{polar_form=}')


#Current in series
Is = Vs/Zs 
print(f'{Is=}')

#Magic????
magic = complex(( rectangular_form * math.cos(math.radians(polar_form))),
 (rectangular_form * math.sin(math.radians(polar_form))))
print(f'{magic=}')
'''


#example 3
'''
Vs = 10 #volts
F = 100 #Hz
R = 300 #Ohms
L = 300 #mF
L = .3
C = 300 #mF
C = .0003

Zr = 100 #Ohms Rectangular. Polar form is 100 with an angle of 0 degrees

Xl = 2 * math.pi * F * L
print(f'{Xl=}')

Xc = -abs(1 / (2 * math.pi * F * C))
print(f'{Xc=}')

Xt = Xc + Xl
print(f'{Xt=}')

Zs = math.sqrt(pow(R,2) + pow(Xt,2))
print(f'{Zs=}')

Zp =  complex(R, Xt)
print(f'{Zp=}')

rectangular_form = math.sqrt(pow(Zp.real,2) + pow(Zp.imag, 2))
print(f'{rectangular_form=}')

polar_form = math.degrees(math.atan(Zp.imag / Zp.real))
print(f'{polar_form=} Degrees')

complex_result = complex(rectangular_form, polar_form)
print(f'{complex_result=}')

Is = Vs/Zs 
print(f'{Is=}')

Is_polar = complex(Is, -abs(polar_form))
print(f'{Is_polar=}')




#volt drop
Vr = Is * R
print(f'{Vr=}')
#Converts to 7.28428 - j4.448 somehow

Vl = complex(Is * Xl, -polar_form + 90)
print(f'{Vl=}')
#converts to 2.7947 +j4.57711


Vc = complex(Is * Xc, -polar_form + -90)
print(f'{Vc=}')
# converts to -0.07875 -j0.12896
'''

'''
Apparent Power (VA)
Reactive Power (VAR)
Real Power (W watts)

P = Real Power = I squared * R = V squared / R

Q = Reactive Power = I squared * X = V squared / X

S = Apparent Power = I squared * Z = V squared / Z
'''

#RCL Parallel circuits
'''
V = 120 #Vrms
F = 60 #Hz
R = 250 #Ohms
L = 650 #Mh
L = .65
C = 1.5 #uF
C = .0000015

Zr = R #total R

Xl = 2 * math.pi * F * L
print(f'{Xl=}')

Xc = -abs(1 / (2 * math.pi * F * C))
print(f'{Xc=}')

Zt = 1/ complex((1/Zr), (1/Xl) + (1/Xc))
print(f'{Zt=}')
Ir = V / R #with 0 degrees
Il = V / Xl #with -90 degrees
Ic = V / Xc #with 90 degrees
It = complex(Ir, Il + Ic)
print(f'{It=}') #should be 0.639 with an angle of -41.307 degrees

convert_to_polar = complex((math.sqrt(pow(It.real,2) + pow(It.imag, 2))), -math.degrees(math.atan(It.imag / It.real)))
print(convert_to_polar)
'''

#test notes
'''
T = 1/f | F = 1/T | F = 1/40ms = 1 / .000040s = 25,000 Hz #peak volt was 2v#
'''

#Parallel example 2
# Ir = Vs/Zr - Il = Vs/Zl - Ic = Vs/Zc
'''
V = 10 #vrms
F = 100 #Hz

R = 300 #Ohms
L = 300 #mH
L = .3
C = 300 #mF
C = .0003

Zr = R

Xl = 2 * math.pi * F * L
print(f'{Xl=} Ohms') 

Xc = 1 / (2 * math.pi * F * C)
print(f'{Xc=} Ohms')

Zl = Xl
print(f'+j {Zl=} Ohms 90 degrees')

Zc = Xc
print(f'-j {Zc=} Ohms -90 degrees')

Ir = V / Zr
print(f'{Ir=} A 0 degrees')

Il = V / Zl
print(f'{Il=} A -90 degrees')

Ic = V / Zc
print(f'{Ic=} A 90 degrees')

Is = complex(Ir, Ic - Il)
print(f'{Is=}')

magnitude = math.sqrt(pow(Is.real,2) + pow(Is.imag, 2))
print(f'{magnitude=}')

Q = math.degrees(math.atan(Is.imag / Is.real))
print(f'{Q=} Degrees')

Zt = V / magnitude
print(f'{Zt=} Ohms {-Q} degrees')
'''

#Combo Circuit!
''''''

V = 120 #Vrms
F = 60 #Hz
C1 = 4.7 #Mf
C1 = 0.0000047
L = 650 #Mh
L = .65
C2 = 1.5 #mF
C2 = .0000015
R = 470 #Ohms

Xc1 = 1 / (2 * math.pi * F * C1)
print(f'{Xc1=} Ohms')

Xl = 2 * math.pi * F * L
print(f'{Xl=} Ohms') 

Xc2 = 1 / (2 * math.pi * F * C2)
print(f'{Xc2=} Ohms')

Zr = R

print(f'Zc1 in rectangular is -j{Xc1} and in polar form it is {Xc1} with -90 degrees')
print(f'Zc2 in rectangular is -j{Xc2} and in polar form it is {Xc2} with -90 degrees')
print(f'Zcl in rectangular is +j{Xl} and in polar form it is {Xl} with +90 degrees')

# L and C2 are in series
G1 = -Xc2 + Xl
print(f'j{G1=} in rectagular and {+G1=} with -90 degrees in polar')

#R is in parallel with G1
G3 = 1/ math.sqrt(pow(1/Zr,2) + pow(1/G1, 2))

Q = math.degrees(math.atan((1/G1) / (1/Zr) )) #Zr is run, G1 is rise. Rise over run for Atan.

print(f'{G3=} with {Q} degrees')

#polar to rectangular convert

G3_Rectangular = complex(( G3 * math.cos(math.radians(Q))),
 (G3 * math.sin(math.radians(Q))))

print(f'{G3_Rectangular=}')

G4 = Xc1
Zt_rectangle = complex(G3_Rectangular.real, abs(G3_Rectangular.imag) + G4)
Zt_polar = complex((math.sqrt(pow(Zt_rectangle.real,2) + pow(Zt_rectangle.imag, 2))), -math.degrees(math.atan(Zt_rectangle.imag / Zt_rectangle.real)))
print(f'{Zt_rectangle=}, {Zt_polar=}')

print('C1 rectangular is 120 VRMS +j0, polar is 120Vrms at an angle of 0 degrees')

I_total_polar = V / Zt_polar.real
print(f'{I_total_polar=} amps at {abs(Zt_polar.imag)} degrees')

I_total_rectangular = complex((I_total_polar * math.cos(math.radians(abs(Zt_polar.imag)))), (I_total_polar * math.sin(math.radians(abs(Zt_polar.imag)))))
print(f'{I_total_rectangular=}')

#Vc1 = Is * Zc1 = 82.795 with -31.6 degrees

# Vc1 = I_total_polar * Xc1
Vc1 = math.degrees(math.atan(Zt_polar.imag / -90))
print(f'{Vc1=}')



