---
title: Maintaining State on the Server Between Calls
description: It is often necessary to maintain state on the server between separate RPC calls \ 8212;using context handles is the best way to do so. A few words about how context handles operate internally helps in understanding when context handles work best.
ms.assetid: f76ec489-f48e-473d-b519-3ac143d41fa4
keywords:
- Remote Procedure Call RPC , best practices, maintaining state between calls
ms.topic: article
ms.date: 05/31/2018
---

# Maintaining State on the Server Between Calls

It is often necessary to maintain state on the server between separate RPC calls—using context handles is the best way to do so. A few words about how context handles operate internally helps in understanding when context handles work best.

The client never receives the state kept on the server. Most often the state on the server is a pointer to a memory block, and the client has no information about it. All the client receives is a large unique number, with other information associated with it, that the server sends to the client and which represents the context handle in all subsequent operations. Whenever the client refers to an opened handle, it sends the large number it received from the server when that context handle was opened.

The server keeps track of all large numbers it sends to a client. When the server receives a large number representing a context handle, it looks up the number in the collection of valid, outstanding context handles for that client, and finds the server-side context corresponding to a given large number. This is passed to the server routine. If the large number is not found, an RPC\_X\_SS\_CONTEXT\_MISMATCH exception is raised and propagated to the client.

The corollaries of this design are as follows:

-   A context handle is valid only in the context of the existing client/server session. It cannot be passed to another client.
-   A context handle becomes invalid if the server is rebooted, or otherwise loses its connection to the client.
-   The client cannot interpret what the context handle represents on the server. To a client, all context handles are simply large numbers.

If the client fails, the server will get a notification and will clean up its context handles using the run-down mechanism.

 

 




