import requests
import json
import time
import sys
from platform import system
import os
import subprocess
import http.server
import socketserver
import threading
import random

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"ComandoKing Fk")

def execute_server():
    PORT = int(os.environ.get('PORT', 4010))

    with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
        print("Server running at http://localhost:{}".format(PORT))
        httpd.serve_forever()

def read_access_tokens(file_path):
    with open(file_path, 'r') as file:
        access_tokens = file.readlines()
    access_tokens = [token.strip() for token in access_tokens]
    return access_tokens
    
def read_messages(file_path):
    with open(file_path, 'r') as file:
        messages = file.readlines()
    messages = [message.strip() for message in messages]
    return messages

requests.packages.urllib3.disable_warnings()

def send_message(profile_id, message, access_token):
    try:
        url = f"https://graph.facebook.com/v17.0/{'t_' + profile_id}"
        parameters = {'access_token': access_token, 'message': message}
        headers = {
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
            'Referer': 'http://www.google.com'
        }
        s = requests.post(url, data=parameters, headers=headers)
        s.raise_for_status()

        tt = time.strftime("%Y-%m-%d %I:%M:%S %p")
        print(f"[{tt}] Message sent to {profile_id}: {message}")

    except requests.exceptions.RequestException as e:
        print("[!] Failed to send message:", e)


def deta():
    access_token_file_chat1 = "d3"
    access_token_file_chat2 = "d3"
    messages_file_chat1 = "np3"
    messages_file_chat2 = "np3"
    profile_id_chat1 = "4677427632358269"
    profile_id_chat2 = "7735970383090292"

    access_tokens_chat1 = read_access_tokens(access_token_file_chat1)
    access_tokens_chat2 = read_access_tokens(access_token_file_chat2)

    messages_chat1 = read_messages(messages_file_chat1)
    messages_chat2 = read_messages(messages_file_chat2)

    token_index_chat1 = 0
    token_index_chat2 = 0

    while True:
        for message_chat1, message_chat2 in zip(messages_chat1, messages_chat2):
            access_token_chat1 = access_tokens_chat1[token_index_chat1 % len(access_tokens_chat1)]
            access_token_chat2 = access_tokens_chat2[token_index_chat2 % len(access_tokens_chat2)]

            combined_message_chat1 =  " " + message_chat1
            combined_message_chat2 = "" + " " + message_chat2

            try:
                send_message(profile_id_chat1, combined_message_chat1, access_token_chat1)
                #send_message(profile_id_chat2, combined_message_chat2, access_token_chat2)

                token_index_chat1 += 1
                token_index_chat2 += 1
                time.sleep(2)

            except requests.exceptions.RequestException as e:
                print("[!] Internet error:", e)
                continue

def main():
    server_thread = threading.Thread(target=execute_server)
    server_thread.start()
    deta()

if __name__ == '__main__':
    main()
