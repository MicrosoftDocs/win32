---
description: Protocol-independent name resolution and Windows Sockets (Winsock).
ms.assetid: f55219b9-1518-4b49-a0da-6a3fa025cca3
title: Protocol-Independent Name Resolution
ms.topic: article
ms.date: 05/31/2018
---

# Protocol-Independent Name Resolution

In developing a protocol-independent client/server application, there are two basic requirements that exist with respect to name resolution and registration:

-   The ability of the server half of the application ( service) to register its existence within (or become accessible to) one or more namespaces.
-   The ability of the client application to find the service within a namespace and obtain the required transport protocol and addressing information.

For those accustomed to developing TCP/IP-based applications, this may seem to involve little more than looking up a host address and then using an agreed upon port number. Other networking schemes however, allow the location of the service, the protocol used for the service, and other attributes to be discovered at run time. To accommodate the broad diversity of capabilities found in existing name services, the Windows Sockets 2 interface adopts the model described in the topics in this section.

This section describes protocol-independent name resolution capabilities available to Winsock developers. The following list describes the topics in this section:

-   [Name Resolution Model](name-resolution-model-2.md)
-   [Summary of Name Resolution Functions](summary-of-name-resolution-functions-2.md)
-   [Name Resolution Data Structures](name-resolution-data-structures-2.md)

## Related topics

<dl> <dt>

[Registration and Name Resolution](registration-and-name-resolution-2.md)
</dt> </dl>

 

 



