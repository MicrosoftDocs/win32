---
title: RtmIsRoute function (Rtm.h)
description: The RtmIsRoute function determines if one or more routes to a specified destination network exist. If so, the function returns information for the best route to that network.
ms.assetid: f9939790-d0a6-487e-9674-a01d436dc962
keywords:
- RtmIsRoute function RAS
topic_type:
- apiref
api_name:
- RtmIsRoute
api_location:
- Rtm.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# RtmIsRoute function

\[This API has been superseded by the [Routing Table Manager Version 2](about-routing-table-manager-version-2.md) API and will not be available beyond Windows Server 2003. Applications should use the Routing Table Manager Version 2 API.\]

The **RtmIsRoute** function determines if one or more routes to a specified destination network exist. If so, the function returns information for the best route to that network.

## Syntax


```C++
BOOL RtmIsRoute(
  _In_  DWORD ProtocolFamily,
  _In_  PVOID Network,
  _Out_ PVOID BestRoute
);
```



## Parameters

<dl> <dt>

*ProtocolFamily* \[in\]
</dt> <dd>

Specifies the type of data structure pointed to by the *Network* parameter, for example, [**IP\_NETWORK**](ip-network.md), [**IPX\_NETWORK**](ipx-network.md).

</dd> <dt>

*Network* \[in\]
</dt> <dd>

Pointer to a structure that specifies protocol-family-specific network number data. This data identifies the network for which the caller seeks route information.

</dd> <dt>

*BestRoute* \[out\]
</dt> <dd>

Pointer to a protocol-family-specific structure that receives the current best route information, if any.

</dd> </dl>

## Return value

The return value is one of the following codes.



| Value                                                                                                       | Description                                                                                                                                              |
|-------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**TRUE**</dt> </dl>                         | At least one route to the specified network exists. The best route is returned in the structure pointed to by the *BestRoute* parameter.<br/>      |
| <dl> <dt>**FALSE**</dt> </dl>                        | There is no route to the specified network, or the operation failed. Call [**GetLastError**](/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror) to obtain more information:<br/> |
| <dl> <dt>**NO\_ERROR**</dt> </dl>                    | The operation succeeded, but there is no route to the specified network.<br/>                                                                      |
| <dl> <dt>**ERROR\_INVALID\_PARAMETER**</dt> </dl>    | The value of the *ProtocolFamily* parameter does not correspond to any installed protocol family.<br/>                                             |
| <dl> <dt>**ERROR\_NO\_SYSTEM\_RESOURCES**</dt> </dl> | There are insufficient resources to carry out the operation.<br/>                                                                                  |



 

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

[**GetLastError**](/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror)
</dt> <dt>

[**IP\_NETWORK**](ip-network.md)
</dt> <dt>

[**IPX\_NETWORK**](ipx-network.md)
</dt> <dt>

[RTMv1 Protocol Family Identifiers](routing-table-manager-version-1-protocol-family-identifiers.md)
</dt> </dl>

 

