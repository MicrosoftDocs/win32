---
title: IP_NEXT_HOP_ADDRESS structure (Rtm.h)
description: The IP\_NEXT\_HOP\_ADDRESS structure contains the address for the next-hop router for an IP route.
ms.assetid: a97b3995-dfaa-4e53-be86-3ad46b8be691
keywords:
- IP_NEXT_HOP_ADDRESS structure RAS
- PIP_NEXT_HOP_ADDRESS structure RAS
topic_type:
- apiref
api_name:
- IP_NEXT_HOP_ADDRESS
api_location:
- Rtm.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# IP\_NEXT\_HOP\_ADDRESS structure

\[This API has been superseded by the [Routing Table Manager Version 2](about-routing-table-manager-version-2.md) API and will not be available beyond Windows Server 2003. Applications should use the Routing Table Manager Version 2 API.\]

The **IP\_NEXT\_HOP\_ADDRESS** structure contains the address for the next-hop router for an IP route.

## Syntax


```C++
typedef struct _IP_NEXT_HOP_ADDRESS {
  DWORD N_NetNumber;
  DWORD N_NetMask;
} IP_NEXT_HOP_ADDRESS, *PIP_NEXT_HOP_ADDRESS;
```



## Members

<dl> <dt>

**N\_NetNumber**
</dt> <dd>

Specifies the IP network address expressed as an IP address in machine-byte order.

</dd> <dt>

**N\_NetMask**
</dt> <dd>

Specifies the network mask. Apply this mask to the IP address in order to extract the network address. The network mask is in machine-byte order.

</dd> </dl>

## Remarks

The **IP\_NEXT\_HOP\_ADDRESS** structure is a typedef of the [**IP\_NETWORK**](ip-network.md) structure. The typedef is in Rtm.h.

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

[**RTM\_IP\_ROUTE**](rtm-ip-route.md)
</dt> </dl>

 

 





