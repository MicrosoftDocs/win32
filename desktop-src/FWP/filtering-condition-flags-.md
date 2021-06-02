---
title: Filtering Condition Flags (Fwptypes.h)
description: The Windows Filtering Platform (WFP) filtering condition flags are each represented by a bitfield.
ms.assetid: fe879479-331d-42ef-ac2f-634f0c13c21d
topic_type:
- apiref
api_name:
- FWP_CONDITION_FLAG_IS_LOOPBACK
- FWP_CONDITION_FLAG_IS_IPSEC_SECURED
- FWP_CONDITION_FLAG_IS_REAUTHORIZE
- FWP_CONDITION_FLAG_IS_WILDCARD_BIND
- FWP_CONDITION_FLAG_IS_RAW_ENDPOINT
- FWP_CONDITION_FLAG_IS_FRAGMENT
- FWP_CONDITION_FLAG_IS_FRAGMENT_GROUP
- FWP_CONDITION_FLAG_IS_IPSEC_NATT_RECLASSIFY
- FWP_CONDITION_FLAG_REQUIRES_ALE_CLASSIFY
- FWP_CONDITION_FLAG_IS_IMPLICIT_BIND
- FWP_CONDITION_FLAG_IS_REASSEMBLED
- FWP_CONDITION_FLAG_IS_NAME_APP_SPECIFIED
- FWP_CONDITION_FLAG_IS_PROMISCUOUS
- FWP_CONDITION_FLAG_IS_AUTH_FW
- FWP_CONDITION_FLAG_IS_RECLASSIFY
- FWP_CONDITION_FLAG_IS_PROXY_CONNECTION
- FWP_CONDITION_FLAG_IS_APPCONTAINER_LOOPBACK
- FWP_CONDITION_FLAG_IS_NON_APPCONTAINER_LOOPBACK
- FWP_CONDITION_FLAG_IS_RESERVED
- FWP_CONDITION_FLAG_IS_HONORING_POLICY_AUTHORIZE
- FWP_CONDITION_REAUTHORIZE_REASON_POLICY_CHANGE
- FWP_CONDITION_REAUTHORIZE_REASON_NEW_ARRIVAL_INTERFACE
- FWP_CONDITION_REAUTHORIZE_REASON_NEW_NEXTHOP_INTERFACE
- FWP_CONDITION_REAUTHORIZE_REASON_PROFILE_CROSSING
- FWP_CONDITION_REAUTHORIZE_REASON_CLASSIFY_COMPLETION
- FWP_CONDITION_REAUTHORIZE_REASON_IPSEC_PROPERTIES_CHANGED
- FWP_CONDITION_REAUTHORIZE_REASON_MID_STREAM_INSPECTION
- FWP_CONDITION_REAUTHORIZE_REASON_SOCKET_PROPERTY_CHANGED
- FWP_CONDITION_REAUTHORIZE_REASON_NEW_INBOUND_MCAST_BCAST_PACKET
- FWP_CONDITION_SOCKET_PROPERTY_FLAG_IS_SYSTEM_PORT_RPC
- FWP_CONDITION_SOCKET_PROPERTY_FLAG_ALLOW_EDGE_TRAFFIC
- FWP_CONDITION_SOCKET_PROPERTY_FLAG_DENY_EDGE_TRAFFIC
- FWP_CONDITION_L2_IS_NATIVE_ETHERNET
- FWP_CONDITION_L2_IS_WIFI
- FWP_CONDITION_L2_IS_MOBILE_BROADBAND
- FWP_CONDITION_L2_IS_WIFI_DIRECT_DATA
- FWP_CONDITION_L2_IS_VM2VM
- FWP_CONDITION_L2_IS_MALFORMED_PACKET
- FWP_CONDITION_L2_IS_IP_FRAGMENT_GROUP
- FWP_CONDITION_L2_IF_CONNECTOR_PRESENT
api_location:
- fwptypes.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# Filtering Condition Flags

The Windows Filtering Platform (WFP) filtering condition flags are each represented by a bitfield.

These flags and the filtering layers where they can be used are defined as follows.

<dl> <dt>

