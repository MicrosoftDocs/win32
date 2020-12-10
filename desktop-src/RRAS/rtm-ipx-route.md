---
title: RTM_IPX_ROUTE structure (Rtm.h)
description: The RTM\_IPX\_ROUTE structure contains information that describes a route for the IPX protocol family.
ms.assetid: ffa0637c-2197-4ebd-a5ef-e174dd0ccb15
keywords:
- RTM_IPX_ROUTE structure RAS
- PRTM_IPX_ROUTE structure pointer RAS
topic_type:
- apiref
api_name:
- RTM_IPX_ROUTE
api_location:
- Rtm.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# RTM\_IPX\_ROUTE structure

\[This API has been superseded by the [Routing Table Manager Version 2](about-routing-table-manager-version-2.md) API and will not be available beyond Windows Server 2003. Applications should use the Routing Table Manager Version 2 API.\]

The **RTM\_IPX\_ROUTE** structure contains information that describes a route for the IPX protocol family.

## Syntax


```C++
typedef struct _RTM_IPX_ROUTE {
  FILETIME               RR_TimeStamp;
  DWORD                  RR_RoutingProtocol;
  DWORD                  RR_InterfaceID;
  PROTOCOL_SPECIFIC_DATA RR_ProtocolSpecificData;
  IPX_NETWORK            RR_Network;
  IPX_NEXT_HOP_ADDRESS   RR_NextHopAddress;
  IPX_SPECIFIC_DATA      RR_FamilySpecificData;
} RTM_IPX_ROUTE, *PRTM_IPX_ROUTE;
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

Specifies a [**PROTOCOL\_SPECIFIC\_DATA**](protocol-specific-data.md) structure containing memory reserved for data specific to routing protocols.

</dd> <dt>

**RR\_Network**
</dt> <dd>

Specifies an [**IPX\_NETWORK**](ipx-network.md) structure that contains an IP network address.

</dd> <dt>

**RR\_NextHopAddress**
</dt> <dd>

Specifies an [**IPX\_NEXT\_HOP\_ADDRESS**](ipx-next-hop-address.md) structure that contains the address of the next-hop router.

</dd> <dt>

**RR\_FamilySpecificData**
</dt> <dd>

Specifies an [**IPX\_SPECIFIC\_DATA**](ipx-specific-data.md) structure that contains data specific to the IPX protocol family.

</dd> </dl>

## Remarks

The members of the **RTM\_IPX\_ROUTE** structure are all **DWORD** aligned.

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

[Routing Table Manager Version\_1\_Structures](routing-table-manager-version-1-structures.md)
</dt> <dt>

[**IPX\_NETWORK**](ipx-network.md)
</dt> <dt>

[**IPX\_NEXT\_HOP\_ADDRESS**](ipx-next-hop-address.md)
</dt> <dt>

[**IPX\_SPECIFIC\_DATA**](ipx-specific-data.md)
</dt> </dl>

 

 





