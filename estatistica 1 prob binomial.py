# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 02:39:46 2020

@author: User
"""
from scipy.stats import binom

#formula da distribuicao binomial: (n k) = n! / k!(n-k)!
# p(x) = (n k)*p^k*(1-p)^(n-k);

#Exercicio 1: Ao se jogar uma moeda 5 vezes, qual a probabilidade de dar 3x cara?
probex1 = binom.pmf(3,5,0.5)

#Exercicio 2: Ao passar por 4 sinais de 4 tempos, qual
#a probabilidade de pegar 0,1,2,3 ou 4 vezes seguidas:

probex2a=binom.pmf(0,4,0.25)
probex2b=binom.pmf(1,4,0.25)
probex2c=binom.pmf(2,4,0.25)
probex2d=binom.pmf(3,4,0.25)
probex2e=binom.pmf(4,4,0.25)

#Exercicio 3: E se for um sinal de 2 tempos?
probex3=binom.pmf(4,4,0.5)


exemploprobcumulativa = binom.cdf(4,4,0.25)

#Dado um concurso de 12 questoes, qual a prob de acertar 
#7 questoes de 4 alternativas?
probex4a = binom.pmf(7,12,0.25)
probex4b = binom.pmf(12,12,0.25)
