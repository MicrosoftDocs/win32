---
title: ALE Stateful Filtering
description: Filters installed at the Application Layer Enforcement (ALE) layers of the Windows Filtering Platform (WFP) perform stateful network filtering.
ms.assetid: d5a3fcad-d55e-4a07-af21-cb40e5e9a9ee
ms.topic: article
ms.date: 05/31/2018
---

# ALE Stateful Filtering

Filters installed at the Application Layer Enforcement (ALE) layers of the Windows Filtering Platform (WFP) perform stateful network filtering. An *ALE flow* is used as the basis for ALE stateful filtering.

An ALE flow is a way of classifying network traffic by grouping it based on a Source IP Address, a Destination IP Address, a Source Port, a Destination Port, and a Protocol. An ALE flow could be generic, that is one or more of the descriptors could be matching everything (or wildcard \*). For example, a generic UDP ALE flow would be described as Source IP Address = \*, Destination IP Address = \*, Source Port = \*, Destination Port = \*, and Protocol = UDP.

Once a connection is authorized (inbound connections are authorized at the [**FWPM\_LAYER\_ALE\_AUTH\_RECV\_ACCEPT\_V{4\|6}**](management-filtering-layer-identifiers-.md) layer and outbound connections at the **FWPM\_LAYER\_ALE\_AUTH\_CONNECT\_V{4\|6}** layer), an ALE flow is created such that, barring a policy change, all packets, inbound and outbound, that belong to the same ALE flow are permitted automatically. Because a policy change might require blocking previously allowed connections, ALE flows need to be [reauthorized](ale-re-authorization.md) when a policy change occurs.

ALE stateful filtering reduces drastically the number of required classifications by classifying only the first packet that belongs to an ALE flow. By comparison, non-stateful filtering requires classification of every packet that traverse the network.

An ALE flow has an associated direction, which is the direction of the first packet of the flow. This allows for more flexible policies, by permitting inbound initiated connections to have different policies from outbound initiated connections.

## TCP ALE Flow

An ALE flow for TCP traffic is identified by the five-tuple of TCP/IP (Source IP Address, Destination IP Address, Source Port, Destination Port, and Protocol).

A TCP ALE flow has the same lifetime as a connected TCP socket. A connected TCP socket could be either a socket created using [**connect()**](/windows/desktop/api/winsock2/nf-winsock2-connect) or a socket created as a result of an [**accept()**](/windows/desktop/api/winsock2/nf-winsock2-accept) call.

ALE maintains a one-to-one relationship between a TCP ALE flow and a TCP Control Block (TCB).

## UDP ALE Flow

> [!Note]  
> Protocols that are not TCP or ICMP are treated like UDP.

 

An ALE flow for UDP traffic is identified by the five-tuple of TCP/IP (Source IP Address, Destination IP Address, Source Port, Destination Port, and Protocol).

A UDP ALE flow is created based on a UDP socket and it represents the remote peer that the application is communicating with. A remote peer is identified by a (Destination IP Address and Destination Port) tuple.

There is a one-to-many relationship between a UDP socket and the remote peers that it talks to.

When the local UDP socket is closed, all the ALE flows associated with it will be deleted.

In the absence of socket closures, UDP unicast ALE flows have a [configurable](ale-flow-customization.md) idle timeout that defaults to 60 seconds. If no packets are sent or received within this window, the ALE flow will be deleted. This default timeout is progressively shortened when the number of ALE flows system-wide reaches a certain threshold.

## ICMP ALE Flow

An ALE flow for ICMP traffic is identified by the six-tuple (Source IP Address, Destination IP Address, ICMP type, ICMP code, Protocol, and ICMP ID). The ICMP ID is part of the ALE flow only for ICMP echo/reply traffic.

In the absence of socket closures, ICMP unicast ALE flows have a [configurable](ale-flow-customization.md) idle timeout that defaults to 60 seconds. If no packets are sent or received within this window, the ALE flow will be deleted. This default timeout is progressively shortened when the number of ALE flows system-wide reaches a certain threshold.

Only ICMP non-error messages are indicated to ALE layers. ICMP error messages can be inspected at ICMP\_ERROR layers.

## Related topics

<dl> <dt>

[Application Layer Enforcement (ALE)](application-layer-enforcement--ale-.md)
</dt> <dt>

[ALE Layers](ale-layers.md)
</dt> <dt>

[ALE Multicast/Broadcast Traffic](ale-multicast-broadcast-traffic.md)
</dt> <dt>

[ALE Reauthorization](ale-re-authorization.md)
</dt> <dt>

[ALE Flow Customization](ale-flow-customization.md)
</dt> <dt>

[TCP Packet Flows](tcp-packet-flows.md)
</dt> <dt>

[UDP Packet Flows](udp-packet-flows.md)
</dt> <dt>

[Winsock Functions](/windows/desktop/WinSock/winsock-functions)
</dt> </dl>

 

 