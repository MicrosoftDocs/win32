---
description: 'There are two distinct types of socket network applications: Server and Client.'
ms.assetid: 05e42384-1746-462d-82c7-8df848b4525e
title: About Servers and Clients
ms.topic: article
ms.date: 05/31/2018
---

# About Servers and Clients

There are two distinct types of socket network applications: Server and Client.

Servers and Clients have different behaviors; therefore, the process of creating them is different. What follows is the general model for creating a streaming TCP/IP Server and Client.

## Server

1.  Initialize Winsock.
2.  Create a socket.
3.  Bind the socket.
4.  Listen on the socket for a client.
5.  Accept a connection from a client.
6.  Receive and send data.
7.  Disconnect.

## Client

1.  Initialize Winsock.
2.  Create a socket.
3.  Connect to the server.
4.  Send and receive data.
5.  Disconnect.

> [!Note]  
> Some of the steps are the same for a client and a server. These steps are implemented almost exactly alike. Some of the steps in this guide will be specific to the type of application being created.

 

First Step: [Creating a Basic Winsock Application](creating-a-basic-winsock-application.md)

## Related topics

<dl> <dt>

[Getting Started With Winsock](getting-started-with-winsock.md)
</dt> </dl>

 

 



