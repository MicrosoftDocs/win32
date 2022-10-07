---
title: Filtering Layer Identifiers (Fwpmu.h)
description: WFP API management filtering layer identifier constants.
ms.assetid: 3b2daef1-558b-4e3a-a98a-f4dfa80a29c0
topic_type:
- apiref
api_name:
- FWPM_LAYER_INBOUND_IPPACKET_V4 / FWPM_LAYER_INBOUND_IPPACKET_V6
- FWPM_LAYER_INBOUND_IPPACKET_V4_DISCARD / FWPM_LAYER_INBOUND_IPPACKET_V6_DISCARD
- FWPM_LAYER_OUTBOUND_IPPACKET_V4 / FWPM_LAYER_OUTBOUND_IPPACKET_V6
- FWPM_LAYER_OUTBOUND_IPPACKET_V4_DISCARD / FWPM_LAYER_OUTBOUND_IPPACKET_V6_DISCARD
- FWPM_LAYER_IPFORWARD_V4 / FWPM_LAYER_IPFORWARD_V6
- FWPM_LAYER_IPFORWARD_V4_DISCARD / FWPM_LAYER_IPFORWARD_V6_DISCARD
- FWPM_LAYER_INBOUND_TRANSPORT_V4 / FWPM_LAYER_INBOUND_TRANSPORT_V6
- FWPM_LAYER_INBOUND_TRANSPORT_V4_DISCARD / FWPM_LAYER_INBOUND_TRANSPORT_V6_DISCARD
- FWPM_LAYER_OUTBOUND_TRANSPORT_V4 / FWPM_LAYER_OUTBOUND_TRANSPORT_V6
- FWPM_LAYER_OUTBOUND_TRANSPORT_V4_DISCARD / FWPM_LAYER_OUTBOUND_TRANSPORT_V6_DISCARD
- FWPM_LAYER_STREAM_V4 / FWPM_LAYER_STREAM_V6
- FWPM_LAYER_STREAM_V4_DISCARD / FWPM_LAYER_STREAM_V6_DISCARD
- FWPM_LAYER_DATAGRAM_DATA_V4 / FWPM_LAYER_DATAGRAM_DATA_V6
- FWPM_LAYER_DATAGRAM_DATA_V4_DISCARD / FWPM_LAYER_DATAGRAM_DATA_V6_DISCARD
- FWPM_LAYER_INBOUND_ICMP_ERROR_V4 / FWPM_LAYER_INBOUND_ICMP_ERROR_V6
- FWPM_LAYER_INBOUND_ICMP_ERROR_V4_DISCARD / FWPM_LAYER_INBOUND_ICMP_ERROR_V6_DISCARD
- FWPM_LAYER_OUTBOUND_ICMP_ERROR_V4 / FWPM_LAYER_OUTBOUND_ICMP_ERROR_V6
- FWPM_LAYER_OUTBOUND_ICMP_ERROR_V4_DISCARD / FWPM_LAYER_OUTBOUND_ICMP_ERROR_V6_DISCARD
- FWPM_LAYER_ALE_RESOURCE_ASSIGNMENT_V4 / FWPM_LAYER_ALE_RESOURCE_ASSIGNMENT_V6
- FWPM_LAYER_ALE_RESOURCE_ASSIGNMENT_V4_DISCARD / FWPM_LAYER_ALE_RESOURCE_ASSIGNMENT_V6_DISCARD
- FWPM_LAYER_ALE_AUTH_LISTEN_V4 / FWPM_LAYER_ALE_AUTH_LISTEN_V6
- FWPM_LAYER_ALE_AUTH_LISTEN_V4_DISCARD / FWPM_LAYER_ALE_AUTH_LISTEN_V6_DISCARD
- FWPM_LAYER_ALE_AUTH_RECV_ACCEPT_V4 / FWPM_LAYER_ALE_AUTH_RECV_ACCEPT_V6
- FWPM_LAYER_ALE_AUTH_RECV_ACCEPT_V4_DISCARD / FWPM_LAYER_ALE_AUTH_RECV_ACCEPT_V6_DISCARD
- FWPM_LAYER_ALE_AUTH_CONNECT_V4 / FWPM_LAYER_ALE_AUTH_CONNECT_V6
- FWPM_LAYER_ALE_AUTH_CONNECT_V4_DISCARD / FWPM_LAYER_ALE_AUTH_CONNECT_V6_DISCARD
- FWPM_LAYER_ALE_FLOW_ESTABLISHED_V4 / FWPM_LAYER_ALE_FLOW_ESTABLISHED_V6
- FWPM_LAYER_ALE_FLOW_ESTABLISHED_V4_DISCARD / FWPM_LAYER_ALE_FLOW_ESTABLISHED_V6_DISCARD
- FWPM_LAYER_INBOUND_MAC_FRAME_ETHERNET
- FWPM_LAYER_OUTBOUND_MAC_FRAME_ETHERNET
- FWPM_LAYER_INBOUND_MAC_FRAME_NATIVE
- FWPM_LAYER_OUTBOUND_MAC_FRAME_NATIVE
- FWPM_LAYER_INGRESS_VSWITCH_ETHERNET
- FWPM_LAYER_EGRESS_VSWITCH_ETHERNET
- FWPM_LAYER_INGRESS_VSWITCH_TRANSPORT_V4 / FWPM_LAYER_INGRESS_VSWITCH_TRANSPORT_V6
- FWPM_LAYER_EGRESS_VSWITCH_TRANSPORT_V4 / FWPM_LAYER_EGRESS_VSWITCH_TRANSPORT_V6
- FWPM_LAYER_IPSEC_KM_DEMUX_V4 / FWPM_LAYER_IPSEC_KM_DEMUX_V6
- FWPM_LAYER_IPSEC_V4 / FWPM_LAYER_IPSEC_V6
- FWPM_LAYER_IKEEXT_V4 / FWPM_LAYER_IKEEXT_V6
- FWPM_LAYER_RPC_UM
- FWPM_LAYER_RPC_EPMAP
- FWPM_LAYER_RPC_EP_ADD
- FWPM_LAYER_RPC_PROXY_CONN
- FWPM_LAYER_RPC_PROXY_IF
- FWPM_LAYER_KM_AUTHORIZATION
- FWPM_LAYER_NAME_RESOLUTION_CACHE_V4 / FWPM_LAYER_NAME_RESOLUTION_CACHE_V6
- FWPM_LAYER_ALE_RESOURCE_RELEASE_V4 / FWPM_LAYER_ALE_RESOURCE_RELEASE_V6
- FWPM_LAYER_ALE_ENDPOINT_CLOSURE_V4 / FWPM_LAYER_ALE_ENDPOINT_CLOSURE_V6
- FWPM_LAYER_ALE_CONNECT_REDIRECT_V4 / FWPM_LAYER_ALE_CONNECT_REDIRECT_V6
- FWPM_LAYER_ALE_BIND_REDIRECT_V4 / FWPM_LAYER_ALE_BIND_REDIRECT_V6
- FWPM_LAYER_STREAM_PACKET_V4 / FWPM_LAYER_STREAM_PACKET_V6
api_location:
- fwpmu.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# Filtering Layer Identifiers

