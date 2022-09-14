---
description: Client/Server Exchange
ms.assetid: 2449c4b3-720d-4b84-b3cf-fcc4abd05d33
title: Client/Server Exchange
ms.topic: article
ms.date: 05/31/2018
---

# Client/Server Exchange

After a user has a ticket to a server, the workstation client can establish a secure communications session with that server.

**To establish a secure communications session with a server**

1.  The client sends the server a message of type KRB\_AP\_REQ (Kerberos Application Request). This message contains an authenticator message that is encrypted with the key sent by the [*Key Distribution Center*](/windows/desktop/SecGloss/k-gly) (KDC) for the session with the server, the ticket for sessions with the server, and a flag that indicates whether the client requests mutual authentication. Setting the flag that requests mutual authentication is one of the options in configuring [*Kerberos*](/windows/desktop/SecGloss/k-gly). The user is never asked whether mutual authentication should be used.
2.  The server receives KRB\_AP\_REQ, decrypts the ticket, and extracts the user's authorization data and the [*session key*](/windows/desktop/SecGloss/s-gly).
3.  The server uses the session key from the ticket to decrypt the user's authenticator message and evaluates the time stamp inside.
4.  If the authenticator message is valid, the server checks the mutual authentication flag in the client's request.
5.  If the mutual authentication flag is set, the server uses the session key to encrypt the time from the user's authenticator message and returns the result in a message of type KRB\_AP\_REP (Kerberos Application Reply).
6.  When the client receives KRB\_AP\_REP, it decrypts the server's authenticator message with the session key it shares with the server and compares the time sent back by the service with the time in its original authenticator message. If they match, the client is assured that the service is genuine, and the connection proceeds.

 

 
