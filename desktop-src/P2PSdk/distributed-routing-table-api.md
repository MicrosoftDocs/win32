---
description: The Distributed Routing Table (DRT) API allows applications to publish and resolve numeric keys in a peer network.
ms.assetid: 17422d71-4c6d-458b-87b6-b31fc2b5bda5
title: Distributed Routing Table API
ms.topic: article
ms.date: 05/31/2018
---

# Distributed Routing Table API

The Distributed Routing Table (DRT) API allows applications to publish and resolve numeric keys in a peer network.

An application utilizing DRT can accomplish the following:

-   Create application-specific Distributed Routing Tables.
-   Register keys, and associate these keys with IP addresses and application data.
-   Search for keys and retrieve the IP addresses and application data associated with them. This functionality can be used to construct Distributed Hash Tables (DHTs), serverless name resolution systems, and overlay mesh networks of many topologies.

> [!Note]  
> The administrators and users of DRT-enabled applications should make the end users of their applications aware of the information being published. Microsoft servers are not employed by this technology and information is not sent to Microsoft.

 

The provided documentation for this API is divided into three sections.



| Section                                                                                | Description                                                                                                          |
|----------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| [About Distributed Routing Tables](about-distributed-routing-tables.md)               | Information detailing the life cycle and state changes of the DRT API.<br/>                                    |
| [Using the Distributed Routing Table API](using-the-distributed-routing-table-api.md) | Information detailing the general usage of the DRT API.<br/>                                                   |
| [Distributed Routing Table API Reference](distributed-routing-table-api-reference.md) | Information detailing the functions, data structures, and enumerated constants that comprise the DRT API.<br/> |



 

 

 




