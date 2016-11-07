import pygame;
import numpy as np;


def drawPixelated(A, screen):
    """Draw 30x30 image of input"""

    A = A.ravel()
    A = (255 - A * 255).transpose()
    size = 30
    for x in range(size):
        for y in range(size):
            z = x * 30 + y
            c = int(A[z])
            pygame.draw.rect(screen, (c, c, c), (x * 11 + 385, 15 + y * 11, 11, 11))


def checkKeys(myData):
    """test for various keyboard inputs"""

    (event, background, drawColor, lineWidth, keepGoing, screen, image) = myData

    if event.key == pygame.K_q:
        keepGoing = False
    elif event.key == pygame.K_c:
        background.fill((255, 255, 255))
        drawPixelated(np.zeros((30, 30)), screen)
    # elif event.key == pygame.K_s:
    #     global changed
    #     try:
    #         mat_contents = sio.loadmat('newX.mat')
    #         X = mat_contents['X']
    #         X = np.append(X, image, axis=0)
    #     except:
    #         X = image
    #     answer = np.matrix(int(ask(screen, "")))
    #     try:
    #         mat_contents = sio.loadmat('newy.mat')
    #         y = mat_contents['y']
    #         y = np.append(y, answer, axis=0)
    #     except:
    #         y = answer
    #     if changed:
    #         sio.savemat('newX.mat', {'X': X})
    #         sio.savemat('newy.mat', {'y': y})
    #         changed = False
    #
    #     background.fill((255, 255, 255))
    #     drawPixelated(np.zeros((30, 30)), screen)

    # elif event.key == pygame.K_t:
    #     screen.fill((255, 255, 255))
    #     myFont1 = pygame.font.SysFont("Verdana", 55)
    #     myFont2 = pygame.font.SysFont("Verdana", 17)
    #     myFont3 = pygame.font.SysFont("Verdana", 9)
    #     screen.blit(myFont1.render("Please wait!", 1, ((0, 0, 0))), (365, 90))
    #     screen.blit(myFont2.render("Neural network training in progress...", 1, ((50, 50, 50))), (368, 150))
    #     screen.blit(myFont3.render("Depending on the training data size this could take long time", 1, ((80, 80, 80))),
    #                 (370, 190))
    #     pygame.display.flip()
    #     global Xtrain;
    #     global Xtest;
    #     global ytrain;
    #     global ytest
    #     mat_contents = sio.loadmat('newX.mat')
    #     Xs = mat_contents['X']
    #     mat_contents = sio.loadmat('newy.mat')
    #     ys = mat_contents['y']
    #     Xtrain, Xtest, ytrain, ytest = splitData(Xs, ys)
    #
    #     rndInit = randomInitialization(25 * 901 + 10 * 26)
    #     answer = sc.fmin_cg(calculateJ, rndInit, calculateGrad, maxiter=100, disp=True, callback=callback)
    #     Theta1 = np.reshape(answer[:num_hidden * (num_input + 1)], (num_hidden, -1))
    #     Theta2 = np.reshape(answer[num_hidden * (num_input + 1):], (num_lables, -1))
    #
    #     acc = returnAccuracy(probabiltyForDrawing(Theta1, Theta2, Xtest), ytest)
    #     sio.savemat('scaledTheta.mat', {'t': answer, 'acc': acc})
    #     screen.fill((0, 0, 0))
    #     background.fill((255, 255, 255))
    # elif event.key == pygame.K_v:
    #     drawStatistics(screen)

    myData = (event, background, drawColor, lineWidth, keepGoing)
    return myData


def main():
    """Main method. Draw interface"""

    global screen
    pygame.init()
    screen = pygame.display.set_mode((730, 450))
    pygame.display.set_caption("Yarn Type recognition")

    background = pygame.Surface((360, 360))
    background.fill((255, 255, 255))
    background2 = pygame.Surface((360, 360))
    background2.fill((255, 255, 255))

    clock = pygame.time.Clock()
    keepGoing = True
    lineStart = (0, 0)
    drawColor = (255, 0, 0)
    lineWidth = 2

  #  inputTheta = sio.loadmat('scaledTheta.mat')
   # theta = inputTheta['t']
    num_hidden = 25
    num_input = 900
    num_lables = 10

    #Theta1 = np.reshape(theta[:num_hidden * (num_input + 1)], (num_hidden, -1))
    #Theta2 = np.reshape(theta[num_hidden * (num_input + 1):], (num_lables, -1))

    pygame.display.update()
    image = None

    while keepGoing:

        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.MOUSEMOTION:
                lineEnd = pygame.mouse.get_pos()
                if pygame.mouse.get_pressed() == (1, 0, 0):
                    pygame.draw.line(background, drawColor, lineStart, lineEnd, lineWidth)
                lineStart = lineEnd
            elif event.type == pygame.MOUSEBUTTONUP:
                screen.fill((0, 0, 0))
                screen.blit(background2, (370, 0))
                #w = threading.Thread(name='worker', target=worker)
                #image = calculateImage(background, screen, Theta1, Theta2, lineWidth)

            elif event.type == pygame.KEYDOWN:
                myData = (event, background, drawColor, lineWidth, keepGoing, screen, image)
                myData = checkKeys(myData)
                (event, background, drawColor, lineWidth, keepGoing) = myData

        screen.blit(background, (0, 0))
        pygame.display.flip()


if __name__ == "__main__":
    main()