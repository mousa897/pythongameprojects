import pygame
from pygame import mixer
import time
import sys

# to initialize the game
pygame.init()

# screen
screen = pygame.display.set_mode((850, 600))

# Background
background = pygame.image.load('background.jpg')
bg_music = mixer.music.load('bgm.wav')

# Title and Icon
pygame.display.set_caption("Nature Explorer")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

# Initialize a dictionary to store object states
object_states = {
    'flower': False,
    'bird': False,
    'tree': False,
    'apple': False,
    'grape': False,
    'pear': False,
    'banana': False,
    'cherries': False,
    'cat': False,
    'dog': False,
    'fox': False,
    'cow': False,
    'turtle': False,
    'rooster': False
}

# X button
x_button_x = 750
x_button_y = 510
x_button_width = 40
x_button_height = 40

# flower
flower_normal = pygame.image.load('sunflower.png')
flower_hover = pygame.image.load('sunflower_hvr.png')
flowerX = 300
flowerY = 400
flower_clicked = False

flowerIMG = flower_normal

# Bird
bird_normal = pygame.image.load('Bird.png')
bird_hover = pygame.image.load('Bird_hvr.png')
birdX = 800
birdY = 40
birdX_change = -0.5
bird_reset_timer = None
bird_clicked = False

birdIMG = bird_normal

# Tree
tree_normal = pygame.image.load('tree.png')
tree_hvr = pygame.image.load('tree_hvr.png')
treeX = 30
treeY = 100

treeIMG = tree_normal
tree_clicked = False

# apple
apple_normal = pygame.image.load('apple.png')
apple_hvr = pygame.image.load('apple_hvr.png')
appleX = 90
appleY = 140
appleY_change = 0.5
apple_clicked = False

appleIMG = apple_normal

# grape
grape_nrm = pygame.image.load('grape.png')
grape_hvr = pygame.image.load('grape_hvr.png')
grapeX = 87
grapeY = 200
grapeY_change = 0.5
grape_clicked = False

grapeIMG = grape_nrm

# pear
pear_nrm = pygame.image.load('pear.png')
pear_hvr = pygame.image.load('pear_hvr.png')
pearX = 140
pearY = 160
pearY_change = 0.5
pear_clicked = False

pearIMG = pear_nrm

# banana
bnn_nrm = pygame.image.load('banana.png')
bnn_hvr = pygame.image.load('banana_hvr.png')
bnn2 = pygame.image.load('banana2.png')
bananaX = 210
bananaY = 210
bananaY_change = 0.5
banana_clicked = False

bnnIMG = bnn_nrm

# Cherries
chr_nrm = pygame.image.load('cherry.png')
chr_hvr = pygame.image.load('cherry_hvr.png')
cherriesX = 190
cherriesY = 150
cherriesY_change = 0.5
cherries_clicked = False

chrIMG = chr_nrm

# Cat
cat_normal = pygame.image.load('cat1.png')
cat_hvr = pygame.image.load('cat1_hvr.png')
cat2_normal = pygame.image.load('cat2.png')
cat2_hvr = pygame.image.load('cat2_hvr.png')
cat3_normal = pygame.image.load('cat3.png')
cat3_hvr = pygame.image.load('cat3_hvr.png')
catX = 500
catY = 430
cat_clicked = False

catIMG = cat_normal

# Dog
dog_normal = pygame.image.load('dog1.png')
dog_hvr = pygame.image.load('dog1_hvr.png')
dog2_normal = pygame.image.load('dog2.png')
dog2_hvr = pygame.image.load('dog2_hvr.png')
dog3_normal = pygame.image.load('dog3.png')
dog3_hvr = pygame.image.load('dog3_hvr.png')
dogX = 700
dogY = 430
dog_clicked = False

dogIMG = dog_normal

# Fox
fox_normal = pygame.image.load('fox.png')
fox_hvr = pygame.image.load('fox_hvr.png')
fox2_normal = pygame.image.load('fox2.png')
fox2_hvr = pygame.image.load('fox2_hvr.png')
fox_X = 200
fox_Y = 300
fox_clicked = False

