import pygame

surface = []
for row in range(25):
    surface.append([])
    for column in range(25):
        surface[row].append(0)

list_d = []
list_l = []

def grid():

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)

    width = 10
    height = 10

    margin = 2

    pygame.init()

    size = (300, 300)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Game of life')

    done = False

    clock = pygame.time.Clock()

    point = True
    while point:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                point = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                column = pos[0] // (width + margin)
                row = pos[1] // (height + margin)
                surface[row][column] = 1
        screen.fill(BLACK)
        for row in range(25):
            for column in range(25):
                color = WHITE
                if surface[row][column] == 1:
                    color = RED
                pygame.draw.rect(screen, color, [(margin + width) * column + margin, (margin + height) * row + margin, width, height])
        clock.tick(5)
        pygame.display.flip()

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        screen.fill(BLACK)

        check_cell()

        for row in range(25):
            for column in range(25):
                color = WHITE
                if surface[row][column] == 1:
                    color = RED
                pygame.draw.rect(screen, color, [(margin + width) * column + margin, (margin + height) * row + margin, width, height])
        clock.tick(5)
        pygame.display.flip()
    pygame.quit()

def check_cell():
    for row in range(25):
        for column in range(25):
            if surface[row][column] == 1:
                count = 0
                try:
                    if surface[row + 1][column] == 1:
                        count += 1
                    if surface[row - 1][column] == 1:
                        count += 1
                    if surface[row][column + 1] == 1:
                        count += 1
                    if surface[row][column - 1] == 1:
                        count += 1
                    if surface[row + 1][column + 1] == 1:
                        count += 1
                    if surface[row + 1][column - 1] == 1:
                        count += 1
                    if surface[row - 1][column - 1] == 1:
                        count += 1
                    if surface[row - 1][column + 1] == 1:
                        count += 1
                except:
                    pass
                if count == 2 or count == 3:
                    list_l.append([row, column])
                else:
                    list_d.append([row, column])

    for row in range(25):
        for column in range(25):
            if surface[row][column] == 0:
                count = 0
                try:
                    if surface[row + 1][column] == 1:
                        count += 1
                    if surface[row - 1][column] == 1:
                        count += 1
                    if surface[row][column + 1] == 1:
                        count += 1
                    if surface[row][column - 1] == 1:
                        count += 1
                    if surface[row + 1][column + 1] == 1:
                        count += 1
                    if surface[row + 1][column - 1] == 1:
                        count += 1
                    if surface[row - 1][column - 1] == 1:
                        count += 1
                    if surface[row - 1][column + 1] == 1:
                        count += 1
                except:
                    pass
                if count == 3:
                    list_l.append([row, column])

    for el in list_l:
        surface[el[0]][el[1]] = 1
    list_l.clear()
    for el in list_d:
        surface[el[0]][el[1]] = 0
    list_d.clear()

if __name__ == '__main__':
    grid()