---
title: The Pipe State
description: On the server, the MIDL compiler creates a state variable that coordinates push, pull, and alloc procedures.
ms.assetid: 7cc59cb3-cf41-40f7-a28f-b896c319ae64
ms.topic: article
ms.date: 05/31/2018
---

# The Pipe State

On the server, the MIDL compiler creates a *state* variable that coordinates push, pull, and alloc procedures. On the client side, the developer must create the *state* variable. Therefore, the *state* variable is local to both sides—that is, the client and server each maintain their own pipe state. The server stub code maintains the state variable on the server. You should not attempt to modify its contents directly. The client must initialize the fields in the pipe control structure and maintain its *state* variable. It uses the *state* variable to identify where to locate or place data.

The client *state* variable can be as simple as a file handle, if you are transferring data from one file to another. It can also be an integer that points to an element in an array. Or you can define a fairly complex state structure to perform additional tasks, such as coordinating the push and pull routines on an \[ [in](/windows/desktop/Midl/in), [out](/windows/desktop/Midl/out-idl)\] parameter.

 

 