foxIMG = fox_normal

# Cow
cow_normal = pygame.image.load('cow.png')
cow_hvr = pygame.image.load('cow_hvr.png')
cowX = 450
cowY = 300
cow_clicked = False

cowIMG = cow_normal

# Turtle
turtle_normal = pygame.image.load('turtle.png')
turtle_hvr = pygame.image.load('turtle_hvr.png')
turtleX = 330
turtleY = 280
turtle_clicked = False

turtleIMG = turtle_normal

# Rooster
rooster_normal = pygame.image.load('rooster.png')
rooster_hvr = pygame.image.load('rooster_hvr.png')
roosterX = 750
roosterY = 225
rooster_clicked = False

roosterIMG = rooster_normal

# Text
fontX = 20
fontY = 510
font = pygame.font.Font('freesansbold.ttf', 20)

counter_font = pygame.font.Font('freesansbold.ttf', 24)
counter_text_pos = (620, 570)

interaction = False

# Star
star_image = pygame.image.load('star.png')
starX = 10
starY = 10
show_star = False


def info_box():
    pygame.draw.rect(screen, (150, 75, 0), (10, 500, 800, 100))


def x_button():
    pygame.draw.rect(screen, (255, 0, 0), (x_button_x, x_button_y, x_button_width, x_button_height))


def flower(x, y):
    screen.blit(flowerIMG, (x, y))
    return flowerIMG.get_rect(topleft=(x, y))


def bird(x, y):
    screen.blit(birdIMG, (x, y))
    return birdIMG.get_rect(topleft=(x, y))


def tree(x, y):
    screen.blit(treeIMG, (x, y))
    return treeIMG.get_rect(topleft=(x, y))


def apple(x, y):
    screen.blit(appleIMG, (x, y))
    return appleIMG.get_rect(topleft=(x, y))


def grape(x, y):
    screen.blit(grapeIMG, (x, y))
    return grapeIMG.get_rect(topleft=(x, y))


def pear(x, y):
    screen.blit(pearIMG, (x, y))
    return pearIMG.get_rect(topleft=(x, y))


def banana(x, y):
    screen.blit(bnnIMG, (x, y))
    return bnnIMG.get_rect(topleft=(x, y))


def cherries(x, y):
    screen.blit(chrIMG, (x, y))
    return chrIMG.get_rect(topleft=(x, y))


def cat(x, y):
    screen.blit(catIMG, (x, y))
    return catIMG.get_rect(topleft=(x, y))


def dog(x, y):
    screen.blit(dogIMG, (x, y))
    return dogIMG.get_rect(topleft=(x, y))


def fox(x, y):
    screen.blit(foxIMG, (x, y))
    return foxIMG.get_rect(topleft=(x, y))


def cow(x, y):
    screen.blit(cowIMG, (x, y))
    return cowIMG.get_rect(topleft=(x, y))


def turtle(x, y):
    screen.blit(turtleIMG, (x, y))
    return turtleIMG.get_rect(topleft=(x, y))


def rooster(x, y):
    screen.blit(roosterIMG, (x, y))
    return roosterIMG.get_rect(topleft=(x, y))


