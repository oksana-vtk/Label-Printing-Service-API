
# Label Printing Service API (Flask API for Printing Stickers)

This is a Flask-based API service for generating and printing custom label stickers using a `barcode label printer`.
This service was developed for a chatbot to automate the gift processing workflow during a promotion event. 
Users scanned a QR code, the chatbot forwarded gift type and customer ID parameters to this Label Printing Service API, 
and labels were generated and printed automatically for each customer and their corresponding gift.


## Features

- Generates sticker templates (including client's information) using a pre-configured sample
- Sends templates to a network barcode label printer via IP
- Logs all requests and responses into a logfile with timestamps.
- Easy configuration using `.env`

## Technologies

- Python 3.8+
- Flask
- python-dotenv
- REST-API
- TSPL (TSC Printer Language)

## Notes

- A pre-configured BMP image file named "sticker.bmp" must be present in the working directory 
for the printer template to work.


