"""This script establishes a connection to a RabbitMQ server, reads data from a CSV file, 
and sends the data to a RabbitMQ queue named 'DeathQueue1'. 
It also configures logging to record received messages and handles potential errors during message processing.

Author: Malcolm Phillip
Date: 10/01/2023
"""

import pika
import logging

# RabbitMQ configuration
rabbit_host = 'localhost'
rabbit_port = 5672  
queue_name = 'DeathQueue1'

# Establish a connection to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbit_host, port=rabbit_port))
channel = connection.channel()

# Declare the queue
channel.queue_declare(queue=queue_name)

# Configure logging
logging.basicConfig(filename='consumer.log', level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Callback function to handle incoming messages from the queue
def callback(ch, method, properties, body):
    try:
        # Split the message into individual data fields
        year, formal_cause, informal_cause, state, num_deaths, age_adjusted_rate = body.decode().split(',')
        # Log and print the received message
        message = f"Received data from {method.routing_key}: Year={year}, Formal Cause={formal_cause}, Informal Cause={informal_cause}, State={state}, Num Deaths={num_deaths}, Age-Adjusted Rate={age_adjusted_rate}"
        print(message)
        logger.info(message)
    except Exception as e:
        # Handle any errors that occur during message processing
        logger.error(f"Error processing message: {e}")

# Set up consumer
channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

if __name__ == '__main__':
    try:
        # Start consuming messages
        print(f"Consumer 1 started for queue: {queue_name}")
        channel.start_consuming()

    except KeyboardInterrupt:
        # Handle keyboard interrupt to exit the consumer safely
        print("\nSafely exiting...")
        connection.close()
