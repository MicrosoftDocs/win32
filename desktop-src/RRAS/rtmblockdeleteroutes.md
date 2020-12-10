---
title: RtmBlockDeleteRoutes function (Rtm.h)
description: The RtmBlockDeleteRoutes function deletes all routes in the specified subset of routes in the table.
ms.assetid: d191883d-da3d-4a91-92e6-4979db96f4a4
keywords:
- RtmBlockDeleteRoutes function RAS
topic_type:
- apiref
api_name:
- RtmBlockDeleteRoutes
api_location:
- Rtm.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# RtmBlockDeleteRoutes function

\[This API has been superseded by the [Routing Table Manager Version 2](about-routing-table-manager-version-2.md) API and will not be available beyond Windows Server 2003. Applications should use the Routing Table Manager Version 2 API.\]

The **RtmBlockDeleteRoutes** function deletes all routes in the specified subset of routes in the table.

## Syntax


```C++
HANDLE RtmBlockDeleteRoutes(
  _In_ HANDLE ClientHandle,
  _In_ DWORD  EnumerationFlags,
  _In_ PVOID  CriteriaRoute
);
```



## Parameters

<dl> <dt>

*ClientHandle* \[in\]
</dt> <dd>

Handle that identifies the client, and therefore the routing protocol, of the routes to be deleted.

</dd> <dt>

*EnumerationFlags* \[in\]
</dt> <dd>

Specifies which routes should be enumerated. This parameter limits the set of deleted routes to a subset defined by the following flags and the values in the corresponding members of the structure pointed to by the *CriteriaRoute* parameter. The flags are the same as those used in [**RtmCreateEnumerationHandle**](rtmcreateenumerationhandle.md) except that RTM\_ONLY\_BEST\_ROUTES is redundant for **RtmBlockDeleteRoutes**. The best-route designation is adjusted as routes are deleted, so the function eventually deletes all the routes in the subset.

</dd> <dt>

*CriteriaRoute* \[in\]
</dt> <dd>

Pointer to a protocol-family-specific route structure ( [**RTM\_IP\_ROUTE**](rtm-ip-route.md) or [**RTM\_IPX\_ROUTE**](rtm-ipx-route.md)). The member values in this structure correspond to the flags specified by the *EnumerationFlags* parameter.

</dd> </dl>

## Return value

If the function succeeds, the return value is NO\_ERROR.

If the function fails, the return value is one of the following error codes.



| Value                                                                                                       | Description                                                                                                |
|-------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**ERROR\_NO\_ROUTES**</dt> </dl>            | There are no routes that have the specified criteria.<br/>                                           |
| <dl> <dt>**ERROR\_INVALID\_HANDLE**</dt> </dl>       | The *ClientHandle* parameter is not valid.<br/>                                                      |
| <dl> <dt>**ERROR\_INVALID\_PARAMETER**</dt> </dl>    | One or more of the input parameters is invalid, for example, the enumeration flags are invalid.<br/> |
| <dl> <dt>**ERROR\_NO\_SYSTEM\_RESOURCES**</dt> </dl> | There are insufficient resources to carry out the operation.<br/>                                    |
| <dl> <dt>**ERROR\_NOT\_ENOUGH\_MEMORY**</dt> </dl>   | There is insufficient memory to carry out the operation.<br/>                                        |



 

## Remarks

The function generates appropriate notification messages to all registered clients including the caller.

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

[**RtmCreateEnumerationHandle**](rtmcreateenumerationhandle.md)
</dt> <dt>

[**RtmRegisterClient**](rtmregisterclient.md)
</dt> </dl>

 

 





