# name: Kristen Mabry
# collaborators: Joy, Favour, Dasha
# newhangman.py
# plays a game of hangman with graphics

import getpass
from graphics import *

#makes a window and keeps it open
win = GraphWin("Hangman", 400,500)

#Scaffold code here
#make list of function for drawing each part of hangman
# list[mistakes]
def draw_scaffold():
	play_anchor = Point(200, 450)
	play_name = Text(play_anchor, "Let's play hangman!")
	play_name.draw(win)

	top_right_corner = Point(100,350)
	bottom_left_corner = Point(15,390)
	scaffold = Rectangle(top_right_corner, bottom_left_corner)
	scaffold.draw(win)

	top_of_pole = Point(57.5, 10)
	bottom_of_pole = Point(57.5, 350)
	pole = Line(top_of_pole, bottom_of_pole)
	pole.draw(win)

	left_horizontal = Point(57.5, 10)
	right_horizontal = Point(132.5, 10)
	horizontal = Line(left_horizontal, right_horizontal)
	horizontal.draw(win)

	top_down = Point(132.5, 10)
	bottom_down = Point(132.5, 30)
	down_line = Line(top_down, bottom_down)
	down_line.draw(win)

	word_box_top = Point(390, 10)
	word_box_bottom = Point(200, 100)
	word_box = Rectangle(word_box_top, word_box_bottom)
	word_box.draw(win)
	
	word_box_text_anchor = Point(295, 30)
	word_box_text_string = "Guessed Letters"
	word_box_text = Text(word_box_text_anchor, word_box_text_string)
	word_box_text.draw(win)

	win.getMouse()
	play_name.undraw()

# draw head
def draw_head():
	circ_center = Point(132.5, 60)
	circ_radius = 30
	head = Circle(circ_center, circ_radius)
	head_circle = head
	head.draw(win)
	return head_circle

# draw torso
def draw_torso():
	top_torso = Point(132.5, 90)
	bottom_torso = Point(132.5, 220)
	torso = Line(top_torso, bottom_torso)
	torso.draw(win)
	return torso

#Left Leg code here
def draw_left_leg():
	top_left_leg = Point(132.5, 220)
	bottom_left_leg = Point(90, 290)
	left_leg = Line(top_left_leg, bottom_left_leg)
	left_leg.draw(win)
	return left_leg

#Right Leg code here
def draw_right_leg():
	top_right_leg = Point(132.5, 220)
	bottom_right_leg = Point(175, 290)
	right_leg = Line(top_right_leg, bottom_right_leg)
	right_leg.draw(win)
	return right_leg

#Left Arm code here
def draw_left_arm():
	top_left_arm = Point(132.5, 120)
	bottom_left_arm = Point(100, 200)
	left_arm = Line(top_left_arm, bottom_left_arm)
	left_arm.draw(win)
	return left_arm

#Right Arm code here
def draw_right_arm():
	top_right_arm = Point(132.5, 120)
	bottom_right_arm = Point(165, 200)
	right_arm = Line(top_right_arm, bottom_right_arm)
	right_arm.draw(win)
	return right_arm
#Displays end message
def end_message(winner):
	end_message_anchor = Point(200, 250)
	end_message_string = "Great job, Player " + str(winner) + "!"
	end_message = Text(end_message_anchor, end_message_string)
	end_message.setSize(20)
	end_message.draw(win)
	return end_message

# Displays the word that's been guessed so far
def word_so_far(underscores, current_word_graphic):
	current_word_graphic.undraw()
	word_x = 200
	word_y = 450
	word_anchor = Point(word_x, word_y)
	word_string = underscores
	word = Text(word_anchor, word_string)
	word.setSize(18)
	word.draw(win)
	return word

#adds letters to the word box
def word_box(old_list, list_of_letters):
	old_list.undraw()
	list_anchor = Point(295, 55)
	letters = ""
	for x in list_of_letters:
		letters = letters + x + ", "
	list_text = Text(list_anchor, letters)
	list_text.setSize(10)
	list_text.draw(win)
	return list_text

draw_something = [draw_scaffold, draw_head, draw_torso, draw_right_leg, draw_left_leg, draw_right_arm, draw_left_arm]


# choose a word
def choose_new_word():
	play_anchor = Point(200, 450)
	play_name = Text(play_anchor, "Player 1, choose a word in the terminal.")
	play_name.draw(win)
	word = getpass.getpass("Player 1, choose a word")
	play_name.undraw()
	return word

#creates underscores

#guess a letter and check if letter has been guessed
def guess_letter(list_of_letters_guessed):
	#new_letter = raw_input("Player 2, guess a letter")

	graphics_input_box_anchor = Point(200, 400)
	graphics_input_box = Entry(graphics_input_box_anchor, 1)
	graphics_input_box.setText("")
	graphics_input_box.draw(win)
	
	win.getMouse()	
	new_letter = graphics_input_box.getText()
	graphics_input_box.undraw()

	if not new_letter in list_of_letters_guessed:
		list_of_letters_guessed.append(new_letter)
		guessed_already = False
	else:
		print("You've already guessed that letter. Try again.")
		guessed_already = True
	return list_of_letters_guessed, guessed_already

