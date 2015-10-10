#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

jogo = [1,2,3]

def novoJogo():
        try:
                assassinos = {1:'Charles B. Abbage', 2: 'Donald Duck Knuth', 3:'Ada L. Ovelace', 4 : 'Alan T. Uring', 5:'Ivar J. Acobson', 6:'Ras Mus Ler Dorf'}
                local = {1:'Redmond', 2: 'Palo Alto', 3:'San Francisco', 4 : 'Tokio', 5:'Restaurante no Fim do Universo', 6:'São Paulo', 7:'Cupertino', 8:'Helsinki', 9:'Maida Vale', 10:'Toronto'}
                armas = {1:'Peixeira', 2: 'DynaTAC 8000X', 3:'Trezoitao', 4 : 'Trebuchet', 5:'Maca', 6:'Gládio'}
         
                for x in range(0,3):
                        if x is 0:
                                jogo[x] = random.choice(assassinos.keys())
                        if x is 1:
                                jogo[x] = random.choice(local.keys())
                        if x is 2:
                                jogo[x] = random.choice(armas.keys())
                print 'o novo jogo é' + str(jogo)
                return True
        except:
                return False
 
def tentativa(chute):

        if chute[0] == jogo[0] and chute[1] == jogo[1] and chute[2] == jogo[2]:
                return 0
        elif chute[0] is not jogo[0]:
                return 1
        elif chute[1] is not jogo[1]:
                return 2
        elif chute[2] is not jogo[2]:
                return 3

