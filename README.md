# smtp_on_socket
Sending smtp emails programmatically on sockets (SSL or Non-SSL)
By default SMTP has no authentication of email senders, so an attacker can send an email to one on behaf of another person.
For example, Attacker(A) connects to a mail server on nc or telnet. Then, using SMTP commands he/she can set the sender, receiver and the message.
Finally, by specifying the end of message, the email will be sent.
Although, this code can be used as double sword, but do not apply it in wrong way ;)
I mostly use it for sending automatic emails.
