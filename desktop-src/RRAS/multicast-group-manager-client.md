---
title: Multicast Group Manager Client
description: A client is an entity that calls an MGM function, such as a routing protocol or an administrative application.
ms.assetid: 98d13b48-9f1d-4649-a5a3-03926c7facee
ms.topic: article
ms.date: 05/31/2018
---

# Multicast Group Manager Client

A client is an entity that calls an MGM function, such as a routing protocol or an administrative application.

The MGM API is used primarily by multicast routing protocols. Developers of multicast routing protocols use the MGM API to:

-   Maintain group membership
-   Control interface ownership
-   Receive notifications from the multicast group manager regarding other multicast routing protocols' requests for multicast data

Specific administrative applications that must monitor multicast forwarding entries (MFEs) can do so without adding or removing group membership. Administrative application developers use specific MGM functions to review information in MFEs.

> [!Note]  
> Multicast routing protocols also access MFEs.

 

An MFE is forwarding information that the multicast group manager creates based on group membership. The MFEs that are retrieved from the multicast group manager can provide statistical information. An administrative application can then use this information to determine the appropriate actions. For example, an administrative application could perform actions that are based on the volume of packets on a specific interface.

 

 




