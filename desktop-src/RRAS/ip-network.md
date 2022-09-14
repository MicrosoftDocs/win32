---
title: IP_NETWORK structure (Rtm.h)
description: The IP\_NETWORK structure describes an IP network address.
ms.assetid: 5dcc733f-c86f-407e-8727-64f3ae71dd48
keywords:
- IP_NETWORK structure RAS
- PIP_NETWORK structure pointer RAS
topic_type:
- apiref
api_name:
- IP_NETWORK
api_location:
- Rtm.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# IP\_NETWORK structure

\[This API has been superseded by the [Routing Table Manager Version 2](about-routing-table-manager-version-2.md) API and will not be available beyond Windows Server 2003. Applications should use the Routing Table Manager Version 2 API.\]

The **IP\_NETWORK** structure describes an IP network address.

## Syntax


```C++
typedef struct _IP_NETWORK {
  DWORD N_NetNumber;
  DWORD N_NetMask;
} IP_NETWORK, *PIP_NETWORK;
```



## Members

<dl> <dt>

**N\_NetNumber**
</dt> <dd>

Specifies the IP network number expressed as an IP address in machine-byte order.

</dd> <dt>

**N\_NetMask**
</dt> <dd>

Specifies the network mask. Apply this mask to the IP address in order to extract the network address. The network mask is in machine-byte order.

</dd> </dl>

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

[**RTM\_IP\_ROUTE**](rtm-ip-route.md)
</dt> </dl>

 

 





