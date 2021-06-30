# coding: utf-8

# ––––––––––––––––––––––––––––––––––––––––––––––––– IMPORT LIBRARIES –––––––––––––––––––––––––––––––––––––––––––––––– #

from flask import Flask
from flask import render_template
import socket
import random
import os
import argparse

# ––––––––––––––––––––––––––––––––––––––––––––––––– GLOBAL VARIABLES –––––––––––––––––––––––––––––––––––––––––––––––– #

app = Flask(__name__)

color_codes = {
	"red": "#e74c3c",
	"green": "#16a085",
	"blue": "#2980b9",
	"pink": "#be2edd",
}

SUPPORTED_COLORS = ",".join(color_codes.keys())

# Get color from Environment variable
COLOR_FROM_ENV = os.environ.get('APP_COLOR')
# Generate a random color
COLOR = random.choice(["red", "green", "blue", "pink"])

# –––––––––––––––––––––––––––––––––––––––––––––––––– MAIN FUNCTION –––––––––––––––––––––––––––––––––––––––––––––––––– #

@app.route("/")
def main():
	return render_template("index.jinja2", name=socket.gethostname(), color=color_codes[COLOR])

# ––––––––––––––––––––––––––––––––––––––––––––––––––– MAIN GUARD –––––––––––––––––––––––––––––––––––––––––––––––––––– #

if __name__ == "__main__":

	print("This \"test_docker_app\" is a Flask web app that can display differnt colored backgrounds.\n"
		"\t– Accepts one of " + SUPPORTED_COLORS + " \n"
		"\t– You can specify the background color for the app in one of two ways: \n"
		"\n"
		"1. Use the \"--color=<color>\" command line argument while using \"$ docker run\".\n" 
		"2. Specify the environment variable \"APP_COLOR=<color>\" while using \"$ docker run -e\".\n"
		"\n"
		"NOTE: The command line argument takes precedence over the environment variable. If a color is not specified with a command line argument or the environment variable, a random color from the supported list will be chosen.\n"
		"\n")

	# Check for command line arguments for background color
	parser = argparse.ArgumentParser()
	parser.add_argument('--color', required=False)
	args = parser.parse_args()

	if args.color:
		print("Color from command line is " + args.color)
		COLOR = args.color
		if COLOR_FROM_ENV:
			print("A color was also set through the APP_COLOR environment variable as " + COLOR_FROM_ENV + ". However, the color from the command line takes precendence.")
	elif COLOR_FROM_ENV:
		print("No command line argument. Color from the APP_COLOR environment variable is " + COLOR_FROM_ENV)
		COLOR = COLOR_FROM_ENV
	else:
		print("No command line argument or environment variable. Picking a random color as " + COLOR)

	# Check if input color is a supported one
	if COLOR not in color_codes:
		print("Color not supported. Received '" + COLOR + "', but expected one of " + SUPPORTED_COLORS)
		exit(1)

	# Run Flask application
	app.run(host="0.0.0.0", port=5000)

# ––––––––––––––––––––––––––––––––––––––––––––––––––––––– EOF ––––––––––––––––––––––––––––––––––––––––––––––––––––––– #