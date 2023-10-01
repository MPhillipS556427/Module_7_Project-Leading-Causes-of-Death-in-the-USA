"""This script reads data from a CSV file containing information about causes of death. 
The data includes details like the year of the cause, formal and informal cause names, state, number of deaths, and age-adjusted death rate. 
The script establishes a connection to a RabbitMQ server running on localhost and declares three queues: 'DeathQueue1', 'DeathQueue2', and 'DeathQueue3'. 
It then processes the CSV data and sends specific rows to these queues based on conditions.

Author: Malcolm Phillip
Date: 10/01/2023
"""

import csv
import webbrowser
import pika

# Set show_offer based on your logic
show_offer = True

def offer_rabbitmq_admin_site(host, port):
    """
    Open the RabbitMQ Admin website without asking
    Parameters:
        host (str): this is the localhost
        port (int): this is RabbitMQ UI default port
    """
    global show_offer
    if show_offer:
        url = f"http://{host}:{port}/#/queues"
        webbrowser.open_new(url)
        print()

# Establish RabbitMQ connection and create a channel
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# Declare queues if not already declared
channel.queue_declare(queue='DeathQueue1')
channel.queue_declare(queue='DeathQueue2')
channel.queue_declare(queue='DeathQueue3')

# Send message to a queue
def send_message_to_queue(data, queue_name):
    # Publish message to the specified queue
    channel.basic_publish(exchange='', routing_key=queue_name, body=data)
    print(f"Sent to {queue_name}: {data}")

# Mock function to process CSV data
def process_death_data(row):
    # Extract data from CSV row
    year_of_cause, formal_cause, informal_cause, state, num_deaths, age_adjusted_rate = row
    data = f"{year_of_cause},{formal_cause},{informal_cause},{state},{num_deaths},{age_adjusted_rate}"
    
  # Sending data to the queue based on specific conditions
    if formal_cause == 'Heart Disease':
        send_message_to_queue(data, 'DeathQueue1')
        
    elif num_deaths.isdigit() and int(num_deaths) > 1000:
        send_message_to_queue(data, 'DeathQueue2')
        
    elif state == 'California' and float(age_adjusted_rate) < 10:
        send_message_to_queue(data, 'DeathQueue3')

# Producer function to read data from the CSV file and process it
def producer():
    # Open the CSV file
    with open('leading_cause_death.csv', 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip header row
        # Process each row of the CSV file
        for row in csv_reader:
            process_death_data(row)

if __name__ == '__main__':
    try:
        # Open RabbitMQ Admin site
        offer_rabbitmq_admin_site('localhost', 15672)  # Assuming RabbitMQ UI port is 15672

        # Start the producer
        producer()
    except KeyboardInterrupt:
        print("\nSafely exiting...")
    finally:
        # Close the RabbitMQ connection
        connection.close()