The Windows Filtering Platform (WFP) layer identifiers are each represented by a GUID. These identifiers are defined as follows.

The V4 and V6 suffixes at the end of the layer identifiers indicate whether the layer is located in the IPv4 network stack or in the IPv6 network stack.

<dl> <dt>

<span id="FWPM_LAYER_INBOUND_IPPACKET_V4___FWPM_LAYER_INBOUND_IPPACKET_V6"></span><span id="fwpm_layer_inbound_ippacket_v4___fwpm_layer_inbound_ippacket_v6"></span>**FWPM\_LAYER\_INBOUND\_IPPACKET\_V4 / FWPM\_LAYER\_INBOUND\_IPPACKET\_V6**
</dt> <dd> <dl> <dt>



This filtering layer is located in the receive path just after the IP header of a received packet has been parsed but before any IP header processing takes place. No IPsec decryption or reassembly has occurred.


</dt> </dl> </dd> <dt>

<span id="FWPM_LAYER_INBOUND_IPPACKET_V4_DISCARD___FWPM_LAYER_INBOUND_IPPACKET_V6_DISCARD"></span><span id="fwpm_layer_inbound_ippacket_v4_discard___fwpm_layer_inbound_ippacket_v6_discard"></span>**FWPM\_LAYER\_INBOUND\_IPPACKET\_V4\_DISCARD / FWPM\_LAYER\_INBOUND\_IPPACKET\_V6\_DISCARD**
</dt> <dd> <dl> <dt>



This filtering layer is located in the receive path for inspecting any received packets that have been discarded at the network layer.


</dt> </dl> </dd> <dt>

<span id="FWPM_LAYER_OUTBOUND_IPPACKET_V4___FWPM_LAYER_OUTBOUND_IPPACKET_V6"></span><span id="fwpm_layer_outbound_ippacket_v4___fwpm_layer_outbound_ippacket_v6"></span>**FWPM\_LAYER\_OUTBOUND\_IPPACKET\_V4 / FWPM\_LAYER\_OUTBOUND\_IPPACKET\_V6**
</dt> <dd> <dl> <dt>



This filtering layer is located in the send path just before the sent packet is evaluated for fragmentation. All IP header processing is complete and all extension headers are in place. Any IPsec authentication and encryption has already occurred.


</dt> </dl> </dd> <dt>

<span id="FWPM_LAYER_OUTBOUND_IPPACKET_V4_DISCARD___FWPM_LAYER_OUTBOUND_IPPACKET_V6_DISCARD"></span><span id="fwpm_layer_outbound_ippacket_v4_discard___fwpm_layer_outbound_ippacket_v6_discard"></span>**FWPM\_LAYER\_OUTBOUND\_IPPACKET\_V4\_DISCARD / FWPM\_LAYER\_OUTBOUND\_IPPACKET\_V6\_DISCARD**
</dt> <dd> <dl> <dt>



This filtering layer is located in the send path for inspecting any sent packets that have been discarded at the network layer.


</dt> </dl> </dd> <dt>

<span id="FWPM_LAYER_IPFORWARD_V4___FWPM_LAYER_IPFORWARD_V6"></span><span id="fwpm_layer_ipforward_v4___fwpm_layer_ipforward_v6"></span>**FWPM\_LAYER\_IPFORWARD\_V4 / FWPM\_LAYER\_IPFORWARD\_V6**
</dt> <dd> <dl> <dt>



