# smtp_on_socket
Sending smtp emails programmatically on sockets (SSL or Non-SSL)
By default SMTP has no authentication of email senders, so an attacker can send an email to one on behaf of another person.

Attacker can normally work on just one domain, so both the sender and the receiver are in that domain. But, somehow the attacker can show the email comes from a different domain.

For example, Attacker(A) connects to a mail server on nc or telnet. Then, using SMTP commands he/she can set the sender(B), receiver(C) and the message.
Finally, by specifying the end of message, the email will be sent from B to C.

When port 25 is open use send_smtp.py, and port 465 is open use send_smtp_ssl.py.
This code can be used as a double edged sword, but do not apply it in illegal works.
I mostly use it for sending automatic emails for personal issues.

Important note: These scripts only work if smtp does not need authentication.
