---
title: Using Opaque Pointers
description: Clients often must store additional, client-specific information about destinations.
ms.assetid: e96805b0-680f-411c-a02c-2c3fda7276ae
ms.topic: article
ms.date: 05/31/2018
---

# Using Opaque Pointers

Clients often must store additional, client-specific information about destinations. The routing table manager enables clients to store this information in destination structures in the routing table. The information is stored and retrieved by using *opaque pointers*. The information stored is private, and accessible only to the client that owns the opaque pointer.

For example, the multicast group manager keeps a list of multicast forwarding entries that are dependent on a particular destination. The multicast group manager uses an opaque pointer in that destination. In another example, a routing protocol that advertises a particular destination can keep information related to its own route advertisement of the destination using an opaque pointer, even though it does not own the best route.

The number of opaque pointers is limited; these pointers are allocated to clients on a first-come, first-served basis. The router administrator must allocate the correct number of pointers during the router configuration; therefore, routing protocols and other clients must document their use of opaque pointers.

 

 




