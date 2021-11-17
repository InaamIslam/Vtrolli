# MY PROJECT WEEK 5: *VTROLLI*
My Project. To create a CRUD application with utilisation of supporting tools, methodologies and technologies that encapsulate all core modules covered during training.

The application is a click and collect service which allows you to create an order at your local butchers. You may also update and delete the order after having processed it. 

# Virtual Trolley Application (VTROLLI)
# Author
## Inaam Islam
[Fundamental Proejct Presentation]

## Contents
- [Brief](#brief)
    - [Objective](#obj)
    - [Requirements](#reqs)
    - [Project Approach](#approach)
- [Architecture](#arch)
    - [Entity Relationship Diagrams](#erd)
- [CI Pipeline](#ci)
- [Project Planning & User Stories](#use_case)
- [Testing](#test_)
- [Deployment](#depl)
- [Technologies used](#tech)
- [Risk Assessment](#risks)
    - [Explanation](#risk-exp)
- [Front end Design](#FE)
    - [Page: Home](#home)
    - [Page: Add Series name](#addSN)
    - [Page: Review Series](#revS)
    - [Page: View Review](#virev)
- [Future Improvements](#improve)

<a name="breif"></a>
## Breif

<a name="obj"></a>
### Objective
The objective of the DevOps Core Fundamental Project is to create a CRUD application with utilisation of supporting tools,
methodologies and technologies that encapsulate all core modules we have covered up until week 5 of the Training Academy.

Core concepts to involve:
- **Project Management**
- **Python Fundamentals**
- **Python Testing**
- **Git**
- **Basic Linux**
- **Python Web Development**
- **Continuous Integration**
- **Cloud Fundamentals**
- **Databases**

<a name="reqs"></a>
### Requirements 
- A Trello board (or equivalent Kanban board tech) with full expansion
on user stories, use cases and tasks needed to complete the project.
It could also provide a record of any issues or risks that you faced
creating your project.
- A relational database used to store data persistently for the
project, this database needs to have at least 2 tables in it, to
demonstrate your understanding, you are also required to model a
relationship.
- Clear Documentation from a design phase describing the architecture
you will use for you project as well as a detailed Risk Assessment.
- A functional CRUD application created in Python, following best
practices and design principles, that meets the requirements set on
your Kanban Board
- Fully designed test suites for the application you are creating, as
well as automated tests for validation of the application. You must
provide high test coverage in your backend and provide consistent
reports and evidence to support a TDD approach.
- A functioning front-end website and integrated API's, using Flask.
- Code fully integrated into a Version Control System using the
Feature-Branch model which will subsequently be built through a CI
server and deployed to a cloud-based virtual machine.

<a name="approach"></a>
### Project Approach
My project focuses on creating a website where you can select products from a butchers, make purchases, update purchases and delete them.

This will consist of users being able to: 

- Create a on online trolley and name it
    -**Title** 

- Create and add items to each trolley created
    

<a name="arch"></a>
## Architecture
<a name="erd"></a>
### Entity Relationship Diagrams (ERD)
#### Plan

Below is shown ERD table for the project. My project will be connected to a GCP hosted MySQL server which will store the name of the trolley and the items within it.


This will allow anyone to Create, Read, Update and Delete from the database.
 

git config --global  user.email "Inaam.islaam@gmail.com"
git config --global user.name "Inaam Islam"
