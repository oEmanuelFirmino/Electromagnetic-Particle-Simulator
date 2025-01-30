from particle import Particle
from integration import without_magnetic_field, with_magnetic_field, runge_kutta


def interactive_simulation():
    q = float(input("Digite a carga (q) da partícula (C): "))
    m = float(input("Digite a massa (m) da partícula (kg): "))
    E = list(
        map(
            float,
            input(
                "Digite o campo elétrico E (em 3 componentes separados por espaço): "
            ).split(),
        )
    )
    B = list(
        map(
            float,
            input(
                "Digite o campo magnético B (em 3 componentes separados por espaço): "
            ).split(),
        )
    )
    v0 = list(
        map(
            float,
            input(
                "Digite a velocidade inicial v0 (em 3 componentes separados por espaço): "
            ).split(),
        )
    )
    r0 = list(
        map(
            float,
            input(
                "Digite a posição inicial r0 (em 3 componentes separados por espaço): "
            ).split(),
        )
    )

    particle = Particle(q, m, E, B, v0, r0)

    print("\nEscolha o tipo de simulação:")
    print("1. Sem campo magnético")
    print("2. Com campo magnético")
    print("3. Usando método de Runge-Kutta")
    choice = int(input("Digite o número da opção: "))

    if choice == 1:
        without_magnetic_field(particle)
    elif choice == 2:
        with_magnetic_field(particle)
    elif choice == 3:
        runge_kutta(particle)
    else:
        print("Opção inválida.")


if __name__ == "__main__":
    interactive_simulation()
