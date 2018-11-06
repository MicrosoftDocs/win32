---
title: The Server Stub
description: The server stub provides surrogate entry points on the server for each of the operations defined in the input IDL file.
ms.assetid: e3263543-e78b-40a8-aafa-4315850112a8
keywords:
- MIDL compiler MIDL , MIDL and RPC MIDL , interfaces, server stub
ms.topic: article
ms.date: 05/31/2018
---

# The Server Stub

The server stub provides surrogate entry points on the server for each of the operations defined in the input IDL file.

When a server stub routine is invoked by the RPC run-time library, it performs the following functions:

-   Unmarshals input arguments (unpacks the arguments from their transmitted formats).
-   Calls the actual implementation of the procedure on the server.
-   Marshals output arguments (packages the arguments into the transmitted forms).

The MIDL compiler switches [**/server**](-server.md), [**/sstub**](-sstub.md), and [**/out**](-out.md) affect the server stub file.

 

 