<span id="FWP_CONDITION_FLAG_IS_LOOPBACK"></span><span id="fwp_condition_flag_is_loopback"></span>**FWP\_CONDITION\_FLAG\_IS\_LOOPBACK**
</dt> <dd> <dl> <dt>



Tests if the network traffic is loopback traffic.

Filtering layers:

-   FWPM\_LAYER\_INBOUND\_IPPACKET\_V{4\|6}
-   FWPM\_LAYER\_OUTBOUND\_IPPACKET\_V{4\|6}
-   FWPM\_LAYER\_INBOUND\_TRANSPORT\_V{4\|6}
-   FWPM\_LAYER\_OUTBOUND\_TRANSPORT\_V{4\|6}
-   FWPM\_LAYER\_STREAM\_{V4\|6}
    > [!Note]  
    > Available only on Windows Server 2008, Windows Vista with SP1, and later.

     

-   FWPM\_LAYER\_INBOUND\_ICMP\_ERROR\_V{4\|6}
    > [!Note]  
    > Available only on Windows Server 2008, Windows Vista with SP1, and later.

     

-   FWPM\_LAYER\_OUTBOUND\_ICMP\_ERROR\_V{4\|6}
    > [!Note]  
    > Available only on Windows Server 2008, Windows Vista with SP1, and later.

     

-   FWPM\_LAYER\_ALE\_AUTH\_RECV\_ACCEPT\_V{4\|6}
-   FWPM\_LAYER\_ALE\_AUTH\_CONNECT\_V{4\|6}
    > [!Note]  
    > Available only on Windows Server 2008, Windows Vista with SP1, and later.

     

-   FWPM\_LAYER\_ALE\_FLOW\_ESTABLISHED\_V{4\|6}
    > [!Note]  
    > Available only on Windows Server 2008, Windows Vista with SP1, and later.

     


</dt> </dl> </dd> <dt>

<span id="FWP_CONDITION_FLAG_IS_IPSEC_SECURED"></span><span id="fwp_condition_flag_is_ipsec_secured"></span>**FWP\_CONDITION\_FLAG\_IS\_IPSEC\_SECURED**
</dt> <dd> <dl> <dt>



Tests if the network traffic is protected by IPsec.

Filtering layers:

-   FWPM\_LAYER\_INBOUND\_IPPACKET\_V{4\|6}
-   FWPM\_LAYER\_INBOUND\_TRANSPORT\_V{4\|6}
-   FWPM\_LAYER\_ALE\_AUTH\_RECV\_ACCEPT\_V{4\|6}
-   FWPM\_LAYER\_ALE\_AUTH\_CONNECT\_V{4\|6}


</dt> </dl> </dd> <dt>

<span id="FWP_CONDITION_FLAG_IS_REAUTHORIZE"></span><span id="fwp_condition_flag_is_reauthorize"></span>**FWP\_CONDITION\_FLAG\_IS\_REAUTHORIZE**
</dt> <dd> <dl> <dt>



Tests for a policy change as opposed to a new connection.

Filtering layers:

-   FWPM\_LAYER\_ALE\_AUTH\_RECV\_ACCEPT\_V{4\|6}
-   FWPM\_LAYER\_ALE\_AUTH\_CONNECT\_V{4\|6}


</dt> </dl> </dd> <dt>

<span id="FWP_CONDITION_FLAG_IS_WILDCARD_BIND"></span><span id="fwp_condition_flag_is_wildcard_bind"></span>**FWP\_CONDITION\_FLAG\_IS\_WILDCARD\_BIND**
</dt> <dd> <dl> <dt>



Tests if the application specified a wildcard address when binding to a local network address.

Filtering layer:

-   FWPM\_LAYER\_ALE\_RESOURCE\_ASSIGNMENT\_V{4\|6}


</dt> </dl> </dd> <dt>

<span id="FWP_CONDITION_FLAG_IS_RAW_ENDPOINT"></span><span id="fwp_condition_flag_is_raw_endpoint"></span>**FWP\_CONDITION\_FLAG\_IS\_RAW\_ENDPOINT**
</dt> <dd> <dl> <dt>



Tests if the local endpoint that is sending and receiving traffic is a raw endpoint.

Filtering layers:

-   FWPM\_LAYER\_INBOUND\_TRANSPORT\_V{4\|6}
    > [!Note]  
    > Available only on Windows Server 2008, Windows Vista with SP1, and later.

     

-   FWPM\_LAYER\_OUTBOUND\_TRANSPORT\_V{4\|6}
    > [!Note]  
    > Available only on Windows Server 2008, Windows Vista with SP1, and later.

     

-   FWPM\_LAYER\_DATAGRAM\_DATA\_{V4\|6}
    > [!Note]  
    > Available only on Windows Server 2008, Windows Vista with SP1, and later.

     

-   FWPM\_LAYER\_ALE\_RESOURCE\_ASSIGNMENT\_V{4\|6}
-   FWPM\_LAYER\_ALE\_AUTH\_RECV\_ACCEPT\_V{4\|6}
-   FWPM\_LAYER\_ALE\_AUTH\_CONNECT\_V{4\|6}


</dt> </dl> </dd> <dt>

<span id="FWP_CONDITION_FLAG_IS_FRAGMENT"></span><span id="fwp_condition_flag_is_fragment"></span>**FWP\_CONDITION\_FLAG\_IS\_FRAGMENT**
</dt> <dd> <dl> <dt>



Tests if the NET\_BUFFER\_LIST structure passed to a callout driver is an IP packet fragment.

Filtering layers:

-   FWPM\_LAYER\_INBOUND\_IPPACKET\_V{4\|6}
-   FWPM\_LAYER\_INBOUND\_IPPACKET\_V{4\|6}\_DISCARD


</dt> </dl> </dd> <dt>

<span id="FWP_CONDITION_FLAG_IS_FRAGMENT_GROUP"></span><span id="fwp_condition_flag_is_fragment_group"></span>**FWP\_CONDITION\_FLAG\_IS\_FRAGMENT\_GROUP**
</dt> <dd> <dl> <dt>



Tests if the NET\_BUFFER\_LIST structure passed to a callout driver describes a linked list of packet fragments.

Filtering layer:

-   FWPM\_LAYER\_IPFORWARD\_V{4\|6}


</dt> </dl> </dd> <dt>

<span id="FWP_CONDITION_FLAG_IS_IPSEC_NATT_RECLASSIFY"></span><span id="fwp_condition_flag_is_ipsec_natt_reclassify"></span>**FWP\_CONDITION\_FLAG\_IS\_IPSEC\_NATT\_RECLASSIFY**
</dt> <dd> <dl> <dt>



Indicates that the same packet is being re-classified at the transport layer, when the IPsec NAT shim translates the remote port value.


</dt> </dl> </dd> <dt>

<span id="FWP_CONDITION_FLAG_REQUIRES_ALE_CLASSIFY"></span><span id="fwp_condition_flag_requires_ale_classify"></span>**FWP\_CONDITION\_FLAG\_REQUIRES\_ALE\_CLASSIFY**
</dt> <dd> <dl> <dt>



Indicates that the packet will be reclassified at the ALE receive/accept layer.


</dt> </dl> </dd> <dt>

<span id="FWP_CONDITION_FLAG_IS_IMPLICIT_BIND"></span><span id="fwp_condition_flag_is_implicit_bind"></span>**FWP\_CONDITION\_FLAG\_IS\_IMPLICIT\_BIND**
</dt> <dd> <dl> <dt>



Tests if Windows Sockets is performing an implicit bind.

Available only on Windows Vista and Windows Server 2008.


</dt> </dl> </dd> <dt>

<span id="FWP_CONDITION_FLAG_IS_REASSEMBLED"></span><span id="fwp_condition_flag_is_reassembled"></span>**FWP\_CONDITION\_FLAG\_IS\_REASSEMBLED**
</dt> <dd> <dl> <dt>



Tests if the packet has been reassembled.

> [!Note]  
> Available only on Windows Server 2008, Windows Vista with SP1, and later.

 

Filtering layer:

-   FWPM\_LAYER\_INBOUND\_IPPACKET\_V{4\|6}


</dt> </dl> </dd> <dt>

