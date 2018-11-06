---
title: Testing and Debugging
description: There is an \ 0034;echo \ 0034; listener that is implemented by the Remote Desktop Connection (RDC) client, which is always present and listening for incoming connections.
ms.assetid: ae14af04-7d19-406b-998e-a0579cfe73eb
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Testing and Debugging

There is an "echo" listener that is implemented by the Remote Desktop Connection (RDC) client, which is always present and listening for incoming connections. When you are writing the server side of a dynamic virtual channel (DVC) module, as a quick test you can open an endpoint named "ECHO". Any write to a channel that is instantiated from this endpoint will result in the receipt of the same data.

You can use this technique to test an input/output (I/O) implementation of the server-side module, to measure the response time for a Remote Desktop Connection (RDC) client plug-in, or to measure the network delay for the Remote Desktop Connection (RDC) client. There is no limitation on the amount of data that can be sent over this channel.

 

 




