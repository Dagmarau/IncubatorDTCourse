import pika
def get_connection():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    return connection

def send_message(message):
    connection = get_connection()
    channel = connection.channel()

    # Declare a queue
    channel.queue_declare(queue='hello')

    # Publish a message to the queue
    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body=message)
    print(f" besked: {message}")
    connection.close()

# Loop der sender x antal beskeder:
for i in range(5):
    send_message(f"spændende {i+1}")  # kan også slette {i+1}, så er alle beskedene bare "spændende". +1 gør at den starter med 1

# Test sending a message (sender 1 besked):
send_message("så er det nu!")

# et loop med x antal beskeder på x sekunder:
import time
for i in range(5):
    send_message(f"Yay det ruller #{i+6}")
    time.sleep(0.5) # sender én besked pr. (x) sekunder

import time     
i = 1               # starter tælleren ved 1
while True: 
    send_message(f"og fortsætter for evigt #{i+10}") 
    i += 1          # tælleren stiger med 1 for hver besked
    time.sleep(1)   # sender én besked pr. (x) sekunder
    # for at stoppe: tryk Ctrl + C i terminalen



