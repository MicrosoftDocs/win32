---
title: Filtering Condition Identifiers (Fwpmu.h)
description: The Windows Filtering Platform (WFP) filtering condition identifiers are each represented by a GUID.
ms.assetid: 4f0b970a-e511-4107-8023-22a8775905b9
topic_type:
- apiref
api_name:
- FWPM_CONDITION_INTERFACE_MAC_ADDRESS
- FWPM_CONDITION_MAC_LOCAL_ADDRESS
- FWPM_CONDITION_MAC_REMOTE_ADDRESS
- FWPM_CONDITION_ETHER_TYPE
- FWPM_CONDITION_VLAN_ID
- FWPM_CONDITION_VSWITCH_TENANT_NETWORK_ID
- FWPM_CONDITION_NDIS_PORT
- FWPM_CONDITION_NDIS_MEDIA_TYPE
- FWPM_CONDITION_NDIS_PHYSICAL_MEDIA_TYPE
- FWPM_CONDITION_L2_FLAGS
- FWPM_CONDITION_MAC_LOCAL_ADDRESS_TYPE
- FWPM_CONDITION_MAC_REMOTE_ADDRESS_TYPE
- FWPM_CONDITION_MAC_SOURCE_ADDRESS
- FWPM_CONDITION_MAC_DESTINATION_ADDRESS
- FWPM_CONDITION_MAC_SOURCE_ADDRESS_TYPE
- FWPM_CONDITION_MAC_DESTINATION_ADDRESS_TYPE
- FWPM_CONDITION_IP_SOURCE_PORT
- FWPM_CONDITION_VSWITCH_ICMP_TYPE
- FWPM_CONDITION_IP_DESTINATION_PORT
- FWPM_CONDITION_VSWITCH_ICMP_CODE
- FWPM_CONDITION_VSWITCH_ID
- FWPM_CONDITION_VSWITCH_NETWORK_TYPE
- FWPM_CONDITION_VSWITCH_SOURCE_INTERFACE_ID
- FWPM_CONDITION_VSWITCH_DESTINATION_INTERFACE_ID
- FWPM_CONDITION_VSWITCH_SOURCE_VM_ID
- FWPM_CONDITION_VSWITCH_DESTINATION_VM_ID
- FWPM_CONDITION_VSWITCH_SOURCE_INTERFACE_TYPE
- FWPM_CONDITION_VSWITCH_DESTINATION_INTERFACE_TYPE
- FWPM_CONDITION_INTERFACE
- FWPM_CONDITION_ALE_PACKAGE_ID
- FWPM_CONDITION_ALE_ORIGINAL_APP_ID
- FWPM_CONDITION_IP_NEXTHOP_ADDRESS
- FWPM_CONDITION_IP_NEXTHOP_INTERFACE
- FWPM_CONDITION_NEXTHOP_INTERFACE_TYPE
- FWPM_CONDITION_NEXTHOP_TUNNEL_TYPE
- FWPM_CONDITION_NEXTHOP_INTERFACE_INDEX
- FWPM_CONDITION_NEXTHOP_SUB_INTERFACE_INDEX
- FWPM_CONDITION_ORIGINAL_PROFILE_ID
- FWPM_CONDITION_CURRENT_PROFILE_ID
- FWPM_CONDITION_LOCAL_INTERFACE_PROFILE_ID
- FWPM_CONDITION_ARRIVAL_INTERFACE_PROFILE_ID
- FWPM_CONDITION_NEXTHOP_INTERFACE_PROFILE_ID
- FWPM_CONDITION_REAUTHORIZE_REASON
- FWPM_CONDITION_ALE_REAUTH_REASON
- FWPM_CONDITION_ORIGINAL_ICMP_TYPE
- FWPM_CONDITION_IP_PHYSICAL_ARRIVAL_INTERFACE
- FWPM_CONDITION_IP_PHYSICAL_NEXTHOP_INTERFACE
- FWPM_CONDITION_INTERFACE_QUARANTINE_EPOCH
- FWPM_CONDITION_ALE_SIO_FIREWALL_SOCKET_PROPERTY
- FWPM_CONDITION_IP_ARRIVAL_INTERFACE
- FWPM_CONDITION_ARRIVAL_INTERFACE_TYPE
- FWPM_CONDITION_ARRIVAL_TUNNEL_TYPE
- FWPM_CONDITION_ARRIVAL_INTERFACE_INDEX
- FWPM_CONDITION_ARRIVAL_SUB_INTERFACE_INDEX
- FWPM_CONDITION_LOCAL_INTERFACE_INDEX
- FWPM_CONDITION_LOCAL_INTERFACE_TYPE
- FWPM_CONDITION_LOCAL_TUNNEL_TYPE
- FWPM_CONDITION_IP_LOCAL_ADDRESS
- FWPM_CONDITION_IP_REMOTE_ADDRESS
- FWPM_CONDITION_IP_SOURCE_ADDRESS
- FWPM_CONDITION_IP_DESTINATION_ADDRESS
- FWPM_CONDITION_IP_LOCAL_ADDRESS_TYPE
- FWPM_CONDITION_IP_DESTINATION_ADDRESS_TYPE
- FWPM_CONDITION_IP_LOCAL_INTERFACE
- FWPM_CONDITION_INTERFACE_TYPE
- FWPM_CONDITION_TUNNEL_TYPE
- FWPM_CONDITION_IP_FORWARD_INTERFACE
- FWPM_CONDITION_IP_PROTOCOL
- FWPM_CONDITION_IP_LOCAL_PORT
- FWPM_CONDITION_ICMP_TYPE
- FWPM_CONDITION_IP_REMOTE_PORT
- FWPM_CONDITION_ICMP_CODE
- FWPM_CONDITION_EMBEDDED_LOCAL_ADDRESS_TYPE
- FWPM_CONDITION_EMBEDDED_REMOTE_ADDRESS
- FWPM_CONDITION_EMBEDDED_PROTOCOL
- FWPM_CONDITION_EMBEDDED_LOCAL_PORT
- FWPM_CONDITION_EMBEDDED_REMOTE_PORT
- FWPM_CONDITION_FLAGS
- FWPM_CONDITION_DIRECTION
- FWPM_CONDITION_INTERFACE_INDEX
- FWPM_CONDITION_SUB_INTERFACE_INDEX
- FWPM_CONDITION_SOURCE_INTERFACE_INDEX
- FWPM_CONDITION_SOURCE_SUB_INTERFACE_INDEX
- FWPM_CONDITION_DESTINATION_INTERFACE_INDEX
- FWPM_CONDITION_DESTINATION_SUB_INTERFACE_INDEX
- FWPM_CONDITION_ALE_APP_ID
- FWPM_CONDITION_ALE_USER_ID
- FWPM_CONDITION_ALE_REMOTE_USER_ID
- FWPM_CONDITION_ALE_REMOTE_MACHINE_ID
- FWPM_CONDITION_ALE_PROMISCUOUS_MODE
- FWPM_CONDITION_ALE_SIO_FIREWALL_SYSTEM_PORT
- FWPM_CONDITION_ALE_NAP_CONTEXT
- FWPM_CONDITION_QM_MODE
- FWPM_CONDITION_KM_AUTH_NAP_CONTEXT
- FWPM_CONDITION_PEER_NAME
- FWPM_CONDITION_REMOTE_ID
- FWPM_CONDITION_AUTHENTICATION_TYPE
- FWPM_CONDITION_KM_TYPE
- FWPM_CONDITION_KM_MODE
- FWPM_CONDITION_IPSEC_POLICY_KEY
- FWPM_CONDITION_AUTHENTICATION_TYPE
- FWPM_CONDITION_REMOTE_USER_TOKEN
- FWPM_CONDITION_RPC_IF_UUID
- FWPM_CONDITION_RPC_IF_VERSION
- FWPM_CONDITION_RPC_IF_FLAG
- FWPM_CONDITION_DCOM_APP_ID
- FWPM_CONDITION_IMAGE_NAME
- FWPM_CONDITION_RPC_PROTOCOL
- FWPM_CONDITION_RPC_AUTH_TYPE
- FWPM_CONDITION_RPC_AUTH_LEVEL
- FWPM_CONDITION_SEC_ENCRYPT_ALGORITHM
- FWPM_CONDITION_SEC_KEY_SIZE
- FWPM_CONDITION_IP_LOCAL_ADDRESS_V4
- FWPM_CONDITION_IP_LOCAL_ADDRESS_V6
- FWPM_CONDITION_IP_REMOTE_ADDRESS_V4
- FWPM_CONDITION_IP_REMOTE_ADDRESS_V6
- FWPM_CONDITION_PIPE
- FWPM_CONDITION_PROCESS_WITH_RPC_IF_UUID
- FWPM_CONDITION_RPC_EP_VALUE
- FWPM_CONDITION_RPC_EP_FLAGS
- FWPM_CONDITION_CLIENT_TOKEN
- FWPM_CONDITION_RPC_SERVER_NAME
- FWPM_CONDITION_RPC_SERVER_PORT
- FWPM_CONDITION_RPC_PROXY_AUTH_TYPE
- FWPM_CONDITION_CLIENT_CERT_KEY_LENGTH
- FWPM_CONDITION_CLIENT_CERT_OID
- FWPM_CONDITION_NET_EVENT_TYPE
api_location:
- Fwpmu.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# Filtering Condition Identifiers

