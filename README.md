# simulador-caixa-eletronico
Criando interface de um caixa eletronico com evolução de menu

Construção de um programa em Python que simule um caixa eletrônico simples.
Requisitos:

Comece com saldo = 1000.0.
Mostrar um menu em loop:

   1 - Consultar saldo
   2 - Depositar
   3 - Sacar
   4 - Sair

O menu vai continuar aparecendo até o usuário escolher Sair.

Depositar: pedir um valor; só aceitar se for maior que zero.
Sacar: pedir um valor; não pode ser maior que o saldo, nem menor/igual a zero.

Em qualquer entrada inválida, mostrar uma mensagem de erro clara (sem quebrar o programa).
Ao sair, imprimir "Obrigado por usar nosso banco!".

Tentar combinar while, if/elif/else e conversão de tipos (float()) vai melhorar a experiência do usuário.
