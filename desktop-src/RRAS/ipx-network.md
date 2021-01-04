---
title: IPX_NETWORK structure (Rtm.h)
description: The IPX\_NETWORK structure describes an IPX network address.
ms.assetid: 83fc4022-8515-4a51-ac47-f92572447fbf
keywords:
- IPX_NETWORK structure RAS
- PIPX_NETWORK structure pointer RAS
topic_type:
- apiref
api_name:
- IPX_NETWORK
api_location:
- Rtm.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# IPX\_NETWORK structure

\[This API has been superseded by the [Routing Table Manager Version 2](about-routing-table-manager-version-2.md) API and will not be available beyond Windows Server 2003. Applications should use the Routing Table Manager Version 2 API.\]

The **IPX\_NETWORK** structure describes an IPX network address.

## Syntax


```C++
typedef struct _IPX_NETWORK {
  DWORD N_NetNumber;
} IPX_NETWORK, *PIPX_NETWORK;
```



## Members

<dl> <dt>

**N\_NetNumber**
</dt> <dd>

Contains the IPX network number in machine-byte order.

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

[**RTM\_IPX\_ROUTE**](rtm-ipx-route.md)
</dt> </dl>

 

 





