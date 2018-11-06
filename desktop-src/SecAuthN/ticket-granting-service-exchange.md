---
Description: After a ticket-granting ticket (TGT) and session key have been established for the client, the client can request a separate session key and ticket for the service.
ms.assetid: b4f63642-9282-4e11-b40c-eec406b2dd2b
title: Ticket-Granting Service Exchange
ms.topic: article
ms.date: 05/31/2018
---

# Ticket-Granting Service Exchange

After a ticket-granting ticket (TGT) and [*session key*](https://msdn.microsoft.com/en-us/library/ms721625(v=VS.85).aspx) have been established for the client, the client can request a separate session key and ticket for the service.

**To request a ticket for another service**

1.  The Kerberos client on the user's workstation requests [*credentials*](https://msdn.microsoft.com/en-us/library/ms721572(v=VS.85).aspx) for the service by sending, to the [*Key Distribution Center*](https://msdn.microsoft.com/en-us/library/ms721590(v=VS.85).aspx) (KDC), a message of type KRB\_TGS\_REQ (Kerberos Ticket-Granting Service Request). This message consists of the identity of the service for which the client is requesting credentials, an authenticator message encrypted with the user's new logon [*session key*](https://msdn.microsoft.com/en-us/library/ms721625(v=VS.85).aspx), and the TGT obtained from the [Authentication Service Exchange](authentication-service-exchange.md).
2.  When the KDC receives a KRB\_TGS\_REQ, the KDC decrypts the TGT with its secret key and extracts the user's logon session key.
3.  The KDC uses the logon [*session key*](https://msdn.microsoft.com/en-us/library/ms721625(v=VS.85).aspx) to decrypt the user's authenticator message and evaluates it. If the authenticator passes the test, the KDC extracts the user's authorization data from the TGT and invents a session key for the user to share with the requested server.
4.  The KDC encrypts one copy of the service session key with the user's logon session key.
5.  The KDC embeds another copy of the service session key in a ticket, along with the user's authorization data, and encrypts the ticket with the server's [*master key*](https://msdn.microsoft.com/en-us/library/ms721594(v=VS.85).aspx).
6.  The KDC sends these credentials back to the client by replying with a message of type KRB\_TGS\_REP (Kerberos Ticket-Granting Service Reply).
7.  When the client receives the reply, it decrypts the service session key with the user's logon session key and stores the service session key in its ticket cache.
8.  The client extracts the ticket to the server and stores that in its ticket cache.

 

 



