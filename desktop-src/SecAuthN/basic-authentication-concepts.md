---
description: In a client/server application model, clients are programs acting on behalf of users who need something done.
ms.assetid: c3e38cd3-3749-4384-80ff-0551acfe1eec
title: Basic Authentication Concepts
ms.topic: article
ms.date: 05/31/2018
---

# Basic Authentication Concepts

In a client/server application model, clients are programs acting on behalf of users who need something done. This might be opening and using a file, accessing a mailbox, querying a database, or printing a document. Servers are programs providing services to clients such as file storage, mail handling, query processing, and print spooling. Clients initiate action, servers respond. Typically, a server listens at a communications port waiting for clients to connect and ask for service.

In the Kerberos protocol model, every client/server connection begins with authentication. Client and server, in turn, step through a sequence of actions designed to verify to the party on each end of the connection that the party on the other end is genuine. If authentication is successful, session setup completes and a secure client/server session is established.

The Kerberos protocol makes use of:

-   [Key authentication](key-authentication.md)
-   [Authenticator messages](authenticator-messages.md)
-   [Key distribution](key-distribution.md)
-   [Session tickets](session-tickets.md)
-   [Ticket-granting tickets](ticket-granting-tickets.md)

 

 



