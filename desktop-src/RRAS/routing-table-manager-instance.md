---
title: Routing Table Manager Instance
description: An instance is a separate table that the routing table manager uses to maintain routing information about a subset of interfaces.
ms.assetid: a17233fc-2c40-4d00-8a6b-86f08fef5690
ms.topic: article
ms.date: 05/31/2018
---

# Routing Table Manager Instance

An instance is a separate table that the routing table manager uses to maintain routing information about a subset of interfaces. Instances are typically used to enable a physical router to act as a set of virtual routers – one virtual router per logical network.

Currently, the routing table manager supports only one instance (identified as zero, the default). The client can register with other instances, but no virtual router except the default one is recognized or used by the router manager.

 

 




