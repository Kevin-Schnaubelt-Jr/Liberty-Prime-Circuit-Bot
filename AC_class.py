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



# polar to rectangular convert
'''
# Z = 4 and L45degrees

z = complex((4 * math.cos(math.radians(45))), (4 * math.sin(math.radians(45))))
print(z) # should be 2.83 + 2.83j
'''

'''
Xl = 2 pi f L

xc = 1/(2 pi f c)

'''

'''
Vs = 120 # Vrms
F = 60 #Hz
R = 100 #ohms
C = 1 #mF .000001 F
C = 0.000001
L = 1 #mH .001 H
L = .001

#Reactence of capacitor
Xc = 1 / (2 * math.pi * F * C) 

print(Xc)
#Reactence of inductor
Xl = 2 * math.pi * F * L
print(Xl)
#Impedence of capacitor
# Zc = Xc 
# print(Zt)

#Impedence of inductor

# Is = Vs/Zt

y = complex(100, Zt)
ypi = (y.real * 2) + (y.imag * 2)
ypi = math.sqrt(ypi)

print(ypi)
'''

#example 2

Vs = 10 #V
F = 60 #Hz
R = 100 #ohms
C = 10 #mF = .000010F
C = .000010
L = 20 #mh = .020 H
L = .020

Xc = 1 / (2 * math.pi * F * C)
print('Xc',Xc)

Xl = 2 * math.pi * F * L
print('Xl',Xl)

Zr = 100 #ohms +-0j
# Zc = ?
# Zt = 274.44 # -68.793 ?should be?

Zt = complex(-Xc, Xl)
print(Zt)

Zt = math.sqrt(abs((Zt.real * 2)) + (Zt.imag * 2))

print(Zt)


