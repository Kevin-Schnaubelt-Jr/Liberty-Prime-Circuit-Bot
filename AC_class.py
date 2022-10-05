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




'''
# Z = 4 and L45degrees

z = complex((4 * math.cos(math.radians(45))), (4 * math.sin(math.radians(45))))
print(z) # should be 2.83 + 2.83j
'''



#example 2

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



