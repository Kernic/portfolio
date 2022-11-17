#! /usr/bin/python
# This file is the main file of the project, it has to do :
# 		- Get the most up to date dataset 
# 		- Create the Dash pages 
from DashBase import application


if __name__ == "__main__":
	application.run(host='0.0.0.0', port='8080')
