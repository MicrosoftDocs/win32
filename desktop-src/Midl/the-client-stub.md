---
title: The Client Stub
description: The client stub module provides surrogate entry points on the client for each of the operations defined in the input IDL file.
ms.assetid: 6b16a4ef-fa18-4cd0-b483-1365b8c2528b
keywords:
- MIDL and RPC MIDL , interfaces, client stub
- interfaces MIDL
- interfaces MIDL , MIDL and RPC
ms.topic: article
ms.date: 05/31/2018
---

# The Client Stub

The client stub module provides surrogate entry points on the client for each of the operations defined in the input IDL file.

When the client application makes a call to the remote procedure, its call first goes to the surrogate routine in the client stub file. The client stub routine performs the following functions:

-   Marshals arguments. The client stub packages input arguments into a form that can be transmitted to the server.
-   Calls the client run-time library to transmit arguments to the remote address space and invokes the remote procedure in the server address space.
-   Unmarshals output arguments. The client stub unpacks output arguments and returns to the caller.

The MIDL compiler switches [**/client**](-client.md), [**/cstub**](-cstub.md), and [**/out**](-out.md) affect the client stub file.

 

 




