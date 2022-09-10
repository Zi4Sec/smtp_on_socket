'''
Sending smtp emails through socket programming
please do not use it for illegal aims
created by zia nazari April 2022, nazari.zia@gmail.com
'''
import socket

HOST, PORT = "mail.domain1.com", 587
sender_email = "user1@domain1.com"
receiver_email = "user2@domain1.com"
forged_sender_email = "user1@domain2.com"
forged_receiver_email = receiver_email
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
client_socket.settimeout(5)
print("--------------------------------------------------------------")
try:
    print("Server:  " + client_socket.recv(1024).decode("utf-8"), end="")

    client_socket.send("HELO        example.com\n".encode("utf-8"))
    print("Client:      HELO example.com\n")
    print("Server:      " + client_socket.recv(1024).decode("utf-8"), end="")

    client_socket.send(("MAIL FROM:      " + sender_email + "\n").encode("utf-8"))
    print("Client:      MAIL FROM: " + sender_email + "\n")
    print("Server:      " + client_socket.recv(1024).decode("utf-8"), end="")

    client_socket.send(("RCPT TO:      " + receiver_email + "\n").encode("utf-8"))
    print("Client:      RCPT TO: " + receiver_email + "\n")
    print("Server:      " + client_socket.recv(1024).decode("utf-8"), end="")

    msg = "Plz click on the following link\n"
    data = "DATA\n\
           Subject: new project\n\
           From: " + forged_sender_email + "\n\
           To: " + forged_receiver_email + "\n\
           " + msg + "\n\
           .\n"
    client_socket.send(msg.encode("utf-8"))
    print("Server:      " + client_socket.recv(1024).decode("utf-8"), end="")

except TimeoutError:
    print("timeout")

client_socket.close()
print("socket is down!")