<span id="FWP_CONDITION_FLAG_IS_NAME_APP_SPECIFIED"></span><span id="fwp_condition_flag_is_name_app_specified"></span>**FWP\_CONDITION\_FLAG\_IS\_NAME\_APP\_SPECIFIED**
</dt> <dd> <dl> <dt>



Tests if the name of the peer machine that the application is expecting to connect to has been received via an API such as [**WSASetSocketPeerTargetName**](/windows/desktop/api/ws2tcpip/nf-ws2tcpip-wsasetsocketpeertargetname) and not obtained via the caching heuristics.

> [!Note]  
> Available only on Windows Server 2008 R2, Windows 7, and later.

 

Filtering layer:

-   FWPM\_LAYER\_ALE\_AUTH\_CONNECT\_V{4\|6}


</dt> </dl> </dd> <dt>

<span id="FWP_CONDITION_FLAG_IS_PROMISCUOUS"></span><span id="fwp_condition_flag_is_promiscuous"></span>**FWP\_CONDITION\_FLAG\_IS\_PROMISCUOUS**
</dt> <dd> <dl> <dt>



Reserved.


</dt> </dl> </dd> <dt>

<span id="FWP_CONDITION_FLAG_IS_AUTH_FW"></span><span id="fwp_condition_flag_is_auth_fw"></span>**FWP\_CONDITION\_FLAG\_IS\_AUTH\_FW**
</dt> <dd> <dl> <dt>



Tests if the connection is end-to-end authenticated, even if the individual packets have not been verified.

> [!Note]  
> Available only on Windows Server 2008 R2, Windows 7, and later.

 

Filtering layer:

-   FWPM\_LAYER\_ALE\_AUTH\_CONNECT\_V{4\|6}
-   FWPM\_LAYER\_ALE\_AUTH\_RECV\_ACCEPT\_V{4\|6}


</dt> </dl> </dd> <dt>

<span id="FWP_CONDITION_FLAG_IS_RECLASSIFY"></span><span id="fwp_condition_flag_is_reclassify"></span>**FWP\_CONDITION\_FLAG\_IS\_RECLASSIFY**
</dt> <dd> <dl> <dt>



Tests if the filtering engine is reclassifying a previous bind or listen request.

> [!Note]  
> Available only on Windows Server 2008 R2, Windows 7, and later.

 

Filtering layer:

-   FWPM\_LAYER\_ALE\_AUTH\_LISTEN\_V{4\|6}
-   FWPM\_LAYER\_ALE\_RESOURCE\_ASSIGNMENT\_V{4\|6}


</dt> </dl> </dd> <dt>

<span id="FWP_CONDITION_FLAG_IS_PROXY_CONNECTION"></span><span id="fwp_condition_flag_is_proxy_connection"></span>**FWP\_CONDITION\_FLAG\_IS\_PROXY\_CONNECTION**
</dt> <dd> <dl> <dt>



Tests if the connection uses a proxy.

> [!Note]  
> Available only on Windows 8 and Windows Server 2012.

 


</dt> </dl> </dd> <dt>

<span id="FWP_CONDITION_FLAG_IS_APPCONTAINER_LOOPBACK"></span><span id="fwp_condition_flag_is_appcontainer_loopback"></span>**FWP\_CONDITION\_FLAG\_IS\_APPCONTAINER\_LOOPBACK**
</dt> <dd> <dl> <dt>



Tests if the network traffic is app container loopback traffic.

> [!Note]  
> Available only on Windows 8 and Windows Server 2012.

 


</dt> </dl> </dd> <dt>

<span id="FWP_CONDITION_FLAG_IS_NON_APPCONTAINER_LOOPBACK"></span><span id="fwp_condition_flag_is_non_appcontainer_loopback"></span>**FWP\_CONDITION\_FLAG\_IS\_NON\_APPCONTAINER\_LOOPBACK**
</dt> <dd> <dl> <dt>



Tests if the network traffic is non-app container loopback traffic.

> [!Note]  
> Available only on Windows 8 and Windows Server 2012.

 


</dt> </dl> </dd> <dt>

<span id="FWP_CONDITION_FLAG_IS_RESERVED"></span><span id="fwp_condition_flag_is_reserved"></span>**FWP\_CONDITION\_FLAG\_IS\_RESERVED**
</dt> <dd> <dl> <dt>



