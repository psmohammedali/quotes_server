import logo
from termcolor import colored
import argparse

# Command line argument input
parser = argparse.ArgumentParser()
parser.add_argument('-n','--name', type=str, required=True, help="Enter your name for customized output")
# print(parser)
args = parser.parse_args()
print(colored(logo.logo_name, "cyan"))
welcome_format = colored(logo.welcome_head.format(args.name), "red", attrs=["bold"])
print(welcome_format)







