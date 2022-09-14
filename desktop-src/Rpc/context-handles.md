---
title: Context Handles
description: It is sometimes the case that distributed applications require the server program to maintain status information between client calls.
ms.assetid: '91732a75-0a3a-44bd-9db9-c11be6fd2d70'
keywords:
- Remote Procedure Call RPC , described, context handles
ms.topic: article
ms.date: 05/31/2018
---

# Context Handles

It is sometimes the case that distributed applications require the server program to maintain status information between client calls. Server programs that service more than one client at a time must keep the state information for each client. Because the client and the server use different address spaces on different computers, and they do not necessarily trust each other, common approaches to data sharing often do not work. For instance, the client and server are unable to maintain status information on their remote session in global variables because they do not share the same global address space. It is difficult to keep the information in a shared file because they run on different computers. A simplistic approach may be to ship all state to the client and have the client return it on the next call, but this approach has flaws: the server does not necessarily trust the client to return the right state, and the state may be implicitly tied to some other state on the server, such as file handles or opened sockets.

Microsoft RPC provides a powerful and secure mechanism called context handles for keeping state associated with a given client on a server. The state information is called the server's context. Clients can obtain a context handle to identify the server's context for their individual RPC sessions.

As an example, each client in a distributed application can have the server program create and update a data file for their RPC session. The server can use its file handle for each client's data file as the context handle. Each time a client requests operations on the data file that the server creates for it, the client passes the context handle to the server. The client does not actually get the file handle itself; it gets an opaque token that the server RPC run time can uniquely associate with the file handle. Since the context handle is really a file handle, the context handle only makes sense in the server's address space. However, the client program can use the context handle to tell the server on which file to perform updates.

Other data can also be context handles. For instance, a client and server can use a record number of a database record as a file handle. If the client needed to perform a number of updates on a particular record, it could obtain the record number as a context handle. It would pass the record number to the server each time it invoked a remote procedure to update the database record.

Most often a context handle points to a block of memory on the server where the server keeps various management information.

This section presents information on defining and using context handles. The discussion is presented in the following topics:

-   [Interface Development Using Context Handles](interface-development-using-context-handles.md)
-   [Server Development Using Context Handles](server-development-using-context-handles.md)
-   [Client Development Using Context Handles](client-development-using-context-handles.md)
-   [Server Context Run-down Routine](server-context-run-down-routine.md)
-   [Client Context Reset](client-context-reset.md)
-   [Multithreaded Clients and Context Handles](multithreaded-clients-and-context-handles.md)

 

 




