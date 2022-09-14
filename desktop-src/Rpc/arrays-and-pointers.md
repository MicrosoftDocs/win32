---
title: Arrays and Pointers
description: Remote Procedure Call (RPC) is designed to be mostly transparent to developers.
ms.assetid: 5ad5a51d-a821-44a5-bbc3-14409cb42cb4
keywords:
- Remote Procedure Call RPC , described, arrays and pointers
ms.topic: article
ms.date: 05/31/2018
---

# Arrays and Pointers

Remote Procedure Call (RPC) is designed to be mostly transparent to developers. To achieve this transparency, the client stub transmits to the server both the pointer and the data object to which it points. If the remote procedure changes the data, the server must transmit the new data back to the client so that the client can copy the new data over the original data.

In general, a remote procedure call behaves just like a local procedure call. That is, when a pointer is a parameter, the remote procedure can access the data object the pointer refers to in the same way that a local procedure can.

Since client and server programs run in different address spaces, developers must use Microsoft Interface Definition Language (MIDL) attributes to describe how array and pointer data is transmitted between the client and the server. This section presents an overview of how to use arrays and pointers in distributed applications, in the following topics:

-   [Arrays and RPC](arrays-and-rpc.md)
-   [Pointers and RPC](pointers-and-rpc.md)
-   [Using Arrays, Strings, and Pointers](using-arrays-strings-and-pointers.md)

 

 




