import random
import copy


class Hat:
    def __init__(self, **kwargs: int) -> None:
        self.contents = []

        for key, value in kwargs.items():
            if not isinstance(value, int):
                continue
            balls = [key for _ in range(value)]
            self.contents.extend(balls)

    def draw(self, number: int) -> list[str]:
        if number >= len(self.contents) - 1:
            return self.contents

        balls = []
        for i in range(number):
            random_ball_ind = random.randint(1, len(self.contents) - 1)
            ball = self.contents.pop(random_ball_ind)
            balls.append(ball)

        return balls


def experiment(hat: 'Hat', expected_balls: dict, num_balls_drawn: int,
               num_experiments: int) -> str:

    counter = 0

    for exp in range(num_experiments):
        another_hat = copy.deepcopy(hat)
        drawn_balls = another_hat.draw(num_balls_drawn)
        drawn_balls = {i: drawn_balls.count(i) for i in set(drawn_balls)}

        if all([drawn_balls.get(key, 0) >= value
                for key, value in expected_balls.items()]):
            counter += 1

    probability = counter / num_experiments
    return f"{int(probability * 100)}%"
