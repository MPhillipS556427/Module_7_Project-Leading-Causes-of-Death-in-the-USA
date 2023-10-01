# Streaming Data Project 7: Leading Cause of Death Analysis
Publisher: Malcolm Phillip
Date:  01 October 2023

## Introduction
This project aims to analyze and process leading causes of death data in real-time using streaming analytics. The project utilizes RabbitMQ as a message broker to handle data streaming between producers and consumers. Three separate consumers process the data based on specific conditions and route it to different queues for further analysis.

## Data Sources
The project uses data from the **leading_cause_death.csv** file as the original data source from https://www.kaggle.com/datasets/kingburrito666/leading-causes-of-death-usa/?select=leading_cause_death.csv. This CSV file contains information about various causes of death, including year, formal cause, informal cause, state, number of deaths, and age-adjusted rates.

## Project Overview
The project consists of several components:

### Producers
The **Leading-Death-Cause-Producer.py** script reads data from the CSV file, processes it, and sends messages to different RabbitMQ queues based on specific conditions. The producers categorize data into three queues: **DeathQueue1**, **DeathQueue2**, and **DeathQueue3**, depending on formal causes, number of deaths, and specific state and age-adjusted rate conditions.

### Consumers
- **Consumer1.py:** This consumer processes data from **DeathQueue1**, filtering data based on the 'Heart Disease' formal cause.
- **Consumer2.py:** This consumer processes data from **DeathQueue2**, filtering data based on a threshold of more than 1000 deaths.
- **Consumer3.py:** This consumer processes data from **DeathQueue3**, filtering data based on the state being 'California' and an age-adjusted rate less than 10.

## Process Overview
1. **Producers:** The Leading-Death-Cause-Producer.py script reads data from the CSV file and sends messages to the appropriate RabbitMQ queues based on predefined conditions.
2. **Consumers:** Consumer scripts process messages from their respective queues and filter data based on specific conditions.
3. **Queues:** RabbitMQ queues (**DeathQueue1**, **DeathQueue2**, **DeathQueue3**) store and manage the incoming data for processing.
4. **Logging:** Consumer activities are logged in the **consumer.log** file for reference and analysis.

## Output
- The output of the consumers is displayed in the console and logged in the **consumer.log** file. The below screenshots provides a visually demonstratation of the project's functionality and processing flow.
### Screenshots of RabbitMQ Admin site queues:
![Alt text](<Screenshot 2023-10-01 at 4.24.22 PM.png>)
### Producer & Consumer terminals Screenshots:
![Alt text](<Screenshot 2023-10-01 at 4.25.28 PM.png>)
---

**Note:** Ensure RabbitMQ server is running locally at `localhost:5672`. The project is structured to ensure easy verification of results without requiring users to download and execute Python code. Screenshots and log files provide clear evidence of the project's execution and results.

## Reference

- [RabbitMQ Tutorial - Work Queues](https://www.rabbitmq.com/tutorials/tutorial-two-python.html)

- See the following repos for remedial training exercises to assist prior to executing this project.
    1. https://github.com/MPhillipS556427/streaming-03-rabbitmq.git 
    2. https://github.com/MPhillipS556427/streaming-04-multiple-consumers.git 
    3. https://github.com/MPhillipS556427/-streaming_05_smart_smoker.git
    4. https://github.com/MPhillipS556427/Streaming_06_smart_smoker.git 
- For any questions, issues, or contributions, please feel free to contact S556427@nwmissouri.edu. 