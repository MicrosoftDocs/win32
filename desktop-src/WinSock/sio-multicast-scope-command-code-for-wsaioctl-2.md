---
description: When multicasting is employed, it is usually necessary to specify the scope over which the multicast should occur.
ms.assetid: 744b43a8-dd89-4e63-ae3c-5bee72864df7
title: SIO_MULTICAST_SCOPE Command Code for WSAIoctl
ms.topic: article
ms.date: 05/31/2018
---

# SIO\_MULTICAST\_SCOPE Command Code for WSAIoctl

When multicasting is employed, it is usually necessary to specify the *scope* over which the multicast should occur. Scope is defined as the number of routed network segments to be covered. A scope of zero would indicate that the multicast transmission would not be placed on the wire but could be disseminated across sockets within the local host. A scope value of 1 (the default) indicates that the transmission will be placed on the wire, but will not cross any routers. Higher scope values determine the number of routers that may be crossed. Note that this corresponds to the time-to-live (TTL) parameter in IP multicasting.

The function [**WSAJoinLeaf**](/windows/desktop/api/Winsock2/nf-winsock2-wsajoinleaf) is used to join a leaf node into the multipoint session. See the following for a discussion on how this function is utilized.

 

 



