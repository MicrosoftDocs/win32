---
title: Dynamic Virtual Channels
description: Dynamic virtual channel (DVC) APIs extend the existing virtual channel APIs for Remote Desktop Services, known as static virtual channel (SVC) APIs.
ms.assetid: bddf0048-482d-40f3-a973-9d7bc15be8fa
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Dynamic Virtual Channels

Dynamic virtual channel (DVC) APIs extend the existing virtual channel APIs for Remote Desktop Services, known as static virtual channel (SVC) APIs. DVC APIs address several limitations that existed in SVC APIs between the client and server, such as:

-   A limited number of channels
-   Packet reconstruction

DVC APIs will help you to implement modules on the server and client side of a Remote Desktop Services connection that communicate with each other.

Like many other client/server architectures, a connection is established based on a commonly agreed upon piece of data, referred to as an endpoint. A similar example is TCP/IP, where an endpoint is established through a combination of server IP address and the port name. Another example is named pipes, where an endpoint is a combination of the server name and the pipe name. In a Remote Desktop Services connection there are only two sides involved. Therefore, the endpoint consists of a simple arbitrary string that uniquely identifies the connection. Much like TCP/IP and named pipes, multiple connections can initiate from the same endpoint name. In that sense, connections do not have names; just a listener that waits for incoming requests on the endpoint.

The DVC APIs consist of the following:

-   Client APIs

    These APIs are available in the Remote Desktop Connection (RDC) client as a plug-in. The client side is in passive mode, where it listens for incoming connections but does not actively establish a connection.

-   Server APIs

    These APIs actively initiate the connection.

For information about how to write a dynamic virtual channel (DVC) module, see [DVC Implementation Details](dvc-implementation-details.md).

 

 




