---
description: The following is a step-by-step guide to getting started with Windows Sockets programming.
ms.assetid: 905cd5bc-44af-4d3f-841a-9e9a2700a785
title: Getting Started with Winsock
ms.topic: article
ms.date: 09/10/2021
---

# Getting Started with Winsock

The following is a step-by-step guide to getting started with Windows Sockets programming. It is designed to provide an understanding of basic Winsock functions and data structures, and how they work together.

The client and server application that is used for illustration is a very basic client and server. More advanced code examples are included in the samples included with the Microsoft Windows Software Development Kit (SDK).

The first few steps are the same for both client and server applications.

- [About Servers and Clients](about-clients-and-servers.md)
- [Creating a Basic Winsock Application](creating-a-basic-winsock-application.md)
- [Initializing Winsock](initializing-winsock.md)

The following sections describe the remaining steps for creating a Winsock client application.

- [Creating a Socket for the Client](creating-a-socket-for-the-client.md)
- [Connecting to a Socket](connecting-to-a-socket.md)
- [Sending and Receiving Data on the Client](sending-and-receiving-data-on-the-client.md)
- [Disconnecting the Client](disconnecting-the-client.md)

The following sections describe the remaining steps for creating a Winsock server application.

- [Creating a Socket for the Server](creating-a-socket-for-the-server.md)
- [Binding a Socket](binding-a-socket.md)
- [Listening on a Socket](listening-on-a-socket.md)
- [Accepting a Connection](accepting-a-connection.md)
- [Receiving and Sending Data on the Server](receiving-and-sending-data-on-the-server.md)
- [Disconnecting the Server](disconnecting-the-server.md)

The complete source code for these basic examples.

- [Running the Winsock Client and Server Code Sample](finished-server-and-client-code.md)
- [Complete Winsock Client Code](complete-client-code.md)
- [Complete Winsock Server Code](complete-server-code.md)

## Advanced Winsock Samples

Several more advanced Winsock client and server samples are available [on GitHub](https://github.com/microsoft/Windows-classic-samples/tree/main/Samples/Win7Samples/netds/winsock). They are listed below in order from higher to lower performance and are found in the following directories:

- iocp

    This directory contains three sample programs that use I/O completion ports. The programs include a Winsock server (iocpserver) that uses the [**WSAAccept**](/windows/desktop/api/Winsock2/nf-winsock2-wsaaccept) function, a Winsock server (iocpserverex) that uses the [**AcceptEx**](/windows/win32/api/mswsock/nf-mswsock-acceptex) function, and a simple multithreaded Winsock client (iocpclient) used to test either of these servers. The server programs support multiple clients connecting via TCP/IP and sending arbitrary sized data buffers which the server then echoes back to the client. For convenience, a simple client program, iocpclient, was developed to connect and continually send data to the server to stress it using multiple threads. Winsock servers that use I/O completion ports provide the most performance capability.

- overlap

    This directory contains a sample server program that uses overlapped I/O. The sample program uses the [**AcceptEx**](/windows/win32/api/mswsock/nf-mswsock-acceptex) function and overlapped I/O to handle multiple asynchronous connection requests from clients effectively. The server uses the **AcceptEx** function to multiplex different client connections in a single-threaded Win32 application. Using overlapped I/O allows for greater scalability.

- WSAPoll

    This directory contains a basic sample program that demonstrates the use of the [**WSAPoll**](/windows/win32/api/winsock2/nf-winsock2-wsapoll) function. The combined client and server program are non-blocking and use the **WSAPoll** function to determine when it is possible to send or receive without blocking. This sample is more for illustration and is not a high-performance server.

- simple

    This directory contains three basic sample programs that demonstrate the use of multiple threads by a server. The programs include a simple TCP/UDP server (simples), a TCP-only server (simples\_ioctl) that uses the [**select**](/windows/desktop/api/Winsock2/nf-winsock2-select) function in a Win32 console application to support multiple client requests, and a client TCP/UDP program (simplec) for testing the servers. The servers demonstrates the use of multiple threads to handle multiple client requests. This method has scalability issues since a separate thread is created for each client request.

- accept

    This directory contains a basic sample server and client program. The server demonstrates the use of either non-blocking accept using the [**select**](/windows/desktop/api/Winsock2/nf-winsock2-select) function or asynchronous accept using the [**WSAAsyncSelect**](/windows/desktop/api/winsock/nf-winsock-wsaasyncselect) function. This sample is more for illustration and is not a high-performance server.