# replaces underscores with correctly guessed letters
def checking_letter_in_word(list_of_letters, word):
	letters_so_far = ""
	for letter in word:
		if letter in list_of_letters:
			letters_so_far = letters_so_far + " " + letter
		else:
			letters_so_far = letters_so_far + " _"
	return letters_so_far

# letter not in word
def incorrect_guess(list_of_letters, word, mistakes, guessed_already, current_shapes):
	last_letter = list_of_letters[-1]
	if not last_letter in word and not guessed_already:
		mistakes = mistakes+1
		print("Sorry, that's incorrect. You've now made " +str(mistakes) + " mistakes so far.")
		new_shape = draw_something[mistakes]()
		current_shapes.append(new_shape)
	return mistakes, current_shapes

# 6 mistakes
def end_game(mistakes, underscores, word):
	if mistakes == 6:
		game_over = True
		winner = 1
	elif not "_" in underscores:
		game_over = True
		winner = 2
	else:
		game_over = False
		winner = 0
	return game_over, winner

# keeps track of score
def new_score(winner, player_1_score, player_2_score):
	if winner == 1:
		player_1_score = player_1_score + 1
	elif winner == 2:
		player_2_score = player_2_score + 1
	return player_1_score, player_2_score


# play again
def play_again(old_word_box, shapes, end_message_text, current_word_graphic, player_1_score, player_2_score):
	
	score_anchor = Point(295, 120)
	score_string = "Scores"
	score_text = Text(score_anchor, score_string)
	score_text.draw(win)

	player_1_score_anchor = Point(295, 140)
	player_1_score_string = "Player 1: " + str(player_1_score)
	player_1_score_text = Text(player_1_score_anchor, player_1_score_string)
	player_1_score_text.draw(win)

	player_2_score_anchor = Point(295, 160)
	player_2_score_string = "Player 2: " + str(player_2_score)
	player_2_score_text = Text(player_2_score_anchor, player_2_score_string)
	player_2_score_text.draw(win)

	play_again_anchor = Point(200, 400)
	play_again_string = "Would you like to play again? (yes/no)"
	play_again_text = Text(play_again_anchor, play_again_string)
	play_again_text.draw(win)
		
	play_again_entry = Entry(Point(200, 430), 3)
	play_again_entry.setText("yes")
	play_again_entry.draw(win)
	win.getMouse()

	play_again = play_again_entry.getText()
	play_again_text.undraw()
	play_again_entry.undraw()
	score_text.undraw()
	player_1_score_text.undraw()
	player_2_score_text.undraw()

	if play_again == "yes":
		for body_part in shapes:
			body_part.undraw()
		current_word_graphic.undraw()
		end_message_text.undraw()
		old_word_box.undraw()
		play_hangman()

#asks the initial questions in the window before guessing letters
def starting_game():
	x = 1
	while x<3:
		player_1_anchor = Point(200, 400)
		player_1_string = "Player " + str(x) + ", what is your name?"
		player_1_text = Text(player_1_anchor, player_1_string)
		player_1_text.draw(win)
		
		player_1_entry = Entry(Point(200, 450), 15)
		player_1_entry.setText("Player " + str(x))
		player_1_entry.draw(win)
		win.getMouse()
		
		player_1_input = player_1_entry.getText()
		player_1_text.undraw()
		player_1_entry.undraw()
		
		player_1_name_anchor = Point(200, 450)
		player_1_name = Text(player_1_name_anchor, "Hello, " + player_1_input + "!")
		player_1_name.draw(win)
		win.getMouse()

		player_1_name.undraw()
		x = x+1
	

def play_hangman():
	
	gameover = False
	letters_guessed = []
	mistakes = 0
	draw_something[mistakes]()
	shapes = []
	current_word_graphic = Text(Point(0,0), "")
	old_word_box = Text(Point(0,0), "")
	

	current_word = choose_new_word()
	underscores = "_ "*len(current_word)
	current_word_graphic = word_so_far(underscores, current_word_graphic)
	
	while gameover == False:
		player_2_turn, guessed_already = guess_letter(letters_guessed)
		old_word_box = word_box(old_word_box, letters_guessed)
		word_shown = checking_letter_in_word(player_2_turn, current_word)
		print(word_shown)
		current_word_graphic = word_so_far(word_shown, current_word_graphic)
		mistakes, shapes = incorrect_guess(player_2_turn, word_shown, mistakes, guessed_already, shapes)	
		gameover, winner = end_game(mistakes, word_shown, current_word)
		
	end_message_text = end_message(winner)
	print("Game over! The word was " + current_word + ".")	
	print("Player " + str(winner) + " wins!")
	
	global player_1_score
	global player_2_score
	player_1_score, player_2_score = new_score(winner, player_1_score, player_2_score)
	print("Current score:")
	print("Player 1 has",player_1_score,"points.")
	print("Player 2 has",player_2_score,"points.")
	
	play_again(old_word_box, shapes, end_message_text, current_word_graphic, player_1_score, player_2_score)

starting_game()
player_1_score = 0
player_2_score = 0
play_hangman()