This filtering layer is located in the forwarding path at the point where a received packet is forwarded.


</dt> </dl> </dd> <dt>

<span id="FWPM_LAYER_IPFORWARD_V4_DISCARD___FWPM_LAYER_IPFORWARD_V6_DISCARD"></span><span id="fwpm_layer_ipforward_v4_discard___fwpm_layer_ipforward_v6_discard"></span>**FWPM\_LAYER\_IPFORWARD\_V4\_DISCARD / FWPM\_LAYER\_IPFORWARD\_V6\_DISCARD**
</dt> <dd> <dl> <dt>



This filtering layer is located in the forwarding path for inspecting any forwarded packets that have been discarded at the forwarding layer.


</dt> </dl> </dd> <dt>

<span id="FWPM_LAYER_INBOUND_TRANSPORT_V4___FWPM_LAYER_INBOUND_TRANSPORT_V6"></span><span id="fwpm_layer_inbound_transport_v4___fwpm_layer_inbound_transport_v6"></span>**FWPM\_LAYER\_INBOUND\_TRANSPORT\_V4 / FWPM\_LAYER\_INBOUND\_TRANSPORT\_V6**
</dt> <dd> <dl> <dt>



This filtering layer is located in the receive path just after a received packet's transport header has been parsed by the network stack at the transport layer, but before any transport layer processing takes place.


</dt> </dl> </dd> <dt>

<span id="FWPM_LAYER_INBOUND_TRANSPORT_V4_DISCARD___FWPM_LAYER_INBOUND_TRANSPORT_V6_DISCARD"></span><span id="fwpm_layer_inbound_transport_v4_discard___fwpm_layer_inbound_transport_v6_discard"></span>**FWPM\_LAYER\_INBOUND\_TRANSPORT\_V4\_DISCARD / FWPM\_LAYER\_INBOUND\_TRANSPORT\_V6\_DISCARD**
</dt> <dd> <dl> <dt>



This filtering layer is located in the receive path for inspecting any received packets that have been discarded at the transport layer.


</dt> </dl> </dd> <dt>

<span id="FWPM_LAYER_OUTBOUND_TRANSPORT_V4___FWPM_LAYER_OUTBOUND_TRANSPORT_V6"></span><span id="fwpm_layer_outbound_transport_v4___fwpm_layer_outbound_transport_v6"></span>**FWPM\_LAYER\_OUTBOUND\_TRANSPORT\_V4 / FWPM\_LAYER\_OUTBOUND\_TRANSPORT\_V6**
</dt> <dd> <dl> <dt>



This filtering layer is located in the send path just after a sent packet has been passed to the network layer for processing but before any network layer processing takes place. This filtering layer is located at the top of the network layer instead of at the bottom of the transport layer so that any packets that are sent by third-party transports or as raw packets are filtered at this layer.


</dt> </dl> </dd> <dt>

<span id="FWPM_LAYER_OUTBOUND_TRANSPORT_V4_DISCARD___FWPM_LAYER_OUTBOUND_TRANSPORT_V6_DISCARD"></span><span id="fwpm_layer_outbound_transport_v4_discard___fwpm_layer_outbound_transport_v6_discard"></span>**FWPM\_LAYER\_OUTBOUND\_TRANSPORT\_V4\_DISCARD / FWPM\_LAYER\_OUTBOUND\_TRANSPORT\_V6\_DISCARD**
</dt> <dd> <dl> <dt>



This filtering layer is located in the send path for inspecting any sent packets that have been discarded at the transport layer.


</dt> </dl> </dd> <dt>

<span id="FWPM_LAYER_STREAM_V4___FWPM_LAYER_STREAM_V6"></span><span id="fwpm_layer_stream_v4___fwpm_layer_stream_v6"></span>**FWPM\_LAYER\_STREAM\_V4 / FWPM\_LAYER\_STREAM\_V6**
</dt> <dd> <dl> <dt>



This filtering layer is located in the stream data path. This layer allows for inspecting network data on a per stream basis. At the stream layer, the network data is bidirectional.


</dt> </dl> </dd> <dt>

<span id="FWPM_LAYER_STREAM_V4_DISCARD___FWPM_LAYER_STREAM_V6_DISCARD"></span><span id="fwpm_layer_stream_v4_discard___fwpm_layer_stream_v6_discard"></span>**FWPM\_LAYER\_STREAM\_V4\_DISCARD / FWPM\_LAYER\_STREAM\_V6\_DISCARD**
</dt> <dd> <dl> <dt>



This filtering layer is located in the stream data path for inspecting any stream data that has been discarded.


</dt> </dl> </dd> <dt>

<span id="FWPM_LAYER_DATAGRAM_DATA_V4___FWPM_LAYER_DATAGRAM_DATA_V6"></span><span id="fwpm_layer_datagram_data_v4___fwpm_layer_datagram_data_v6"></span>**FWPM\_LAYER\_DATAGRAM\_DATA\_V4 / FWPM\_LAYER\_DATAGRAM\_DATA\_V6**
</dt> <dd> <dl> <dt>



This filtering layer is located in the datagram data path. This layer allows for inspecting network data on a per datagram basis. At the datagram layer, the network data is bidirectional.


