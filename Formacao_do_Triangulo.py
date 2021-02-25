nome="Diego"
  # Iremos considerar um triângulo retângulo para facilitar o raciocínio.
a = int(input("Qual é o valor do cateto oposto?"))
b = int(input("Qual é o valor do cateto adjacente?"))
c = int(input("Qual é o valor da hipotenusa?"))
is_triangle= ((a**2) + (b**2) == (c**2))
  # para que o triângulo retângulo exista,é necessário que a soma dos quadrados do cateto
  # sejam maiores que o quadrado da hipotenusa. Segue as condições:


if (is_triangle >= (a**2) + (b**2)):
      print("Parabéns{}, você demonstrou que o triângulo existe!".format(nome))
else:
    print("Poxa {}, o triângulo infelizmente não existe!".format(nome))


