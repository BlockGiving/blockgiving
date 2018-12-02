### Colony Hackathon Submission
<!-- Fill this out now to RSVP. You can always come back and edit it when info changes. -->
<!-- You *don't* need to delete all the comments like this one since they won't show up in the viewer. -->
<!-- Use your project name as the title of this issue. This is what we’ll call your winning project! -->


**A decentalized, self-perpuating, cross-border giving network on top of COLONY**
<!--(Please also add it above ^^ as the title of this issue)-->

---

**Project Description**
<!--(1-2 sentences about this project. Motivations, goals, functionality -- you name it.)-->

## Goal:
To create a self-perpetuating, decentralized, cross-borders, Giving Platform.

## Overview:

We aim to create a platform where users can create projects, work on projects and fund projects to help people around the globe.
By the nature of design of the platform, there is a complete transparency in the way the funding works and the way funds are disbursed.
People in the grassroots can directly take up tasks and get funded instantly for the service provided.
The community as a whole evaluates the task completion submissions and approves or disapproves it.

![alt text](https://raw.githubusercontent.com/blockgiving/blockGiving/master/colony/assets/flow.png)

## Problems with Large NGOs
* Donors don’t see the real impact of how their funds are getting used immediately. 
* Some donors might be more passionate about certain cause and he/she might not be willing to donate to a large NGO because he might feel his contributions are insignificant. But, by using our platform he/she can fund small Actions of Goodness and see the impact in a short time. 
* There is no transparency on how the funds are being disbursed

## The Solution   
* Allow anyone to Create Projects concerning a particular social issue(_Domains in Colony_) by staking ETH.
* Allow anyone to Create Actionable Tasks related to a particular project by staking ETH.
* Allow anyone to Take up tasks, submit proof of work in the form of images and videos
* Allows the Creators of the Tasks/Evaluators to validate tasks
* Do-ers claim funds after task validation and gets ETH directly into their wallet.
 
## You can access it live at http://localhost:8080/
* You should have MetaMask installed and connected to Rinkeby Test Network to view Project Funds and Create New Project.
* While funding New Project, Enter Atleast 0.1 ETH to Create a New Project.

##Our Hackathon Results
![alt text](https://raw.githubusercontent.com/blockgiving/blockGiving/master/colony/assets/rank.png)
[Judges comments][colony_judges_comments.md]

## Walkthrough
https://github.com/mdhalim/blockGiving/blob/master/BlockGivingDeck.pdf


## Setup
 - clone the repo
 - install python, pip and virtualenv
 - pip install django
 - cd colony
 - python manage.py makemigrations
 - python manage.py migrate
 - python runserver 0.0.0.0:8080
## Things to do
- Auto assign task to anyone through permissioned smart contract (similar to how Create Project smart contract)
- Task Validation/Submission front-end views left to be implemented due to deadline.
