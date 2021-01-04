---
title: RtmEnumerateGetNextRoute function (Rtm.h)
description: The RtmEnumerateGetNextRoute function returns the next-route entry in the enumeration started by a call to RtmCreateEnumerationHandle.
ms.assetid: fff6fb58-8a37-49f0-abc5-354b5bc340f8
keywords:
- RtmEnumerateGetNextRoute function RAS
topic_type:
- apiref
api_name:
- RtmEnumerateGetNextRoute
api_location:
- Rtm.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# RtmEnumerateGetNextRoute function

\[This API has been superseded by the [Routing Table Manager Version 2](about-routing-table-manager-version-2.md) API and will not be available beyond Windows Server 2003. Applications should use the Routing Table Manager Version 2 API.\]

The **RtmEnumerateGetNextRoute** function returns the next-route entry in the enumeration started by a call to [**RtmCreateEnumerationHandle**](rtmcreateenumerationhandle.md).

## Syntax


```C++
DWORD RtmEnumerateGetNextRoute(
  _In_  HANDLE EnumerationHandle,
  _Out_ PVOID  Route
);
```



## Parameters

<dl> <dt>

*EnumerationHandle* \[in\]
</dt> <dd>

Handle that identifies the enumeration and specifies its scope. Obtain this handle by calling [**RtmCreateEnumerationHandle**](rtmcreateenumerationhandle.md).

</dd> <dt>

*Route* \[out\]
</dt> <dd>

Pointer to a protocol-family-specific route structure ( [**RTM\_IP\_ROUTE**](rtm-ip-route.md) or [**RTM\_IPX\_ROUTE**](rtm-ipx-route.md)). This structure will receive the next route in the enumeration.

</dd> </dl>

## Return value

If the function succeeds, the return value is NO\_ERROR.

If the function fails, the return value is one of the following error codes.



| Value                                                                                                       | Description                                                             |
|-------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| <dl> <dt>**ERROR\_INVALID\_HANDLE**</dt> </dl>       | The *EnumerationHandle* parameter is not valid.<br/>              |
| <dl> <dt>**ERROR\_NO\_MORE\_ROUTES**</dt> </dl>      | There are no more routes in the enumeration.<br/>                 |
| <dl> <dt>**ERROR\_NO\_SYSTEM\_RESOURCES**</dt> </dl> | There are insufficient resources to carry out the operation.<br/> |



 

## Remarks

Although routes are not returned in any particular order, each route in the enumeration is returned only once.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                               |
| End of server support<br/>    | Windows Server 2003<br/>                                                     |
| Header<br/>                   | <dl> <dt>Rtm.h</dt> </dl>   |
| Library<br/>                  | <dl> <dt>Rtm.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Rtm.dll</dt> </dl> |



## See also

<dl> <dt>

[Routing Table Manager Version 1 Reference](routing-table-manager-version-1-reference.md)
</dt> <dt>

[Routing Table Manager Version 1 Functions](routing-table-manager-version-1-functions.md)
</dt> <dt>

[**RTM\_IP\_ROUTE**](rtm-ip-route.md)
</dt> <dt>

[**RTM\_IPX\_ROUTE**](rtm-ipx-route.md)
</dt> <dt>

[**RtmCloseEnumerationHandle**](rtmcloseenumerationhandle.md)
</dt> <dt>

[**RtmCreateEnumerationHandle**](rtmcreateenumerationhandle.md)
</dt> </dl>

 

 





