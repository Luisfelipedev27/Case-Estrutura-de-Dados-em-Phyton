clientes_na_espera = []
clientes_atendidos = []
print("Recebendo ligações...")
for i in range(1,5):
     print(i)

cliente1 = input("Digite seu nome: ")
print(cliente1 , "Aguarde o momento,estaremos lhe atendendo em alguns segundos")
for z in range(1,5):
    print(z,"s")
clientes_na_espera.append(cliente1)
numero = 9
numero2 = 8
confirmacao = int(input("Se você foi atendido, aperte 9. Se Ainda não foi atendido,aperte 8:"))
if confirmacao == numero:
    clientes_atendidos.append(cliente1)
    print("Obrigado pela preferência")
    print("Lista de clientes atendidos atualizada: ")
    print(clientes_atendidos)
elif confirmacao == numero2:
    clientes_na_espera.append(cliente1)
    print("Você será direcionado para a fila de espera. Aguarde só um momento")
    print("Lista atualizada de clientes na fila de espera : ")
    print(clientes_na_espera)







