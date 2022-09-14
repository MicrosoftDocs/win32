---
title: Interfaces in Distributed Objects
description: In distributed computing, an interface is a collection of definitions and remote functions that enables two or more programs to interoperate between different contexts.
ms.assetid: d7cd6bf3-58ec-426d-850a-9c5456ed816d
keywords:
- interfaces MIDL , in distributed objects
ms.topic: article
ms.date: 05/31/2018
---

# Interfaces in Distributed Objects

In distributed computing, an interface is a collection of definitions and remote functions that enables two or more programs to interoperate between different contexts. In an RPC application, an interface specifies:

-   How client and server applications identify themselves to each other.
-   How data is transmitted between client and server.
-   Remote procedures that the client application can call.
-   Data types for the parameters and return values of the remote procedures.

The Microsoft Interface Definition Language (MIDL) is for implementing interfaces used in distributed applications. With MIDL, an application can have one interface or many. Each interface specifies a unique distributed contract between the client and server programs. Applications based on remote procedure calls (RPC), Component Object Model (COM), and Distributed Component Object Model (DCOM) specify their interfaces using MIDL.

MIDL resembles C and C++ in many ways. For an overview of writing MIDL interfaces, see [Developing the Interface](/windows/desktop/Rpc/developing-the-interface).

 

 