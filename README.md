
# Label Printing Service API (Flask API for Printing Stickers)

This is a Flask-based API service for generating and printing custom label stickers using a network printer over IP.
This service was used in a special chatbot to automate the gift processing workflow during a promotion event. 
It enabled scanning of QR codes, transferring gift type and customer ID parameters 
and sending this information to a server to generate and print stickers for each customer and their corresponding gift.

## Features

- Generates sticker templates (including client's information) using a pre-configured sample
- Sends templates to a network printer via IP
- Logs all requests and responses into a logfile with timestamps.
- Easy configuration using `.env`

## Technologies

- Python 3.8+
- Flask
- python-dotenv
- REST-API

## Notes

- A pre-configured BMP image file named "sticker.bmp" must be present in the working directory 
for the printer template to work.


