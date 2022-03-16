import math

#Function that calculate
def calculate(maiorDH, menorDH, subidaCabo, descidaCabo, sobraTele, sobraATrab, numPontos, margemSeg, precoMetro, mtCaixa):
    
    totalMetros = (((( maiorDH + menorDH) / 2) + subidaCabo + descidaCabo + sobraTele + sobraATrab ) * numPontos)
    totalMetros = totalMetros + (totalMetros * margemSeg / 100)
    
    print(totalMetros)
    
    if mtCaixa > 0:
        totalCaixas = math.ceil(totalMetros / mtCaixa)
    
        print(totalCaixas)
    
    if precoMetro > 0:
        totalValor = totalMetros * precoMetro
    
        print(totalValor)
    
    return True
    