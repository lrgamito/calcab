#Basics python -m venv <path>
#Calcab app
import calcab as cc

if __name__ == "__main__":
    
    print("\n** Calculo de Cabeamento Estruturado **\n")
    
    try:
        majorHorizontalDistance = input("Informe a maior distancia horizontal, em metros: ")
        minorHorizontalDistance = input("Informe a menor distancia horizontal, em metros: ")
        cableAscend             = input("Informe a subida do cabo, em metros: ")
        cableDescend            = input("Informe a descida do cabo, em metros: ")
        teleCableLeftover       = input("Informe a quantidade de sobra na área de telecom: ")
        workareaCableLefover    = input("Informe a quantidade de sobra na área de trabalho: ")
        numberCables            = input("Informe a quantidade de Pontos do projeto: ")
        safetyMargin            = input("Informe a margem de segurança: ")
        pricePerMeter           = input("Informe o preço por metro: ")
        meterInBox              = input("Informe a quantidade de metros por caixa: ")
        
    except (KeyboardInterrupt):
        
        print("\nSaindo...\n")
    
    else:
        # Add stuff
        cc.calculate(majorHorizontalDistance, minorHorizontalDistance, cableAscend, cableDescend, teleCableLeftover, workareaCableLefover, numberCables, safetyMargin, pricePerMeter, meterInBox)
    