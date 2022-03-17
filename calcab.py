import math

#Function that calculate
def calculate(maiorDH, menorDH, subidaCabo, descidaCabo, sobraTele, sobraATrab, numPontos, margemSeg, precoMetro, mtCaixa):
    
    totalMetros = ((( float(maiorDH) + float(menorDH) / 2) + float(subidaCabo) + float(descidaCabo) + float(sobraTele) + float(sobraATrab) ) * int(numPontos))
    totalMetros = totalMetros + (totalMetros * float(margemSeg) / 100)
    
    print(totalMetros)
    
    if float(mtCaixa) > 0:
        totalCaixas = math.ceil( totalMetros / float(mtCaixa) )
    
        print(totalCaixas)
    
    if float(precoMetro) > 0:
        totalValor = totalMetros * float(precoMetro)
    
        print(totalValor)
    
    ret = totalMetros + "\n" + totalCaixas + "\n" + totalValor + "\n"
    
    return ret