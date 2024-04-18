def start_quiz(current_question=0):
    screen.fill((255, 255, 255))  # Fill the screen with white color

    questions = [
        {"question": "Which fruit used to be called 'butter-fruit'?", "choices": ["Apple", "Pear", "Grapes"],
         "correct_answer": "2"},
        {"question": "which animal is the most flexible out of these?", "choices": ["dog", "cow", "cat"],
         "correct_answer": "3"},
        {"question": "which plant does not get old?", "choices": ["Tree", "Flower", "Bird"], "correct_answer": "1"},
        {"question": "which animal has 10,000 species?", "choices": ["Bird", "chicken", "fox"], "correct_answer": "1"},
        {"question": "which animal can make over 40 sounds?", "choices": ["dog", "cow", "fox"], "correct_answer": "3"}

    ]

    question_font = pygame.font.Font('freesansbold.ttf', 30)
    question_text = question_font.render(questions[current_question]["question"], True, (0, 0, 0))
    screen.blit(question_text, (50, 50))

    correct_answers = 0  # Counter for correct answers

    # Choices
    choice_font = pygame.font.Font('freesansbold.ttf', 24)

    choice1_text = choice_font.render(f"1. {questions[current_question]['choices'][0]}", True, (0, 0, 0))
    screen.blit(choice1_text, (50, 150))

    choice2_text = choice_font.render(f"2. {questions[current_question]['choices'][1]}", True, (0, 0, 0))
    screen.blit(choice2_text, (50, 200))

    choice3_text = choice_font.render(f"3. {questions[current_question]['choices'][2]}", True, (0, 0, 0))
    screen.blit(choice3_text, (50, 250))

    pygame.display.update()

    # Quiz loop
    quiz_running = True
    while quiz_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                correct_answer = questions[current_question]['correct_answer']
                if event.key == pygame.K_1:
                    if correct_answer == "1":
                        correct_answers += 1
                    else:
                        print("Incorrect! You chose", questions[current_question]['choices'][0])
                        main_menu()
                        return
                elif event.key == pygame.K_2:
                    if correct_answer == "2":
                        correct_answers += 1
                    else:
                        print("Incorrect! You chose", questions[current_question]['choices'][1])
                        main_menu()
                        return
                elif event.key == pygame.K_3:
                    if correct_answer == "3":
                        correct_answers += 1
                    else:
                        print("Incorrect! You chose", questions[current_question]['choices'][2])
                        main_menu()
                        return

                current_question += 1  # Move to the next question

                if current_question < len(questions):
                    # Load the next question
                    screen.fill((255, 255, 255))  # Clear the screen
                    question_text = question_font.render(questions[current_question]["question"], True, (0, 0, 0))
                    screen.blit(question_text, (50, 50))

                    # Render choices for the next question
                    choice1_text = choice_font.render(f"1. {questions[current_question]['choices'][0]}", True,
                                                      (0, 0, 0))
                    screen.blit(choice1_text, (50, 150))

                    choice2_text = choice_font.render(f"2. {questions[current_question]['choices'][1]}", True,
                                                      (0, 0, 0))
                    screen.blit(choice2_text, (50, 200))

                    choice3_text = choice_font.render(f"3. {questions[current_question]['choices'][2]}", True,
                                                      (0, 0, 0))
                    screen.blit(choice3_text, (50, 250))

                    pygame.display.update()

                else:
                    if correct_answers == len(questions):
                        global star2  # Access the global variable
                        star2 = True  # Set star2 to True to display the star
                        break

                    else:
                        pygame.quit()  # Exit the game when all questions are answered incorrectly

