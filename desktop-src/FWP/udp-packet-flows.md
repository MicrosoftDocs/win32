---
title: UDP Packet Flows
description: The order in which the layers of the Windows Filtering Platform (WFP) filter engine are traversed during a typical UDP session.
ms.assetid: ab618c1f-3e7c-4f4b-b4ff-9e396d3258d9
ms.topic: article
ms.date: 05/31/2018
---

# UDP Packet Flows

This section describes the order in which the layers of the Windows Filtering Platform (WFP) filter engine are traversed during a typical UDP session.

> [!Note]  
> UDP packet flows for IPv6 follow the same pattern as for IPv4.

 

> [!Note]  
> All non-TCP packet flows follow the same pattern as UDP packet flows.

 

## UDP Connection Establishment

<dl> Server (receiver) performs Passive Open

-   bind: FWPM\_LAYER\_ALE\_BIND\_REDIRECT\_V4 (Windows 7 / Windows Server 2008 R2 only)
-   bind: FWPM\_LAYER\_ALE\_RESOURCE\_ASSIGNMENT\_V4

  
Client (sender) performs Active Open

-   bind: FWPM\_LAYER\_ALE\_BIND\_REDIRECT\_V4 (Windows 7 / Windows Server 2008 R2 only)
-   bind: FWPM\_LAYER\_ALE\_RESOURCE\_ASSIGNMENT\_V4
-   sendto: FWPM\_LAYER\_ALE\_CONNECT\_REDIRECT\_V4 (Windows 7 / Windows Server 2008 R2 only)
-   sendto: FWPM\_LAYER\_ALE\_AUTH\_CONNECT\_V4
-   FWPM\_LAYER\_ALE\_FLOW\_ESTABLISHED\_V4
-   data: FWPM\_LAYER\_DATAGRAM\_DATA\_V4
-   UDP message: FWPM\_LAYER\_OUTBOUND\_TRANSPORT\_V4
-   IP datagrams: FWPM\_LAYER\_OUTBOUND\_IPPACKET\_V4

  
Server

-   IP datagrams: FWPM\_LAYER\_INBOUND\_IPPACKET\_V4
-   UDP message: FWPM\_LAYER\_INBOUND\_TRANSPORT\_V4
-   UDP message: FWPM\_LAYER\_ALE\_AUTH\_RECV\_ACCEPT\_V4
-   FWPM\_LAYER\_ALE\_FLOW\_ESTABLISHED\_V4
-   data: FWPM\_LAYER\_DATAGRAM\_DATA\_V4

  
</dl>

## UDP Message Received with No One Listening on the Port or Protocol

Server (receiver)

-   IP datagrams: FWPM\_LAYER\_INBOUND\_IPPACKET\_V4
-   IP datagrams: FWPM\_LAYER\_INBOUND\_IPPACKET\_V4\_DISCARD
-   ICMP Dest Unreachable: FWPM\_LAYER\_OUTBOUND\_ICMP\_ERROR\_V4
-   ICMP Dest Unreachable: FWPM\_LAYER\_OUTBOUND\_TRANSPORT\_V4
-   ICMP Dest Unreachable: FWPM\_LAYER\_OUTBOUND\_IPPACKET\_V4

> [!Note]  
> UDP with no endpoint is indicated at IPPACKET discard with a specific error condition. Block this packet at IPPACKET discard to cause the stack not to send the corresponding event (ICMP error).

 

## Successful Reauthorization of a UDP Packet

Server (receiver)

-   IP datagrams: FWPM\_LAYER\_INBOUND\_IPPACKET\_V4
-   UDP message: FWPM\_LAYER\_INBOUND\_TRANSPORT\_V4
-   UDP message: FWPM\_LAYER\_ALE\_AUTH\_RECV\_ACCEPT\_V4
-   UDP message: FWPM\_LAYER\_DATAGRAM\_DATA\_V4(INBOUND)

## Failed Reauthorization of a UDP Packet

Server (receiver)

-   IP datagrams: FWPM\_LAYER\_INBOUND\_IPPACKET\_V4
-   UDP message: FWPM\_LAYER\_INBOUND\_TRANSPORT\_V4
-   UDP message: FWPM\_LAYER\_ALE\_AUTH\_RECV\_ACCEPT\_V4
-   UDP message: FWPM\_LAYER\_ALE\_AUTH\_RECV\_ACCEPT\_V4\_DISCARD

## UDP Connection Termination

UDP connection termination is not indicated at any WFP layer.

## Related topics

<dl> <dt>

[ALE Reauthorization](ale-re-authorization.md)
</dt> <dt>

[**Filtering Layer Identifiers**](management-filtering-layer-identifiers-.md)
</dt> </dl>

 

 




