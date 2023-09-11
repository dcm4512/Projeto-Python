valor1= float(input("Tempo como fumante (em anos): "))
valor2= float(input("Valor do maço: "))
valor3= float(input("Quantida de maços por dia: "))

dias_fumando= valor1*12*30
resultado=dias_fumando*valor2*valor3

if resultado < 20000.00:
    print(f"Com o valor R$ {resultado}, você poderia ter dado entrada em um carro.")
elif resultado > 20000.00 and resultado < 50000.00:
    print(f"Com o valor R$ {resultado}, você poderia ter comprado um carro popular usado.")
elif resultado > 50000.00:
    print(f"Com o valor R$ {resultado}, você poderia ter comprado um carro zero.")    