Reserved.


</dt> </dl> </dd> <dt>

<span id="FWP_CONDITION_FLAG_IS_HONORING_POLICY_AUTHORIZE"></span><span id="fwp_condition_flag_is_honoring_policy_authorize"></span>**FWP\_CONDITION\_FLAG\_IS\_HONORING\_POLICY\_AUTHORIZE**
</dt> <dd> <dl> <dt>



Indicates that the current classification is being performed to honor the intention of a redirected Windows Store app to connect to a specified host. Such a classification will contain the same classifiable field values as if the app were never redirected. The flag also indicates that a future classification will be invoked to match the effective redirected destination. If the app is redirected to a proxy service for inspection, it also means a future classification will be invoked on the proxy connection. Callout drivers should generally allow this classification.

> [!Note]  
> Available only on Windows 8 and Windows Server 2012.

 

Filtering layer:

-   FWPM\_LAYER\_ALE\_AUTH\_CONNECT\_V{4\|6}


</dt> </dl> </dd> </dl>

The following flags specify the reason for reauthorizing a previously authorized connection. These flags and the filtering layers where they can be used are defined as follows.

> [!Note]  
> These filtering conditions are available only on Windows Server 2008 R2, Windows 7, and later.

 

<dl> <dt>

<span id="FWP_CONDITION_REAUTHORIZE_REASON_POLICY_CHANGE"></span><span id="fwp_condition_reauthorize_reason_policy_change"></span>**FWP\_CONDITION\_REAUTHORIZE\_REASON\_POLICY\_CHANGE**
</dt> <dd> <dl> <dt>



Indicates that the connection was reauthorized due to filters being added or removed.

Filtering layer:

-   FWPM\_LAYER\_ALE\_AUTH\_CONNECT\_V{4\|6}
-   FWPM\_LAYER\_ALE\_AUTH\_RECV\_ACCEPT\_V{4\|6}


</dt> </dl> </dd> <dt>

<span id="FWP_CONDITION_REAUTHORIZE_REASON_NEW_ARRIVAL_INTERFACE"></span><span id="fwp_condition_reauthorize_reason_new_arrival_interface"></span>**FWP\_CONDITION\_REAUTHORIZE\_REASON\_NEW\_ARRIVAL\_INTERFACE**
</dt> <dd> <dl> <dt>



Indicates that the packet has arrived from an unknown interface.

Filtering layer:

-   FWPM\_LAYER\_ALE\_AUTH\_CONNECT\_V{4\|6}
-   FWPM\_LAYER\_ALE\_AUTH\_RECV\_ACCEPT\_V{4\|6}


</dt> </dl> </dd> <dt>

<span id="FWP_CONDITION_REAUTHORIZE_REASON_NEW_NEXTHOP_INTERFACE"></span><span id="fwp_condition_reauthorize_reason_new_nexthop_interface"></span>**FWP\_CONDITION\_REAUTHORIZE\_REASON\_NEW\_NEXTHOP\_INTERFACE**
</dt> <dd> <dl> <dt>



Indicates that the packet will be departing from an unknown interface.

Filtering layer:

-   FWPM\_LAYER\_ALE\_AUTH\_CONNECT\_V{4\|6}
-   FWPM\_LAYER\_ALE\_AUTH\_RECV\_ACCEPT\_V{4\|6}


</dt> </dl> </dd> <dt>

<span id="FWP_CONDITION_REAUTHORIZE_REASON_PROFILE_CROSSING"></span><span id="fwp_condition_reauthorize_reason_profile_crossing"></span>**FWP\_CONDITION\_REAUTHORIZE\_REASON\_PROFILE\_CROSSING**
</dt> <dd> <dl> <dt>



Indicates that the packet has passed through interfaces of more than one network category.

Filtering layer:

-   FWPM\_LAYER\_ALE\_AUTH\_CONNECT\_V{4\|6}
-   FWPM\_LAYER\_ALE\_AUTH\_RECV\_ACCEPT\_V{4\|6}


</dt> </dl> </dd> <dt>

