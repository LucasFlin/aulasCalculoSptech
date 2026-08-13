import math

c_str = int(input("Digite o valor de C: "))
d_str = int(input("Digite o valor de D: "))

c = int(c_str)
d = int(d_str)

c_elevado_ao_quadrado = math.pow(c,2)
c_elevado_ao_cubo = math.pow(c,3)
c_elevado_a_quarta = math.pow(c,4)
c_elevado_a_d = math.pow(c,d)

print(f"C elevado ao quadrado: {c_elevado_ao_quadrado}")
print(f"C elevado ao cubo: {c_elevado_ao_cubo}")
print(f"C elevado à quarta: {c_elevado_a_quarta}")
print(f"C elevado à D: {c_elevado_a_d}")