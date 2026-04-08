import pygame

from base.const import WIN_WIDTH, MENU_OPTIONS, COLOR_WHITE


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/background/orig.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        pygame.mixer_music.load('./asset/sound/menu_sound.wav')
        pygame.mixer_music.play(-1)


        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "Mountain", (255, 128, 0), ((WIN_WIDTH/2), 70))
            self.menu_text(40, "GAMER", (255, 128, 0), ((WIN_WIDTH/2), 110))

            for i in range(len(MENU_OPTIONS)):
                self.menu_text(20, MENU_OPTIONS[i], COLOR_WHITE, ((WIN_WIDTH/2), 150 + 25 * i))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                    quit()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect = text_surface.get_rect(center=text_center_pos)
        self.window.blit(source=text_surface, dest=text_rect);