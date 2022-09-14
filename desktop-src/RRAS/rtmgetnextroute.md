---
title: RtmGetNextRoute function (Rtm.h)
description: The RtmGetNextRoute function returns the next route from the specified subset of routes in the table.
ms.assetid: 0f413276-2ace-4216-a1a0-1b3061bacc4a
keywords:
- RtmGetNextRoute function RAS
topic_type:
- apiref
api_name:
- RtmGetNextRoute
api_location:
- Rtm.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# RtmGetNextRoute function

\[This API has been superseded by the [Routing Table Manager Version 2](about-routing-table-manager-version-2.md) API and will not be available beyond Windows Server 2003. Applications should use the Routing Table Manager Version 2 API.\]

The **RtmGetNextRoute** function returns the next route from the specified subset of routes in the table.

## Syntax


```C++
DWORD RtmGetNextRoute(
  _In_    DWORD ProtocolFamily,
  _In_    DWORD EnumerationFlags,
  _Inout_ PVOID Route
);
```



## Parameters

<dl> <dt>

*ProtocolFamily* \[in\]
</dt> <dd>

Specifies the protocol family of routes to retrieve, for example, IP or IPX.

</dd> <dt>

*EnumerationFlags* \[in\]
</dt> <dd>

Specifies which routes should be enumerated. This parameter limits the set of deleted routes to a subset defined by the following flags and the values in the corresponding members of the structure pointed to by the *CriteriaRoute* parameter. The flags are the same as those used in [**RtmCreateEnumerationHandle**](rtmcreateenumerationhandle.md).

</dd> <dt>

*Route* \[in, out\]
</dt> <dd>

On input, *Route* points to a protocol-family-specific structure ( [**RTM\_IP\_ROUTE**](rtm-ip-route.md) or [**RTM\_IPX\_ROUTE**](rtm-ipx-route.md)).

The calling function provides member values for this structure. These values, in conjunction with the *EnumerationFlags* parameter, specify the set from which to return routes.

On output, *Route* points to a structure that receives the first route that matched the specified criteria.

</dd> </dl>

## Return value

If the function succeeds, the return value is **NO\_ERROR**.

If the function fails, the return value is one of the following error codes.



| Value                                                                                                       | Description                                                             |
|-------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| <dl> <dt>**ERROR\_INVALID\_PARAMETER**</dt> </dl>    | One of the parameters is invalid.<br/>                            |
| <dl> <dt>**ERROR\_NO\_ROUTES**</dt> </dl>            | There are no routes that match the specified criteria.<br/>       |
| <dl> <dt>**ERROR\_NO\_SYSTEM\_RESOURCES**</dt> </dl> | There are insufficient resources to carry out the operation.<br/> |



 

## Remarks

The routes are returned in the following order:

1.  Network number
2.  Routing protocol
3.  Interface identifier
4.  Next-hop address

This function is less efficient than the corresponding enumeration handle functions.

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

[**RtmCloseEnumerationHandle**](rtmcloseenumerationhandle.md)
</dt> <dt>

[**RtmCreateEnumerationHandle**](rtmcreateenumerationhandle.md)
</dt> <dt>

[**RtmEnumerateGetNextRoute**](rtmenumerategetnextroute.md)
</dt> <dt>

[**RtmGetFirstRoute**](rtmgetfirstroute.md)
</dt> </dl>

 

 