</dt> </dl> </dd> <dt>

<span id="FWPM_LAYER_DATAGRAM_DATA_V4_DISCARD___FWPM_LAYER_DATAGRAM_DATA_V6_DISCARD"></span><span id="fwpm_layer_datagram_data_v4_discard___fwpm_layer_datagram_data_v6_discard"></span>**FWPM\_LAYER\_DATAGRAM\_DATA\_V4\_DISCARD / FWPM\_LAYER\_DATAGRAM\_DATA\_V6\_DISCARD**
</dt> <dd> <dl> <dt>



This filtering layer is located in the datagram data path for inspecting any datagrams that have been discarded.


</dt> </dl> </dd> <dt>

<span id="FWPM_LAYER_INBOUND_ICMP_ERROR_V4___FWPM_LAYER_INBOUND_ICMP_ERROR_V6"></span><span id="fwpm_layer_inbound_icmp_error_v4___fwpm_layer_inbound_icmp_error_v6"></span>**FWPM\_LAYER\_INBOUND\_ICMP\_ERROR\_V4 / FWPM\_LAYER\_INBOUND\_ICMP\_ERROR\_V6**
</dt> <dd> <dl> <dt>



This filtering layer is located in the receive path for inspecting received ICMP error messages for the transport protocol.


</dt> </dl> </dd> <dt>

<span id="FWPM_LAYER_INBOUND_ICMP_ERROR_V4_DISCARD___FWPM_LAYER_INBOUND_ICMP_ERROR_V6_DISCARD"></span><span id="fwpm_layer_inbound_icmp_error_v4_discard___fwpm_layer_inbound_icmp_error_v6_discard"></span>**FWPM\_LAYER\_INBOUND\_ICMP\_ERROR\_V4\_DISCARD / FWPM\_LAYER\_INBOUND\_ICMP\_ERROR\_V6\_DISCARD**
</dt> <dd> <dl> <dt>



This filtering layer is located in the receive path for inspecting received ICMP error messages that have been discarded.


</dt> </dl> </dd> <dt>

<span id="FWPM_LAYER_OUTBOUND_ICMP_ERROR_V4___FWPM_LAYER_OUTBOUND_ICMP_ERROR_V6"></span><span id="fwpm_layer_outbound_icmp_error_v4___fwpm_layer_outbound_icmp_error_v6"></span>**FWPM\_LAYER\_OUTBOUND\_ICMP\_ERROR\_V4 / FWPM\_LAYER\_OUTBOUND\_ICMP\_ERROR\_V6**
</dt> <dd> <dl> <dt>



This filtering layer is located in the send path for inspecting received ICMP error messages for the transport protocol.


</dt> </dl> </dd> <dt>

<span id="FWPM_LAYER_OUTBOUND_ICMP_ERROR_V4_DISCARD___FWPM_LAYER_OUTBOUND_ICMP_ERROR_V6_DISCARD"></span><span id="fwpm_layer_outbound_icmp_error_v4_discard___fwpm_layer_outbound_icmp_error_v6_discard"></span>**FWPM\_LAYER\_OUTBOUND\_ICMP\_ERROR\_V4\_DISCARD / FWPM\_LAYER\_OUTBOUND\_ICMP\_ERROR\_V6\_DISCARD**
</dt> <dd> <dl> <dt>



This filtering layer is located in the send path for inspecting received ICMP error messages that have been discarded.


</dt> </dl> </dd> <dt>

<span id="FWPM_LAYER_ALE_RESOURCE_ASSIGNMENT_V4___FWPM_LAYER_ALE_RESOURCE_ASSIGNMENT_V6"></span><span id="fwpm_layer_ale_resource_assignment_v4___fwpm_layer_ale_resource_assignment_v6"></span>**FWPM\_LAYER\_ALE\_RESOURCE\_ASSIGNMENT\_V4 / FWPM\_LAYER\_ALE\_RESOURCE\_ASSIGNMENT\_V6**
</dt> <dd> <dl> <dt>



This filtering layer allows for authorizing transport port assignments, bind requests, promiscuous mode requests, and raw mode requests.

See [ALE Layers](ale-layers.md) for more information.


</dt> </dl> </dd> <dt>

<span id="FWPM_LAYER_ALE_RESOURCE_ASSIGNMENT_V4_DISCARD___FWPM_LAYER_ALE_RESOURCE_ASSIGNMENT_V6_DISCARD"></span><span id="fwpm_layer_ale_resource_assignment_v4_discard___fwpm_layer_ale_resource_assignment_v6_discard"></span>**FWPM\_LAYER\_ALE\_RESOURCE\_ASSIGNMENT\_V4\_DISCARD / FWPM\_LAYER\_ALE\_RESOURCE\_ASSIGNMENT\_V6\_DISCARD**
</dt> <dd> <dl> <dt>



This filtering layer allows for inspecting the following discarded items: transport port assignments, bind requests, promiscuous mode requests, and raw mode requests.


</dt> </dl> </dd> <dt>

<span id="FWPM_LAYER_ALE_AUTH_LISTEN_V4___FWPM_LAYER_ALE_AUTH_LISTEN_V6"></span><span id="fwpm_layer_ale_auth_listen_v4___fwpm_layer_ale_auth_listen_v6"></span>**FWPM\_LAYER\_ALE\_AUTH\_LISTEN\_V4 / FWPM\_LAYER\_ALE\_AUTH\_LISTEN\_V6**
</dt> <dd> <dl> <dt>



