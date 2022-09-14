---
title: System Requirements for RPC-Message Queuing Applications
description: To use the message-queuing transport in an RPC client/server application, the server and client computers must have the appropriate operating system platform and Message Queuing software installed.
ms.assetid: f90318a6-0be6-4e1a-a1a5-1709808b5d3b
ms.topic: article
ms.date: 05/31/2018
---

# System Requirements for RPC-Message Queuing Applications

To use the message-queuing transport in an RPC client/server application, the server and client computers must have the appropriate operating system platform and Message Queuing software installed.

Requirements for server computers are:

-   Microsoft Windows Server 2003, Windows XP, or Windows 2000 or later.
-   SQL Server version 6.5 or later.
-   Message Queuing Primary Enterprise Controller or Primary Site Controller.
-   RPC server-side transport DLL (RpcMqSvr.dll).

Requirements for client computers are:

-   Microsoft Windows Server 2003, Windows XP, or Windows 2000 or later.
-   Microsoft Message Queuing Client.
-   RPC client-side transport DLL (RpcMqCl.dll).

When the MSMQ components are installed on the client and server computers, the system registries are automatically configured to include the [ncadg\_mq](/windows/desktop/Midl/ncadg-mq) message-queuing transport protocol for remote procedure calls.

To build your RPC-MSMQ application you need the following:

-   Microsoft Windows Server 2003, Windows XP, or Windows 2000 or later
-   MIDL version 3.1.76 or later.

 

 