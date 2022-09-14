---
title: Components of the Router Architecture
description: The router administration documentation makes frequent reference to the following components of the router.
ms.assetid: 841a5728-39d6-4bd7-a41a-6543b4ed9985
keywords:
- routers RRAS , components
ms.topic: article
ms.date: 05/31/2018
---

# Components of the Router Architecture

The router administration documentation makes frequent reference to the following components of the router.

Dynamic Interface Manager (DIM)

All router administration functions pass through DIM. Depending on the nature of the function, DIM may pass the call on to one of the router managers. Functions that deal only with interfaces are handled by DIM. If the function affects routing protocols, DIM will call into the router manager for the transport corresponding to that protocol. For example, if the function affects the Open Shortest Path First (OSPF) protocol, DIM will call into the IP Router Manager, since OSPF is an IP routing protocol.

Router Managers

Each routable transport that fits into the router architecture has its own router manager. Currently router managers exist for the IP and IPX transports. The router managers manage router protocols and other types of routing clients that run on interfaces on the local computer.

Routing Protocols and other Clients

Clients are service providers that function within the framework of the router architecture. Routing protocols are one type of client that is supported by the router.

Clients are specific to a particular routable transport: either IP or IPX. Routing protocols for the IP transport include Open Shortest Path First (OSPF) and Routing Information Protocol (RIP). Examples of IPX routing protocols are Service Advertising Protocol (SAP) and RIP for IPX. An example of a client that is not a routing protocol is Network Address Translation (NAT) for IP.

The interface between the router manager and a client is described in the section [Routing Protocol Interface](about-routing-protocol-interface.md). All clients conform to this interface. Using this interface, vendors can implement their own clients that are compatible with the router.

[Interfaces](interfaces.md)

An interface is a connection to an external network. Each interface is identified by a unique interface *index*. Interfaces are logical entities; router clients such at NAT or OSPF deal with all types of interfaces similarly. In terms of implementation however, an interface can represent a dedicated connection (such as to a Local Area Network (LAN)) or a non-dedicated, dial up connection (such as a PPP connection to a Wide Area Network (WAN)).

In the case of a LAN interface, the interface corresponds to an actual physical device in the computer, a LAN adapter. In the case of a WAN interface, the interface is mapped to a port at the time a connection is established. The port could be a COM port, a parallel port or a virtual port (for tunnels such as PPTP and L2TP).

WAN interfaces have the additional quality that they typically receive a network address only at the time that a connection is established. For example, a WAN interface using PPP receives its network layer address from the remote peer during the connection process. Receiving a network address as part of the connection process is sometimes referred to as *late-binding*.

 

 




