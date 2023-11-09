Projeto de uma  calculadora que permita fornecer descontos proporcionais de antecipação de pagamento em pedidos de venda.

 serão recebidos do usuários os seguntes paramentros de entrada:
 1. valor original do pedido para vencimento futuro em reais
 2. data de vencimento original do pedido
 3. nova data de vencimento para pagamento antecipado
 4. data de validade da lista de preços do pedido

O algoritimo deverá realizar o calculo de desconto do pedido considerando os seguintes fatores:

1. Caso o vencimento do novo pedidido(antecipado), seja  igual ou posterior  à data de vencimento da lista , será fornecido um desconto na taxa de 2% ao mês:

- O calculo será realizado calculando  a diferença em dias entre a data do vencimento original e a nova data de vencimento,
- dividir a taxa de 2% ao mês por um mês padrão que consiretamos como 30 dias, para obter o desconto por dia
- multiplicar o desconto por dia pelo número de dias em que o pedido será antecipado para obter o percentual total de desconto concedido
- multiplicar o valor do pedido original pelo percentual de  desconto total concedido e assim obter o desconto total em reais
- subtrair o desconto total em reais do valor do pedido original para obter o valor do novo pedido

2. Caso o vencimento do novo pedido , seja anterior ao vencimento da lista será fornecido um desconto de 2% ao mês até a data de valodadr da lista acrescido de um desconto de 0,7% ao mês no período compreendido entre i vencimento da lista e o novo vencimento antecipado do pedido

Neste caso além do calculo anteriormante realizado do desconto ate a lista iremos calcular a diferença em dias entre o vancomento da lista e o novo vencimento do pedido
- dividir a taxa de 0,7% ao mês por um mês padrão que consiretamos como 30 dias, para obter o desconto por dia
- multiplicar o desconto por dia pelo número de dias em que o pedido será antecipado entre o vencomento da lista e o novo vencimento do pedido  para obter o percentual total de desconto concedido
- multiplicar o valor do pedido já com desconto calculado ate a data de validade da lista pelo percentual de  desconto concedido  anterior a validade da lisa para obter o desconto total em reais
- subtrair o desconto total em reais do valor do pedido com desconto até a data de validade da lista (calculado anteriormente) para obter o valor do novo pedido

A saída do algoritimo deverá ser o valor em reais do novo pedido com o descinto total calculado conforme o caso.