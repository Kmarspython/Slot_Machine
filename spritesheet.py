import pygame as p

class SpriteSheet():
    """Loading in individual sprites from a sprite sheet"""
    def __init__(self, image):
        self.sheet = image

    def get_image(self, frame_x, frame_y, width, height, scale, color):
        image = p.Surface((width, height)).convert_alpha()
        image.blit(self.sheet, (0, 0), ((frame_x * width), (frame_y * height), width, height))
        image = p.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(color)

        return image

    def create_image_list(self, width, height, scale, color):
        result = []
        for i in range(4):
            for j in range(4):
                if j == 3 and i == 3:
                    break
                else:
                    result += [self.get_image(j, i, width, height, scale, color)]
        return result

