---
title: Routing Protocol
description: A routing protocol is a type of client that registers with the routing table manager. Routers use routing protocols to exchange information regarding routes to a destination.
ms.assetid: '957ec896-94e3-4bdb-801a-12b861460fff'
ms.topic: article
ms.date: 05/31/2018
---

# Routing Protocol

A routing protocol is a type of client that registers with the routing table manager. Routers use routing protocols to exchange information regarding routes to a destination.

Routing protocols are either unicast or multicast. Routing protocols advertise routes to a destination.

A unicast route to a destination is used by a unicast routing protocol to forward unicast data to that destination. Examples of unicast routing protocols include: Routing Information Protocol (RIP), Open Shortest Path First (OSPF), and Border Gateway Protocol (BGP).

A multicast route to a destination is used by some multicast routing protocols to create the information that is used to forward multicast data from hosts on the destination network of the route (known as reverse path forwarding).Examples of multicast routing protocols include: Multicast Open Shortest Path First (MOSPF), Distance Vector Multicast Routing Protocol (DVMRP), and Protocol Independent Multicast (PIM).

The routing table manager supports multiple instances of the same protocol (such as Microsoft's implementation of OSPF and a third-party OSPF) running on the router. This allows routers to use the different capabilities of each version. These protocols have different protocol identifiers.

Protocol identifiers are comprised of a vendor identifier and a protocol-specific identifier. The protocol-specific identifier is the same for different implementations of the protocol, such as Microsoft's implementation of OSPF and a third-party implementation of OSPF. Only when the vendor and protocol-specific identifiers are combined is there a unique identifier for a routing protocol.

A protocol with the same protocol identifier (that is, the same vendor identifier and protocol-specific identifier) can register with the routing table manager multiple times. Each time, the protocol registers using a different protocol instance identifier. For example, an implementation of OSPF from a particular vendor can register as Vendor-OSPF-1 and Vendor-OSPF-2. This enables a specific protocol implementation to partition the information that it keeps in the routing table.

 

 




