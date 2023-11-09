from datetime import datetime

#Recebendo o valor original do pedido do usuário
valor_do_pedido = float(input("Digíte o valor da tonelada do pedido original em R$: \n"))

# Função para calcular a diferença em dias entre duas datas
def calcular_diferenca_em_dias(data1, data2):
    diferenca = abs((data2 - data1).days)
    return diferenca

# Função para receber uma data no formato 'dd/mm/aaaa' e retornar um objeto datetime
def receber_data():
    while True:
        try:
            data_str = input("Digite a data (dd/mm/aaaa):  ")
            data_obj = datetime.strptime(data_str, "%d/%m/%Y")
            return data_obj
        except ValueError:
            print("Formato de data inválido. Tente novamente.")

# Recebendo as três datas do usuário
data_original = receber_data()
data_lista = receber_data()
data_nova = receber_data()

#calculando o desconto proporcional para obter o valor do novo pedido
if data_nova >= data_lista:
    diferenca_venc_original_e_novo = calcular_diferenca_em_dias(data_original,data_nova)
    valor_novo_pedido = valor_do_pedido - (valor_do_pedido * (diferenca_venc_original_e_novo * (0.02/30)))
    print(f"O valor do novo pedido será R$ {valor_novo_pedido:.2f}")
else:
    diferença_original_ate_lista = calcular_diferenca_em_dias(data_original,data_lista)
    desconto_ate_lista = valor_do_pedido - (valor_do_pedido * (diferença_original_ate_lista * (0.02/30)))
    diferença_lista_ate_novo_vencimento = calcular_diferenca_em_dias(data_lista,data_nova)
    valor_novo_pedido = desconto_ate_lista - (desconto_ate_lista * (diferença_lista_ate_novo_vencimento * (0.007/30)))
    print(f"O valor do novo pedido será R$ {valor_novo_pedido:.2f}")


