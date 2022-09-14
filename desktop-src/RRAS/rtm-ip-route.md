---
title: RTM_IP_ROUTE structure (Rtm.h)
description: The RTM\_IP\_ROUTE structure contains information that describes a route owned by the IP protocol family.
ms.assetid: e752a4ae-a6bf-4cd3-9638-7615ff3901b7
keywords:
- RTM_IP_ROUTE structure RAS
- PRTM_IP_ROUTE structure pointer RAS
topic_type:
- apiref
api_name:
- RTM_IP_ROUTE
api_location:
- Rtm.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# RTM\_IP\_ROUTE structure

\[This API has been superseded by the [Routing Table Manager Version 2](about-routing-table-manager-version-2.md) API and will not be available beyond Windows Server 2003. Applications should use the Routing Table Manager Version 2 API.\]

The **RTM\_IP\_ROUTE** structure contains information that describes a route owned by the IP protocol family.

## Syntax


```C++
typedef struct _RTM_IP_ROUTE {
  FILETIME               RR_TimeStamp;
  DWORD                  RR_RoutingProtocol;
  DWORD                  RR_InterfaceID;
  PROTOCOL_SPECIFIC_DATA RR_ProtocolSpecificData;
  IP_NETWORK             RR_Network;
  IP_NEXT_HOP_ADDRESS    RR_NextHopAddress;
  IP_SPECIFIC_DATA       RR_FamilySpecificData;
} RTM_IP_ROUTE, *PRTM_IP_ROUTE;
```



## Members

<dl> <dt>

**RR\_TimeStamp**
</dt> <dd>

Specifies the time that the route entry was created or last updated. This member is set by the routing table manager. The time is expressed as a FILETIME structure.

</dd> <dt>

**RR\_RoutingProtocol**
</dt> <dd>

Specifies the routing protocol that added the route.

</dd> <dt>

**RR\_InterfaceID**
</dt> <dd>

Specifies the interface through which the route was obtained.

</dd> <dt>

**RR\_ProtocolSpecificData**
</dt> <dd>

Specifies a [**PROTOCOL\_SPECIFIC\_DATA**](protocol-specific-data.md) structure that contains memory reserved for routing-protocol-specific data.

</dd> <dt>

**RR\_Network**
</dt> <dd>

Specifies an [**IP\_NETWORK**](ip-network.md) structure that contains an IP network address.

</dd> <dt>

**RR\_NextHopAddress**
</dt> <dd>

Specifies an [**IP\_NEXT\_HOP\_ADDRESS**](ip-next-hop-address.md) structure that contains the address of the next-hop router.

</dd> <dt>

**RR\_FamilySpecificData**
</dt> <dd>

Specifies an [**IP\_SPECIFIC\_DATA**](ip-specific-data.md) structure that contains IP protocol-family-specific data.

</dd> </dl>

## Remarks

The members of the **RTM\_IP\_ROUTE** structure are all **DWORD** aligned.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                        |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                             |
| End of server support<br/>    | Windows Server 2003<br/>                                                   |
| Header<br/>                   | <dl> <dt>Rtm.h</dt> </dl> |



## See also

<dl> <dt>

[Routing Table Manager Version 1 Reference](routing-table-manager-version-1-reference.md)
</dt> <dt>

[Routing Table Manager Version 1 Structures](routing-table-manager-version-1-structures.md)
</dt> <dt>

[**IP\_NETWORK**](ip-network.md)
</dt> <dt>

[**IP\_NEXT\_HOP\_ADDRESS**](ip-next-hop-address.md)
</dt> <dt>

[**IP\_SPECIFIC\_DATA**](ip-specific-data.md)
</dt> </dl>

 

 





