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

'''

z = 3+4j

c = math.sqrt((z.real * 2) + (z.imag * 2)) # rectangular form, <int>

q = math.degrees(math.atan(z.imag/z.real)) # polar form. Notice the order, in degrees

print(q)


'''


'''
# polar to rectangular convert
# Z = 4 and L45degrees

z = complex((4 * math.cos(math.radians(45))), (4 * math.sin(math.radians(45))))
print(z) # should be 2.83 + 2.83j
'''

'''
Xl = 2 pi f L

xc = 1/(2 pi f c)

'''