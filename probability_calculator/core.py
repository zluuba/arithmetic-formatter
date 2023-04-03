import random
import copy


class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            balls = [key for _ in range(value)]
            self.contents.extend(balls)

    def draw(self, number):
        if number >= len(self.contents) - 1:
            return self.contents

        balls = []
        for i in range(number):
            random_ball_ind = random.randint(1, len(self.contents) - 1)
            ball = self.contents.pop(random_ball_ind)
            balls.append(ball)

        return balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    counter = 0
    for exp in range(num_experiments):
        another_hat = copy.deepcopy(hat)
        drawn_balls = another_hat.draw(num_balls_drawn)
        drawn_balls = {i: drawn_balls.count(i) for i in set(drawn_balls)}
        if all([
            drawn_balls.get(key, 0) >= value
            for key, value
            in expected_balls.items()
        ]):
            counter += 1

    probability = counter / num_experiments
    probability_percentage = f"{int(probability * 100)}%"
    return probability_percentage
