---
title: RtmGetRouteAge function (Rtm.h)
description: The RtmGetRouteAge function returns the age of a route. The age is the time, in seconds, since it was created or last updated.
ms.assetid: 93052412-227f-4c9e-978b-3ec4bde4a256
keywords:
- RtmGetRouteAge function RAS
topic_type:
- apiref
api_name:
- RtmGetRouteAge
api_location:
- Rtm.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# RtmGetRouteAge function

\[This API has been superseded by the [Routing Table Manager Version 2](about-routing-table-manager-version-2.md) API and will not be available beyond Windows Server 2003. Applications should use the Routing Table Manager Version 2 API.\]

The **RtmGetRouteAge** function returns the age of a route. The age is the time, in seconds, since it was created or last updated.

## Syntax


```C++
ULONG RtmGetRouteAge(
  _In_ PVOID Route
);
```



## Parameters

<dl> <dt>

*Route* \[in\]
</dt> <dd>

Pointer to a protocol-family-specific structure that specifies route data recently obtained from the routing table manager.

</dd> </dl>

## Return value

The return value is one of the following values.



| Value                                                                                   | Description                                                                                                                                                  |
|-----------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**RouteAge**</dt> </dl> | The time in seconds since a route was created or last updated.<br/>                                                                                    |
| <dl> <dt>**INFINITE**</dt> </dl> | The content of the route structure is invalid. In this case, a call to [**GetLastError**](/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror) returns ERROR\_INVALID\_PARAMETER.<br/> |



 

## Remarks

The route age is computed from the RR\_TimeStamp member of the structure that is pointed to by the *Route* parameter. The routing table manager sets the value of this member when a route is added or updated.

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

[Routing Table Manager Version\_1 Reference](routing-table-manager-version-1-reference.md)
</dt> <dt>

[Routing Table Manager Version 1 Functions](routing-table-manager-version-1-functions.md)
</dt> <dt>

[**GetLastError**](/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror)
</dt> <dt>

[**RTM\_IP\_ROUTE**](rtm-ip-route.md)
</dt> <dt>

[**RTM\_IPX\_ROUTE**](rtm-ipx-route.md)
</dt> </dl>

 

