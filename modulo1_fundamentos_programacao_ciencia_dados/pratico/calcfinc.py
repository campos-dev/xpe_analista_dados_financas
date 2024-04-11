#importação do módulo math para usar a função log
import math

#mensagem inicial e legenda dos códigos a serem utilizados
#\n foi usado para criar quebras de linha e deixar o output mais legível
print('Bem-vindo à calculadora de Juros Compostos!\n')
print('vf = valor final \nci = capital inicial \nt = período de investimento em meses \ni = taxa de juros\n')

'''criada a função calculadora que será reutilizada em outros momentos no código
primeiro o usuário deve inserir o código da função a ser utilizada com auxílio do método input.
Este código irá validar qual fórmula será utilizada pela calculadora através de uma condicional.
A reposta é formatada pelos f-strings e realizada através do uso dos operadores matemáticos,
após uma devida conversão dos tipo de dados.
Ao término de cada cálculo a função reiniciar_calculadora irá ser chamada'''

def calculadora():
  tipo_calculo = str.lower(input('O que você gostaria de calcular? vf, ci, t, i): '))
  if tipo_calculo =='vf':
    capital_inicial = float(input('Qual o capital inicial? '))
    taxa_juros = float(input('Qual a taxa de juros ao mês? '))
    tempo_meses = float(input('Qual o período em meses? '))
    valor_final = capital_inicial * (1 + taxa_juros / 100)**tempo_meses
    print(f'O valor final (vf) é igual a: R${valor_final:.2f} \n')
    reiniciar_calculadora()

  elif tipo_calculo == 'ci':
    valor_final = float(input('Qual o valor final? '))
    taxa_juros = float(input('Qual a taxa de juros ao mês? '))
    tempo_meses = float(input('Qual o período em meses? '))
    capital_inicial = valor_final / (1 + taxa_juros / 100)**tempo_meses
    print(f'O capital inicial (ci) é igual a: R${capital_inicial:.2f} \n')
    reiniciar_calculadora()

  elif tipo_calculo == 'i':
    valor_final = float(input('Qual o valor final? '))
    capital_inicial = float(input('Qual o capital inicial? '))
    tempo_meses = float(input('Qual o período em meses? '))
    taxa_juros = 100*(((valor_final/capital_inicial)**(1 / tempo_meses)) - 1)
    print(f'A taxa de juros (i) é igual a: {taxa_juros:.2f}% \n')
    reiniciar_calculadora()

  elif tipo_calculo == 't':
    valor_final = float(input('Qual o valor final? '))
    capital_inicial = float(input('Qual o capital inicial? '))
    taxa_juros = float(input('Qual a taxa de juros ao mês? '))
    tempo_meses = math.log(valor_final / capital_inicial) / math.log(1 + taxa_juros / 100)
    print(f'O período de investimento (t) é igual a: {round(tempo_meses)} meses \n')
    reiniciar_calculadora()

#tratamento de exceção: caso o usuário digite um código inexistente gerará uma mensagem de erro e reinicia a calculadora.
  else:
    print('Código inválido: digite somente vf, ci, t ou i')
    calculadora()

# Esta função irá reiniciar a calculadora caso usuário digite 's' ou terminar o programa caso digite 'n', gerando um loop
def reiniciar_calculadora():
  outro_calculo = str.lower(input('Você quer fazer outro cálculo? Digite "S" para sim ou "N" para não: '))
  if outro_calculo == 's':
    calculadora()
  elif outro_calculo == 'n':
    print("Se precisar fazer mais cálculos, volte a me executar.")
    return
  else:
    print("Resposta inválida. Por favor, digite 'S' para sim ou 'N' para não.")
    reiniciar_calculadora()

calculadora()

