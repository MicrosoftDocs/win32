---
title: Connecting the Client and the Server
description: To communicate, client and server programs must establish a communication session across the network or networks that connect them.
ms.assetid: 1164252a-7615-4958-9d2f-cf35c0db513a
keywords:
- Remote Procedure Call RPC , tasks, connecting client and server
ms.topic: article
ms.date: 05/31/2018
---

# Connecting the Client and the Server

To communicate, client and server programs must establish a communication session across the network or networks that connect them. Once they establish the connection, the client can call remote procedures in the server program as if they were local to the client program.

This section provides a conceptual overview of how to establish a connection between clients and servers for remote procedure calls. It does not provide an in-depth discussion of this topic. All of the concepts in this section are presented in detail in later chapters and in the RPC Function Reference section.

The discussion presented in this section is divided into the following topics:

-   [Essential RPC Binding Terminology](essential-rpc-binding-terminology.md)
-   [How the Server Prepares for a Connection](how-the-server-prepares-for-a-connection.md)
-   [How the Client Establishes a Connection](how-the-client-establishes-a-connection.md)

Note that the discussion assumes explicit binding handles. However, if your application uses other types of binding handles, you may have to modify the steps presented in this section. For more information, see [Binding and Handles](binding-and-handles.md).

 

 




