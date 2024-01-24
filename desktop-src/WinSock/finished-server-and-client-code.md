---
description: Running the complete TCP/IP client and server application sample code.
ms.assetid: 617dfdf6-f7a7-4e72-8c77-8cfa3ab232e7
title: Running the Winsock Client and Server Code Sample
ms.topic: article
ms.date: 05/31/2018
---

# Running the Winsock Client and Server Code Sample

This section contains the complete source code for the TCP/IP Client and Server applications:

-   [Complete Winsock Client Code](complete-client-code.md)
-   [Complete Winsock Server Code](complete-server-code.md)

The server application should be started before the client application is started.

To execute the server, compile the complete server source code and run the executable file. The server application listens on TCP port 27015 for a client to connect. Once a client connects, the server receives data from the client and echoes (sends) the data received back to the client. When the client shuts down the connection, the server shuts down the client socket, closes the socket, and exits.

To execute the client, compile the complete client source code and run the executable file. The client application requires that name of the computer or IP address of the computer where the server application is running is passed as a command-line parameter when the client is executed. If the client and server are executed on the sample computer, the client can be started as follows:

**client localhost**

The client tries to connect to the server on TCP port 27015. Once the client connects, the client sends data to the server and receives any data send back from the server. The client then closes the socket and exits.

## Related topics

<dl> <dt>

[Getting Started With Winsock](getting-started-with-winsock.md)
</dt> </dl>

 

 



