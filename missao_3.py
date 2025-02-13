# Missão 3: Recuperando o Sistema de Notas

nota = float(input("Para saber sua classificação na prova, digite sua nota: "))

if nota >= 90 and nota <= 100:
    print("Parabéns, você tirou A!")
elif nota >= 80 and nota <= 89:
    print("Muito bem, você tirou B.")
elif nota >= 70 and nota <= 79:
    print("Bom trabalho, você tirou C.")
elif nota >= 60 and nota <= 69:
    print("Fique atento, você tirou D.")
else:
    print("Estude um pouco mais, você tirou F.")
