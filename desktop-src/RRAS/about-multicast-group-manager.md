---
title: About Multicast Group Manager
description: This documentation describes the Multicast Group Manager (MGM) technology.
ms.assetid: 55216742-d67c-4a17-aaf9-0b087938061e
keywords:
- Multicast Group Manager RRAS
- Multicast Group Manager RRAS , described
- Routing and Remote Access Service RRAS , Multicast Group Manager
- Routing and Remote Access Service RRAS , Multicast Group Manager, described
ms.topic: article
ms.date: 05/31/2018
---

# About Multicast Group Manager

This documentation describes the Multicast Group Manager (MGM) technology.

Multicasting allows a host to send data to only those destinations that specifically request to receive the data. In this way, multicasting differs from sending broadcast data, since broadcast data is sent to all hosts.

Multicasting saves network bandwidth because multicast data is only received by those hosts that request the data, and the data travels over any link only once. Multicasting saves server bandwidth because a server has to send only one multicast message per network instead of one unicast message per receiver. Examples of popular multicast applications are online meetings and Internet radio.

The MGM API enables developers to write multicast routing protocols that interoperate with routers running the multicast group manager.

When more than one multicast routing protocol is enabled on a router, the multicast group manager coordinates operations between all routing protocols. The multicast group manager informs each routing protocol when group membership changes occur, and when multicast data from a new source or destined to a new group is received.

The MGM API provides the following features:

-   Protocol registration
-   Group management
-   Multicast forwarding entry (MFE) enumeration
-   Callback definitions for multicast routing protocols

This overview describes the components of the multicast architecture, the client scenarios that are used to interoperate with the multicast group manager, and programming considerations for using the MGM API.

 

 