This filtering layer allows for authorizing TCP listen requests.

See [ALE Layers](ale-layers.md) for more information.


</dt> </dl> </dd> <dt>

<span id="FWPM_LAYER_ALE_AUTH_LISTEN_V4_DISCARD___FWPM_LAYER_ALE_AUTH_LISTEN_V6_DISCARD"></span><span id="fwpm_layer_ale_auth_listen_v4_discard___fwpm_layer_ale_auth_listen_v6_discard"></span>**FWPM\_LAYER\_ALE\_AUTH\_LISTEN\_V4\_DISCARD / FWPM\_LAYER\_ALE\_AUTH\_LISTEN\_V6\_DISCARD**
</dt> <dd> <dl> <dt>



This filtering layer allows for inspecting TCP listen requests that have been discarded.


</dt> </dl> </dd> <dt>

<span id="FWPM_LAYER_ALE_AUTH_RECV_ACCEPT_V4___FWPM_LAYER_ALE_AUTH_RECV_ACCEPT_V6"></span><span id="fwpm_layer_ale_auth_recv_accept_v4___fwpm_layer_ale_auth_recv_accept_v6"></span>**FWPM\_LAYER\_ALE\_AUTH\_RECV\_ACCEPT\_V4 / FWPM\_LAYER\_ALE\_AUTH\_RECV\_ACCEPT\_V6**
</dt> <dd> <dl> <dt>



This filtering layer allows for authorizing accept requests for incoming TCP connections, as well as authorizing incoming non-TCP traffic based on the first packet received.

See [ALE Layers](ale-layers.md) for more information.


</dt> </dl> </dd> <dt>

<span id="FWPM_LAYER_ALE_AUTH_RECV_ACCEPT_V4_DISCARD___FWPM_LAYER_ALE_AUTH_RECV_ACCEPT_V6_DISCARD"></span><span id="fwpm_layer_ale_auth_recv_accept_v4_discard___fwpm_layer_ale_auth_recv_accept_v6_discard"></span>**FWPM\_LAYER\_ALE\_AUTH\_RECV\_ACCEPT\_V4\_DISCARD / FWPM\_LAYER\_ALE\_AUTH\_RECV\_ACCEPT\_V6\_DISCARD**
</dt> <dd> <dl> <dt>



This filtering layer allows for inspecting accept requests for incoming TCP connections that have been discarded, as well as inspecting authorizations for incoming non-TCP traffic that have been discarded.


</dt> </dl> </dd> <dt>

<span id="FWPM_LAYER_ALE_AUTH_CONNECT_V4___FWPM_LAYER_ALE_AUTH_CONNECT_V6"></span><span id="fwpm_layer_ale_auth_connect_v4___fwpm_layer_ale_auth_connect_v6"></span>**FWPM\_LAYER\_ALE\_AUTH\_CONNECT\_V4 / FWPM\_LAYER\_ALE\_AUTH\_CONNECT\_V6**
</dt> <dd> <dl> <dt>



This filtering layer allows for authorizing connect requests for outgoing TCP connections, as well as authorizing outgoing non-TCP traffic based on the first packet sent.

See [ALE Layers](ale-layers.md) for more information.


</dt> </dl> </dd> <dt>

<span id="FWPM_LAYER_ALE_AUTH_CONNECT_V4_DISCARD___FWPM_LAYER_ALE_AUTH_CONNECT_V6_DISCARD"></span><span id="fwpm_layer_ale_auth_connect_v4_discard___fwpm_layer_ale_auth_connect_v6_discard"></span>**FWPM\_LAYER\_ALE\_AUTH\_CONNECT\_V4\_DISCARD / FWPM\_LAYER\_ALE\_AUTH\_CONNECT\_V6\_DISCARD**
</dt> <dd> <dl> <dt>



This filtering layer allows for inspecting connect requests for outgoing TCP connections that have been discarded, as well as inspecting authorizations for outgoing non-TCP traffic that have been discarded.


</dt> </dl> </dd> <dt>

<span id="FWPM_LAYER_ALE_FLOW_ESTABLISHED_V4___FWPM_LAYER_ALE_FLOW_ESTABLISHED_V6"></span><span id="fwpm_layer_ale_flow_established_v4___fwpm_layer_ale_flow_established_v6"></span>**FWPM\_LAYER\_ALE\_FLOW\_ESTABLISHED\_V4 / FWPM\_LAYER\_ALE\_FLOW\_ESTABLISHED\_V6**
</dt> <dd> <dl> <dt>



This filtering layer allows for notification of when a TCP connection has been established, or when non-TCP traffic has been authorized.

See [ALE Layers](ale-layers.md) for more information.


</dt> </dl> </dd> <dt>

<span id="FWPM_LAYER_ALE_FLOW_ESTABLISHED_V4_DISCARD___FWPM_LAYER_ALE_FLOW_ESTABLISHED_V6_DISCARD"></span><span id="fwpm_layer_ale_flow_established_v4_discard___fwpm_layer_ale_flow_established_v6_discard"></span>**FWPM\_LAYER\_ALE\_FLOW\_ESTABLISHED\_V4\_DISCARD / FWPM\_LAYER\_ALE\_FLOW\_ESTABLISHED\_V6\_DISCARD**
</dt> <dd> <dl> <dt>



