---
title: ALE Layers
description: Application Layer Enforcement (ALE) consists of several filtering layers and many matching discard layers.
ms.assetid: 3ac71787-2350-4a60-b0bf-b00b52d30b83
ms.topic: article
ms.date: 05/31/2018
---

# ALE Layers

The Application Layer Enforcement (ALE) consists of several filtering layers and many matching discard layers. All the Windows Filtering Platform (WFP) filtering engine layers, including ALE, are described in [**Filtering Layer Identifiers**](management-filtering-layer-identifiers-.md). This topic contains a more detailed description of the filtering layers that are part of ALE.

## RESOURCE\_ASSIGNMENT

A filter at the [**FWPM\_LAYER\_ALE\_RESOURCE\_ASSIGNMENT\_V{4\|6}**](management-filtering-layer-identifiers-.md) layer is matched for network bind operations, explicit or implicit.

If a filter at this layer is matched to authorize raw socket creation, the [**FWP\_CONDITION\_FLAG\_IS\_RAW\_ENDPOINT**](filtering-condition-flags-.md) flag will be set.

If a filter at this layer is matched to authorize promiscuous mode receiving, the [**FWP\_CONDITION\_ALE\_PROMISCUOUS\_MODE**](filtering-condition-identifiers-.md) field will be set to SIO\_RCVALL. For a description of SIO\_RCVALL, see [**WSAIoctl**](/windows/desktop/api/winsock2/nf-winsock2-wsaioctl).

> [!Note]  
> This is the only layer where promiscuous mode can be filtered.

 

If no port is specified during **bind()**, that is, port is set to 0 (zero), then the TCP/IP stack will select a port from the dynamic port range (19152–65535). The selected port will be classified at this layer along with the [**FWP\_CONDITION\_FLAG\_IS\_WILDCARD\_BIND**](filtering-condition-flags-.md) flag.

If the local address is not specified in the [**bind()**](/windows/desktop/api/winsock/nf-winsock-bind) call, the local address field is set to [**FWP\_EMPTY**](/windows/desktop/api/Fwptypes/ne-fwptypes-fwp_data_type).

## AUTH\_LISTEN

A filter at the [**FWPM\_LAYER\_ALE\_AUTH\_LISTEN\_V{4\|6}**](management-filtering-layer-identifiers-.md) layer is matched for TCP [**listen()**](/windows/desktop/api/winsock2/nf-winsock2-listen) calls.

## AUTH\_RECV\_ACCEPT

A filter at the [**FWPM\_LAYER\_ALE\_AUTH\_RECV\_ACCEPT\_V{4\|6}**](management-filtering-layer-identifiers-.md) layer is matched for TCP [**accept()**](/windows/desktop/api/winsock2/nf-winsock2-accept) calls, for first UDP packets (unicast) from a unique remote address/port tuple, and for first inbound non-error ICMP messages (unicast) with a unique ICMP type, code, and ID.

> [!Note]  
> Protocols that are not TCP or ICMP are treated like UDP.

 

TCP packets received by raw sockets are handled similarly to UDP traffic. That is, only the first TCP [**send()**](/windows/desktop/api/winsock2/nf-winsock2-send) and the first TCP [**recv()**](/windows/desktop/api/winsock/nf-winsock-recv) over raw sockets will be filtered.

## AUTH\_CONNECT

A filter at the [**FWPM\_LAYER\_ALE\_AUTH\_CONNECT\_V{4\|6}**](management-filtering-layer-identifiers-.md) layer is matched for TCP [**connect()**](/windows/desktop/api/winsock2/nf-winsock2-connect) calls, for first UDP packets sent to a unique remote address and port tuple, and for first outbound non-error ICMP messages with a unique ICMP type, code, and ID.

> [!Note]  
> Protocols that are not TCP or ICMP are treated like UDP.

 

TCP packets sent by raw sockets are handled similarly to UDP traffic. That is, only the first TCP [**send()**](/windows/desktop/api/winsock2/nf-winsock2-send) and the first TCP [**recv()**](/windows/desktop/api/winsock/nf-winsock-recv) over raw sockets will be filtered.

## FLOW\_ESTABLISHED

A filter at the [**FWPM\_LAYER\_ALE\_FLOW\_ESTABLISHED\_V{4\|6}**](management-filtering-layer-identifiers-.md) layer is matched after a TCP three-way handshake has successfully completed. For non-TCP traffic, the filter is matched immediately after filters from **AUTH\_RECV\_ACCEPT** or **AUTH\_CONNECT** layers are matched.

A filter at this layer should not return Block or Permit.

This layer is used by callout drivers to track connection state, described in detail in the [Windows Driver Kit](/windows-hardware/drivers/network/windows-filtering-platform-callout-drivers2) documentation.

## RESOURCE\_RELEASE

A filter at the [**FWPM\_LAYER\_ALE\_RESOURCE\_RELEASE\_V{4\|6}**](management-filtering-layer-identifiers-.md) layer is matched after resources that were allocated via **RESOURCE\_ASSIGNMENT** have been freed.

## ENDPOINT\_CLOSURE

A filter at the [**FWPM\_LAYER\_ALE\_ENDPOINT\_CLOSURE\_V{4\|6}**](management-filtering-layer-identifiers-.md) layer is matched when a connected TCP flow or UDP sockets endpoint is closed.

## CONNECT\_REDIRECT

A filter at the [**FWPM\_LAYER\_ALE\_CONNECT\_REDIRECT\_V{4\|6}**](management-filtering-layer-identifiers-.md) layer allows for modification of remote addresses and ports. The outbound connection will be redirected for the duration of that connection.

## BIND\_REDIRECT

A filter at the [**FWPM\_LAYER\_ALE\_BIND\_REDIRECT\_V{4\|6}**](management-filtering-layer-identifiers-.md) layer allows for modification of the underlying socket's local address and ports. The local socket will be redirected for the lifetime of the socket

## ALE DISCARD Layers

For each of the ALE layers described above the filtering engine contains a matching discard layer. The ALE discard layers are used by callouts for logging purposes. Packets and indications that have been discarded at one of the ALE filtering layers are indicated to the matching ALE discard layer.

## Related topics

<dl> <dt>

[Application Layer Enforcement (ALE)](application-layer-enforcement--ale-.md)
</dt> <dt>

[ALE Stateful Filtering](ale-stateful-filtering.md)
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
</dt> <dt>

[**Filtering Condition Flags**](filtering-condition-flags-.md)
</dt> <dt>

[**Filtering Conditions Available At Each Filtering Layer**](filtering-conditions-available-at-each-filtering-layer.md)
</dt> </dl>

 

 