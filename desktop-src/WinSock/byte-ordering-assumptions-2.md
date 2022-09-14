---
description: Sockaddr structures and byte ordering assumptions in Winsock.
ms.assetid: 792353eb-dc51-4c6d-b137-2d81083dc192
title: Byte Ordering Assumptions
ms.topic: article
ms.date: 05/31/2018
---

# Byte Ordering Assumptions

A service provider should treat all [**sockaddr**](sockaddr-2.md) components exclusive of the address family parameter as if they are in the network byte order, and the address family parameter as in the local computer's byte order. It is the Winsock application's responsibility to make sure that addresses contained in **sockaddr** structures are properly arranged. The Winsock API provides a number of conversion routines to simplify this task. Currently these routines understand conversion between the local host's natural byte order and either big-Endian or little-Endian network byte ordering. The Winsock architecture can support other byte ordering schemes in the future.

 

 



