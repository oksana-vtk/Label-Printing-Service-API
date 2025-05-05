# -*- coding: utf-8 -*-

from flask import Flask, request, jsonify
import socket
from datetime import datetime
import json
from dotenv import load_dotenv
import os


# Завантаження змінних з середовища .env
load_dotenv()
PRINTER_IP = os.getenv("PRINTER_IP")


# API
app = Flask(__name__)


# Функція надсилання даних на принтер
def send_to_printer(printer_ip, port, data):

    current_datetime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    try:
        with socket.create_connection((printer_ip, port), timeout=5) as printer:
            printer.sendall(data.encode())
        return True

    except Exception as e:
        print(f"{current_datetime} Error sending data to printer: {e}")
        return False


def generate_full_template(gifts, contact_id):

    number_of_stickers_in_set = 3

    template = f'SIZE 26 mm,18 mm\n' \
               f'GAP 3 mm,0 mm\n' \
               f'DIRECTION 1\n'

    # Generate commands for each set
    for i in range(len(gifts)):

        template += f'CLS\n' \
                    f'SOUND 5,200\n' \
                    f'PUTBMP 0,0,"sticker.bmp",1,100\n' \
                    f'TEXT 50,44,"3",0,2,2,0,"{gifts[i]["gift_number"]}"\n' \
                    f'TEXT 5,105,"2",0,1,1,0,"{contact_id} / {gifts[i]["gift_type"]}"\n' \
                    f'PRINT {number_of_stickers_in_set}\n'

    return template


# API_1 Документація в файлі API_DOC.md /label/print-sets
@app.route('/print-sets', methods=['POST'])
def print_sticker_sets():

    current_datetime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    # Параметри підключення принтеру
    #printer_ip = os.getenv("PRINTER_IP") - перенесено в глобальну змінну

    # Отримуємо дані з запиту
    request_data = request.json

    printer_port = request_data.get("printer")
    contact_id = request_data.get("contact_id")
    gifts = request_data.get("gifts")

    # Формуємо завдання для друку
    stickers_content = generate_full_template(gifts, contact_id)

    # Відправляємо на принтер
    if send_to_printer(PRINTER_IP, printer_port, stickers_content):

        status = {"code": 200,
                  "message": "Success: All stickers are printed."}

        with open("label_logs.log", "a", encoding="utf-8") as log_file:
            log_file.write(f"\n{current_datetime} API print_sets\n")
            log_file.write(f"Request_content: {json.dumps(request_data)}\n")
            log_file.write(f"Stickers_content: {json.dumps(stickers_content)}\n")
            log_file.write(f"Status: {json.dumps(status)}\n")

        return jsonify(status), 200

    else:

        status = {"code": 500,
                  "message": "Error: Failed to send to printer!"}

        with open("label_logs.log", "a", encoding="utf-8") as log_file:
            log_file.write(f"\n{current_datetime} API print_sets\n")
            log_file.write(f"Request_content: {json.dumps(request_data)}\n")
            log_file.write(f"Stickers_content: {json.dumps(stickers_content)}\n")
            log_file.write(f"Status: {json.dumps(status)}\n")
            
        return jsonify(status), 500


if __name__ == '__main__':
    app.run(debug=True)

