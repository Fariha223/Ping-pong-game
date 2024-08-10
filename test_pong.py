import unittest
from ball import Ball
from paddle import Paddle


class Test_Pong(unittest.TestCase):

    def test_ball_bounce_y(self):
        ball = Ball()
        initial_y_pos = ball.y_move
        ball.bounce_y()
        self.assertEqual(ball.y_move, -initial_y_pos)

    def test_ball_bounce_x(self):
        ball = Ball()
        initial_x_move = ball.x_move
        ball.bounce_x()
        self.assertEqual(ball.x_move, -initial_x_move)
        self.assertLess(ball.move_speed, 0.1)  # Speed should decrease

    def test_ball_reset_position(self):
        ball = Ball()
        ball.goto(100, 100)
        ball.reset_position()
        self.assertEqual(ball.position(), (0, 0))
        self.assertEqual(ball.move_speed, 0.1)

    def test_paddle_movement(self):
        paddle = Paddle((0, 0))
        initial_y = paddle.ycor()
        paddle.up()
        self.assertEqual(paddle.ycor(), initial_y + 20)
        paddle.down()
        self.assertEqual(paddle.ycor(), initial_y)

if __name__ == "__main__":
    unittest.main()
