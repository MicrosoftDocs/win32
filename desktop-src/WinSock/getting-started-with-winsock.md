---
title: Getting started with Winsock
description: Use the links and resources in this topic as a step-by-step guide to getting started with Windows Sockets programming.
ms.assetid: 905cd5bc-44af-4d3f-841a-9e9a2700a785
ms.topic: conceptual
ms.date: 02/09/2023
---

# Getting started with Winsock

This section is a step-by-step guide to getting started with Windows Sockets programming. It's designed to provide an understanding of basic Winsock functions and data structures, and how they work together.

The client and server application that we use in this topic for illustration is a very basic client and server. More advanced code examples are included in the samples included with the Microsoft Windows Software Development Kit (SDK).

The first few steps are the same for both client and server applications.

- [About servers and clients](about-clients-and-servers.md)
- [Creating a basic Winsock application](creating-a-basic-winsock-application.md)
- [Initializing Winsock](initializing-winsock.md)

The following articles describe the remaining steps for creating a Winsock client application.

- [Creating a socket for the client](creating-a-socket-for-the-client.md)
- [Connecting to a socket](connecting-to-a-socket.md)
- [Sending and receiving data on the client](sending-and-receiving-data-on-the-client.md)
- [Disconnecting the client](disconnecting-the-client.md)

The following articles describe the remaining steps for creating a Winsock server application.

- [Creating a socket for the server](creating-a-socket-for-the-server.md)
- [Binding a socket](binding-a-socket.md)
- [Listening on a socket](listening-on-a-socket.md)
- [Accepting a connection](accepting-a-connection.md)
- [Receiving and sending data on the server](receiving-and-sending-data-on-the-server.md)
- [Disconnecting the server](disconnecting-the-server.md)

The complete source code for these basic examples.

- [Running the Winsock client and server code sample](finished-server-and-client-code.md)
- [Complete Winsock client code](complete-client-code.md)
- [Complete Winsock server code](complete-server-code.md)

## Advanced Winsock sample apps

Several more advanced [Winsock client and server sample apps](https://github.com/microsoft/Windows-classic-samples/tree/main/Samples/Win7Samples/netds/winsock) are available on GitHub. They're listed here in order from higher to lower performance, and are found in the following directories:

- iocp

  That folder contains three sample programs that use I/O completion ports. The programs include: a Winsock server, `iocpserver`, that uses the [**WSAAccept**](/windows/win32/api/Winsock2/nf-winsock2-wsaaccept) function; a Winsock server, `iocpserverex`, that uses the [**AcceptEx**](/windows/win32/api/mswsock/nf-mswsock-acceptex) function; and a simple multithreaded Winsock client, `iocpclient`, used to test either of these servers.

  The server programs support multiple clients connecting by using TCP/IP, and sending arbitrary-sized data buffers that the server then echoes back to the client. For convenience, a simple client program, `iocpclient`, was developed to connect and continually send data to the server to stress it using multiple threads. Winsock servers that use I/O completion ports provide the highest performance.

- overlap

  This folder contains a sample server program that uses overlapped I/O. The sample program uses the [**AcceptEx**](/windows/win32/api/mswsock/nf-mswsock-acceptex) function and overlapped I/O to effectively handle multiple asynchronous connection requests from clients. The server uses the **AcceptEx** function to multiplex different client connections in a single-threaded Win32 application. Using overlapped I/O allows for greater scalability.

- WSAPoll

  This folder contains a basic sample program that demonstrates the use of the [**WSAPoll**](/windows/win32/api/winsock2/nf-winsock2-wsapoll) function. The combined client and server program are non-blocking, and use the **WSAPoll** function to determine when it's possible to send or receive without blocking. This sample is for illustration, and isn't a high-performance server.

- simple

  This folder contains three basic sample programs that demonstrate the use of multiple threads by a server. The programs include: a simple TCP/UDP server, `simples`; a TCP-only server, `simples_ioctl`, that uses the [**select**](/windows/win32/api/Winsock2/nf-winsock2-select) function in a Win32 console application to support multiple client requests; and a client TCP/UDP program, `simplec`, for testing the servers. The servers demonstrate the use of multiple threads to handle multiple client requests. That method has scalability issues since a separate thread is created for each client request.

- accept

  This folder contains a basic sample server and client program. The server demonstrates the use of either non-blocking accept using the [**select**](/windows/win32/api/Winsock2/nf-winsock2-select) function, or asynchronous accept using the [**WSAAsyncSelect**](/windows/win32/api/winsock/nf-winsock-wsaasyncselect) function. This sample is for illustration, and isn't a high-performance server.
