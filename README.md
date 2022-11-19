![Site Logo](/assets/images/readme_title_white_background_small.png)
## Table of Contents
* [Purpose](#Purpose)
    * [Goals](#Goals)
    * [Audience](#Audience)
* [Features](#Features)
    * [Existing](#Existing)
    * [Left to Implement](#Left-to-Implement)
* [User Experience](#User-Experience-(UX))
    * [User Stories](#User-Stories)
    * [Scenarios](#Scenarios)
        * [Available IPs](#Available-IPs)
        * [Subnet range calculation](#Subnet-range-calculation)
        * [Generate IP within subnet range](#Generate-IP-within-subnet-range)
* [Design](#Design)
    * [Heroku](#Heroku)
    * [Limitations](Limitations)
* [Testing](#Testing)
    * [Technologies](Technologies)
        * [PEP8](#PEP8)
        * [Python](#Python)
    * [Testing Issues](#Testing-Issues)
* [Deployment](#Deployment)
    * [Project](#Project)
        * [Heroku App](#Heroku-App)
        * [Github Pages](#Github-Pages)
        * [Locally](#Locally)
        * [Fork](#Fork)
        * [Commands](#Commands)
* [Credits](#Credits)
    * [Content](#Content)
    * [Acknowledgements](#Acknowledgements)

## Purpose
This tools was developed to help Network Engineers on their daily operations, when facing some of the most common requests regarding subnetting.
With IP Subnetting tool the engineer will be able to determine the amount of available IP addresses or find how many subnets can be used within a network.
Currently the tool is limited for IPv4 but IPv6 may be developed in future releases.

This tool can be found [here](https://ip-subnetting.herokuapp.com/).

### Goals
* Provide a tool for IP subnetting calculations.
* Allow engineers to get answers for design or project requirements.
* Desmistifying IP subnetting (hard for juniors or less experienced engineers).
* Educational engagement in training sessions.

### Audience
* Help Desk Engineer
* IT Engineer
* Field Support Engineer
* Network Administrator
* Network Engineer
* Network Security Engineer
* Network Architect
* Network Specialist

[Table-of-Contents](#Table-of-Contents)

## Features
### Existing
### Left-to-Implement
This website has a few limitations as some errors were found while deploying JavaScript functions and DOM. These have not been fixed yet but are planned for the new release.
- adaptative quiz where the questions can be o any type (movie or song) but the type must change after a sequence of two with same type
- username requested at the beginning for the player name
- different levels of difficulty

[Table-of-Contents](#Table-of-Contents)

## User-Experience (UX)
The tool was created with support in mind as an application to help Network Engineers, either junior or senior.
IP subnetting is a task requiring proficiency for those engineers working in support or project.
### User Stories
- [support role] an engineer needs to calculate how many IP addresses are available for a certain network/mask in order to:
    a) troubleshoot an incident with a DHCP server 
    b) investigate a static IP assignement to a server in the network
    c) calculate maximum number of hosts for a certain network
- [architect role] an engineer needs to calculate the network and broadcast addresses of a customer to generate the HLD/LLD documentation
- [support role] an engineer needs to validate if an IP address is well defined for a certain network/mask (support role)
### Scenarios
#### Available IPs
- given a NETWORK and a MASK
- calculate number of HOSTS
#### Subnet range calculation
- given a NETWORK and a MASK
- identify the IP addresses for the SUBNET and BROADCAST
#### Generate IP within subnet range
- given a NETWORK and a MASK
- generate a RANDOM IP address within the subnet

[Table-of-Contents](#Table-of-Contents)

## Design
### Heroku
![main-page](/assets/images/heroku_main_page.PNG)
![input-page](/assets/images/heroku_input_page.PNG)
![options-page](/assets/images/heroku_options_page.PNG)

### Limitations
This tool has a potential for further features and capabilities but these are not yet implemented.
- can't provide a list of all possible subnets within a subnet scope (subnetting - network segmentation) 
- can't do supernetting (aggregation of subnets)
- this tool is not yet developed for IPv6

[Table-of-Contents](#Table-of-Contents)

## Testing
### Technologies
* GitPod - Online IDE [here](https://www.gitpod.io/).
* GitHub - Code and version control [here](https://github.com/).
* Heroku - Site deployment [here](https://dashboard.heroku.com/).
* W3Schools - Code reference for Python [here](https://www.w3schools.com/python/default.asp).

#### PEP8
![Run.py](/assets/images/pep8_checks.PNG)
#### Python
No syntax errors found.
### Testing-Issues
* Bugs identified that need to be fixed.
    * IP address and subnet mask validation not deployed (input values not validated)
    * menu cycle not working so there is no return to main page after results
    * menu options not working so new functions required to present the three scenarios

[Table-of-Contents](#Table-of-Contents)

## Deployment
### Project
This project site and tool was created using Heroku.
#### Heroku App
When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:
1. `heroku/python`
2. `heroku/nodejs`
You must then create a _Config Var_ called `PORT`. Set this to `8000`
If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.
Connect your GitHub repository and deploy as normal.
Constraints:
The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.
#### Github-Pages
Repository
1. Navigate to the GitHub [Repository:](https://github.com/baptistapaulo/pp1)
1. Click the 'Settings' Tab.
1. Scroll Down to the Git Hub Pages Heading.
1. Select 'Master Branch' as the source.
1. Click the Save button.
1. Click on the link to go to the live deployed page.
#### Locally
Clone
1. Navigate to the GitHub [Repository:](https://github.com/baptistapaulo/pp1)
1. Click the Code drop down menu.
1. Either Download the ZIP file, unpackage locally and open with IDE (This route ends here) OR Copy Git URL from the HTTPS dialogue box.
1. Open your developement editor of choice and open a terminal window in a directory of your choice.
1. Use the 'git clone' command in terminal followed by the copied git URL.
1. A clone of the project will be created locally on your machine.
#### Fork
Most commonly, forks are used to either propose changes to someone else's project to which you do not have write access, or to use someone else's project as a starting point for your own idea. You can fork a repository to create a copy of the repository and make changes without affecting the upstream repository.
So a fork is a copy of a repository. Forking a repository allows you to freely experiment with changes without affecting the original project.
1. Navigate to the GitHub Repository you want to fork.
1. On the top right of the page under the header, click the fork button.
1. Create a new fork.
1. This will create a duplicate of the full project in your GitHub Repository.
#### Commands
* `CTRL + S` was used to save the page.
* `CTRL + Z` was used to undo a change.
* `python3 -m http.server` was used to view and test site before pushing live.
* `git add` was used to add pages to the stage area.
* `git commit -m "fix: message here"` was used to comit them them to github and provide a relevant message to the changes that had been made.
* `git push` was used to push the changes upto Github for public viewing.

[Table-of-Contents](#Table-of-Contents)

## Credits
### Content
* [Code Institute](https://codeinstitute.net/ie/) course material, mainly the "Love Maths" Walkthrough.
* [StackOverflow](https://stackoverflow.com/questions)
* [Real Python](https://realpython.com/working-with-files-in-python/)
* [GeeksforGeeks](https://www.geeksforgeeks.org/python-program-to-validate-an-ip-address/)

### Acknowledgements
* Huge thank you to my mentor **Ronan McClelland** for his guidance throughout my project.

[Table-of-Contents](#Table-of-Contents)