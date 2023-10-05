import math
import time

def animacao(texto):
    for char in texto:
        print(char, end='', flush=True)
        time.sleep(0.03)
    print()

def obter_coordenadas(mensagem):
    while True:
        coordenadas = input(mensagem)
        if "," in coordenadas:
            try:
                coordenadas = [float(x) for x in coordenadas.split(",")]
                if len(coordenadas) == 2:
                    return coordenadas
            except ValueError:
                pass
        print("Por favor, digite as coordenadas corretamente (formato: x,y).")

apresentacao = (
    "Bem-vindo à Calculadora de Engenharia Estrutural!\n"
    "Essa calculadora determinará a área, o momento estático, o centro de gravidade e o momento de inércia de várias figuras!\n"
)

animacao(apresentacao)
print("\nDessa forma, vamos calcular a área, o momento estático, o centro de gravidade e o momento de inércia de várias figuras!")

while True:
    area_total = 0
    momento_estatico_total_x = 0
    momento_estatico_total_y = 0
    momento_inercia_x = 0
    momento_inercia_y = 0

    figuras = int(input("Quantas figuras você deseja calcular?\n"))

    for i in range(figuras):
        tipo_figura = int(input(f"Qual o tipo de figura está sendo adicionada? (Figura {i + 1})\n"
                                "1- quadrado ou retângulo\n"
                                "2- triângulo\n"
                                "3- círculo\n"
                                "4- semicírculo\n"
                                "5- 1/4 de círculo\n"))

        if tipo_figura == 1 or tipo_figura == 2:
            base = obter_coordenadas("Quais as coordenadas em X da base? (separar por vírgula)\n")
            altura = obter_coordenadas("Quais as coordenadas em Y da altura? (separar por vírgula)\n")
            base_conta = base[1] - base[0]
            altura_conta = altura[1] - altura[0]
            area = base_conta * altura_conta

            if tipo_figura == 1:
                centro_gx = (base_conta / 2) + base[0]
                centro_gy = (altura_conta / 2) + altura[0]
                dIx = (altura_conta ** 3) * base_conta / 12
                dIy = (base_conta ** 3) * altura_conta / 12
            else:
                area = area / 2
                angulo_reto = obter_coordenadas("Quais as coordenadas do ângulo reto? (separar por vírgula)\n")
                centro_gx = (base_conta / 3) + angulo_reto[0]
                centro_gy = (altura_conta / 3) + angulo_reto[1]
                dIx = (altura_conta ** 3) * base_conta / 36
                dIy = (base_conta ** 3) * altura_conta / 36

        elif tipo_figura == 3 or tipo_figura == 4 or tipo_figura == 5:
            centro_circulo = obter_coordenadas("Quais as coordenadas do centro da figura? (separar por vírgula)\n")
            raio = float(input("Qual o raio da figura?\n"))
            area = math.pi * (raio ** 2)

            if tipo_figura == 3:
                centro_gx = centro_circulo[0]
                centro_gy = centro_circulo[1]
                dIx = (math.pi * raio ** 4) / 4
                dIy = (math.pi * raio ** 4) / 4
            elif tipo_figura == 4:
                area = area / 2
                direction = int(input("Para qual direção está o semicírculo?\n"
                                      "1 - esquerda\n"
                                      "2 - baixo\n"
                                      "3 - direita\n"
                                      "4 - cima\n"))
                if direction == 1 or direction == 3:
                    centro_gy = centro_circulo[1]
                    center_x = (4 * raio / (3 * math.pi)) if direction == 1 else (-4 * raio / (3 * math.pi))
                    centro_gx = centro_circulo[0] + center_x
                    dIx = (math.pi * raio ** 4) / 4
                    dIy = (math.pi * raio ** 4) / 4
                else:
                    centro_gx = centro_circulo[0]
                    center_y = (4 * raio / (3 * math.pi)) if direction == 2 else (-4 * raio / (3 * math.pi))
                    centro_gy = centro_circulo[1] + center_y
                    dIx = (math.pi * raio ** 4) / 4
                    dIy = (math.pi * raio ** 4) / 4
            else:
                area = area / 4
                direction = int(input("Em qual quadrante está o ¼ de círculo?\n"
                                      "1 - primeiro\n"
                                      "2 - segundo\n"
                                      "3 - terceiro\n"
                                      "4 - quarto\n"))
                if direction == 1 or direction == 2:
                    centro_gy = centro_circulo[1] + (4 * raio / (3 * math.pi))
                    center_x = (4 * raio / (3 * math.pi)) if direction == 1 else (-4 * raio / (3 * math.pi))
                    centro_gx = centro_circulo[0] + center_x
                    dIx = (math.pi * raio ** 4) / 4
                    dIy = (math.pi * raio ** 4) / 4
                elif direction == 3 or direction == 4:
                    centro_gy = centro_circulo[1] - (4 * raio / (3 * math.pi))
                    center_x = (-4 * raio / (3 * math.pi)) if direction == 3 else (4 * raio / (3 * math.pi))
                    centro_gx = centro_circulo[0] + center_x
                    dIx = (math.pi * raio ** 4) / 4
                    dIy = (math.pi * raio ** 4) / 4

        momento_estatico_total_x += centro_gx * area
        momento_estatico_total_y += centro_gy * area
        momento_inercia_x += dIx
        momento_inercia_y += dIy
        area_total += area

    print(f"Área Total: {area_total}")
    print(f"Centro de Gravidade (Eixo X): {momento_estatico_total_x / area_total}")
    print(f"Centro de Gravidade (Eixo Y): {momento_estatico_total_y / area_total}")
    print(f"Momento de Inércia (Eixo X): {momento_inercia_x}")
    print(f"Momento de Inércia (Eixo Y): {momento_inercia_y}")

    sair = input("Digite 'SAIR' para parar ou pressione ENTER↵ para continuar: ")

    if sair == 'SAIR':
        break
