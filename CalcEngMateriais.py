import math
import time

class Figura:
    def __init__(self, tipo):
        self.tipo = tipo
        self.area = 0
        self.centro_gx = 0
        self.centro_gy = 0
        self.momento_inercia_x = 0
        self.momento_inercia_y = 0

    def calcular_area(self):
        pass

    def calcular_centro_gravidade(self):
        pass

    def calcular_momento_inercia(self):
        pass

class QuadradoRetangulo(Figura):
    def __init__(self, base, altura):
        super().__init__("Quadrado/Retângulo")
        self.base = base
        self.altura = altura

    def calcular_area(self):
        self.area = self.base * self.altura

    def calcular_centro_gravidade(self):
        self.centro_gx = self.base / 2
        self.centro_gy = self.altura / 2

    def calcular_momento_inercia(self):
        self.momento_inercia_x = (self.altura ** 3) * self.base / 12
        self.momento_inercia_y = (self.base ** 3) * self.altura / 12

class Triangulo(Figura):
    def __init__(self, base, altura):
        super().__init__("Triângulo")
        self.base = base
        self.altura = altura

    def calcular_area(self):
        self.area = (self.base * self.altura) / 2

    def calcular_centro_gravidade(self):
        self.centro_gx = self.base / 3
        self.centro_gy = self.altura / 3

    def calcular_momento_inercia(self):
        self.momento_inercia_x = (self.altura ** 3) * self.base / 36
        self.momento_inercia_y = (self.base ** 3) * self.altura / 36

class Circulo(Figura):
    def __init__(self, raio):
        super().__init__("Círculo")
        self.raio = raio

    def calcular_area(self):
        self.area = math.pi * (self.raio ** 2)

    def calcular_centro_gravidade(self):
        self.centro_gx = 0
        self.centro_gy = 0

    def calcular_momento_inercia(self):
        self.momento_inercia_x = (math.pi * self.raio ** 4) / 4
        self.momento_inercia_y = (math.pi * self.raio ** 4) / 4

class Semicirculo(Figura):
    def __init__(self, raio, direcao):
        super().__init__("Semicírculo")
        self.raio = raio
        self.direcao = direcao

    def calcular_area(self):
        self.area = (math.pi * (self.raio ** 2)) / 2

    def calcular_centro_gravidade(self):
        if self.direcao in [1, 3]:
            self.centro_gx = 0
            self.centro_gy = 0
        else:
            self.centro_gx = 0
            self.centro_gy = (4 * self.raio / (3 * math.pi))

    def calcular_momento_inercia(self):
        self.momento_inercia_x = (math.pi * self.raio ** 4) / 4
        self.momento_inercia_y = (math.pi * self.raio ** 4) / 4

# Função para obter coordenadas
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

# Função principal
def main():
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

            if tipo_figura == 1:
                base = obter_coordenadas("Quais as coordenadas em X da base? (separar por vírgula)\n")
                altura = obter_coordenadas("Quais as coordenadas em Y da altura? (separar por vírgula)\n")
                figura = QuadradoRetangulo(base[1] - base[0], altura[1] - altura[0])
            elif tipo_figura == 2:
                base = obter_coordenadas("Quais as coordenadas em X da base? (separar por vírgula)\n")
                altura = obter_coordenadas("Quais as coordenadas em Y da altura? (separar por vírgula)\n")
                figura = Triangulo(base[1] - base[0], altura[1] - altura[0])
            elif tipo_figura == 3:
                raio = float(input("Qual o raio do círculo?\n"))
                figura = Circulo(raio)
            elif tipo_figura == 4:
                raio = float(input("Qual o raio do semicírculo?\n"))
                direcao = int(input("Para qual direção está o semicírculo?\n"
                                    "1 - esquerda\n"
                                    "2 - baixo\n"
                                    "3 - direita\n"
                                    "4 - cima\n"))
                figura = Semicirculo(raio, direcao)

            figura.calcular_area()
            figura.calcular_centro_gravidade()
            figura.calcular_momento_inercia()

            momento_estatico_total_x += figura.centro_gx * figura.area
            momento_estatico_total_y += figura.centro_gy * figura.area
            momento_inercia_x += figura.momento_inercia_x
            momento_inercia_y += figura.momento_inercia_y
            area_total += figura.area

        print(f"Área Total: {area_total}")
        print(f"Centro de Gravidade (Eixo X): {momento_estatico_total_x / area_total}")
        print(f"Centro de Gravidade (Eixo Y): {momento_estatico_total_y / area_total}")
        print(f"Momento de Inércia (Eixo X): {momento_inercia_x}")
        print(f"Momento de Inércia (Eixo Y): {momento_inercia_y}")

        sair = input("Digite 'SAIR' para parar ou pressione ENTER↵ para continuar: ")

        if sair == 'SAIR':
            break

if __name__ == "__main__":
    main()
