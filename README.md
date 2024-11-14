# FlightCal

## Overview

This is some work for my 2024 NCEA Level 2 Digitech Class at [Wainuiomata High School](https://wainuiomatahigh.school.nz/).

## Main Project (FlightCal)

FlightCal is a program designed for use by Travel Agents who wish to provide their customers the cost of a next-day flight through email. The program calculates the cost of the flight using the age, destination, and class (flight-wise) of the customer as well as the amount of seats remaining, and then provides a simple copy-pastable email for the Agent to send.
To the best of my ability I have followed pep8 and pep257 styling conventions for the python language to maximize readability and 

### Project Planning

To plan this project, I used Microsoft Planner (Kan-Ban Board) and a Gantt Chart in order to determine what I needed to do, and when to do it.
[](images/Opera%20Snapshot_2024-11-09_164043_planner.cloud.microsoft.png)
[](images/Screenshot%202024-11-14%20022343.png)
These helped me by allowing me to visualise my pending tasks and budget my time appropriately. 

I also created a flowchart to pre-configure the structure of my program:
[](images/flowchart.drawio.png)

### Development

During development I again used Microsoft Planner in order to track each subtask required.
I also used GitHub as my version control utility. As you probably can tell.
However, due to some issues with my account security and a slow response from GitHub Support I was unable to push or create commits for a long while. I still progressed further however despite this.

### Reflection

I believe that I did well in my planning and execution of my program. I accomplished and wrote everything I had planned for in my flowchart, even adding a database by the end for data storage. 

One flaw in my planning was that I didn't account for sudden interruptions such as my GitHub account issues. In future I need to prepare better for such eventualities. For example, I could host my own Gitea server and get that Git server to relay commits to GitHub every so often. This would decentralise and therefore improve the availability and accessibility of my code, as the GitHub links would be for simple sharing, and my server would be a perfect backup, being the intermediary between me and GitHub.
I also need to allot time between tasks in for program for such sudden interruptions.

Other than that however, I think I did a pretty good job of handling my development processes and sticking to my Gantt Chart.

### Relevant Implications

1. I have placed many error-catching algorithms within the program to increase the usability and functionality of the program. This is important because, in order to create a smooth service for both the customer and the travel agent, if the Travel Agent (User) enters an incorrect value or number, it's a good idea to cover your bases and watch out for human error. To give an example, in the program, for the client's flight class, I've set it so that numbers 1-4 correspond to a class which would be listed above simply for the user to enter. After the user's entry, it will check if the input can be converted to an integer, which would mean that the user did in fact input a number rather than text. It will then store this state in a boolean variable called `class_is_int`. While `class_is_int` is false AND the value of temp_class is either over 4 or under 1, it will keep re-prompting the user for values which conform to the program's requirements.
2. My program is sustainable and future-proofed. This is because the way my program is structured, it is not a waterfall model, and is instead a group of definitions and classes like `XMLHandler` that can easily be added to and modified. The modularity of my functions are a major key component for adding new features and improving older ones down the line. For example, if I wanted to add a feature which tells the user the time and closes, all I would need to do is create and define function which can read the time and print it, and then simply reference it as an option in the main definition. The modularity of the definitions and class structure is of utmost convenience in scenarios like that.

## Iteration Directory

[IterationDir](Iterations/README.md)
