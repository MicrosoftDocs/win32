---
title: RAS interfaces
description: An interface represents a network that can be reached over a LAN or WAN adapter.
ms.assetid: 26eec1af-43b4-4719-bec9-bc3f9b0341e6
ms.topic: article
ms.date: 05/31/2018
---

# RAS interfaces

An interface represents a network that can be reached over a LAN or WAN adapter. Each interface has a unique identifier on the router. Interfaces that are active have an adapter that is providing connectivity to the network they represent. Interfaces that are inactive do not have an adapter providing connectivity, unless an administrator disabled the interface after it already had an adapter.

Routing a packet to a network represented by an interface will cause the router to allocate an adapter for that interface, and establish a WAN connection to the remote network. Allocating an adapter to an interface is referred to as *binding*.

Interfaces are manageable objects. Each interface appears as a row in the Interface Table of the appropriate SNMP MIB.