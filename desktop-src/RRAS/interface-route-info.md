---
title: INTERFACE_ROUTE_INFO structure
description: Used to specify the routes to be added or deleted on an RRAS server.
ms.assetid: 6dbf86b8-80bd-4000-8047-91a76875829f
keywords:
- INTERFACE_ROUTE_INFO structure RAS
- PINTERFACE_ROUTE_INFO structure pointer RAS
topic_type:
- apiref
api_name:
- INTERFACE_ROUTE_INFO
api_type:
- NA
ms.topic: structure
ms.date: 05/31/2018
api_location: 
---

# INTERFACE\_ROUTE\_INFO structure

The [INTERFACE\_ROUTE\_INFO](https://docs.microsoft.com/windows) structure is used to specify the routes to be added or deleted on an RRAS server.

## Syntax


```C++
typedef struct _INTERFACE_ROUTE_INFO {
  union {
    struct {
      DWORD dwRtInfoDest;
      DWORD dwRtInfoPolicy;
      DWORD dwRtInfoNextHop;
      DWORD dwRtInfoAge;
      DWORD dwRtInfoNextHopAS;
      DWORD dwRtInfoMetric1;
      DWORD dwRtInfoMetric2;
      DWORD dwRtInfoMetric3;
    };
    struct {
      IN6_ADDR DestinationPrefix;
      DWORD    DestPrefixLength;
      IN6_ADDR NextHopAddress;
      ULONG    ValidLifeTime;
      DWORD    Flags;
      ULONG    Metric;
    };
  };
  DWORD dwRtInfoIfIndex;
  DWORD dwRtInfoType;
  DWORD dwRtInfoProto;
  DWORD dwRtInfoPreference;
  DWORD dwRtInfoViewSet;
  BOOL  bV4;
} INTERFACE_ROUTE_INFO, *PINTERFACE_ROUTE_INFO;
```



## Members

<dl> <dt>

( *unnamed struct* )
</dt> <dd>

The members of this struct are used to specify IPv4 route information.

<dl> <dt>

**dwRtInfoDest**
</dt> <dd>

The destination IPv4 address of the route. An entry with an IPv4 address of 0.0.0.0 (0x00000000) is considered a default route. This member cannot be set to a multicast (class D) IPv4 address.

</dd> <dt>

**dwRtInfoPolicy**
</dt> <dd>

The set of conditions that would cause the selection of a multi-path route (the set of next hops for a given destination). This member is typically encoded in IP TOS format as described in [RFC 1354](Http://go.microsoft.com/fwlink/p/?linkid=84028).

</dd> <dt>

**dwRtInfoNextHop**
</dt> <dd>

For remote routes, this is the IPv4 address of the next system en route. Otherwise, this is an IPv4 address of 0.0.0.0 (0x00000000).

</dd> <dt>

**dwRtInfoAge**
</dt> <dd>

The number of seconds since the route was added or modified in the network routing table.

</dd> <dt>

**dwRtInfoNextHopAS**
</dt> <dd>

The autonomous system number of the next hop. When this member is unknown or not relevant to the protocol or routing mechanism specified in **dwRtInfoProto**, this value should be set to zero. This value is documented in [RFC 1354](Http://go.microsoft.com/fwlink/p/?linkid=84028).

</dd> <dt>

**dwRtInfoMetric1**
</dt> <dd>

An alternate routing metric value for this route. The semantics of this metric are determined by the routing protocol specified in **dwRtInfoProto**. If this metric is not used, its value should be set to  1. This value is documented in [RFC 1354](Http://go.microsoft.com/fwlink/p/?linkid=84028).

</dd> <dt>

**dwRtInfoMetric2**
</dt> <dd>

An alternate routing metric value for this route. The semantics of this metric are determined by the routing protocol specified in **dwRtInfoProto**. If this metric is not used, its value should be set to  1. This value is documented in [RFC 1354](Http://go.microsoft.com/fwlink/p/?linkid=84028).

</dd> <dt>

**dwRtInfoMetric3**
</dt> <dd>

An alternate routing metric value for this route. The semantics of this metric are determined by the routing protocol specified in **dwRtInfoProto**. If this metric is not used, its value should be set to  1. This value is documented in [RFC 1354](Http://go.microsoft.com/fwlink/p/?linkid=84028).

</dd> </dl> </dd> <dt>

( *unnamed struct* )
</dt> <dd>

The members of this struct are used to specify IPv6 route information.

<dl> <dt>

**DestinationPrefix**
</dt> <dd>

An [IN6\_ADDR](Http://go.microsoft.com/fwlink/p/?linkid=116889) structure that contains the IP address prefix for the destination IP address for this route

</dd> <dt>

**DestPrefixLength**
</dt> <dd>

The length, in bits, of the site prefix or network part of the IP address specified in *DestinationPrefix*. Any value greater than 128 is an illegal value. A value of 255 is commonly used to represent an illegal value.

</dd> <dt>

**NextHopAddress**
</dt> <dd>

An [IN6\_ADDR](Http://go.microsoft.com/fwlink/p/?linkid=116889) structure that contains the IP address of the next system or gateway for a remote route. If the route is to a local loopback address or an IP address on the local link, the next hop is unspecified (all zeros). For a local loopback route, this member should be an IPv6 address of 0::0.

</dd> <dt>

**ValidLifeTime**
</dt> <dd>

The maximum time, in seconds, the IP route entry is valid. A value of 0xffffffff is infinite

</dd> <dt>

**Flags**
</dt> <dd>

Reserved. Do not use.

</dd> <dt>

**Metric**
</dt> <dd>

The route metric offset for this IP route entry. The actual route metric used to compute the route preference is the summation of the interface metric specified in the **Metric** member of the [**MIB\_IPINTERFACE\_ROW**](https://msdn.microsoft.com/library/windows/desktop/aa814496) structure and the route metric offset specified in this member. The semantics of this metric are determined by the routing protocol specified in **Protocol**. If this metric is not used, its value should be set to  1. This value is documented in [RFC 4292](Http://go.microsoft.com/fwlink/p/?linkid=84065).

</dd> </dl> </dd> <dt>

**dwRtInfoIfIndex**
</dt> <dd>

The index of the local interface through which the next hop of this route should be reached.

</dd> <dt>

**dwRtInfoType**
</dt> <dd>

The route type as described in [RFC 1354](Http://go.microsoft.com/fwlink/p/?linkid=84028) can take one of the following values.



| Value                                                                                                                                                                                                                                                      | Meaning                                                                                              |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| <span id="MIB_IPROUTE_TYPE_OTHER"></span><span id="mib_iproute_type_other"></span><dl> <dt>**MIB\_IPROUTE\_TYPE\_OTHER**</dt> <dt>1</dt> </dl>          | A route type not specified in [RFC 1354](Http://go.microsoft.com/fwlink/p/?linkid=84028).<br/> |
| <span id="MIB_IPROUTE_TYPE_INVALID"></span><span id="mib_iproute_type_invalid"></span><dl> <dt>**MIB\_IPROUTE\_TYPE\_INVALID**</dt> <dt>2</dt> </dl>    | An invalid route is logically deleted.<br/>                                                    |
| <span id="MIB_IPROUTE_TYPE_DIRECT"></span><span id="mib_iproute_type_direct"></span><dl> <dt>**MIB\_IPROUTE\_TYPE\_DIRECT**</dt> <dt>3</dt> </dl>       | A local route where the next hop is the final destination (a local interface).<br/>            |
| <span id="MIB_IPROUTE_TYPE_INDIRECT"></span><span id="mib_iproute_type_indirect"></span><dl> <dt>**MIB\_IPROUTE\_TYPE\_INDIRECT**</dt> <dt>4</dt> </dl> | A remote route where the next hop is not the final destination (a remote destination).<br/>    |



 

</dd> <dt>

**dwRtInfoProto**
</dt> <dd>

The protocol or routing mechanism that generated the route. See [Protocol Identifiers](protocol-identifiers.md) for a list of possible protocol identifiers used by routing protocols. It can take one of the following values as described in [RFC 1354](Http://go.microsoft.com/fwlink/p/?linkid=84028).



| Value                                                                                                                                                                                                             | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                        |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="MIB_IPPROTO_OTHER_"></span><span id="mib_ipproto_other_"></span><dl> <dt>**MIB\_IPPROTO\_OTHER** </dt> </dl>                                     | Some other protocol not specified in [RFC 1354](Http://go.microsoft.com/fwlink/p/?linkid=84028).<br/>                                                                                                                                                                                                                                                                                                                    |
| <span id="MIB_IPPROTO_LOCAL"></span><span id="mib_ipproto_local"></span><dl> <dt>**MIB\_IPPROTO\_LOCAL**</dt> </dl>                                        | A local interface.<br/>                                                                                                                                                                                                                                                                                                                                                                                                  |
| <span id="MIB_IPPROTO_NETMGMT"></span><span id="mib_ipproto_netmgmt"></span><dl> <dt>**MIB\_IPPROTO\_NETMGMT**</dt> </dl>                                  | A static route. This value is used to identify route information for IP routing set through network management such as Dynamic Host Configuration Protocol (DHCP), the Simple Network Management Protocol (SNMP), or by calls to the [**CreateIpForwardEntry**](https://msdn.microsoft.com/library/windows/desktop/aa365860), [**DeleteIpForwardEntry**](https://msdn.microsoft.com/library/windows/desktop/aa365878), or [**SetIpForwardEntry**](https://msdn.microsoft.com/library/windows/desktop/aa366363) functions.<br/> |
| <span id="MIB_IPPROTO_ICMP"></span><span id="mib_ipproto_icmp"></span><dl> <dt>**MIB\_IPPROTO\_ICMP**</dt> </dl>                                           | The result of an Internet Control Message Protocol (ICMP redirect.<br/>                                                                                                                                                                                                                                                                                                                                                  |
| <span id="MIB_IPPROTO_EGP"></span><span id="mib_ipproto_egp"></span><dl> <dt>**MIB\_IPPROTO\_EGP**</dt> </dl>                                              | The Exterior Gateway Protocol (EGP), a dynamic routing protocol.<br/>                                                                                                                                                                                                                                                                                                                                                    |
| <span id="MIB_IPPROTO_GGP"></span><span id="mib_ipproto_ggp"></span><dl> <dt>**MIB\_IPPROTO\_GGP**</dt> </dl>                                              | The Gateway-to-Gateway Protocol (GGP), a dynamic routing protocol.<br/>                                                                                                                                                                                                                                                                                                                                                  |
| <span id="MIB_IPPROTO_HELLO"></span><span id="mib_ipproto_hello"></span><dl> <dt>**MIB\_IPPROTO\_HELLO**</dt> </dl>                                        | The Hellospeak protocol, a dynamic routing protocol. This protocol is not supported and should not be used.<br/>                                                                                                                                                                                                                                                                                                         |
| <span id="MIB_IPPROTO_NT_STATIC"></span><span id="mib_ipproto_nt_static"></span><dl> <dt>**MIB\_IPPROTO\_NT\_STATIC**</dt> </dl>                           | A Windows specific entry added as a static route from the routing user interface or a routing command.<br/>                                                                                                                                                                                                                                                                                                              |
| <span id="MIB_IPPROTO_NT_STATIC_NON_DOD"></span><span id="mib_ipproto_nt_static_non_dod"></span><dl> <dt>**MIB\_IPPROTO\_NT\_STATIC\_NON\_DOD**</dt> </dl> | A Windows specific entry added as a static route from the routing user interface or a routing command and these routes do not cause Dial On Demand (DOD).<br/>                                                                                                                                                                                                                                                           |
| <span id="MIB_IPPROTO_BGP"></span><span id="mib_ipproto_bgp"></span><dl> <dt>**MIB\_IPPROTO\_BGP**</dt> </dl>                                              | The Border Gateway Protocol (BGP), a dynamic routing protocol.<br/>                                                                                                                                                                                                                                                                                                                                                      |
| <span id="MIB_IPPROTO_OSPF"></span><span id="mib_ipproto_ospf"></span><dl> <dt>**MIB\_IPPROTO\_OSPF**</dt> </dl>                                           | The Open Shortest Path First (OSPF) protocol, a dynamic routing protocol.<br/>                                                                                                                                                                                                                                                                                                                                           |
| <span id="MIB_IPPROTO_BBN"></span><span id="mib_ipproto_bbn"></span><dl> <dt>**MIB\_IPPROTO\_BBN**</dt> </dl>                                              | The Bolt, Beranek, and Newman (BBN) Interior Gateway Protocol (IGP) that used the Shortest Path First (SPF) algorithm, a dynamic routing protocol.<br/>                                                                                                                                                                                                                                                                  |
| <span id="MIB_IPPROTO_CISCO"></span><span id="mib_ipproto_cisco"></span><dl> <dt>**MIB\_IPPROTO\_CISCO**</dt> </dl>                                        | The Cisco Interior Gateway Routing Protocol (IGRP), a dynamic routing protocol.<br/>                                                                                                                                                                                                                                                                                                                                     |
| <span id="MIB_IPPROTO_ES_IS"></span><span id="mib_ipproto_es_is"></span><dl> <dt>**MIB\_IPPROTO\_ES\_IS**</dt> </dl>                                       | The End System-to-Intermediate System (ES-IS) protocol, a dynamic routing protocol. The ES-IS protocol was developed for use in the Open Systems Interconnection (OSI) protocol suite.<br/>                                                                                                                                                                                                                              |
| <span id="MIB_IPPROTO_IS_IS"></span><span id="mib_ipproto_is_is"></span><dl> <dt>**MIB\_IPPROTO\_IS\_IS**</dt> </dl>                                       | The Intermediate System-to-Intermediate System (IS-IS) protocol, a dynamic routing protocol. The IS-IS protocol was developed for use in the Open Systems Interconnection (OSI) protocol suite.<br/>                                                                                                                                                                                                                     |
| <span id="MIB_IPPROTO_RIP"></span><span id="mib_ipproto_rip"></span><dl> <dt>**MIB\_IPPROTO\_RIP**</dt> </dl>                                              | The Berkeley Routing Information Protocol (RIP) or RIP-II, a dynamic routing protocol.<br/>                                                                                                                                                                                                                                                                                                                              |



 

</dd> <dt>

**dwRtInfoPreference**
</dt> <dd>

Specifies the route preference as determined by the routing protocol in **dwRtInfoProto**.

</dd> <dt>

**dwRtInfoViewSet**
</dt> <dd>

Specifies the Route Information Table Views. It can take one of the following values.



| Value                                                                                                                                                                             | Meaning                                                                                                                                 |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| <span id="RTM_VIEW_ID_UCAST"></span><span id="rtm_view_id_ucast"></span><dl> <dt>**RTM\_VIEW\_ID\_UCAST**</dt> </dl>       | This value is used to define or set the type of route. This value specifies a Unicast Route Information Table view.<br/>          |
| <span id="RTM_VIEW_ID_MCAST"></span><span id="rtm_view_id_mcast"></span><dl> <dt>**RTM\_VIEW\_ID\_MCAST**</dt> </dl>       | This value is used to define or set the type of route. This value specifies a Multicast Route Information Table view.<br/>        |
| <span id="RTM_VIEW_MASK_NONE"></span><span id="rtm_view_mask_none"></span><dl> <dt>**RTM\_VIEW\_MASK\_NONE**</dt> </dl>    | This value is used to define or set the mask for Route Information Table view. This value is a mask for no routes.<br/>           |
| <span id="RTM_VIEW_MASK_ANY"></span><span id="rtm_view_mask_any"></span><dl> <dt>**RTM\_VIEW\_MASK\_ANY**</dt> </dl>       | This value is used to define or set the mask for Route Information Table view. This value is a mask for any types of routes.<br/> |
| <span id="RTM_VIEW_MASK_UCAST"></span><span id="rtm_view_mask_ucast"></span><dl> <dt>**RTM\_VIEW\_MASK\_UCAST**</dt> </dl> | This value is used to define or set the mask for Route Information Table view. This value is a mask for Unicast routes.<br/>      |
| <span id="RTM_VIEW_MASK_MCAST"></span><span id="rtm_view_mask_mcast"></span><dl> <dt>**RTM\_VIEW\_MASK\_MCAST**</dt> </dl> | This value is used to define or set the mask for Route Information Table view. This value is a mask for Multicast routes.<br/>    |
| <span id="RTM_VIEW_MASK_ALL"></span><span id="rtm_view_mask_all"></span><dl> <dt>**RTM\_VIEW\_MASK\_ALL**</dt> </dl>       | This value is used to define or set the mask for Route Information Table view. This value is a mask for all types of routes.<br/> |



 

</dd> <dt>

**bV4**
</dt> <dd>

A **BOOL** that specifies if the route information if for IPv4 or IPv6. If **TRUE**, the route information is IPv4, otherwise it is **FALSE**.

</dd> </dl>

## Remarks

The [INTERFACE\_ROUTE\_INFO](https://docs.microsoft.com/windows) structure is not defined in a publicly available header in the Platform Software Development Kit (SDK). Therefore, this structure must be manually defined by application developers.

## Requirements



|                                     |                                                      |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>          |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[Router Information Structures](router-information-structures.md)
</dt> <dt>

[**MprInfoBlockAdd**](/windows/desktop/api/Mprapi/nf-mprapi-mprinfoblockadd)
</dt> </dl>

 

 