This filtering layer allows for inspecting when an established TCP connection has been discarded at the flow established layer, as well as when authorized non-TCP traffic has been discarded at the flow established layer.


</dt> </dl> </dd> <dt>

<span id="FWPM_LAYER_INBOUND_MAC_FRAME_ETHERNET"></span><span id="fwpm_layer_inbound_mac_frame_ethernet"></span>**FWPM\_LAYER\_INBOUND\_MAC\_FRAME\_ETHERNET**
</dt> <dd> <dl> <dt>



This filtering layer is located in the receive path after the MAC (802.3) layer processing has occurred but before the frame is processed by the framing layer. This is the layer after native in which all frames look like Ethernet frames.

> [!Note]  
> Available only in Windows 8 and Windows Server 2012.

 


</dt> </dl> </dd> <dt>

<span id="FWPM_LAYER_OUTBOUND_MAC_FRAME_ETHERNET"></span><span id="fwpm_layer_outbound_mac_frame_ethernet"></span>**FWPM\_LAYER\_OUTBOUND\_MAC\_FRAME\_ETHERNET**
</dt> <dd> <dl> <dt>



This filtering layer is located in the send path after the framing layer processing has occurred but before the frame is processed by the MAC (802.3) layer. This is the layer after native in which all frames look like Ethernet frames.

> [!Note]  
> Available only in Windows 8 and Windows Server 2012.

 


</dt> </dl> </dd> <dt>

<span id="FWPM_LAYER_INBOUND_MAC_FRAME_NATIVE"></span><span id="fwpm_layer_inbound_mac_frame_native"></span>**FWPM\_LAYER\_INBOUND\_MAC\_FRAME\_NATIVE**
</dt> <dd> <dl> <dt>



This filtering layer is located in the receive path after the MAC layer processing has occurred but before the frame is processed by the framing layer. It is the first layer after the Miniport delivers the frame to NDIS.

> [!Note]  
> Available only in Windows 8 and Windows Server 2012.

 


</dt> </dl> </dd> <dt>

<span id="FWPM_LAYER_OUTBOUND_MAC_FRAME_NATIVE"></span><span id="fwpm_layer_outbound_mac_frame_native"></span>**FWPM\_LAYER\_OUTBOUND\_MAC\_FRAME\_NATIVE**
</dt> <dd> <dl> <dt>



This filtering layer is located in the send path after the framing layer processing has occurred but before the frame is processed by the MAC (Native 802.11) layer. It is the first layer after the Miniport delivers the frame to NDIS.

> [!Note]  
> Available only in Windows 8 and Windows Server 2012.

 


</dt> </dl> </dd> <dt>

<span id="FWPM_LAYER_INGRESS_VSWITCH_ETHERNET"></span><span id="fwpm_layer_ingress_vswitch_ethernet"></span>**FWPM\_LAYER\_INGRESS\_VSWITCH\_ETHERNET**
</dt> <dd> <dl> <dt>



This filtering layer is located in the vSwitch ingress path just after the MAC header has been parsed, but before any MAC header processing takes place.

> [!Note]  
> Available only in Windows 8 and Windows Server 2012.

 


</dt> </dl> </dd> <dt>

<span id="FWPM_LAYER_EGRESS_VSWITCH_ETHERNET"></span><span id="fwpm_layer_egress_vswitch_ethernet"></span>**FWPM\_LAYER\_EGRESS\_VSWITCH\_ETHERNET**
</dt> <dd> <dl> <dt>



This filtering layer is located in the vSwitch egress path just after the MAC header has been parsed, but before any MAC header processing takes place.

> [!Note]  
> Available only in Windows 8 and Windows Server 2012.

 


</dt> </dl> </dd> <dt>

<span id="FWPM_LAYER_INGRESS_VSWITCH_TRANSPORT_V4___FWPM_LAYER_INGRESS_VSWITCH_TRANSPORT_V6"></span><span id="fwpm_layer_ingress_vswitch_transport_v4___fwpm_layer_ingress_vswitch_transport_v6"></span>**FWPM\_LAYER\_INGRESS\_VSWITCH\_TRANSPORT\_V4 / FWPM\_LAYER\_INGRESS\_VSWITCH\_TRANSPORT\_V6**
</dt> <dd> <dl> <dt>



This filtering layer is located in the vSwitch ingress path just after the MAC header has been parsed, but before any MAC header processing takes place. This layer allows for TRANSPORT level filtering conditions to aid in filtering traffic.

If a vSwitchPort is in PVLAN or trunk mode, filters at this layer will be bypassed, letting the traffic flow through without any filtering.

If IPv4 is uninstalled in the host, filters in this layer will cause packets to be dropped.

> [!Note]  
> Available only in Windows 8 and Windows Server 2012.

 


</dt> </dl> </dd> <dt>

<span id="FWPM_LAYER_EGRESS_VSWITCH_TRANSPORT_V4___FWPM_LAYER_EGRESS_VSWITCH_TRANSPORT_V6"></span><span id="fwpm_layer_egress_vswitch_transport_v4___fwpm_layer_egress_vswitch_transport_v6"></span>**FWPM\_LAYER\_EGRESS\_VSWITCH\_TRANSPORT\_V4 / FWPM\_LAYER\_EGRESS\_VSWITCH\_TRANSPORT\_V6**
</dt> <dd> <dl> <dt>



