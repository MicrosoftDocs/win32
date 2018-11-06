---
title: Sending the Call to the Server Program
description: Once the client side RPC run time has connected to the server endpoint, it marshalls the arguments and sends them to the server.
ms.assetid: 170316b1-4185-45b1-845e-ca6f0285b7f9
keywords:
- Remote Procedure Call RPC , tasks, sending the call to the server
ms.topic: article
ms.date: 05/31/2018
---

# Sending the Call to the Server Program

Once the client side RPC run time has connected to the server endpoint, it marshalls the arguments and sends them to the server. The server RPC run time gives the marshalled arguments to the stub that unmarshalls them, and then passes them to the server routines. When the server routines return, the stub picks up the \[out\] and \[in,out\] parameters and the return value, marshalls them, and sends the marshalled data to the server RPC run time. The RPC run time sends the data back to the client, where the client RPC run time hands them off to the client side stub that unmarshalls them and returns them to the caller.

 

 




