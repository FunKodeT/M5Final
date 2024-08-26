import pygame
from pygame.locals import *

import math

class PlayerChar:
    def __init__(self, x, y, radius, color, vel=2.5):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed = vel
        self.angle = -90

    def player_movement(self, keys, window_x, window_y):
        if keys[pygame.K_w] and self.y - self.radius > 0:
            self.y -= self.speed
        if keys[pygame.K_a] and self.x - self.radius > 0:
            self.x -= self.speed
        if keys[pygame.K_s] and self.y + self.radius < window_y:
            self.y += self.speed
        if keys[pygame.K_d] and self.x + self.radius < window_x:
            self.x += self.speed

    def player_turning(self, mouse_x, mouse_y):
        mx = mouse_x - self.x
        my = mouse_y - self.y
        self.angle = math.degrees(math.atan2(my, mx)) + 0

    def player_model(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)
        self.player_face(surface)

    def player_face(self, surface):
        radius_pos = self.radius

        p1 = (
            self.x + radius_pos * math.cos(math.radians(self.angle)),
            self.y + radius_pos * math.sin(math.radians(self.angle))
        )

        edge_len = 5
        # edge_len_half = edge_len // 2
        # offset = edge_len_half
        # offset = self.radius - 10
        
        p2 = (
            self.x + (self.radius - edge_len / 2) * math.cos(math.radians(self.angle + 60)),
            self.y + (self.radius - edge_len / 2) * math.sin(math.radians(self.angle + 60))
        )
        p3 = (
            self.x + (self.radius - edge_len / 2) * math.cos(math.radians(self.angle + 300)),
            self.y + (self.radius - edge_len / 2) * math.sin(math.radians(self.angle + 300))
        )
        # p2 = (
        #     self.x + offset * math.cos(math.radians(self.angle + 120)),
        #     self.y + offset * math.sin(math.radians(self.angle + 120))
        # )
        # p3 = (
        #     self.x + offset * math.cos(math.radians(self.angle + 240)),
        #     self.y + offset * math.sin(math.radians(self.angle + 240))
        # )
        # p2 = (
        #     p1[0] + offset * math.cos(math.radians(self.angle + 120)),
        #     p1[1] + offset * math.sin(math.radians(self.angle + 120))
        # )
        # p3 = (
        #     p1[0] + offset * math.cos(math.radians(self.angle + 240)),
        #     p1[1] + offset * math.sin(math.radians(self.angle + 240))
        # )

        pygame.draw.polygon(surface, (0, 0, 178), [p1, p2, p3])

    def player_collision(self):
        return pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2)