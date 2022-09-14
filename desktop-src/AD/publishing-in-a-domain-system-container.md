---
title: Publishing in a Domain System Container
description: The System container of a domain partition holds per-domain operational information.
ms.assetid: 18bb3409-774e-42d9-8f27-6c582d74ca86
ms.tgt_platform: multiple
keywords:
- Publishing in a Domain System Container AD
ms.topic: article
ms.date: 05/31/2018
---

# Publishing in a Domain System Container

The System container of a domain partition holds per-domain operational information. This includes the default local security policy, file link tracking, network meetings, and containers for Windows Sockets registration and resolution (RnR) and RPC name service (RpcNs) connection points. The system container is hidden, by default, and provides a convenient place for storing objects that are of interest to administrators, but not to end users.

Services that are not tied to a single host may want to create their SCPs under the System container of a domain partition. This alternative can be useful for services with replicas installed on multiple hosts, each replica providing identical services to clients throughout the domain. It enables you to group all the objects for the replicated service under a single container.

Services that create service-specific objects in the System container must do the following:

1.  Create a sub-container of object class **container** as an immediate child of the System container. Give this sub-container a name that clearly identifies it as pertaining to the service.
2.  Create the service-related objects in this sub-container. For example, NetMeeting uses the Meetings container to publish network meeting objects.

A vendor with multiple products can use a similar strategy to group service-related objects for all of its products. In this case, you could create a **container** object with a name that clearly identifies the vendor; then create **container** objects for each service as children of the vendor container. Create the vendor-specific container as a child of the System container.

 

 




