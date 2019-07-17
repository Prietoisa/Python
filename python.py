nome= input ('digite seu nome ')
idade= int(input ('qual a sua idade?'))
renda= int (input ('qual a sua renda? '))
valor_emprestimo= int (input ('qual o valor do empréstimo? '))

if (renda> 1000) and (idade> 22 and idade> 55) and (valor_emprestimo>= 2000 and 15* renda):
    print ('Empréstimo APROVADO')

else:
    print ('Empréstimo RECUSADO')
