---
title: TCP Packet Flows
description: The order in which the layers of the Windows Filtering Platform (WFP) filter engine are traversed during a typical TCP session.
ms.assetid: 75319c91-f77b-4dec-b94f-36772f1f1d53
ms.topic: article
ms.date: 05/31/2018
---

# TCP Packet Flows

This section describes the order in which the layers of the Windows Filtering Platform (WFP) filter engine are traversed during a typical TCP session.

> [!Note]  
> TCP packet flows for IPv6 follow the same pattern as for IPv4.

 

> [!Note]  
> Non-TCP packet flows follow the same pattern as [UDP packet flows](udp-packet-flows.md).

 

## TCP Connection Establishment

<dl> Server (receiver) performs Passive Open

-   bind: FWPM\_LAYER\_ALE\_BIND\_REDIRECT\_V4 (Windows 7 / Windows Server 2008 R2 only)
-   bind: FWPM\_LAYER\_ALE\_RESOURCE\_ASSIGNMENT\_V4
-   listen: FWPM\_LAYER\_ALE\_AUTH\_LISTEN\_V4

  
Client (sender) performs Active Open

-   bind: FWPM\_LAYER\_ALE\_BIND\_REDIRECT\_V4 (Windows 7 / Windows Server 2008 R2 only)
-   bind: FWPM\_LAYER\_ALE\_RESOURCE\_ASSIGNMENT\_V4
-   connect: FWPM\_LAYER\_ALE\_CONNECT\_REDIRECT\_V4 (Windows 7 / Windows Server 2008 R2 only)
-   connect: FWPM\_LAYER\_ALE\_AUTH\_CONNECT\_V4
-   SYN: FWPM\_LAYER\_OUTBOUND\_TRANSPORT\_V4
-   SYN: FWPM\_LAYER\_OUTBOUND\_IPPACKET\_V4

  
Server

-   SYN: FWPM\_LAYER\_INBOUND\_IPPACKET\_V4
-   SYN: FWPM\_LAYER\_INBOUND\_TRANSPORT\_V4
-   SYN: FWPM\_LAYER\_ALE\_AUTH\_RECV\_ACCEPT\_V4
-   SYN-ACK: FWPM\_LAYER\_OUTBOUND\_TRANSPORT\_V4
-   SYN-ACK: FWPM\_LAYER\_OUTBOUND\_IPPACKET\_V4

  
Client

-   SYN-ACK: FWPM\_LAYER\_INBOUND\_IPPACKET\_V4
-   SYN-ACK: FWPM\_LAYER\_INBOUND\_TRANSPORT\_V4
-   FWPM\_LAYER\_ALE\_FLOW\_ESTABLISHED\_V4
-   ACK: FWPM\_LAYER\_OUTBOUND\_TRANSPORT\_V4
-   ACK: FWPM\_LAYER\_OUTBOUND\_IPPACKET\_V4

  
Server

-   ACK: FWPM\_LAYER\_INBOUND\_IPPACKET\_V4
-   ACK: FWPM\_LAYER\_INBOUND\_TRANSPORT\_V4
-   FWPM\_LAYER\_ALE\_FLOW\_ESTABLISHED\_V4
-   Listen completes. Server can perform an accept.

  
</dl>

## TCP SYN Received with No One Listening on the Port or Protocol

Server (receiver)

-   SYN: FWPM\_LAYER\_INBOUND\_IPPACKET\_V4
-   SYN: FWPM\_LAYER\_INBOUND\_TRANSPORT\_V4\_DISCARD
-   RST: FWPM\_LAYER\_OUTBOUND\_TRANSPORT\_V4
-   RST: FWPM\_LAYER\_OUTBOUND\_IPPACKET\_V4

> [!Note]  
> TCP SYN with no endpoint is indicated at TRANSPORT discard with a specific error condition. Block this packet at TRANSPORT discard to cause the stack not to send the corresponding event (RST). For an example of stealth-mode filtering, see [Preventing Port Scanning](preventing-port-scanning.md).

 

## Data Transmitted Over a TCP Connection

<dl> Client (sender)

-   send
-   data: FWPM\_LAYER\_STREAM\_V4
-   TCP segments: FWPM\_LAYER\_OUTBOUND\_TRANSPORT\_V4
-   IP datagrams: FWPM\_LAYER\_OUTBOUND\_IPPACKET\_V4

  
Server (receiver)

-   IP datagrams: FWPM\_LAYER\_INBOUND\_IPPACKET\_V4
-   TCP segments: FWPM\_LAYER\_INBOUND\_TRANSPORT\_V4
-   data: FWPM\_LAYER\_STREAM\_V4
-   Data is available to read.

  
</dl>

## Successful Reauthorization of a TCP Packet

Server (receiver)

-   IP datagrams: FWPM\_LAYER\_INBOUND\_IPPACKET\_V4
-   TCP segment: FWPM\_LAYER\_INBOUND\_TRANSPORT\_V4
-   TCP segment: FWPM\_LAYER\_ALE\_AUTH\_RECV\_ACCEPT\_V4
-   data: FWPM\_LAYER\_STREAM\_V4(INBOUND)

## Failed Reauthorization of a TCP Packet

Server (receiver)

-   IP datagrams: FWPM\_LAYER\_INBOUND\_IPPACKET\_V4
-   TCP segment: FWPM\_LAYER\_INBOUND\_TRANSPORT\_V4
-   TCP segment: FWPM\_LAYER\_ALE\_AUTH\_RECV\_ACCEPT\_V4
-   TCP segment: FWPM\_LAYER\_ALE\_AUTH\_RECV\_ACCEPT\_V4\_DISCARD

## TCP Connection Termination

TCP connection termination is not indicated at any WFP layer.

## Related topics

<dl> <dt>

[ALE Reauthorization](ale-re-authorization.md)
</dt> <dt>

[**Filtering Layer Identifiers**](management-filtering-layer-identifiers-.md)
</dt> </dl>

 

 