<span id="FWP_CONDITION_REAUTHORIZE_REASON_CLASSIFY_COMPLETION"></span><span id="fwp_condition_reauthorize_reason_classify_completion"></span>**FWP\_CONDITION\_REAUTHORIZE\_REASON\_CLASSIFY\_COMPLETION**
</dt> <dd> <dl> <dt>



Indicates that a previously held connection is now being allowed to complete.

Filtering layer:

-   FWPM\_LAYER\_ALE\_AUTH\_CONNECT\_V{4\|6}
-   FWPM\_LAYER\_ALE\_AUTH\_RECV\_ACCEPT\_V{4\|6}


</dt> </dl> </dd> <dt>

<span id="FWP_CONDITION_REAUTHORIZE_REASON_IPSEC_PROPERTIES_CHANGED"></span><span id="fwp_condition_reauthorize_reason_ipsec_properties_changed"></span>**FWP\_CONDITION\_REAUTHORIZE\_REASON\_IPSEC\_PROPERTIES\_CHANGED**
</dt> <dd> <dl> <dt>



Indicates that IPsec properties have changed, or that the connection has changed from clear text to a secure connection.

Filtering layer:

-   FWPM\_LAYER\_ALE\_AUTH\_CONNECT\_V{4\|6}
-   FWPM\_LAYER\_ALE\_AUTH\_RECV\_ACCEPT\_V{4\|6}


</dt> </dl> </dd> <dt>

<span id="FWP_CONDITION_REAUTHORIZE_REASON_MID_STREAM_INSPECTION"></span><span id="fwp_condition_reauthorize_reason_mid_stream_inspection"></span>**FWP\_CONDITION\_REAUTHORIZE\_REASON\_MID\_STREAM\_INSPECTION**
</dt> <dd> <dl> <dt>



Indicates that a previously established TCP connection is now being inspected.

Filtering layer:

-   FWPM\_LAYER\_ALE\_AUTH\_CONNECT\_V{4\|6}
-   FWPM\_LAYER\_ALE\_AUTH\_RECV\_ACCEPT\_V{4\|6}


</dt> </dl> </dd> <dt>

<span id="FWP_CONDITION_REAUTHORIZE_REASON_SOCKET_PROPERTY_CHANGED"></span><span id="fwp_condition_reauthorize_reason_socket_property_changed"></span>**FWP\_CONDITION\_REAUTHORIZE\_REASON\_SOCKET\_PROPERTY\_CHANGED**
</dt> <dd> <dl> <dt>



Indicates that socket properties have been set after a connection was authorized and established.

Filtering layer:

-   FWPM\_LAYER\_ALE\_AUTH\_CONNECT\_V{4\|6}
-   FWPM\_LAYER\_ALE\_AUTH\_RECV\_ACCEPT\_V{4\|6}


</dt> </dl> </dd> <dt>

<span id="FWP_CONDITION_REAUTHORIZE_REASON_NEW_INBOUND_MCAST_BCAST_PACKET"></span><span id="fwp_condition_reauthorize_reason_new_inbound_mcast_bcast_packet"></span>**FWP\_CONDITION\_REAUTHORIZE\_REASON\_NEW\_INBOUND\_MCAST\_BCAST\_PACKET**
</dt> <dd> <dl> <dt>



Indicates that new inbound multicast or broadcast packets are being re-authorized at ALE\_RECV\_ACCEPT callouts.

Filtering layer:

-   FWPM\_LAYER\_ALE\_AUTH\_RECV\_ACCEPT\_V{4\|6}


</dt> </dl> </dd> </dl>

The following flags specify socket properties which are related to whether an application wants to receive Edge Traversal traffic. These flags and the filtering layers where they can be used are defined as follows.

> [!Note]  
> These filtering conditions are available only on Windows Server 2008 R2, Windows 7, and later.

 

<dl> <dt>

<span id="FWP_CONDITION_SOCKET_PROPERTY_FLAG_IS_SYSTEM_PORT_RPC"></span><span id="fwp_condition_socket_property_flag_is_system_port_rpc"></span>**FWP\_CONDITION\_SOCKET\_PROPERTY\_FLAG\_IS\_SYSTEM\_PORT\_RPC**
</dt> <dd> <dl> <dt>



Indicates that the application is communicating with a dynamic RPC port.

Filtering layer:

-   FWPM\_LAYER\_ALE\_AUTH\_LISTEN\_V{4\|6}
-   FWPM\_LAYER\_ALE\_RESOURCE\_ASSIGNMENT\_V{4\|6}


</dt> </dl> </dd> <dt>

<span id="FWP_CONDITION_SOCKET_PROPERTY_FLAG_ALLOW_EDGE_TRAFFIC"></span><span id="fwp_condition_socket_property_flag_allow_edge_traffic"></span>**FWP\_CONDITION\_SOCKET\_PROPERTY\_FLAG\_ALLOW\_EDGE\_TRAFFIC**
</dt> <dd> <dl> <dt>



Indicates that the application wants to receive edge traversal-specific traffic.

Filtering layer:

-   FWPM\_LAYER\_ALE\_AUTH\_LISTEN\_V{4\|6}
-   FWPM\_LAYER\_ALE\_RESOURCE\_ASSIGNMENT\_V{4\|6}


</dt> </dl> </dd> <dt>

<span id="FWP_CONDITION_SOCKET_PROPERTY_FLAG_DENY_EDGE_TRAFFIC"></span><span id="fwp_condition_socket_property_flag_deny_edge_traffic"></span>**FWP\_CONDITION\_SOCKET\_PROPERTY\_FLAG\_DENY\_EDGE\_TRAFFIC**
</dt> <dd> <dl> <dt>



Indicates that the application does not want to receive or process edge traversal-specific traffic.

Filtering layer:

-   FWPM\_LAYER\_ALE\_AUTH\_LISTEN\_V{4\|6}
-   FWPM\_LAYER\_ALE\_RESOURCE\_ASSIGNMENT\_V{4\|6}


</dt> </dl> </dd> </dl>

The following flags specify connection details related to L2 filtering.

> [!Note]  
> These filtering conditions are available only on Windows 8 and Windows Server 2012.

 

<dl> <dt>

<span id="FWP_CONDITION_L2_IS_NATIVE_ETHERNET"></span><span id="fwp_condition_l2_is_native_ethernet"></span>**FWP\_CONDITION\_L2\_IS\_NATIVE\_ETHERNET**
</dt> <dd> <dl> <dt>



Indicates that the connection is native Ethernet.

Filtering layer:

-   FWPM\_LAYER\_INBOUND\_MAC\_FRAME\_ETHERNET
-   FWPM\_LAYER\_INBOUND\_MAC\_FRAME\_NATIVE
-   FWPM\_LAYER\_OUTBOUND\_MAC\_FRAME\_ETHERNET
-   FWPM\_LAYER\_OUTBOUND\_MAC\_FRAME\_NATIVE


</dt> </dl> </dd> <dt>

<span id="FWP_CONDITION_L2_IS_WIFI"></span><span id="fwp_condition_l2_is_wifi"></span>**FWP\_CONDITION\_L2\_IS\_WIFI**
</dt> <dd> <dl> <dt>



Indicates that the connection is Wi-Fi.

Filtering layer:

-   FWPM\_LAYER\_INBOUND\_MAC\_FRAME\_ETHERNET
-   FWPM\_LAYER\_INBOUND\_MAC\_FRAME\_NATIVE
-   FWPM\_LAYER\_OUTBOUND\_MAC\_FRAME\_ETHERNET
-   FWPM\_LAYER\_OUTBOUND\_MAC\_FRAME\_NATIVE


</dt> </dl> </dd> <dt>

<span id="FWP_CONDITION_L2_IS_MOBILE_BROADBAND"></span><span id="fwp_condition_l2_is_mobile_broadband"></span>**FWP\_CONDITION\_L2\_IS\_MOBILE\_BROADBAND**
</dt> <dd> <dl> <dt>



Indicates that the connection is mobile broadband.

Filtering layer:

-   FWPM\_LAYER\_INBOUND\_MAC\_FRAME\_ETHERNET
-   FWPM\_LAYER\_INBOUND\_MAC\_FRAME\_NATIVE
-   FWPM\_LAYER\_OUTBOUND\_MAC\_FRAME\_ETHERNET
-   FWPM\_LAYER\_OUTBOUND\_MAC\_FRAME\_NATIVE


