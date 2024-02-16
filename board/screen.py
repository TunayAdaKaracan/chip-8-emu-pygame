class Screen:
    def __init__(self, scale):
        self.cols = 64
        self.rows = 32

        self.scale = scale

        self.display = [0] * self.cols * self.rows

    def set_pixel(self, x, y):
        if x > self.cols:
            x -= self.cols
        elif x < 0:
            x += self.cols

        if y > self.rows:
            y -= self.rows
        elif y < 0:
            y += self.rows

        pixel_loc = x + (y * self.cols)
        self.display[pixel_loc] ^= 1  # b0000 0001
        return not self.display[pixel_loc]

    def clear(self):
        self.display = [0] * self.cols * self.rows

    def test_render(self):
        self.set_pixel(1, 1)
        self.set_pixel(6, 1)
        self.set_pixel(12, 0)
        self.set_pixel(0, 0)
        self.set_pixel(0, -1)