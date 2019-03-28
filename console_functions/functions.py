import os, shutil, builtins
from termcolor import colored, cprint
from pick import pick

class console():
	#init code, define constants
	os.system('color')
	t_width = shutil.get_terminal_size((80, 20)).columns #Get terminal width

	#Define default colors
	default_text_color = "white" # set default text color for normal text
	default_important_color = "blue" # set default color for 'important' text, like headers
	default_special_color = "cyan" # set default color for 'special' text like variable names and whatnot
	default_input_color = "green" # set default color for printing string before user input
	default_warn_color = "yellow" # set default color for warning messages
	default_error_color = "red" # set default color for error messages

	default_input_prepend = "*" # add a number of spaces/text/whatever before input
	default_variable_prepend = "   " #add text before .variable(":dasdasd", var) prints out

	#Prints to the console. Alignment can be center. Fill is a character to fill empty space with
	@classmethod
	def log (cls, text, color=None, alignment=None, fill_char=None) :
		
		#If user wants text centered
		if alignment == "center" :
			#Print fill char if user wants
			if fill_char is None :
				text = ('{:^'+ str(cls.t_width) +'}').format(text)
			else:
				text = ('{:' + fill_char +'^'+ str(cls.t_width) +'}').format(text)

		#set color to white if not defined
		if color is None : color = 'white'

		cprint(text, color)

	#Prints a warning message
	@classmethod
	def warn (cls, text) :
		cls.log(text, cls.default_warn_color)

	#Prints an error message
	@classmethod
	def error (cls, text) :
		cls.log(text, cls.default_error_color)

	#Prints an special message
	@classmethod
	def special (cls, text) :
		cls.log(text, cls.default_special_color)

	#Prints an important message
	@classmethod
	def important (cls, text) :
		cls.log(text, cls.default_important_color)


	#Prints a string normally then colors the variable passed in
	@classmethod
	def variable (cls, text, variable) :
		cprint(cls.default_variable_prepend + text, "white", end="")
		cprint(variable, cls.default_special_color)

	#Prints a prompt for an input
	@classmethod
	def input_prompt(cls, text, color=None):
		if color is None : color = cls.default_input_color #set color to default input color if not defined
		cprint(cls.default_input_prepend + text, color, end="")

	#Create a new input function that allows for colored prompts
	@classmethod
	def input (cls, text, default_value=None, allow_empty=False, color=None) :
		# Prompt and get input
		if default_value is not None : #Add default value to prompt, if provided
			cls.input_prompt(text + " (" + default_value + ") ", color) # Add text indicating there is a default value user can hit enter to select
			response = builtins.input()
		else:
			cls.input_prompt(text, color)
			response = builtins.input()

		#Use default value if exists and no repsonse provided from user
		if response is None or len(response) == 0 and default_value is not None: response = default_value # if user just hits enter, we will use the default value
		
		#Handle empty input if a user MUST provide a value to continue and there is no default
		if response is None or len(response) == 0 and default_value is None and allow_empty == False:
				cls.warn("Input is required. Please input a value.")
				return cls.input(text, default_value, allow_empty, color)

		return response

	#Allows a user to select from a list
	@classmethod
	def input_list(cls, text, values, multi=False, allow_empty=False, color=None):
		cls.input_prompt(text, color) # Prompt user

		#Set up pick
		options = values
		option, index = pick(options, text)

		return index 

	#Prints a big header to the console. Like this:
	#---------------------------------------------------
	#                       text
	#---------------------------------------------------
	@classmethod
	def header (cls, text, text_color=None, accent_color=None, accent_char=None) :
		if accent_char is None:
			accent_char = "-"

		#set colors to default if not defined
		if text_color is None : color = cls.default_important_color
		if accent_color is None : accent_color = cls.default_important_color

		#Log row of accent chars
		cls.log("", accent_color, "center", accent_char)
		
		#If text is a list, print each line
		if isinstance(text, list):
			for row in text:
				cls.log(row, text_color, "center", "")
		else:
			cls.log(text, text_color, "center", "")

		#Log row of accent chars
		cls.log("", accent_color, "center", accent_char)
