import argparse
import turtle


def koch_segment(t: turtle.Turtle, length: float, level: int):
    if level == 0:
        t.forward(length)
        return

    length /= 3.0
    koch_segment(t, length, level - 1)
    t.left(60)
    koch_segment(t, length, level - 1)
    t.right(120)
    koch_segment(t, length, level - 1)
    t.left(60)
    koch_segment(t, length, level - 1)


def koch_snowflake(t: turtle.Turtle, length: float, level: int):
    for _ in range(3):
        koch_segment(t, length, level)
        t.right(120)


def parse_args():
    parser = argparse.ArgumentParser(description="Draw Koch snowflake using recursion.")
    parser.add_argument("--level", type=int, default=3, help="Recursion level (default: 3)")
    parser.add_argument("--length", type=int, default=300, help="Side length (default: 300)")
    parser.add_argument("--speed", type=int, default=0, help="Turtle speed 0..10 (default: 0 fastest)")
    return parser.parse_args()


def main():
    args = parse_args()
    if args.level < 0:
        raise ValueError("level must be >= 0")
    if args.length <= 0:
        raise ValueError("length must be > 0")

    screen = turtle.Screen()
    screen.title(f"Koch Snowflake (level={args.level})")

    t = turtle.Turtle()
    t.hideturtle()
    t.speed(args.speed)
    t.penup()

    t.goto(-args.length / 2, args.length / 3)
    t.pendown()

    koch_snowflake(t, args.length, args.level)

    turtle.done()


if __name__ == "__main__":
    main()
