---
title: IPX_SPECIFIC_DATA structure (Rtm.h)
description: The IPX\_SPECIFIC\_DATA structure contains IPX-specific data.
ms.assetid: 4d97092d-692c-4dc7-af7f-260dc76c6c08
keywords:
- IPX_SPECIFIC_DATA structure RAS
- PIPX_SPECIFIC_DATA structure pointer RAS
topic_type:
- apiref
api_name:
- IPX_SPECIFIC_DATA
api_location:
- Rtm.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# IPX\_SPECIFIC\_DATA structure

\[This API has been superseded by the [Routing Table Manager Version 2](about-routing-table-manager-version-2.md) API and will not be available beyond Windows Server 2003. Applications should use the Routing Table Manager Version 2 API.\]

The **IPX\_SPECIFIC\_DATA** structure contains IPX-specific data.

## Syntax


```C++
typedef struct _IPX_SPECIFIC_DATA {
  DWORD  FSD_Flags;
  USHORT FSD_TickCount;
  USHORT FSD_HopCount;
} IPX_SPECIFIC_DATA, *PIPX_SPECIFIC_DATA;
```



## Members

<dl> <dt>

**FSD\_Flags**
</dt> <dd>

Specifies flags that describe the route. Currently, this member is either zero or the following flag value.



| Value                                                                                                                                                                                                      | Meaning                                                                                       |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| <span id="IPX_GLOBAL_CLIENT_WAN_ROUTE"></span><span id="ipx_global_client_wan_route"></span><dl> <dt>**IPX\_GLOBAL\_CLIENT\_WAN\_ROUTE**</dt> </dl> | Specifies that this route is for the global network allocated for all WAN clients.<br/> |



 

</dd> <dt>

**FSD\_TickCount**
</dt> <dd>

Specifies the number of ticks it takes to reach the destination network. Routing protocols other than RIP should convert their metrics into ticks.

</dd> <dt>

**FSD\_HopCount**
</dt> <dd>

Specifies the hop count associated with the route.

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

 

 