The Windows Filtering Platform (WFP) filtering condition identifiers are each represented by a **GUID**. The data type for the condition value for each filtering condition is specified as an [**FWP\_DATA\_TYPE**](/windows/desktop/api/Fwptypes/ne-fwptypes-fwp_data_type). These identifiers and their data types are defined here.

The standard conditions are listed first, followed by the conditions specific to user mode. Conditions are grouped by supported operating system, so that you can easily tell which conditions are supported for a given OS.

> [!Note]  
> Each of the following filtering conditions is available only at a subset of the WFP filtering layers. For more information on each condition's availability at any given layer, see [**Filtering Conditions Available at Each Filtering Layer**](filtering-conditions-available-at-each-filtering-layer.md).

 




| Conditions available for Windows 8 and Windows Server 2012 | Description | 
|------------------------------------------------------------|-------------|
| <span id="FWPM_CONDITION_INTERFACE_MAC_ADDRESS"></span><span id="fwpm_condition_interface_mac_address"></span><dl><dt><strong>FWPM_CONDITION_INTERFACE_MAC_ADDRESS</strong></dt></dl> | The MAC address of a particular local interface.<br /><strong>Data type:</strong> FWP_BYTE_ARRAY6_TYPE <br /> | 
| <span id="FWPM_CONDITION_MAC_LOCAL_ADDRESS"></span><span id="fwpm_condition_mac_local_address"></span><dl><dt><strong>FWPM_CONDITION_MAC_LOCAL_ADDRESS</strong></dt></dl> | Destination address of an inbound frame, or source address of an outbound frame.<br /><strong>Data type:</strong> FWP_BYTE_ARRAY6_TYPE<br /> | 
| <span id="FWPM_CONDITION_MAC_REMOTE_ADDRESS"></span><span id="fwpm_condition_mac_remote_address"></span><dl><dt><strong>FWPM_CONDITION_MAC_REMOTE_ADDRESS</strong></dt></dl> | Source address of an inbound frame, or destination address of an outbound frame.<br /><strong>Data type:</strong> FWP_BYTE_ARRAY6_TYPE<br /> | 
| <span id="FWPM_CONDITION_ETHER_TYPE"></span><span id="fwpm_condition_ether_type"></span><dl><dt><strong>FWPM_CONDITION_ETHER_TYPE</strong></dt></dl> | The Ethernet V2 network payload data type. (See ETHERNET_TYPE_IPV4, etc. in netiodef.h.)<br /><strong>Data type:</strong> FWP_UINT16<br /> | 
| <span id="FWPM_CONDITION_VLAN_ID"></span><span id="fwpm_condition_vlan_id"></span><dl><dt><strong>FWPM_CONDITION_VLAN_ID</strong></dt></dl> | The 16-bits of VLAN header including the VID, CFI, and Priority fields as per the 802.1q standard (see VLAN_TAG in netiodef.h for the positions of the bitfields).<br /><strong>Data type:</strong> FWP_UINT16<br /> | 
| <span id="FWPM_CONDITION_VSWITCH_TENANT_NETWORK_ID"></span><span id="fwpm_condition_vswitch_tenant_network_id"></span><dl><dt><strong>FWPM_CONDITION_VSWITCH_TENANT_NETWORK_ID</strong></dt></dl> | Unique identifier for the vSwitch network. Cannot be used in conjunction with VLAN_IDs.<br /><strong>Data type:</strong> FWP_UINT16<br /> | 
| <span id="FWPM_CONDITION_NDIS_PORT"></span><span id="fwpm_condition_ndis_port"></span><dl><dt><strong>FWPM_CONDITION_NDIS_PORT</strong></dt></dl> | The port number of the NDIS port.<br /><strong>Data type:</strong> FWP_UINT32<br /> | 
| <span id="FWPM_CONDITION_NDIS_MEDIA_TYPE"></span><span id="fwpm_condition_ndis_media_type"></span><dl><dt><strong>FWPM_CONDITION_NDIS_MEDIA_TYPE</strong></dt></dl> | The media type of the NDIS port.<br /><strong>Data type:</strong> FWP_UINT32<br /><strong>Possible values:</strong> Any of the <strong>NDIS_MEDIUM</strong> enumeration values. (See ntddndis.h.) <br /> | 
| <span id="FWPM_CONDITION_NDIS_PHYSICAL_MEDIA_TYPE"></span><span id="fwpm_condition_ndis_physical_media_type"></span><dl><dt><strong>FWPM_CONDITION_NDIS_PHYSICAL_MEDIA_TYPE</strong></dt></dl> | The physical media type of the NDIS port.<br /><strong>Data type:</strong> FWP_UINT32<br /><strong>Possible values:</strong> Any of the <strong>NDIS_PHYSICAL_MEDIUM</strong> enumeration values. (See ntddndis.h.) <br /> | 
| <span id="FWPM_CONDITION_L2_FLAGS"></span><span id="fwpm_condition_l2_flags"></span><dl><dt><strong>FWPM_CONDITION_L2_FLAGS</strong></dt></dl> | A bitwise OR of a combination of filtering condition flags. <br /><strong>Data type:</strong> FWP_UINT32<br /><strong>Possible values:  </strong><ul><li>FWP_CONDITION_L2_IS_MOBILE_BROADBAND</li><li>FWP_CONDITION_L2_IS_NATIVE_ETHERNET</li><li>FWP_CONDITION_L2_IS_WIFI</li><li>FWP_CONDITION_L2_IS_WIFI_DIRECT_DATA</li></ul><br /> | 
| <span id="FWPM_CONDITION_MAC_LOCAL_ADDRESS_TYPE"></span><span id="fwpm_condition_mac_local_address_type"></span><dl><dt><strong>FWPM_CONDITION_MAC_LOCAL_ADDRESS_TYPE</strong></dt></dl> | The address type of the physical local address.<br /><strong>Data type:</strong> FWP_UINT8<br /><strong>Possible values:</strong> Any of the following <strong>DL_ADDRESS_TYPE</strong> enumeration values.<ul><li>DlUnicast</li><li>DlMulticast</li><li>DlBroadcast</li></ul><br /> | 
| <span id="FWPM_CONDITION_MAC_REMOTE_ADDRESS_TYPE"></span><span id="fwpm_condition_mac_remote_address_type"></span><dl><dt><strong>FWPM_CONDITION_MAC_REMOTE_ADDRESS_TYPE</strong></dt></dl> | The address type of the physical remote address.<br /><strong>Data type:</strong> FWP_UINT8<br /><strong>Possible values:</strong> Any of the following <strong>DL_ADDRESS_TYPE</strong> enumeration values.<ul><li>DlUnicast</li><li>DlMulticast</li><li>DlBroadcast</li></ul><br /> | 
| <span id="FWPM_CONDITION_MAC_SOURCE_ADDRESS"></span><span id="fwpm_condition_mac_source_address"></span><dl><dt><strong>FWPM_CONDITION_MAC_SOURCE_ADDRESS</strong></dt></dl> | The physical source address of a frame.<br /><strong>Data type:</strong> FWP_BYTE_ARRAY6_TYPE<br /> | 
| <span id="FWPM_CONDITION_MAC_DESTINATION_ADDRESS"></span><span id="fwpm_condition_mac_destination_address"></span><dl><dt><strong>FWPM_CONDITION_MAC_DESTINATION_ADDRESS</strong></dt></dl> | The physical destination address of a frame.<br /><strong>Data type:</strong> FWP_BYTE_ARRAY6_TYPE<br /> | 
| <span id="FWPM_CONDITION_MAC_SOURCE_ADDRESS_TYPE"></span><span id="fwpm_condition_mac_source_address_type"></span><dl><dt><strong>FWPM_CONDITION_MAC_SOURCE_ADDRESS_TYPE</strong></dt></dl> | The address type of the physical destination address.<br /><strong>Data type:</strong> FWP_UINT8<br /><strong>Possible values:</strong> Any of the following <strong>DL_ADDRESS_TYPE</strong> enumeration values.<ul><li>DlUnicast</li><li>DlMulticast</li><li>DlBroadcast</li></ul><br /> | 
| <span id="FWPM_CONDITION_MAC_DESTINATION_ADDRESS_TYPE"></span><span id="fwpm_condition_mac_destination_address_type"></span><dl><dt><strong>FWPM_CONDITION_MAC_DESTINATION_ADDRESS_TYPE</strong></dt></dl> | The address type of the physical destination address.<br /><strong>Data type:</strong> FWP_UINT8<br /><strong>Possible values:</strong> Any of the following <strong>DL_ADDRESS_TYPE</strong> enumeration values.<ul><li>DlUnicast</li><li>DlMulticast</li><li>DlBroadcast</li></ul><br /> | 
| <span id="FWPM_CONDITION_IP_SOURCE_PORT"></span><span id="fwpm_condition_ip_source_port"></span><dl><dt><strong>FWPM_CONDITION_IP_SOURCE_PORT</strong></dt></dl> | The source port of the packet's transport.<br /><strong>Data type:</strong> FWP_UINT16<br /> | 
| <span id="FWPM_CONDITION_VSWITCH_ICMP_TYPE"></span><span id="fwpm_condition_vswitch_icmp_type"></span><dl><dt><strong>FWPM_CONDITION_VSWITCH_ICMP_TYPE</strong></dt></dl> | The ICMP type field, as specified in RFC 792.<br /><strong>Data type:</strong> FWP_UINT16<br /> | 
| <span id="FWPM_CONDITION_IP_DESTINATION_PORT"></span><span id="fwpm_condition_ip_destination_port"></span><dl><dt><strong>FWPM_CONDITION_IP_DESTINATION_PORT</strong></dt></dl> | The destination port of the packet's transport.<br /><strong>Data type:</strong> FWP_UINT16<br /> | 
| <span id="FWPM_CONDITION_VSWITCH_ICMP_CODE"></span><span id="fwpm_condition_vswitch_icmp_code"></span><dl><dt><strong>FWPM_CONDITION_VSWITCH_ICMP_CODE</strong></dt></dl> | The ICMP code field, as specified in RFC 792. <br /><strong>Data type:</strong> FWP_UINT16<br /> | 
| <span id="FWPM_CONDITION_VSWITCH_ID"></span><span id="fwpm_condition_vswitch_id"></span><dl><dt><strong>FWPM_CONDITION_VSWITCH_ID</strong></dt></dl> | Unique identifier of an vSwitch instance.<br /><strong>Data type:</strong> FWP_BYTE_BLOB_TYPE<br /> | 
| <span id="FWPM_CONDITION_VSWITCH_NETWORK_TYPE"></span><span id="fwpm_condition_vswitch_network_type"></span><dl><dt><strong>FWPM_CONDITION_VSWITCH_NETWORK_TYPE</strong></dt></dl> | Specifies whether the vSwitch instance is part of an external, internal, or private virtual network.<br /><strong>Data type:</strong> FWP_UINT8<br /> | 
| <span id="FWPM_CONDITION_VSWITCH_SOURCE_INTERFACE_ID"></span><span id="fwpm_condition_vswitch_source_interface_id"></span><dl><dt><strong>FWPM_CONDITION_VSWITCH_SOURCE_INTERFACE_ID</strong></dt></dl> | Unique identifier of the source of the current packet. (The name of a VM-NIC, P-NIC, or V-NIC.)<br /><strong>Data type:</strong> FWP_BYTE_BLOB_TYPE<br /> | 
| <span id="FWPM_CONDITION_VSWITCH_DESTINATION_INTERFACE_ID"></span><span id="fwpm_condition_vswitch_destination_interface_id"></span><dl><dt><strong>FWPM_CONDITION_VSWITCH_DESTINATION_INTERFACE_ID</strong></dt></dl> | Unique identifier of the destination of the current packet. (The name of a VM-NIC, P-NIC, or V-NIC.)<br /><strong>Data type:</strong> FWP_BYTE_BLOB_TYPE<br /> | 
| <span id="FWPM_CONDITION_VSWITCH_SOURCE_VM_ID"></span><span id="fwpm_condition_vswitch_source_vm_id"></span><dl><dt><strong>FWPM_CONDITION_VSWITCH_SOURCE_VM_ID</strong></dt></dl> | Unique identifier of the vSwitch source virtual machine.<br /><strong>Data type:</strong> FWP_BYTE_BLOB_TYPE<br /> | 
| <span id="FWPM_CONDITION_VSWITCH_DESTINATION_VM_ID"></span><span id="fwpm_condition_vswitch_destination_vm_id"></span><dl><dt><strong>FWPM_CONDITION_VSWITCH_DESTINATION_VM_ID</strong></dt></dl> | Unique identifier of the vSwitch destination virtual machine.<br /><strong>Data type:</strong> FWP_BYTE_BLOB_TYPE<br /> | 
| <span id="FWPM_CONDITION_VSWITCH_SOURCE_INTERFACE_TYPE"></span><span id="fwpm_condition_vswitch_source_interface_type"></span><dl><dt><strong>FWPM_CONDITION_VSWITCH_SOURCE_INTERFACE_TYPE</strong></dt></dl> | Interface type of the source of the current packet.<br /><strong>Data type:</strong> FWP_UINT8<br /><strong>Possible values:  </strong><ul><li>SwitchNicSyntheticNic (when interface type is VM-NIC)</li><li>SwitchNicEmulatedNic (when interface type is VM-NIC)</li><li>SwitchNicPhysicalNic (when interface type is P-NIC)</li><li>SwitchNicVNic (when interface type is V-NIC, connected to the host partition)</li></ul><br /> | 
| <span id="FWPM_CONDITION_VSWITCH_DESTINATION_INTERFACE_TYPE"></span><span id="fwpm_condition_vswitch_destination_interface_type"></span><dl><dt><strong>FWPM_CONDITION_VSWITCH_DESTINATION_INTERFACE_TYPE</strong></dt></dl> | Interface type of the destination of the current packet.<br /><strong>Data type:</strong> FWP_UINT8<br /><strong>Possible values:  </strong><ul><li>SwitchNicSyntheticNic (when interface type is VM-NIC)</li><li>SwitchNicEmulatedNic (when interface type is VM-NIC)</li><li>SwitchNicPhysicalNic (when interface type is P-NIC)</li><li>SwitchNicVNic (when interface type is V-NIC, connected to the host partition)</li></ul><br /> | 
| <span id="FWPM_CONDITION_INTERFACE"></span><span id="fwpm_condition_interface"></span><dl><dt><strong>FWPM_CONDITION_INTERFACE</strong></dt></dl> | The LUID for the network interface associated with the local IP address. <br /><strong>Data type:</strong> FWP_UINT64<br /> | 
| <span id="FWPM_CONDITION_ALE_PACKAGE_ID"></span><span id="fwpm_condition_ale_package_id"></span><dl><dt><strong>FWPM_CONDITION_ALE_PACKAGE_ID</strong></dt></dl> | The security identifier (SID) of an app container.<br /><strong>Data type:</strong> FWP_SID<br /> | 
| <span id="FWPM_CONDITION_ALE_ORIGINAL_APP_ID"></span><span id="fwpm_condition_ale_original_app_id"></span><dl><dt><strong>FWPM_CONDITION_ALE_ORIGINAL_APP_ID</strong></dt></dl> | The fully qualified lower-case device path of the application, such as "\device\hardiskvolume1\program files\application.exe". When a connection has been redirected, this will be the identifier of the originating app; otherwise this will be the same as <strong>FWPM_CONDITION_ALE_APP_ID</strong>.<br /><strong>Data type:</strong> FWP_BYTE_BLOB_TYPE<br /> | 