</dt> </dl> </dd> <dt>

<span id="FWP_CONDITION_L2_IS_WIFI_DIRECT_DATA"></span><span id="fwp_condition_l2_is_wifi_direct_data"></span>**FWP\_CONDITION\_L2\_IS\_WIFI\_DIRECT\_DATA**
</dt> <dd> <dl> <dt>



Indicates that the connection is Wi-Fi Direct.

Filtering layer:

-   FWPM\_LAYER\_INBOUND\_MAC\_FRAME\_ETHERNET
-   FWPM\_LAYER\_INBOUND\_MAC\_FRAME\_NATIVE
-   FWPM\_LAYER\_OUTBOUND\_MAC\_FRAME\_ETHERNET
-   FWPM\_LAYER\_OUTBOUND\_MAC\_FRAME\_NATIVE


</dt> </dl> </dd> <dt>

<span id="FWP_CONDITION_L2_IS_VM2VM"></span><span id="fwp_condition_l2_is_vm2vm"></span>**FWP\_CONDITION\_L2\_IS\_VM2VM**
</dt> <dd> <dl> <dt>



Indicates that the connection is between virtual machines.

Filtering layer:

-   FWPM\_LAYER\_INBOUND\_MAC\_FRAME\_ETHERNET
-   FWPM\_LAYER\_INBOUND\_MAC\_FRAME\_NATIVE
-   FWPM\_LAYER\_OUTBOUND\_MAC\_FRAME\_ETHERNET
-   FWPM\_LAYER\_OUTBOUND\_MAC\_FRAME\_NATIVE


</dt> </dl> </dd> <dt>

<span id="FWP_CONDITION_L2_IS_MALFORMED_PACKET"></span><span id="fwp_condition_l2_is_malformed_packet"></span>**FWP\_CONDITION\_L2\_IS\_MALFORMED\_PACKET**
</dt> <dd> <dl> <dt>



Indicates that a packet appears to be malformed.

Filtering layer:

-   FWPM\_LAYER\_INBOUND\_MAC\_FRAME\_ETHERNET
-   FWPM\_LAYER\_INBOUND\_MAC\_FRAME\_NATIVE
-   FWPM\_LAYER\_OUTBOUND\_MAC\_FRAME\_ETHERNET
-   FWPM\_LAYER\_OUTBOUND\_MAC\_FRAME\_NATIVE


</dt> </dl> </dd> <dt>

<span id="FWP_CONDITION_L2_IS_IP_FRAGMENT_GROUP"></span><span id="fwp_condition_l2_is_ip_fragment_group"></span>**FWP\_CONDITION\_L2\_IS\_IP\_FRAGMENT\_GROUP**
</dt> <dd> <dl> <dt>



Indicates an IP packet fragment group.

Filtering layer:

-   FWPM\_LAYER\_INBOUND\_MAC\_FRAME\_ETHERNET
-   FWPM\_LAYER\_INBOUND\_MAC\_FRAME\_NATIVE
-   FWPM\_LAYER\_OUTBOUND\_MAC\_FRAME\_ETHERNET
-   FWPM\_LAYER\_OUTBOUND\_MAC\_FRAME\_NATIVE


</dt> </dl> </dd> <dt>

<span id="FWP_CONDITION_L2_IF_CONNECTOR_PRESENT"></span><span id="fwp_condition_l2_if_connector_present"></span>**FWP\_CONDITION\_L2\_IF\_CONNECTOR\_PRESENT**
</dt> <dd> <dl> <dt>



Indicates that a connector is present.

Filtering layer:

-   FWPM\_LAYER\_INBOUND\_MAC\_FRAME\_ETHERNET
-   FWPM\_LAYER\_INBOUND\_MAC\_FRAME\_NATIVE
-   FWPM\_LAYER\_OUTBOUND\_MAC\_FRAME\_ETHERNET
-   FWPM\_LAYER\_OUTBOUND\_MAC\_FRAME\_NATIVE


</dt> </dl> </dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Fwptypes.h</dt> </dl> |



## See also

<dl> <dt>

[**Filtering Layer Identifiers**](management-filtering-layer-identifiers-.md)
</dt> </dl>

 

