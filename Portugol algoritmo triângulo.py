Algoritimo Triangulo
Inicio
A,B,C, int
escreva('Digite o valor de A: ')
escreva('Digite o valor de B: ')
escreva('Digite o valor de C: ')
se ((A+B)>C) e ((A+C)>B) e ((B+C)>A):escreva('Os valores dão um triangulo')
se A=B e B=C: escreva('Os dados formam um triangulo equilátero')
se A=B ou A=C ou B=C:escreva('Os dados formam um triangulo isósceles')
#(<>) = Diferente em portugol
#(!=) = Diferente em phyton
senão: escreva('Os dados formam um triangulo escaleno')