| Conditions available for Windows 7, Windows Server 2008 R2, and later                                                                                                                                                                                                    | Description                                                                                                                                                                                                                                                                               |
|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="FWPM_CONDITION_IP_NEXTHOP_ADDRESS"></span><span id="fwpm_condition_ip_nexthop_address"></span><dl> <dt>**FWPM\_CONDITION\_IP\_NEXTHOP\_ADDRESS**</dt> </dl>                                             | The IP address of the next-hop interface.<br/> **Data type:** FWP\_V4\_ADDR\_MASK<br/>                                                                                                                                                                                        |
| <span id="FWPM_CONDITION_IP_NEXTHOP_INTERFACE"></span><span id="fwpm_condition_ip_nexthop_interface"></span><dl> <dt>**FWPM\_CONDITION\_IP\_NEXTHOP\_INTERFACE**</dt> </dl>                                       | The next-hop interface from which the packet will be departing. <br/> **Data type:** FWP\_UINT64<br/>                                                                                                                                                                         |
| <span id="FWPM_CONDITION_NEXTHOP_INTERFACE_TYPE"></span><span id="fwpm_condition_nexthop_interface_type"></span><dl> <dt>**FWPM\_CONDITION\_NEXTHOP\_INTERFACE\_TYPE**</dt> </dl>                                 | The interface type of the next-hop interface.<br/> **Data type:** FWP\_UINT32<br/>                                                                                                                                                                                            |
| <span id="FWPM_CONDITION_NEXTHOP_TUNNEL_TYPE"></span><span id="fwpm_condition_nexthop_tunnel_type"></span><dl> <dt>**FWPM\_CONDITION\_NEXTHOP\_TUNNEL\_TYPE**</dt> </dl>                                          | The tunnel type of the next-hop interface.<br/> **Data type:** FWP\_UINT32<br/>                                                                                                                                                                                               |
| <span id="FWPM_CONDITION_NEXTHOP_INTERFACE_INDEX"></span><span id="fwpm_condition_nexthop_interface_index"></span><dl> <dt>**FWPM\_CONDITION\_NEXTHOP\_INTERFACE\_INDEX**</dt> </dl>                              | The interface index of the next-hop interface.<br/> **Data type:** FWP\_UINT32<br/>                                                                                                                                                                                           |
| <span id="FWPM_CONDITION_NEXTHOP_SUB_INTERFACE_INDEX"></span><span id="fwpm_condition_nexthop_sub_interface_index"></span><dl> <dt>**FWPM\_CONDITION\_NEXTHOP\_SUB\_INTERFACE\_INDEX**</dt> </dl>                 | The sub-interface index of the next-hop interface.<br/> **Data type:** FWP\_UINT32<br/>                                                                                                                                                                                       |
| <span id="FWPM_CONDITION_ORIGINAL_PROFILE_ID"></span><span id="fwpm_condition_original_profile_id"></span><dl> <dt>**FWPM\_CONDITION\_ORIGINAL\_PROFILE\_ID**</dt> </dl>                                          | The network category of the arrival or next-hop interface through which the ALE flow (inbound or outbound) is created. <br/> **Data type:** FWP\_UINT32<br/>                                                                                                                  |
| <span id="FWPM_CONDITION_CURRENT_PROFILE_ID"></span><span id="fwpm_condition_current_profile_id"></span><dl> <dt>**FWPM\_CONDITION\_CURRENT\_PROFILE\_ID**</dt> </dl>                                             | The network category of the arrival or next-hop interface through which the current packet (inbound or outbound) is created. <br/> **Data type:** FWP\_UINT32<br/>                                                                                                            |
| <span id="FWPM_CONDITION_LOCAL_INTERFACE_PROFILE_ID"></span><span id="fwpm_condition_local_interface_profile_id"></span><dl> <dt>**FWPM\_CONDITION\_LOCAL\_INTERFACE\_PROFILE\_ID**</dt> </dl>                    | The network category of the delivery interface.<br/> **Data type:** FWP\_UINT32<br/>                                                                                                                                                                                          |
| <span id="FWPM_CONDITION_ARRIVAL_INTERFACE_PROFILE_ID"></span><span id="fwpm_condition_arrival_interface_profile_id"></span><dl> <dt>**FWPM\_CONDITION\_ARRIVAL\_INTERFACE\_PROFILE\_ID**</dt> </dl>              | The network category of the arrival interface.<br/> **Data type:** FWP\_UINT32<br/>                                                                                                                                                                                           |
| <span id="FWPM_CONDITION_NEXTHOP_INTERFACE_PROFILE_ID"></span><span id="fwpm_condition_nexthop_interface_profile_id"></span><dl> <dt>**FWPM\_CONDITION\_NEXTHOP\_INTERFACE\_PROFILE\_ID**</dt> </dl>              | The network category of the next-hop interface.<br/> **Data type:** FWP\_UINT32<br/>                                                                                                                                                                                          |
| <span id="FWPM_CONDITION_REAUTHORIZE_REASON"></span><span id="fwpm_condition_reauthorize_reason"></span><dl> <dt>**FWPM\_CONDITION\_REAUTHORIZE\_REASON**</dt> </dl>                                              | The reason for reauthorizing a previously authorized connection.<br/> **Data type:** FWP\_UINT32<br/>                                                                                                                                                                         |
| <span id="FWPM_CONDITION_ALE_REAUTH_REASON"></span><span id="fwpm_condition_ale_reauth_reason"></span><dl> <dt>**FWPM\_CONDITION\_ALE\_REAUTH\_REASON**</dt> </dl>                                                | The reason for reauthorizing a previously authorized connection, such as **FWP\_CONDITION\_REAUTHORIZE\_REASON\_POLICY\_CHANGE** (or one of the other values listed in [**Filtering Condition Flags**](filtering-condition-flags-.md)).<br/> **Data type:** FWP\_UINT32<br/> |
| <span id="FWPM_CONDITION_ORIGINAL_ICMP_TYPE"></span><span id="fwpm_condition_original_icmp_type"></span><dl> <dt>**FWPM\_CONDITION\_ORIGINAL\_ICMP\_TYPE**</dt> </dl>                                             | The ICMP type with which the flow was created.<br/> **Data type:** FWP\_UINT16<br/>                                                                                                                                                                                           |
| <span id="FWPM_CONDITION_IP_PHYSICAL_ARRIVAL_INTERFACE"></span><span id="fwpm_condition_ip_physical_arrival_interface"></span><dl> <dt>**FWPM\_CONDITION\_IP\_PHYSICAL\_ARRIVAL\_INTERFACE**</dt> </dl>           | The LUID of the physical interface associated with the arrival IP address.<br/> **Data type:** FWP\_UINT64<br/>                                                                                                                                                               |
| <span id="FWPM_CONDITION_IP_PHYSICAL_NEXTHOP_INTERFACE"></span><span id="fwpm_condition_ip_physical_nexthop_interface"></span><dl> <dt>**FWPM\_CONDITION\_IP\_PHYSICAL\_NEXTHOP\_INTERFACE**</dt> </dl>           | The LUID of the physical interface of the next hop.<br/> **Data type:** FWP\_UINT64<br/>                                                                                                                                                                                      |
| <span id="FWPM_CONDITION_INTERFACE_QUARANTINE_EPOCH"></span><span id="fwpm_condition_interface_quarantine_epoch"></span><dl> <dt>**FWPM\_CONDITION\_INTERFACE\_QUARANTINE\_EPOCH**</dt> </dl>                     | The epoch count associated with an interface. Reserved.<br/> **Data type:** FWP\_UINT64<br/>                                                                                                                                                                                  |
| <span id="FWPM_CONDITION_ALE_SIO_FIREWALL_SOCKET_PROPERTY"></span><span id="fwpm_condition_ale_sio_firewall_socket_property"></span><dl> <dt>**FWPM\_CONDITION\_ALE\_SIO\_FIREWALL\_SOCKET\_PROPERTY**</dt> </dl> | Reserved for internal use. <br/> **Data type:** FWP\_UINT32<br/>                                                                                                                                                                                                              |





