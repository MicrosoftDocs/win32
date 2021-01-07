---
description: This topic discusses specific programming considerations when using the Peer Infrastructure.
ms.assetid: 525b0625-ec13-4aba-a741-dbacff3587f9
title: Programming Considerations (Peer-to-Peer)
ms.topic: article
ms.date: 05/31/2018
---

# Programming Considerations (Peer-to-Peer)

This topic discusses specific programming considerations when using the Peer Infrastructure.

When using the Peer Infrastructure to develop peer applications, you must take the following programming considerations into account:

-   IPv6

    The Peer Infrastructure requires that IPv6 be installed and started to enable peer networking applications to function.

-   Firewall Ports

    When a firewall is being used on a network (such as the IPv6 Internet Connection firewall), specific ports must be opened to allow the Peer Infrastructure to function. The following ports must be open:

    TCP port 3587 for the Peer Grouping Infrastructure.

    UDP port 3540 for the Peer Graphing Infrastructure.

    > [!Note]  
    > Applications that use the Peer Graphing Infrastructure over TCP choose their own TCP port when calling [**PeerGraphListen**](/windows/desktop/api/P2P/nf-p2p-peergraphlisten).

     

-   Socket Option

    When attempting to connect to other IPv6 peer nodes directly (without using the Peer Infrastructure), ensure that the socket option IPV6\_PROTECTION\_LEVEL is set to **PROTECTION\_LEVEL\_UNRESTRICTED**.

-   Bandwidth

    When using PNRP, an application can publish one or more [peer names](peer-names.md) that can be resolved. For each peer name registered with PNRP, there is an increase in the network bandwidth that PNRP uses to publish the peer name, and keep it available to be resolved by other nodes.

    To prevent using too much bandwidth, applications should avoid registering large numbers of peer names on a computer. For example, an application that publishes pictures should not create a peer name for each picture, but should create one peer name for the service that publishes pictures, and use a different protocol for clients to query the service for specific pictures.

-   Peer Name Registration

    Some applications may be required to register the same [peer name](peer-names.md) on more than one computer. Typically, this happens if a peer name is associated with a person who uses more than one computer. One method that you can use to register the same peer name on multiple computers is to create a peer group for the person, and connect to that group from all computers. Another method is to create a peer identity and peer name on one computer, export the peer identity from that computer, and import it on other computers. This allows the same secure peer name to be created on all the computers that have imported the peer identity.

 

 



