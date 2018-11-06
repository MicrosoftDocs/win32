---
title: Forwarder
description: The forwarder is the kernel-mode component of the router that is responsible for forwarding data from one router interface to the others.
ms.assetid: 69cdbefa-9137-48cb-940a-badfb3f4f231
ms.topic: article
ms.date: 05/31/2018
---

# Forwarder

The forwarder is the kernel-mode component of the router that is responsible for forwarding data from one router interface to the others. The forwarder also decides whether a packet is destined for local delivery, whether it is destined to be forwarded out of another interface, or both.

There are two kernel-mode forwarders: unicast and multicast.

The router manager obtains the best routes to all destinations from the routing table manager. These routes are passed to the unicast forwarder. The unicast forwarder uses these routes to perform the actual forwarding of unicast data. In this manner, the unicast forwarder maintains a cache of the best routes in the unicast view of the routing table.

The multicast group manager uses information from the multicast view of the routing table to add multicast forwarding entries to the multicast forwarder.

 

 