def main_menu():
    pygame.display.set_caption("Nature Explorer")

    # MENU
    # Colors
    start_font = pygame.font.Font('freesansbold.ttf', 40)
    title_font = pygame.font.Font('freesansbold.ttf', 80)

    background_image = pygame.image.load('menu_bg.jpg')

    while True:
        screen.blit(background_image, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    # Start the game if Enter key is pressed
                    return
            # Draw menu items
        title_text = title_font.render("Nature Explorer", True, (0, 100, 0))
        start_text = start_font.render("Press 'Enter' to play!", True, (0, 100, 0))

        screen.blit(title_text, (120, 250))
        screen.blit(start_text, (10, 550))

        pygame.display.update()


main_menu()  # Enter the main menu loop

mixer.music.play(-1)
mixer.music.set_volume(0.2)

# Game loop

running = True
while running:

    screen.blit(background, (0, 0))

    flower_rect = flower(flowerX, flowerY)
    bird_rect = bird(birdX, birdY)
    apple_rect = apple(appleX, appleY)
    grape_rect = grape(grapeX, grapeY)
    pear_rect = pear(pearX, pearY)
    banana_rect = banana(bananaX, bananaY)
    cherries_rect = cherries(cherriesX, cherriesY)
    cat_rect = cat(catX, catY)
    dog_rect = dog(dogX, dogY)
    fox_rect = fox(fox_X, fox_Y)
    cow_rect = cow(cowX, cowY)
    turtle_rect = turtle(turtleX, turtleY)
    rooster_rect = rooster(roosterX, roosterY)
    tree_rect = tree(treeX, treeY)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEMOTION:
            mouseX, mouseY = pygame.mouse.get_pos()

            # Flower
            if flower_rect.collidepoint(mouseX, mouseY):
                flowerIMG = flower_hover
            else:
                flowerIMG = flower_normal

            # Bird
            if bird_rect.collidepoint(mouseX, mouseY):
                birdIMG = bird_hover
                birdX_change = 0
            else:
                birdIMG = bird_normal
                birdX_change = -0.5

            # Tree
            if tree_rect.collidepoint(mouseX, mouseY):
                treeIMG = tree_hvr
                appleIMG = apple_normal
            else:
                treeIMG = tree_normal

            # Apple
            if apple_rect.collidepoint(mouseX, mouseY):
                appleIMG = apple_hvr
                treeIMG = tree_normal
            else:
                appleIMG = apple_normal

            # Grape
            if grape_rect.collidepoint(mouseX, mouseY):
                grapeIMG = grape_hvr
                treeIMG = tree_normal

            else:
                grapeIMG = grape_nrm

            # Pear
            if pear_rect.collidepoint(mouseX, mouseY):
                pearIMG = pear_hvr
                treeIMG = tree_normal
            else:
                pearIMG = pear_nrm

            # Banana
            if banana_rect.collidepoint(mouseX, mouseY):
                bnnIMG = bnn_hvr
                treeIMG = tree_normal
            else:
                bnnIMG = bnn_nrm

            # Cherries
            if cherries_rect.collidepoint(mouseX, mouseY):
                chrIMG = chr_hvr
                treeIMG = tree_normal
            else:
                chrIMG = chr_nrm

            # Cat
            if cat_rect.collidepoint(mouseX, mouseY):
                catIMG = cat_hvr
            else:
                catIMG = cat_normal

            # Dog
            if dog_rect.collidepoint(mouseX, mouseY):
                dogIMG = dog_hvr
            else:
                dogIMG = dog_normal

            # Fox
            if fox_rect.collidepoint(mouseX, mouseY):
                foxIMG = fox_hvr
                treeIMG = tree_normal
            else:
                foxIMG = fox_normal

            # Cow
            if cow_rect.collidepoint(mouseX, mouseY):
                cowIMG = cow_hvr
            else:
                cowIMG = cow_normal

            # Turtle
            if turtle_rect.collidepoint(mouseX, mouseY):
                turtleIMG = turtle_hvr
            else:
                turtleIMG = turtle_normal

            # Rooster
            if rooster_rect.collidepoint(mouseX, mouseY):
                roosterIMG = rooster_hvr
            else:
                roosterIMG = rooster_normal

        # When mouse clicked at the object
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = pygame.mouse.get_pos()

            # X button
            if x_button_x <= mouseX <= x_button_x + x_button_width and \
                    x_button_y <= mouseY <= x_button_y + x_button_height:

                flower_clicked = False
                if flower_clicked is False:
                    interaction = False

                bird_clicked = False
                if bird_clicked is False:
                    interaction = False

                tree_clicked = False
                if tree_clicked is False:
                    interaction = False

                apple_clicked = False
                if apple_clicked is False:
                    appleY_change = 0.5
                    appleY = 140
                    interaction = False

                grape_clicked = False
                if grape_clicked is False:
                    grapeY_change = 0.5
                    grapeY = 200
                    interaction = False

                pear_clicked = False
                if pear_clicked is False:
                    pearY_change = 0.5
                    pearY = 160
                    interaction = False

                banana_clicked = False
                if banana_clicked is False:
                    bananaY_change = 0.5
                    bananaY = 210
                    bnnIMG = bnn_nrm
                    interaction = False

                cherries_clicked = False
                if cherries_clicked is False:
                    cherriesY_change = 0.5
                    cherriesY = 150
                    interaction = False

                cat_clicked = False
                if cat_clicked is False:
                    catIMG = cat_normal
                    interaction = False

                dog_clicked = False
                if dog_clicked is False:
                    dogIMG = dog_normal
                    interaction = False

                fox_clicked = False
                if fox_clicked is False:
                    foxIMG = fox_normal
                    interaction = False

                cow_clicked = False
                if cow_clicked is False:
                    interaction = False

                turtle_clicked = False
                if turtle_clicked is False:
                    interaction = False

                rooster_clicked = False
                if rooster_clicked is False:
                    interaction = False

            if interaction is False:
                # flower
                if flower_rect.collidepoint(mouseX, mouseY):
                    if not object_states['flower']:  # Check if the flower hasn't been explored before
                        object_states['flower'] = True  # Mark the flower as explored
                    flower_clicked = True
                    flw_sound = mixer.Sound('chime_sound.wav')
                    flw_sound.play()

                # bird
                if bird_rect.collidepoint(mouseX, mouseY):
                    if not object_states['bird']:
                        object_states['bird'] = True
                    bird_clicked = True
                    bird_sound = mixer.Sound('bird_sound.wav')
                    bird_sound.play()

                # apple
                if apple_rect.collidepoint(mouseX, mouseY):
                    if not object_states['apple']:
                        object_states['apple'] = True
                    apple_clicked = True
                    apl_sound = mixer.Sound('apl_snd.wav')
                    apl_sound.play()

                # Tree
                if tree_rect.collidepoint(mouseX, mouseY):
                    if not object_states['tree']:
                        object_states['tree'] = True
                    tree_clicked = True
                    tree_sound = mixer.Sound('tree_snd.wav')
                    tree_sound.play()
                else:
                    tree_clicked = False

                # Grape
                if grape_rect.collidepoint(mouseX, mouseY):
                    if not object_states['grape']:
                        object_states['grape'] = True
                    grape_clicked = True
                    grp_sound = mixer.Sound('apl_snd.wav')
                    grp_sound.play()

                # Pear
                if pear_rect.collidepoint(mouseX, mouseY):
                    if not object_states['pear']:
                        object_states['pear'] = True
                    pear_clicked = True
                    pear_sound = mixer.Sound('apl_snd.wav')
                    pear_sound.play()

                # Banana
                if banana_rect.collidepoint(mouseX, mouseY):
                    if not object_states['banana']:
                        object_states['banana'] = True
                    banana_clicked = True
                    bnn_sound = mixer.Sound('apl_snd.wav')
                    bnn_sound.play()

                # Cherries
                if cherries_rect.collidepoint(mouseX, mouseY):
                    if not object_states['cherries']:
                        object_states['cherries'] = True
                    cherries_clicked = True
                    chr_sound = mixer.Sound('apl_snd.wav')
                    chr_sound.play()

                # Cat
                if cat_rect.collidepoint(mouseX, mouseY):
                    if not object_states['cat']:
                        object_states['cat'] = True
                    cat_clicked = True
                    cat_sound = mixer.Sound('cat_snd.wav')
                    cat_sound.play()

                # Dog
                if dog_rect.collidepoint(mouseX, mouseY):
                    if not object_states['dog']:
                        object_states['dog'] = True
                    dog_clicked = True
                    dog_sound = mixer.Sound('dog_bark.wav')
                    dog_sound.play()

                # Fox
                if fox_rect.collidepoint(mouseX, mouseY):
                    if not object_states['fox']:
                        object_states['fox'] = True
                    fox_clicked = True
                    fox_sound = mixer.Sound('fox_snd.wav')
                    fox_sound.play()

                # Cow
                if cow_rect.collidepoint(mouseX, mouseY):
                    if not object_states['cow']:
                        object_states['cow'] = True
                    cow_clicked = True
                    cow_sound = mixer.Sound('cow_sound.wav')
                    cow_sound.play()

                # Turtle
                if turtle_rect.collidepoint(mouseX, mouseY):
                    if not object_states['turtle']:
                        object_states['turtle'] = True
                    turtle_clicked = True
                    turtle_sound = mixer.Sound('turtle_sound.wav')
                    turtle_sound.play()

                if rooster_rect.collidepoint(mouseX, mouseY):
                    if not object_states['rooster']:
                        object_states['rooster'] = True
                    rooster_clicked = True
                    rstr_snd = mixer.Sound('rooster_sound.wav')
                    rstr_snd.play()

    if flower_clicked:
        interaction = True
        info_box()
        x_button()
        flw_info = font.render("This is a Flower!", True, (230, 230, 0))
        flw_info2 = font.render("The sunflower always faces toward the sun!", True, (230, 230, 0))
        screen.blit(flw_info, (fontX, fontY))
        screen.blit(flw_info2, (fontX, fontY + 30))

    if bird_clicked:
        interaction = True
        info_box()
        x_button()
        bird_info = font.render("This is a Bird!", True, (100, 150, 255))
        bird_info2 = font.render('Did you know that there are around 10,000 different species of birds?!',
                                 True,
                                 (100, 150, 255))
        screen.blit(bird_info, (fontX, fontY))
        screen.blit(bird_info2, (fontX, fontY + 30))

    if tree_clicked:
        interaction = True
        info_box()
        x_button()
        tree_info = font.render("This is a Tree!", True, (0, 255, 0))
        tree_info2 = font.render(
            "Trees dont get old! there are trees that are 5,000 years old!", True,
            (0, 255, 0))
        screen.blit(tree_info, (fontX, fontY))
        screen.blit(tree_info2, (fontX, fontY + 30))

    if apple_clicked:
        interaction = True
        info_box()
        x_button()
        tree_clicked = False
        # Apple Movement
        appleY += appleY_change
        if appleY >= 350:
            appleY_change = 0
        apple_info = font.render("This is an Apple!", True, (255, 0, 0))
        apple_info2 = font.render("One apple has around 6-10 apple seeds!", True, (255, 0, 0))
        screen.blit(apple_info, (fontX, fontY))
        screen.blit(apple_info2, (fontX, fontY + 30))

    if grape_clicked:
        interaction = True
        info_box()
        x_button()
        # grape movement
        grapeY += grapeY_change
        if grapeY >= 350:
            grapeY_change = 0
        tree_clicked = False
        grape_info = font.render("These are grapes!", True, (128, 0, 128))
        grape_info2 = font.render("There are more than 8,000 varieties of grape!", True, (128, 0, 128))
        screen.blit(grape_info, (fontX, fontY))
        screen.blit(grape_info2, (fontX, fontY + 30))

    if pear_clicked:
        interaction = True
        info_box()
        x_button()
        # Pear movement
        pearY += pearY_change
        if pearY >= 350:
            pearY_change = 0
        tree_clicked = False
        pear_info = font.render("This is a Pear!", True, (144, 238, 144))
        pear_info2 = font.render("Pears used to be called “butter fruit” for their soft, butter-like texture.!", True,
                                 (144, 238, 144))
        screen.blit(pear_info, (fontX, fontY))
        screen.blit(pear_info2, (fontX, fontY + 30))

    if banana_clicked:
        interaction = True
        info_box()
        x_button()
        # banana movement
        bananaY += bananaY_change
        if bananaY >= 350:
            bananaY_change = 0
            bnnIMG = bnn2
        tree_clicked = False
        bnn_info = font.render("This is a Banana!", True, (255, 255, 153))
        bnn_info2 = font.render("Humans share 50% of our DNA with bananas!", True,
                                (255, 255, 153))
        screen.blit(bnn_info, (fontX, fontY))
        screen.blit(bnn_info2, (fontX, fontY + 30))

    if cherries_clicked:
        interaction = True
        info_box()
        x_button()
        cherriesY += cherriesY_change
        if cherriesY >= 350:
            cherriesY_change = 0
        tree_clicked = False
        chr_info = font.render("These are Cherries!", True, (220, 20, 60))
        chr_info2 = font.render("The word 'cherry' comes from the Turkish town of Cerasus!", True,
                                (220, 20, 60))
        screen.blit(chr_info, (fontX, fontY))
        screen.blit(chr_info2, (fontX, fontY + 30))

    if cat_clicked:
        interaction = True
        info_box()
        x_button()
        catIMG = cat3_normal
        cat_info = font.render("This is a Cat!", True, (70, 130, 180))
        cat_info2 = font.render("Cats are very flexible animals and can jump very high!", True,
                                (70, 130, 180))
        screen.blit(cat_info, (fontX, fontY))
        screen.blit(cat_info2, (fontX, fontY + 30))

    if dog_clicked:
        interaction = True
        info_box()
        x_button()
        dogIMG = dog3_normal
        dog_info = font.render("This is a Dog!", True, (188, 143, 143))
        dog_info2 = font.render("Dogs have incredible hearing!", True,
                                (188, 143, 143))
        screen.blit(dog_info, (fontX, fontY))
        screen.blit(dog_info2, (fontX, fontY + 30))

    if fox_clicked:
        interaction = True
        info_box()
        x_button()
        tree_clicked = False
        foxIMG = fox2_normal
        fox_info = font.render("This is a Fox!", True, (255, 69, 0))
        fox_info2 = font.render("Foxes can make over 40 different sounds!", True,
                                (255, 69, 0))
        screen.blit(fox_info, (fontX, fontY))
        screen.blit(fox_info2, (fontX, fontY + 30))

    if cow_clicked:
        interaction = True
        info_box()
        x_button()
        cow_info = font.render("This is a Cow!", True, (112, 128, 144))
        cow_info2 = font.render("Cows have great memories!", True,
                                (112, 128, 144))
        screen.blit(cow_info, (fontX, fontY))
        screen.blit(cow_info2, (fontX, fontY + 30))

    if turtle_clicked:
        interaction = True
        info_box()
        x_button()
        trtl_info = font.render("This is a Turtle!", True, (124, 252, 0))
        trtl_info2 = font.render("Turtles have a long lifespan!", True,
                                 (124, 252, 0))
        screen.blit(trtl_info, (fontX, fontY))
        screen.blit(trtl_info2, (fontX, fontY + 30))

    if rooster_clicked:
        interaction = True
        info_box()
        x_button()
        rstr_info = font.render("This is a Chicken!", True, (245, 245, 245))
        rstr_info2 = font.render("Chickens are living descendants of dinosaurs!", True,
                                 (245, 245, 245))
        screen.blit(rstr_info, (fontX, fontY))
        screen.blit(rstr_info2, (fontX, fontY + 30))

    # Bird Movement
    birdX += birdX_change
    if birdX <= -100:
        if bird_reset_timer is None:
            bird_reset_timer = time.time() + 10
        elif time.time() > bird_reset_timer:
            birdX = 850
            bird_reset_timer = None

    # Calculate the total number of unique objects explored
    total_explored = sum(object_states.values())
    total_possible_objects = 14

    # Display number of explored objects on the screen
    counter_text = f"Explored: {total_explored}/{total_possible_objects}"
    counter_surface = counter_font.render(counter_text, True, (255, 255, 255))
    screen.blit(counter_surface, counter_text_pos)

    # Check if all objects have been explored
    if total_explored == total_possible_objects:
        show_star = True

    if show_star:
        screen.blit(star_image, (starX, starY))

    fox(fox_X, fox_Y)
    flower(flowerX, flowerY)
    bird(birdX, birdY)
    tree(treeX, treeY)
    apple(appleX, appleY)
    grape(grapeX, grapeY)
    pear(pearX, pearY)
    banana(bananaX, bananaY)
    cherries(cherriesX, cherriesY)
    cat(catX, catY)
    dog(dogX, dogY)
    cow(cowX, cowY)
    turtle(turtleX, turtleY)
    rooster(roosterX, roosterY)
    pygame.display.update()
