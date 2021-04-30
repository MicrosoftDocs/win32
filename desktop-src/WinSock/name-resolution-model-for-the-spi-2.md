---
description: Name resolution and registration model for the Windows Sockets (Winsock) SPI.
ms.assetid: b173b63e-42c7-4f85-b55f-1f7b3bff7c4f
title: Name Resolution Model for the SPI
ms.topic: article
ms.date: 05/31/2018
---

# Name Resolution Model for the SPI

In developing a protocol-independent client/server application, there are two basic requirements that exist with respect to name resolution and registration:

-   The ability of the server half of the application (hereafter referred to as a service) to register its existence within (or become accessible to) one or more namespaces.
-   The ability of the client application to find the service within a namespace and obtain the required transport protocol and addressing information.

For those accustomed to developing TCP/IP-based applications, this may involve little more than looking up a host address and then using an agreed upon port number. Other networking schemes, however, allow the location of the service, the protocol used for the service, and other attributes to be discovered at run-time. To accommodate the range of capabilities found in existing name services, the Windows Sockets 2 interface adopts the model described below.

A *namespace* refers to some capability to associate (as a minimum) the protocol and addressing attributes of a network service with one or more human-friendly names. Many namespaces are currently in wide use including the Internet's Domain Name System (DNS), NetWare Directory Services (NDS), X.500, etc. These namespaces vary widely in how they are organized and implemented. Some of their properties are particularly important to understand from the perspective of Windows Sockets name resolution.

 

 



