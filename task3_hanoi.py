import argparse
from copy import deepcopy


def print_state(title: str, rods: dict):
    print(f"{title}: {rods}")


def move_disk(rods: dict, src: str, dst: str):
    disk = rods[src].pop()
    rods[dst].append(disk)
    print(f"Перемістити диск з {src} на {dst}: {disk}")
    print_state("Проміжний стан", rods)


def hanoi(n: int, src: str, aux: str, dst: str, rods: dict):
    if n == 0:
        return
    hanoi(n - 1, src, dst, aux, rods)
    move_disk(rods, src, dst)
    hanoi(n - 1, aux, src, dst, rods)


def parse_args():
    parser = argparse.ArgumentParser(description="Towers of Hanoi.")
    parser.add_argument("n", type=int, help="Number of disks")
    return parser.parse_args()


def main():
    args = parse_args()
    n = args.n
    if n <= 0:
        raise ValueError("n must be > 0")

    rods = {"A": list(range(n, 0, -1)), "B": [], "C": []}
    print_state("Початковий стан", deepcopy(rods))

    hanoi(n, "A", "B", "C", rods)

    print_state("Кінцевий стан", rods)


if __name__ == "__main__":
    main()
