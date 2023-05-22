#faça um programa que receba um número indicando qual o grau da equação, se esse número for menor do que 1 ou maior
 #do que 2, o programa deve imprimir .Grau inválido

#Se o grau for 1, o programa deve imprimir A equação é do 
#primeiro grau. Em seguida ele deve pedir para o usuário 
#digitar o valor de a. Caso o usuário digite 0 para a, 
# o programa deve imprimir Valor de a inválido ee de 0 para
#  a, o programa terminar o 
# #programa. Se o usuário digitar um valor diferent deve pedir para o usuário digitar o valor #de b e imprimir o valor da raiz da da equação ax + b = 0 com exatamente duas casas decimais, independentemente se o #número for inteiro ou não.
#Se o grau for 2, o programa deve imprimir A equação é
#  do segundo grau. Em seguida ele deve pedir para o
#  usuário #digitar o valor de a. Caso o usuário digite 0 para a, o programa deve imprimir Valor de a inválido e terminar.
#Se o usuário digitar um valor diferente de 0 para a o programa deve pedir os valores b e c correspondente à equação #ax² + bx + c = 0.
#Caso o usuário digite um valor de b² - 4ac menor do que 0, o programa deve imprimir A equação não possui raízes reais #e terminar.
#Caso o usuário digite um valor de b² - 4ac igual a 0, o programa deve imprimir A equação possui uma raiz real #e terminar. Em seguida ele deve imprimir o valor da raiz com exatamente duas casas decimais, independentemente se o #número for inteiro ou não.
#Caso o usuário digite um valor de b² - 4ac maior do que 0, o programa deve imprimir A equação possui duas raízes #reais e terminar. Em seguida ele deve imprimir o valor das raízes com exatamente duas casas decimais, #independentemente se o número for inteiro ou não. A primeira raiz deve ser menor do que a segunda raiz e termina

Grau =  int(input("Digite um número;"))
if Grau < 1:
    print ("Grau inválido")
if Grau > 2:
     print("Grau inválido") 
if Grau == 1:
    print("A equação é do primeiro grau") 
    a = int(input("Digite o valor de a;"))
    if a == 0:
        print("Valor de a inválido")
    if a != 0:
         b = int(input("Digite valor de b:"))
         x = - b/a
         print(f"{x:.2f}")
if Grau == 2:
    print("A equação é do segundo grau")
    a2 = int(input("Digite o valor de a:"))
    if a2 == 0:
        print("Valor de a inválido")
    else:
        b2= int(input("Digite o valor de b:"))
        c = int(input("Digite o valor de c:"))
        Delta = ((b2**2) - (4 * a2 * c))
        raiz1 = (- b2 + (Delta**0.5))/(2 * a2)
        raiz2 = (- b2 - (Delta**0.5))/(2 * a2)
        if a2 != 0:   
            if Delta < 0:
                print("A equação não possui raízes reais")
            if Delta == 0 :
                print ("A equação possui uma raiz real")
            
                print(f"{raiz1:.2f}")
            if Delta > 0:
            
                print("A equação possui duas raízes reais")
                print(f"{raiz2:.2f}") 
                print(f"{raiz1:.2f}")
            
            



  

    