This filtering layer is located in the vSwitch egress path just after the MAC header has been parsed, but before any MAC header processing takes place. This layer allows for TRANSPORT level filtering conditions to aid in filtering traffic.

If a vSwitchPort is in PVLAN or trunk mode, filters at this layer will be bypassed, letting the traffic flow through without any filtering.

If IPv4 is uninstalled in the host, filters in this layer will cause packets to be dropped.

> [!Note]  
> Available only in Windows 8 and Windows Server 2012.

 


</dt> </dl> </dd> <dt>

<span id="FWPM_LAYER_IPSEC_KM_DEMUX_V4___FWPM_LAYER_IPSEC_KM_DEMUX_V6"></span><span id="fwpm_layer_ipsec_km_demux_v4___fwpm_layer_ipsec_km_demux_v6"></span>**FWPM\_LAYER\_IPSEC\_KM\_DEMUX\_V4 / FWPM\_LAYER\_IPSEC\_KM\_DEMUX\_V6**
</dt> <dd> <dl> <dt>



This filtering layer is used to determine which keying modules are invoked when the local system is the initiator. This is a user-mode filtering layer.


</dt> </dl> </dd> <dt>

<span id="FWPM_LAYER_IPSEC_V4___FWPM_LAYER_IPSEC_V6"></span><span id="fwpm_layer_ipsec_v4___fwpm_layer_ipsec_v6"></span>**FWPM\_LAYER\_IPSEC\_V4 / FWPM\_LAYER\_IPSEC\_V6**
</dt> <dd> <dl> <dt>



This filtering layer allows the keying module to look up quick-mode policy information when negotiating quick-mode security associations. This is a user-mode filtering layer.


</dt> </dl> </dd> <dt>

<span id="FWPM_LAYER_IKEEXT_V4___FWPM_LAYER_IKEEXT_V6"></span><span id="fwpm_layer_ikeext_v4___fwpm_layer_ikeext_v6"></span>**FWPM\_LAYER\_IKEEXT\_V4 / FWPM\_LAYER\_IKEEXT\_V6**
</dt> <dd> <dl> <dt>



This filtering layer allows the IKE and authenticated IP modules to look up main-mode policy information when negotiating main-mode security associations. This is a user-mode filtering layer.


</dt> </dl> </dd> <dt>

<span id="FWPM_LAYER_RPC_UM"></span><span id="fwpm_layer_rpc_um"></span>**FWPM\_LAYER\_RPC\_UM**
</dt> <dd> <dl> <dt>



This filtering layer allows for inspecting the RPC data fields that are available in user mode. This is a user-mode filtering layer.


</dt> </dl> </dd> <dt>

<span id="FWPM_LAYER_RPC_EPMAP"></span><span id="fwpm_layer_rpc_epmap"></span>**FWPM\_LAYER\_RPC\_EPMAP**
</dt> <dd> <dl> <dt>



This filtering layer allows for inspecting the RPC data fields that are available in user mode during endpoint resolution. This is a user-mode filtering layer.


</dt> </dl> </dd> <dt>

<span id="FWPM_LAYER_RPC_EP_ADD"></span><span id="fwpm_layer_rpc_ep_add"></span>**FWPM\_LAYER\_RPC\_EP\_ADD**
</dt> <dd> <dl> <dt>



This filtering layer allows for inspecting the RPC data fields that are available in user mode when a new endpoint is added. This is a user-mode filtering layer.


</dt> </dl> </dd> <dt>

<span id="FWPM_LAYER_RPC_PROXY_CONN"></span><span id="fwpm_layer_rpc_proxy_conn"></span>**FWPM\_LAYER\_RPC\_PROXY\_CONN**
</dt> <dd> <dl> <dt>



This filtering layer allows for inspecting the RpcProxy connection requests. This is a user-mode filtering layer.


</dt> </dl> </dd> <dt>

<span id="FWPM_LAYER_RPC_PROXY_IF"></span><span id="fwpm_layer_rpc_proxy_if"></span>**FWPM\_LAYER\_RPC\_PROXY\_IF**
</dt> <dd> <dl> <dt>



This filtering layer allows for inspecting the interface used for RpcProxy connections. This is a user-mode filtering layer.


</dt> </dl> </dd> <dt>

<span id="FWPM_LAYER_KM_AUTHORIZATION"></span><span id="fwpm_layer_km_authorization"></span>**FWPM\_LAYER\_KM\_AUTHORIZATION**
</dt> <dd> <dl> <dt>



This filtering layer allows for authorizing security association establishment.

See [ALE Layers](ale-layers.md) for more information.


</dt> </dl> </dd> <dt>

<span id="FWPM_LAYER_NAME_RESOLUTION_CACHE_V4___FWPM_LAYER_NAME_RESOLUTION_CACHE_V6"></span><span id="fwpm_layer_name_resolution_cache_v4___fwpm_layer_name_resolution_cache_v6"></span>**FWPM\_LAYER\_NAME\_RESOLUTION\_CACHE\_V4 / FWPM\_LAYER\_NAME\_RESOLUTION\_CACHE\_V6**
</dt> <dd> <dl> <dt>



