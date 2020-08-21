---
title: Asynchronous Pipes
description: Using pipe parameters with asynchronous RPC allows you to transmit data incrementally, as it becomes available, without tying up the client and server.
ms.assetid: e5c466b8-c0b0-4fa8-8867-d0715fd614b2
ms.topic: article
ms.date: 05/31/2018
---

# Asynchronous Pipes

Using [pipe](/windows/desktop/Midl/pipe) parameters with asynchronous RPC allows you to transmit data incrementally, as it becomes available, without tying up the client and server. This is particularly useful when you have a large amount of data to transfer, combined with a slow client, a slow server, or a slow network. If you use a pipe in an asynchronous function call, it is, by definition, an asynchronous pipe. Synchronous pipes are not supported in conjunction with asynchronous functions.

Unlike conventional (synchronous) pipes where the server handles all the details of sending and receiving pipe data, asynchronous pipes are symmetrical. That is, both the client and the server can push and pull data through the pipe.

> [!Note]  
> Pipe parameters can only be passed by reference. Even if the IDL file shows [pipe](/windows/desktop/Midl/pipe) parameters being passed by value, the generated stubs will accept pipe parameters by reference only.

 

In the following discussion of asynchronous pipes, familiarity with the pipe type constructor is assumed. For more information on the pipe procedures described in these topics, see [Pipes](pipes.md).

 

 