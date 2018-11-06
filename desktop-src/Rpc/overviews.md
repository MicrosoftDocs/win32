---
title: Overviews
description: Remote Procedure Call (RPC) navigation page for overview sections.
ms.assetid: 49dc35c3-efd7-45a2-bec0-cd68ac150754
keywords:
- Remote Procedure Call RPC , described
ms.topic: article
ms.date: 05/31/2018
---

# Overviews

This portion of the Remote Procedure Call (RPC) Programmer's Guide and Reference consists of a sequence of topics that will help you understand distributed application programming and RPC as follows:

-   [Microsoft RPC Model](microsoft-rpc-model.md) provides an overview of the client-server programming model, standards for distributed application programming, and a description of how Microsoft RPC works.
-   [Installing The RPC Programming Environment](installing-the-rpc-programming-environment.md) tells how to install the files and tools needed to develop distributed applications with Microsoft RPC.
-   [Building RPC Applications](building-rpc-applications.md) describes the MIDL compiler and the necessary environment for building distributed applications with Microsoft RPC.
-   [Connecting the Client and the Server](connecting-the-client-and-the-server.md) provides an overview of the process of initializing and running distributed applications.
-   [Tutorial](tutorial.md) provides an overview of the development of a small distributed application. This example demonstrates all the steps in developing a distributed application, the tools you use, and the components that make up the executable programs.
-   [IDL and ACF Files](the-idl-and-acf-files.md) describes the IDL and ACF files used to specify the interface to the remote procedure call and the MIDL compiler switches that control how these files are processed.
-   [Data and Language Features](data-and-language-features.md) demonstrates the use of standard data types.
-   [Arrays and Pointers](arrays-and-pointers.md) explains how to pass arrays pointers as parameters.
-   [Pipes](pipes.md) describes how to use named pipes as the transport mechanism for remote procedure calls.
-   [Binding and Handles](binding-and-handles.md) describes the binding handle — the data structure that allows the developer to bind the calling application to the remote procedure.
-   [Memory Management](memory-management.md) offers ideas about how to manage memory on the client and server when performing remote procedure calls.
-   [Serialization Services](serialization-services.md) describes the methods for encoding or decoding data.
-   [Security](security.md) describes the methods for implementing security features in your distributed applications.
-   [Installing and Configuring RPC Applications](installing-and-configuring-rpc-applications.md) discusses installing your client and server applications, describes how to configure the name service provider and the security service. This section also contains network transport information for RPC.
-   [Asynchronous RPC](asynchronous-rpc.md) presents information on the Microsoft asynchronous extensions to the RPC definition. Asynchronous remote procedure calls return immediately without waiting for output. When the remote procedure finishes executing on the server, it transfers return data to the client.
-   [RPC Message Queuing](rpc-message-queuing.md) describes the use of the Message Queuing Service (MSMQ), which lets users communicate across networks and systems regardless of the current state of the communicating applications and systems.
-   [Remote Procedure Calls Using RPC over HTTP](remote-procedure-calls-using-rpc-over-http.md) provides RPC clients with the ability to securely connect across the Internet to RPC server programs and execute remote procedure calls.
-   [RPC Load Balancing](rpc-load-balancing.md) describes distributing high volumes of RPC over HTTP traffic among numerous RPC servers within a server farm.
-   [Samples](examples.md) contains a description of the example RPC programs shipped with the Microsoft Platform Software Developer's Kit.

 

 