This filtering layer allows for querying the names recently resolved by the system.

See [ALE Layers](ale-layers.md) for more information.


</dt> </dl> </dd> <dt>

<span id="FWPM_LAYER_ALE_RESOURCE_RELEASE_V4___FWPM_LAYER_ALE_RESOURCE_RELEASE_V6"></span><span id="fwpm_layer_ale_resource_release_v4___fwpm_layer_ale_resource_release_v6"></span>**FWPM\_LAYER\_ALE\_RESOURCE\_RELEASE\_V4 / FWPM\_LAYER\_ALE\_RESOURCE\_RELEASE\_V6**
</dt> <dd> <dl> <dt>



This filtering layer allows for resources previously allocated to be released.

See [ALE Layers](ale-layers.md) for more information.


</dt> </dl> </dd> <dt>

<span id="FWPM_LAYER_ALE_ENDPOINT_CLOSURE_V4___FWPM_LAYER_ALE_ENDPOINT_CLOSURE_V6"></span><span id="fwpm_layer_ale_endpoint_closure_v4___fwpm_layer_ale_endpoint_closure_v6"></span>**FWPM\_LAYER\_ALE\_ENDPOINT\_CLOSURE\_V4 / FWPM\_LAYER\_ALE\_ENDPOINT\_CLOSURE\_V6**
</dt> <dd> <dl> <dt>



This filtering layer allows for tracking de-activation of connected TCP flow or UDP sockets.

See [ALE Layers](ale-layers.md) for more information.


</dt> </dl> </dd> <dt>

<span id="FWPM_LAYER_ALE_CONNECT_REDIRECT_V4___FWPM_LAYER_ALE_CONNECT_REDIRECT_V6"></span><span id="fwpm_layer_ale_connect_redirect_v4___fwpm_layer_ale_connect_redirect_v6"></span>**FWPM\_LAYER\_ALE\_CONNECT\_REDIRECT\_V4 / FWPM\_LAYER\_ALE\_CONNECT\_REDIRECT\_V6**
</dt> <dd> <dl> <dt>



This filtering layer allows for modification of remote address an/or port of an outgoing TCP connections, as well as for non-TCP traffic based on the first packet sent..

See [ALE Layers](ale-layers.md) for more information.


</dt> </dl> </dd> <dt>

<span id="FWPM_LAYER_ALE_BIND_REDIRECT_V4___FWPM_LAYER_ALE_BIND_REDIRECT_V6"></span><span id="fwpm_layer_ale_bind_redirect_v4___fwpm_layer_ale_bind_redirect_v6"></span>**FWPM\_LAYER\_ALE\_BIND\_REDIRECT\_V4 / FWPM\_LAYER\_ALE\_BIND\_REDIRECT\_V6**
</dt> <dd> <dl> <dt>



This filtering layer allows for modification of local address and/or port during the bind opreation on a TCP or UDP socket.

See [ALE Layers](ale-layers.md) for more information.


</dt> </dl> </dd> <dt>

<span id="FWPM_LAYER_STREAM_PACKET_V4___FWPM_LAYER_STREAM_PACKET_V6"></span><span id="fwpm_layer_stream_packet_v4___fwpm_layer_stream_packet_v6"></span>**FWPM\_LAYER\_STREAM\_PACKET\_V4 / FWPM\_LAYER\_STREAM\_PACKET\_V6**
</dt> <dd> <dl> <dt>



This filtering layer allows for inspection of TCP packets including handshake and flow control exchanges.

See [ALE Layers](ale-layers.md) for more information.


</dt> </dl> </dd> </dl>

## Remarks

These filtering layer identifiers are also referred to as management filtering layer identifiers. WFP API also contains a set of [run-time filtering layer identifiers](/windows-hardware/drivers/network/management-filtering-layer-identifiers), documented in the Windows Driver Kit (WDK). Run-time filtering layer identifiers are LUIDs, and therefore are smaller, only 64 bits in size, compared to the management filtering layer identifiers, which are 128 bits in size.

Management filtering layer identifiers and run-time filtering layer identifiers point to the same layers.

Management filtering layer identifiers are used by functions that interact with the Base Filtering Engine (BFE) from either user mode or kernel mode (for example, [**FwpmFilterAdd0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmfilteradd0)).

Run-time filtering layer identifiers are used by functions that interact with the filter engine from kernel mode only (for example, [FwpsFlowAssociateContext0](/windows-hardware/drivers/ddi/fwpsk/nf-fwpsk-fwpsflowassociatecontext0), [FwpsStreamInjectAsync0](/windows-hardware/drivers/ddi/fwpsk/nf-fwpsk-fwpsstreaminjectasync0)), and in data structures that come directly from the kernel (for example, [**FWPM\_NET\_EVENT\_CLASSIFY\_DROP0**](/windows/desktop/api/Fwpmtypes/ns-fwpmtypes-fwpm_net_event_classify_drop0)).

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Fwpmu.h</dt> </dl> |



## See also

<dl> <dt>

[ALE Layers](ale-layers.md)
</dt> <dt>

[WFP Architecture](windows-filtering-platform-architecture-overview.md)
</dt> </dl>

