---
title: Teredo Components
ms.assetid: 95d83030-b1de-4f09-b9d0-f443d9672ca1
description: "Learn more about: Teredo Components"
ms.topic: article
ms.date: 05/31/2018
---

# Teredo Components

The [Teredo](about-teredo.md) infrastructure consists of the following components:

## Teredo Clients

A Teredo client is an IPv6/IPv4 node that supports a Teredo tunneling interface through which packets are tunneled to other Teredo clients or nodes on the IPv6 Internet (via a Teredo relay). A Teredo client communicates with a Teredo server to obtain an address prefix from which a Teredo-based IPv6 address is configured or used to facilitate communication with other Teredo clients or hosts on the IPv6 Internet.

Windows XP with Service Pack 1 (SP1) with the Advanced Networking Pack, Windows XP with Service Pack 2 (SP2), Windows Server 2003 with Service Pack 1 (SP1),Windows Server 2003 with Service Pack 2 (SP2), Windows Vista, and Windows Server 2008 all include the Teredo client.

## Teredo Servers

A Teredo server is an IPv6/IPv4 node that is connected to both the IPv4 Internet and the IPv6 Internet, and supports a Teredo tunneling interface over which packets are received. The general role of the Teredo server is to assist in the address configuration of Teredo clients and to facilitate the initial communication between Teredo clients and other Teredo clients or between Teredo clients and IPv6-only hosts. The Teredo server listens on UDP port 3544 for Teredo traffic.

Unlike the client, the Teredo server is not included with Microsoft operating platforms. To facilitate communication between Windows-based Teredo client computers, Microsoft has deployed Teredo servers on the IPv4 Internet.

## Teredo Relays

A Teredo relay is an IPv6/IPv4 router that can forward packets between Teredo clients on the IPv4 Internet (using a Teredo tunneling interface) and IPv6-only hosts. In some cases, the Teredo relay interacts with a Teredo server to facilitate initial communication between Teredo clients and IPv6-only hosts. The Teredo relay listens on UDP port 3544 for Teredo traffic.

Like the Teredo server, Microsoft operating platforms do not include Teredo relay functionality. Microsoft does not currently plan to deploy Teredo relays on the IPv4 Internet. Teredo relays are not required to communicate with Teredo host-specific relays.

## Teredo Host-Specific Relays

Communication between Teredo clients and IPv6 hosts that are configured with a global address must go through a Teredo relay. This is required for IPv6-only hosts connected to the IPv6 Internet. However, when the IPv6 host is IPv6 and IPv4-capable and connected to both the IPv4 Internet and IPv6 Internet, then communication should occur between the Teredo client and the IPv6 host over the IPv4 Internet, rather than having to traverse the IPv6 Internet and go through a Teredo relay.

A Teredo host-specific relay is an IPv6/IPv4 node that has an interface and connectivity to both the IPv4 Internet and the IPv6 Internet and can communicate directly with Teredo clients over the IPv4 Internet, without the need for an intermediate Teredo relay. The connectivity to the IPv4 Internet can be through a public IPv4 address or through a private IPv4 address and a neighboring NAT. The connectivity to the IPv6 Internet can be through a direct connection to the IPv6 Internet or through an IPv6 transition technology such as 6to4, where IPv6 packets are tunneled across the IPv4 Internet. The Teredo host-specific relay listens on UDP port 3544 for Teredo traffic.

Windows XP with SP1 with the Advanced Networking Pack, Windows XP with SP2, Windows Server 2003 with SP1, Windows Server 2003 with SP2, Windows Vista, and Windows Server 2008 include Teredo host-specific relay functionality, which is automatically enabled if the computer has a global address assigned. A global address is assigned in a received Router Advertisement message from a native IPv6 router, an ISATAP router, or a 6to4 router. If the computer does not have a global address, Teredo client functionality is enabled.

The Teredo host-specific relay allows Teredo clients to efficiently communicate with 6to4 hosts, IPv6 hosts with a non-6to4 global prefix, or ISATAP or 6over4 hosts within organizations that use a global prefix for their addresses, provided both hosts are using a version of Windows that supports Teredo.

 

 




