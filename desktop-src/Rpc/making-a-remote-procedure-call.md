---
title: Making a Remote Procedure Call
description: Once the client program of distributed applications that uses explicit binding handles has a binding handle, it can execute remote procedures.
ms.assetid: f424bb01-e562-49eb-abaf-cc2d76a6ad8f
keywords:
- Remote Procedure Call RPC , tasks, making a call
ms.topic: article
ms.date: 05/31/2018
---

# Making a Remote Procedure Call

Once the client program of distributed applications that uses explicit binding handles has a binding handle, it can execute remote procedures.

Microsoft RPC also offers custom binding handles, implicit binding handles, and automatic binding handles. These binding handles offer client and server programs different levels of control over the process of executing remote procedures. For details on different handle types and the flexibility they offer, see [Binding and Handles](binding-and-handles.md).

To execute the procedure call remotely, call the client-side stub function in the same manner any C function is called.

 

 