| Constants available for Windows Vista with SP1, Windows Server 2008, and later                                                                                                                                                                           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="FWPM_CONDITION_IP_ARRIVAL_INTERFACE"></span><span id="fwpm_condition_ip_arrival_interface"></span><dl> <dt>**FWPM\_CONDITION\_IP\_ARRIVAL\_INTERFACE**</dt> </dl>                       | The LUID for the network interface associated with the arrival IP address. <br/> **Data type:** FWP\_UINT64<br/>                                                                                                                                                                                                                                                                                                                                                                          |
| <span id="FWPM_CONDITION_ARRIVAL_INTERFACE_TYPE"></span><span id="fwpm_condition_arrival_interface_type"></span><dl> <dt>**FWPM\_CONDITION\_ARRIVAL\_INTERFACE\_TYPE**</dt> </dl>                 | The type of the arrival network interface as defined by the Internet Assigned Names Authority (IANA). For more information, see [https://www.iana.org/assignments/ianaiftype-mib](https://www.iana.org/assignments/ianaiftype-mib). <br/> **Possible values:** The interface type values listed in the Ipifcons.h header file.<br/> **Data type:** FWP\_UINT32<br/>                                                                                                                   |
| <span id="_FWPM_CONDITION_ARRIVAL_TUNNEL_TYPE"></span><span id="_fwpm_condition_arrival_tunnel_type"></span><dl> <dt> **FWPM\_CONDITION\_ARRIVAL\_TUNNEL\_TYPE**</dt> </dl>                       | The encapsulation method used by a tunnel associated with the arrival network interface if the Type member is IF\_TYPE\_TUNNEL. The tunnel type is defined by the Internet Assigned Names Authority (IANA). For more information, see [https://www.iana.org/assignments/ianaiftype-mib](https://www.iana.org/assignments/ianaiftype-mib). <br/> **Possible values:** The TUNNEL\_TYPE enumeration type values listed in the Ifdef.h header file.<br/> **Data type:** FWP\_UINT32<br/> |
| <span id="FWPM_CONDITION_ARRIVAL_INTERFACE_INDEX"></span><span id="fwpm_condition_arrival_interface_index"></span><dl> <dt>**FWPM\_CONDITION\_ARRIVAL\_INTERFACE\_INDEX**</dt> </dl>              | The index of the arrival network interface, as enumerated by the network stack.<br/> **Data type:** FWP\_UINT32<br/>                                                                                                                                                                                                                                                                                                                                                                      |
| <span id="FWPM_CONDITION_ARRIVAL_SUB_INTERFACE_INDEX"></span><span id="fwpm_condition_arrival_sub_interface_index"></span><dl> <dt>**FWPM\_CONDITION\_ARRIVAL\_SUB\_INTERFACE\_INDEX**</dt> </dl> | The index of the arrival network interface, as enumerated by the network stack. <br/> **Data type:** FWP\_UINT32<br/>                                                                                                                                                                                                                                                                                                                                                                     |
| <span id="FWPM_CONDITION_LOCAL_INTERFACE_INDEX"></span><span id="fwpm_condition_local_interface_index"></span><dl> <dt>**FWPM\_CONDITION\_LOCAL\_INTERFACE\_INDEX**</dt> </dl>                    | The index of the network interface, as enumerated by the network stack. <br/> **Data type:** FWP\_UINT32<br/>                                                                                                                                                                                                                                                                                                                                                                             |
| <span id="FWPM_CONDITION_LOCAL_INTERFACE_TYPE"></span><span id="fwpm_condition_local_interface_type"></span><dl> <dt>**FWPM\_CONDITION\_LOCAL\_INTERFACE\_TYPE**</dt> </dl>                       | The interface type as defined by the Internet Assigned Names Authority (IANA). For more information, see [https://www.iana.org/assignments/ianaiftype-mib](https://www.iana.org/assignments/ianaiftype-mib). <br/> **Possible values:** The interface type values listed in the Ipifcons.h header file.<br/> **Data type:** FWP\_UINT32<br/>                                                                                                                                          |
| <span id="FWPM_CONDITION_LOCAL_TUNNEL_TYPE"></span><span id="fwpm_condition_local_tunnel_type"></span><dl> <dt>**FWPM\_CONDITION\_LOCAL\_TUNNEL\_TYPE**</dt> </dl>                                | The encapsulation method used by a tunnel if the Type member is IF\_TYPE\_TUNNEL. The tunnel type is defined by the Internet Assigned Names Authority (IANA). For more information, see [https://www.iana.org/assignments/ianaiftype-mib](https://www.iana.org/assignments/ianaiftype-mib). <br/> **Possible values:** The TUNNEL\_TYPE enumeration type values listed in the Ifdef.h header file.<br/> **Data type:** FWP\_UINT32 <br/>                                              |






| Constants available for Windows Vista and later | Description | 
|-------------------------------------------------|-------------|
| <span id="FWPM_CONDITION_IP_LOCAL_ADDRESS"></span><span id="fwpm_condition_ip_local_address"></span><dl><dt><strong>FWPM_CONDITION_IP_LOCAL_ADDRESS</strong></dt></dl> | The local IP address. <br /><strong>Data type:</strong> For an IPv4 address<ul><li>FWP_V4_ADDR_MASK, or</li><li>FWP_UINT32</li></ul><br /><strong>Data type:</strong> For an IPv6 address<ul><li>FWP_V6_ADDR_MASK, or</li><li>FWP_BYTE_ARRAY16_TYPE</li></ul><br /> | 
| <span id="FWPM_CONDITION_IP_REMOTE_ADDRESS"></span><span id="fwpm_condition_ip_remote_address"></span><dl><dt><strong>FWPM_CONDITION_IP_REMOTE_ADDRESS</strong></dt></dl> | The remote IP address. <br /><strong>Data type:</strong> For an IPv4 address<ul><li>FWP_V4_ADDR_MASK, or</li><li>FWP_UINT32</li></ul><br /><strong>Data type:</strong> For an IPv6 address<ul><li>FWP_V6_ADDR_MASK, or</li><li>FWP_BYTE_ARRAY16_TYPE</li></ul><br /> | 
| <span id="FWPM_CONDITION_IP_SOURCE_ADDRESS"></span><span id="fwpm_condition_ip_source_address"></span><dl><dt><strong>FWPM_CONDITION_IP_SOURCE_ADDRESS</strong></dt></dl> | The source IP address for forwarded packets. <br /><strong>Data type:</strong> For an IPv4 address<ul><li>FWP_V4_ADDR_MASK, or</li><li>FWP_UINT32</li></ul><br /><strong>Data type:</strong> For an IPv6 address<ul><li>FWP_V6_ADDR_MASK, or</li><li>FWP_BYTE_ARRAY16_TYPE</li></ul><br /> | 
| <span id="FWPM_CONDITION_IP_DESTINATION_ADDRESS"></span><span id="fwpm_condition_ip_destination_address"></span><dl><dt><strong>FWPM_CONDITION_IP_DESTINATION_ADDRESS</strong></dt></dl> | The destination IP address for forwarded packets. <br /><strong>Data type:</strong> For an IPv4 address<ul><li>FWP_V4_ADDR_MASK, or</li><li>FWP_UINT32</li></ul><br /><strong>Data type:</strong> For an IPv6 address<ul><li>FWP_V6_ADDR_MASK, or</li><li>FWP_BYTE_ARRAY16_TYPE</li></ul><br /> | 
| <span id="FWPM_CONDITION_IP_LOCAL_ADDRESS_TYPE"></span><span id="fwpm_condition_ip_local_address_type"></span><dl><dt><strong>FWPM_CONDITION_IP_LOCAL_ADDRESS_TYPE</strong></dt></dl> | The local IP address type. <br /><strong>Possible values:</strong> Any of the following <a href="/windows/win32/api/nldef/ne-nldef-nl_address_type">NL_ADDRESS_TYPE</a> enumeration values.<ul><li>NlatUnspecified</li><li>NlatUnicast</li><li>NlatAnycast</li><li>NlatMulticast</li><li>NlatBroadcast</li></ul><br /><strong>Data type:</strong> FWP_UINT8<br /> | 
| <span id="FWPM_CONDITION_IP_DESTINATION_ADDRESS_TYPE"></span><span id="fwpm_condition_ip_destination_address_type"></span><dl><dt><strong>FWPM_CONDITION_IP_DESTINATION_ADDRESS_TYPE</strong></dt></dl> | The destination IP address type for forwarded packets. <br /><strong>Possible values:</strong> Any of the following <a href="/windows/win32/api/nldef/ne-nldef-nl_address_type">NL_ADDRESS_TYPE</a> enumeration values.<ul><li>NlatUnspecified</li><li>NlatUnicast</li><li>NlatAnycast</li><li>NlatMulticast</li><li>NlatBroadcast</li></ul><br /><strong>Data type:</strong> FWP_UINT8<br /> | 
| <span id="FWPM_CONDITION_IP_LOCAL_INTERFACE"></span><span id="fwpm_condition_ip_local_interface"></span><dl><dt><strong>FWPM_CONDITION_IP_LOCAL_INTERFACE</strong></dt></dl> | The LUID for the network interface associated with the local IP address. <br /><strong>Data type:</strong> FWP_UINT64<br /> | 
| <span id="FWPM_CONDITION_INTERFACE_TYPE"></span><span id="fwpm_condition_interface_type"></span><dl><dt><strong>FWPM_CONDITION_INTERFACE_TYPE</strong></dt></dl> | The interface type as defined by the Internet Assigned Names Authority (IANA). For more information, see [https://www.iana.org/assignments/ianaiftype-mib](https://www.iana.org/assignments/ianaiftype-mib). <br /><strong>Possible values:</strong> The interface type values listed in the Ipifcons.h header file.<br /><strong>Data type:</strong> FWP_UINT32<br /> | 
| <span id="FWPM_CONDITION_TUNNEL_TYPE"></span><span id="fwpm_condition_tunnel_type"></span><dl><dt><strong>FWPM_CONDITION_TUNNEL_TYPE</strong></dt></dl> | The encapsulation method used by a tunnel if the Type member is IF_TYPE_TUNNEL. The tunnel type is defined by the Internet Assigned Names Authority (IANA). For more information, see <a href="https://www.iana.org/assignments/ianaiftype-mib">https://www.iana.org/assignments/ianaiftype-mib</a>. <br /><strong>Possible values:</strong> The TUNNEL_TYPE enumeration type values listed in the Ifdef.h header file.<br /><strong>Data type:</strong> FWP_UINT32 <br /> | 
| <span id="FWPM_CONDITION_IP_FORWARD_INTERFACE"></span><span id="fwpm_condition_ip_forward_interface"></span><dl><dt><strong>FWPM_CONDITION_IP_FORWARD_INTERFACE</strong></dt></dl> | The LUID for the network interface on which the packet being forwarded is to be sent out. <br /><strong>Data type:</strong> FWP_UINT64<br /> | 
| <span id="FWPM_CONDITION_IP_PROTOCOL"></span><span id="fwpm_condition_ip_protocol"></span><dl><dt><strong>FWPM_CONDITION_IP_PROTOCOL</strong></dt></dl> | The IP protocol number, as specified in RFC 1700. <br /><strong>Data type:</strong> FWP_UINT8<br /> | 
| <span id="FWPM_CONDITION_IP_LOCAL_PORT"></span><span id="fwpm_condition_ip_local_port"></span><dl><dt><strong>FWPM_CONDITION_IP_LOCAL_PORT</strong></dt></dl> | The local transport protocol port number.<br /><strong>Data type:</strong> FWP_UINT16<br /> | 
| <span id="FWPM_CONDITION_ICMP_TYPE"></span><span id="fwpm_condition_icmp_type"></span><dl><dt><strong>FWPM_CONDITION_ICMP_TYPE</strong></dt></dl> | The ICMP type field, as specified in RFC 792. <br /><strong>Data type:</strong> FWP_UINT16<br /> | 
| <span id="FWPM_CONDITION_IP_REMOTE_PORT"></span><span id="fwpm_condition_ip_remote_port"></span><dl><dt><strong>FWPM_CONDITION_IP_REMOTE_PORT</strong></dt></dl> | The remote transport protocol port number. <br /><strong>Data type:</strong> FWP_UINT16<br /> | 
| <span id="FWPM_CONDITION_ICMP_CODE"></span><span id="fwpm_condition_icmp_code"></span><dl><dt><strong>FWPM_CONDITION_ICMP_CODE</strong></dt></dl> | The ICMP code field, as specified in RFC 792. <br /><strong>Data type:</strong> FWP_UINT16<br /> | 
| <span id="FWPM_CONDITION_EMBEDDED_LOCAL_ADDRESS_TYPE"></span><span id="fwpm_condition_embedded_local_address_type"></span><dl><dt><strong>FWPM_CONDITION_EMBEDDED_LOCAL_ADDRESS_TYPE</strong></dt></dl> | The local IP address type that is embedded in the ICMP packet.<br /><strong>Possible values:</strong> Any of the following <a href="/windows/win32/api/nldef/ne-nldef-nl_address_type">NL_ADDRESS_TYPE</a> enumeration values.<ul><li>NlatUnspecified</li><li>NlatUnicast</li><li>NlatAnycast</li><li>NlatMulticast</li><li>NlatBroadcast</li></ul><br /><strong>Data type:</strong> FWP_UINT8<br /> | 
| <span id="FWPM_CONDITION_EMBEDDED_REMOTE_ADDRESS"></span><span id="fwpm_condition_embedded_remote_address"></span><dl><dt><strong>FWPM_CONDITION_EMBEDDED_REMOTE_ADDRESS</strong></dt></dl> | The remote IP address that is embedded in the ICMP packet. <br /><strong>Data type:</strong> For an IPv4 address<ul><li>FWP_V4_ADDR_MASK, or</li><li>FWP_UINT32</li></ul><br /><strong>Data type:</strong> For an IPv6 address<ul><li>FWP_V6_ADDR_MASK, or</li><li>FWP_BYTE_ARRAY16_TYPE</li></ul><br /> | 
| <span id="FWPM_CONDITION_EMBEDDED_PROTOCOL"></span><span id="fwpm_condition_embedded_protocol"></span><dl><dt><strong>FWPM_CONDITION_EMBEDDED_PROTOCOL</strong></dt></dl> | The IP protocol number that is embedded in the ICMP packet, as specified in RFC 1700. <br /><strong>Data type:</strong> FWP_UINT8<br /> | 
| <span id="FWPM_CONDITION_EMBEDDED_LOCAL_PORT"></span><span id="fwpm_condition_embedded_local_port"></span><dl><dt><strong>FWPM_CONDITION_EMBEDDED_LOCAL_PORT</strong></dt></dl> | The local transport protocol port number that is embedded in the ICMP packet. <br /><strong>Data type:</strong> FWP_UINT16<br /> | 
| <span id="FWPM_CONDITION_EMBEDDED_REMOTE_PORT"></span><span id="fwpm_condition_embedded_remote_port"></span><dl><dt><strong>FWPM_CONDITION_EMBEDDED_REMOTE_PORT</strong></dt></dl> | The remote transport protocol port number that is embedded in the ICMP packet. <br /><strong>Data type:</strong> FWP_UINT16<br /> | 
| <span id="FWPM_CONDITION_FLAGS"></span><span id="fwpm_condition_flags"></span><dl><dt><strong>FWPM_CONDITION_FLAGS</strong></dt></dl> | A bitwise OR of a combination of filtering condition flags. <br /><strong>Possible values:</strong> See <a href="filtering-condition-flags-.md"><strong>Filtering Condition Flags</strong></a><br /><strong>Data type:</strong> FWP_UINT32<br /> | 
| <span id="FWPM_CONDITION_DIRECTION"></span><span id="fwpm_condition_direction"></span><dl><dt><strong>FWPM_CONDITION_DIRECTION</strong></dt></dl> | The direction of the traffic or data flow. <br /><strong>Possible values:  </strong><ul><li>FWP_DIRECTION_INBOUND</li><li>FWP_DIRECTION_OUTBOUND</li></ul><br /> For datagram layers (FWPM_LAYER_DATAGRAM_DATA_*) and stream packet layers (FWPM_LAYER_STREAM_PACKET_*), the value will be the same as the direction of the packet. <br /> For stream layers (FWPM_LAYER_STREAM_*) and flow established layers (FWPM_LAYER_ALE_FLOW_ESTABLISHED_*), the value will be the same as direction of the connection. (For example, when a local application initiates the connection, an inbound packet has <strong>FWPM_CONDITION_DIRECTION</strong> set to <strong>FWP_DIRECTION_OUTBOUND</strong>.) <br /><strong>Data type:</strong> FWP_UINT32<br /> | 
| <span id="FWPM_CONDITION_INTERFACE_INDEX"></span><span id="fwpm_condition_interface_index"></span><dl><dt><strong>FWPM_CONDITION_INTERFACE_INDEX</strong></dt></dl> | The index of the network interface, as enumerated by the network stack. <br /><strong>Data type:</strong> FWP_UINT32<br /> | 
| <span id="FWPM_CONDITION_SUB_INTERFACE_INDEX"></span><span id="fwpm_condition_sub_interface_index"></span><dl><dt><strong>FWPM_CONDITION_SUB_INTERFACE_INDEX</strong></dt></dl> | The index of the logical network interface, as enumerated by the network stack. <br /><strong>Data type:</strong> FWP_UINT32<br /> | 
| <span id="FWPM_CONDITION_SOURCE_INTERFACE_INDEX"></span><span id="fwpm_condition_source_interface_index"></span><dl><dt><strong>FWPM_CONDITION_SOURCE_INTERFACE_INDEX</strong></dt></dl> | The index of the source network interface for forwarded packets, as enumerated by the network stack.<br /><strong>Data type:</strong> FWP_UINT32<br /> | 
| <span id="FWPM_CONDITION_SOURCE_SUB_INTERFACE_INDEX"></span><span id="fwpm_condition_source_sub_interface_index"></span><dl><dt><strong>FWPM_CONDITION_SOURCE_SUB_INTERFACE_INDEX</strong></dt></dl> | The index of the source logical network interface for forwarded packets, as enumerated by the network stack. <br /><strong>Data type:</strong> FWP_UINT32<br /> | 
| <span id="FWPM_CONDITION_DESTINATION_INTERFACE_INDEX"></span><span id="fwpm_condition_destination_interface_index"></span><dl><dt><strong>FWPM_CONDITION_DESTINATION_INTERFACE_INDEX</strong></dt></dl> | The index of the destination network interface for forwarded packets, as enumerated by the network stack. <br /><strong>Data type:</strong> FWP_UINT32<br /> | 
| <span id="FWPM_CONDITION_DESTINATION_SUB_INTERFACE_INDEX"></span><span id="fwpm_condition_destination_sub_interface_index"></span><dl><dt><strong>FWPM_CONDITION_DESTINATION_SUB_INTERFACE_INDEX</strong></dt></dl> | The index of the destination logical network interface for forwarded packets, as enumerated by the network stack. <br /><strong>Data type:</strong> FWP_UINT32<br /> | 
| <span id="FWPM_CONDITION_ALE_APP_ID"></span><span id="fwpm_condition_ale_app_id"></span><dl><dt><strong>FWPM_CONDITION_ALE_APP_ID</strong></dt></dl> | The lower-case fully qualified device path of the application, as returned by the <a href="/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmgetappidfromfilename0"><strong>FwpmGetAppIdFromFileName0</strong></a> function. <br /> (For example, "\device\hardiskvolume1\program files\application.exe".)<br /><strong>Data type:</strong> FWP_BYTE_BLOB_TYPE<br /> | 
| <span id="FWPM_CONDITION_ALE_USER_ID"></span><span id="fwpm_condition_ale_user_id"></span><dl><dt><strong>FWPM_CONDITION_ALE_USER_ID</strong></dt></dl> | The identification of the local user. <br /><strong>Data type:</strong> FWP_SECURITY_DESCRIPTOR_TYPE<br /> | 
| <span id="FWPM_CONDITION_ALE_REMOTE_USER_ID"></span><span id="fwpm_condition_ale_remote_user_id"></span><dl><dt><strong>FWPM_CONDITION_ALE_REMOTE_USER_ID</strong></dt></dl> | The identification of the remote user. <br /><strong>Data type:</strong> FWP_SECURITY_DESCRIPTOR_TYPE<br /> | 
| <span id="FWPM_CONDITION_ALE_REMOTE_MACHINE_ID"></span><span id="fwpm_condition_ale_remote_machine_id"></span><dl><dt><strong>FWPM_CONDITION_ALE_REMOTE_MACHINE_ID</strong></dt></dl> | The identification of the remote machine. <br /><strong>Data type:</strong> FWP_SECURITY_DESCRIPTOR_TYPE<br /> | 
| <span id="FWPM_CONDITION_ALE_PROMISCUOUS_MODE"></span><span id="fwpm_condition_ale_promiscuous_mode"></span><dl><dt><strong>FWPM_CONDITION_ALE_PROMISCUOUS_MODE</strong></dt></dl> | The raw socket mode that is allowed or denied.<br /><strong>Possible values:  </strong><ul><li>SIO_RCVALL</li><li>SIO_RCVALL_IGMPMCAST</li><li>SIO_RCVALL_MCAST</li></ul>For a description of these raw socket modes, see the <a href="/windows/desktop/api/winsock2/nf-winsock2-wsaioctl"><strong>WSAIoctl</strong></a> function.<br /><strong>Data type:</strong> FWP_UINT32<br /> | 
| <span id="FWPM_CONDITION_ALE_SIO_FIREWALL_SYSTEM_PORT"></span><span id="fwpm_condition_ale_sio_firewall_system_port"></span><dl><dt><strong>FWPM_CONDITION_ALE_SIO_FIREWALL_SYSTEM_PORT</strong></dt></dl> | Reserved for internal use. <br /><strong>Data type:</strong> FWP_UINT32<br /> | 
| <span id="FWPM_CONDITION_ALE_NAP_CONTEXT"></span><span id="fwpm_condition_ale_nap_context"></span><dl><dt><strong>FWPM_CONDITION_ALE_NAP_CONTEXT</strong></dt></dl> | Reserved for internal use. <br /><strong>Data type:</strong> FWP_UINT32<br /> | 




The following constants are available for user mode only.



| User-mode conditions available for Windows 8 and Windows Server 2012                                                                                                                       | Description                                                                                                                                                               |
|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="FWPM_CONDITION_QM_MODE"></span><span id="fwpm_condition_qm_mode"></span><dl> <dt>**FWPM\_CONDITION\_QM\_MODE**</dt> </dl> | The mode of the quick mode (QM) filter. See [**IPSEC\_TRAFFIC\_TYPE**](/windows/desktop/api/Ipsectypes/ne-ipsectypes-ipsec_traffic_type) for possible values.<br/> **Data type:** FWP\_UINT32<br/> |






| User-mode conditions available for Windows 7, Windows Server 2008 R2, and later | Description | 
|---------------------------------------------------------------------------------|-------------|
| <span id="FWPM_CONDITION_KM_AUTH_NAP_CONTEXT"></span><span id="fwpm_condition_km_auth_nap_context"></span><dl><dt><strong>FWPM_CONDITION_KM_AUTH_NAP_CONTEXT</strong></dt></dl> | Reserved for internal use.<br /><strong>Data type:</strong> FWP_UINT32<br /> | 
| <span id="FWPM_CONDITION_PEER_NAME"></span><span id="fwpm_condition_peer_name"></span><dl><dt><strong>FWPM_CONDITION_PEER_NAME</strong></dt></dl> | The name of the peer. For example, the peer's DNS name.<br /><strong>Data type:</strong> FWP_BYTE_BLOB_TYPE<br /> | 
| <span id="FWPM_CONDITION_REMOTE_ID"></span><span id="fwpm_condition_remote_id"></span><dl><dt><strong>FWPM_CONDITION_REMOTE_ID</strong></dt></dl> | The identity of the remote authentication principal. <br /><strong>Data type:</strong> FWP_SECURITY_DESCRIPTOR_TYPE<br /> | 
| <span id="FWPM_CONDITION_AUTHENTICATION_TYPE"></span><span id="fwpm_condition_authentication_type"></span><dl><dt><strong>FWPM_CONDITION_AUTHENTICATION_TYPE</strong></dt></dl> | The type of IKE, IKEv2, or AuthIP authentication method. <br /><strong>Data type:</strong> IKEEXT_AUTHENTICATION_METHOD_TYPE<br /> | 
| <span id="FWPM_CONDITION_KM_TYPE"></span><span id="fwpm_condition_km_type"></span><dl><dt><strong>FWPM_CONDITION_KM_TYPE</strong></dt></dl> | The type of keying module.<br /><strong>Data type:</strong> IKEEXT_KEY_MODULE_TYPE<br /> | 
| <span id="FWPM_CONDITION_KM_MODE"></span><span id="fwpm_condition_km_mode"></span><dl><dt><strong>FWPM_CONDITION_KM_MODE</strong></dt></dl> | The IPsec mode in which a token can be obtained.<br /><strong>Data type:</strong> IPSEC_TOKEN_MODE<br /> | 
| <span id="FWPM_CONDITION_IPSEC_POLICY_KEY"></span><span id="fwpm_condition_ipsec_policy_key"></span><dl><dt><strong>FWPM_CONDITION_IPSEC_POLICY_KEY</strong></dt></dl> | The main mode (MM) or quick mode (QM) policy provider context key of the SA being authorized. Useful for restricting the scope of the authorization rule to SAs formed using a specified IPsec MM or QM policy key.<br /><strong>Data type:</strong> FWP_BYTE_ARRAY16_TYPE<br /> | 
| <span id="FWPM_CONDITION_AUTHENTICATION_TYPE"></span><span id="fwpm_condition_authentication_type"></span><dl><dt><strong>FWPM_CONDITION_AUTHENTICATION_TYPE</strong></dt></dl> | The method used to authenticate the security association.<br /><blockquote>[!Note]<br />Available only on Windows Server 2008 R2, Windows 7, and later.</blockquote><br /><strong>Data type:</strong> FWP_UINT32 <br /> | 







| Constants available for Windows Vista and later | Description | 
|-------------------------------------------------|-------------|
| <span id="FWPM_CONDITION_REMOTE_USER_TOKEN"></span><span id="fwpm_condition_remote_user_token"></span><dl><dt><strong>FWPM_CONDITION_REMOTE_USER_TOKEN</strong></dt></dl> | The identification of the remote user.<br /><strong>Data type:</strong> FWP_SECURITY_DESCRIPTOR_TYPE<br /> | 
| <span id="FWPM_CONDITION_RPC_IF_UUID"></span><span id="fwpm_condition_rpc_if_uuid"></span><dl><dt><strong>FWPM_CONDITION_RPC_IF_UUID</strong></dt></dl> | The UUID of the RPC interface. <br /><strong>Data type:</strong> FWP_BYTE_ARRAY16_TYPE<br /> | 
| <span id="FWPM_CONDITION_RPC_IF_VERSION"></span><span id="fwpm_condition_rpc_if_version"></span><dl><dt><strong>FWPM_CONDITION_RPC_IF_VERSION</strong></dt></dl> | The version of the RPC interface. <br /><strong>Data type:</strong> FWP_UINT16<br /> | 
| <span id="FWPM_CONDITION_RPC_IF_FLAG"></span><span id="fwpm_condition_rpc_if_flag"></span><dl><dt><strong>FWPM_CONDITION_RPC_IF_FLAG</strong></dt></dl> | Reserved for internal use. <br /><strong>Data type:</strong> FWP_UINT32<br /> | 
| <span id="FWPM_CONDITION_DCOM_APP_ID"></span><span id="fwpm_condition_dcom_app_id"></span><dl><dt><strong>FWPM_CONDITION_DCOM_APP_ID</strong></dt></dl> | The identification of the COM application.<br /><strong>Data type:</strong> FWP_BYTE_ARRAY16_TYPE<br /> | 
| <span id="FWPM_CONDITION_IMAGE_NAME"></span><span id="fwpm_condition_image_name"></span><dl><dt><strong>FWPM_CONDITION_IMAGE_NAME</strong></dt></dl> | The name of the application.<br /><strong>Data type:</strong> FWP_BYTE_BLOB_TYPE<br /> | 
| <span id="FWPM_CONDITION_RPC_PROTOCOL"></span><span id="fwpm_condition_rpc_protocol"></span><dl><dt><strong>FWPM_CONDITION_RPC_PROTOCOL</strong></dt></dl> | The RPC protocol. <br /><strong>Possible values:  </strong><ul><li>RPC_PROTSEQ_TCP</li><li>RPC_PROTSEQ_NMP</li><li>RPC_PROTSEQ_LRPC</li><li>RPC_PROTSEQ_HTTP</li></ul><br /><strong>Data type:</strong> FWP_UINT8<br /> | 
| <span id="FWPM_CONDITION_RPC_AUTH_TYPE"></span><span id="fwpm_condition_rpc_auth_type"></span><dl><dt><strong>FWPM_CONDITION_RPC_AUTH_TYPE</strong></dt></dl> | The authentication service type. For more information about authentication service types, see <a href="/windows/desktop/Rpc/authentication-service-constants"><strong>Authentication-Service Constants</strong></a>. <br /><strong>Data type:</strong> FWP_UINT8<br /> | 
| <span id="FWPM_CONDITION_RPC_AUTH_LEVEL"></span><span id="fwpm_condition_rpc_auth_level"></span><dl><dt><strong>FWPM_CONDITION_RPC_AUTH_LEVEL</strong></dt></dl> | The authentication service level. For more information about authentication service levels, see <a href="/windows/desktop/Rpc/authentication-level-constants"><strong>Authentication-Level Constants</strong></a>. <br /><strong>Data type:</strong> FWP_UINT8<br /> | 
| <span id="FWPM_CONDITION_SEC_ENCRYPT_ALGORITHM"></span><span id="fwpm_condition_sec_encrypt_algorithm"></span><dl><dt><strong>FWPM_CONDITION_SEC_ENCRYPT_ALGORITHM</strong></dt></dl> | The certificate based Security Service Provider Interface (SSPI) encryption algorithm.<br /><strong>Data type:</strong> FWP_UINT32<br /> | 
| <span id="FWPM_CONDITION_SEC_KEY_SIZE"></span><span id="fwpm_condition_sec_key_size"></span><dl><dt><strong>FWPM_CONDITION_SEC_KEY_SIZE</strong></dt></dl> | The certificate based SSPI encryption key size.<br /><strong>Data type:</strong> FWP_UINT32<br /> | 
| <span id="FWPM_CONDITION_IP_LOCAL_ADDRESS_V4"></span><span id="fwpm_condition_ip_local_address_v4"></span><dl><dt><strong>FWPM_CONDITION_IP_LOCAL_ADDRESS_V4</strong></dt></dl> | The local IPv4 address. <br /><strong>Data type:  </strong><ul><li>FWP_V4_ADDR_MASK, or</li><li>FWP_UINT32</li></ul><br /> | 
| <span id="FWPM_CONDITION_IP_LOCAL_ADDRESS_V6"></span><span id="fwpm_condition_ip_local_address_v6"></span><dl><dt><strong>FWPM_CONDITION_IP_LOCAL_ADDRESS_V6</strong></dt></dl> | The local IPv6 address. <br /><strong>Data type:  </strong><ul><li>FWP_V6_ADDR_MASK, or</li><li>FWP_BYTE_ARRAY16_TYPE</li></ul><br /> | 
| <span id="FWPM_CONDITION_IP_REMOTE_ADDRESS_V4"></span><span id="fwpm_condition_ip_remote_address_v4"></span><dl><dt><strong>FWPM_CONDITION_IP_REMOTE_ADDRESS_V4</strong></dt></dl> | The remote IPv4 address. <br /><strong>Data type:  </strong><ul><li>FWP_V4_ADDR_MASK, or</li><li>FWP_UINT32</li></ul><br /> | 
| <span id="FWPM_CONDITION_IP_REMOTE_ADDRESS_V6"></span><span id="fwpm_condition_ip_remote_address_v6"></span><dl><dt><strong>FWPM_CONDITION_IP_REMOTE_ADDRESS_V6</strong></dt></dl> | The remote IPv6 address. <br /><strong>Data type:  </strong><ul><li>FWP_V6_ADDR_MASK, or</li><li>FWP_BYTE_ARRAY16_TYPE</li></ul><br /> | 
| <span id="FWPM_CONDITION_PIPE"></span><span id="fwpm_condition_pipe"></span><dl><dt><strong>FWPM_CONDITION_PIPE</strong></dt></dl> | The name of the remote named pipe.<br /><strong>Data type:</strong> FWP_BYTE_BLOB_TYPE<br /> | 
| <span id="FWPM_CONDITION_PROCESS_WITH_RPC_IF_UUID"></span><span id="fwpm_condition_process_with_rpc_if_uuid"></span><dl><dt><strong>FWPM_CONDITION_PROCESS_WITH_RPC_IF_UUID</strong></dt></dl> | The UUID of the process with the RPC interface.<br /><strong>Data type:</strong> FWP_BYTE_ARRAY16_TYPE<br /> | 
| <span id="FWPM_CONDITION_RPC_EP_VALUE"></span><span id="fwpm_condition_rpc_ep_value"></span><dl><dt><strong>FWPM_CONDITION_RPC_EP_VALUE</strong></dt></dl> | Reserved for internal use.<br /><strong>Data type:</strong> FWP_BYTE_BLOB_TYPE<br /> | 
| <span id="FWPM_CONDITION_RPC_EP_FLAGS"></span><span id="fwpm_condition_rpc_ep_flags"></span><dl><dt><strong>FWPM_CONDITION_RPC_EP_FLAGS</strong></dt></dl> | Reserved for internal use.<br /><strong>Data type:</strong> FWP_UINT32<br /> | 
| <span id="FWPM_CONDITION_CLIENT_TOKEN"></span><span id="fwpm_condition_client_token"></span><dl><dt><strong>FWPM_CONDITION_CLIENT_TOKEN</strong></dt></dl> | The identification of the client when using RpcProxy.<br /><strong>Data type:</strong> FWP_SECURITY_DESCRIPTOR_TYPE<br /> | 
| <span id="FWPM_CONDITION_RPC_SERVER_NAME"></span><span id="fwpm_condition_rpc_server_name"></span><dl><dt><strong>FWPM_CONDITION_RPC_SERVER_NAME</strong></dt></dl> | The name of the RPC server when using RpcProxy.<br /><strong>Data type:</strong> FWP_BYTE_BLOB_TYPE<br /> | 
| <span id="FWPM_CONDITION_RPC_SERVER_PORT"></span><span id="fwpm_condition_rpc_server_port"></span><dl><dt><strong>FWPM_CONDITION_RPC_SERVER_PORT</strong></dt></dl> | The port on the RPC server when using RpcProxy.<br /><strong>Data type:</strong> FWP_UINT16<br /> | 
| <span id="FWPM_CONDITION_RPC_PROXY_AUTH_TYPE"></span><span id="fwpm_condition_rpc_proxy_auth_type"></span><dl><dt><strong>FWPM_CONDITION_RPC_PROXY_AUTH_TYPE</strong></dt></dl> | The RPC proxy authentication service type.<br /><strong>Data type:</strong> FWP_BYTE_BLOB_TYPE<br /> | 
| <span id="FWPM_CONDITION_CLIENT_CERT_KEY_LENGTH"></span><span id="fwpm_condition_client_cert_key_length"></span><dl><dt><strong>FWPM_CONDITION_CLIENT_CERT_KEY_LENGTH</strong></dt></dl> | The Secure Socket Layer (SSL) key length in the client certificate.<br /><strong>Data type:</strong> FWP_UINT32<br /> | 
| <span id="FWPM_CONDITION_CLIENT_CERT_OID"></span><span id="fwpm_condition_client_cert_oid"></span><dl><dt><strong>FWPM_CONDITION_CLIENT_CERT_OID</strong></dt></dl> | The object identifier in the client certificate.<br /><strong>Data type:</strong> FWP_BYTE_BLOB_TYPE<br /> | 
| <span id="FWPM_CONDITION_NET_EVENT_TYPE"></span><span id="fwpm_condition_net_event_type"></span><dl><dt><strong>FWPM_CONDITION_NET_EVENT_TYPE</strong></dt></dl> | The type of net event.<br /><strong>Data type:</strong> FWP_UINT32<br /> | 




## Remarks

When IP addresses are stored in FWP\_UINT32 format or when an IP port is stored in FWP\_UINT16 format, they are stored in host-order, not network-order.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Fwpmu.h</dt> </dl> |
