from probability_calculator.core import Hat, experiment
import random

random.seed(1)


def main():
    hat = Hat(black=6, red=4, green=3)
    print(experiment(hat=hat, expected_balls={"red": 2, "green": 1},
                     num_balls_drawn=5, num_experiments=100))


if __name__ == '__main__':
    main()
