---
title: RtmCreateEnumerationHandle function (Rtm.h)
description: The RtmCreateEnumerationHandle function returns a handle to use with RtmEnumerateGetNextRoute to scan through all routes, or a subset of routes, known to the routing table manager.
ms.assetid: 73e3ac7d-498a-4d89-a6b5-17aaf4b17ec2
keywords:
- RtmCreateEnumerationHandle function RAS
topic_type:
- apiref
api_name:
- RtmCreateEnumerationHandle
api_location:
- Rtm.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# RtmCreateEnumerationHandle function

\[This API has been superseded by the [Routing Table Manager Version 2](about-routing-table-manager-version-2.md) API and will not be available beyond Windows Server 2003. Applications should use the Routing Table Manager Version 2 API.\]

The **RtmCreateEnumerationHandle** function returns a handle to use with [**RtmEnumerateGetNextRoute**](rtmenumerategetnextroute.md) to scan through all routes, or a subset of routes, known to the routing table manager.

## Syntax


```C++
HANDLE RtmCreateEnumerationHandle(
  _In_ DWORD ProtocolFamily,
  _In_ DWORD EnumerationFlags,
  _In_ PVOID CriteriaRoute
);
```



## Parameters

<dl> <dt>

*ProtocolFamily* \[in\]
</dt> <dd>

Specifies the protocol family of the routes to enumerate.

</dd> <dt>

*EnumerationFlags* \[in\]
</dt> <dd>

Specifies which routes should be enumerated. This parameter limits the set of routes returned by the enumeration API to a subset defined by the following flags and the values in the corresponding members of the structure pointed to by the *CriteriaRoute* parameter. This parameter can be one of the following values.



| EnumerationFlags                                                                                                                                                                              | Meaning                                                                                                                                                                 |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="RTM_ONLY_THIS_NETWORK"></span><span id="rtm_only_this_network"></span><dl> <dt>**RTM\_ONLY\_THIS\_NETWORK**</dt> </dl>       | Enumerate only those routes that have the same network number as the RR\_Network member of the structure pointed to by CriteriaRoute.<br/>                        |
| <span id="RTM_ONLY_THIS_INTERFACE"></span><span id="rtm_only_this_interface"></span><dl> <dt>**RTM\_ONLY\_THIS\_INTERFACE**</dt> </dl> | Enumerate only those routes that were obtained through the interface specified by the RR\_InterfaceID field of the structure pointed to by CriteriaRoute.<br/>    |
| <span id="RTM_ONLY_THIS_PROTOCOL"></span><span id="rtm_only_this_protocol"></span><dl> <dt>**RTM\_ONLY\_THIS\_PROTOCOL**</dt> </dl>    | Enumerate only those routes that were added by the routing protocol specified by the RR\_RoutingProtocol field of the structure pointed to by CriteriaRoute.<br/> |
| <span id="RTM_ONLY_BEST_ROUTES"></span><span id="rtm_only_best_routes"></span><dl> <dt>**RTM\_ONLY\_BEST\_ROUTES**</dt> </dl>          | Enumerate only the best routes to each of the networks in the set.<br/>                                                                                           |



 

</dd> <dt>

*CriteriaRoute* \[in\]
</dt> <dd>

Pointer to a protocol-family-specific route structure ([**RTM\_IP\_ROUTE**](rtm-ip-route.md) or [**RTM\_IPX\_ROUTE**](rtm-ipx-route.md)). The member values in this structure correspond to the flags specified by the *EnumerationFlags* parameter.

</dd> </dl>

## Return value

If the function succeeds, the return value is a **HANDLE** to use with subsequent enumeration calls.

If the function fails, or no routes exist with the specified criteria, the return value is **NULL**. Call [**GetLastError**](/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror) to obtain more information.



| Value                                                                                                       | Description                                                                                                                  |
|-------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**ERROR\_NO\_ROUTES**</dt> </dl>            | There are no routes that have the specified criteria.<br/>                                                             |
| <dl> <dt>**ERROR\_INVALID\_PARAMETER**</dt> </dl>    | One or more of the input parameters is invalid (for example, unknown protocol family, invalid enumeration flags).<br/> |
| <dl> <dt>**ERROR\_NO\_SYSTEM\_RESOURCES**</dt> </dl> | There are insufficient resources to carry out the operation.<br/>                                                      |
| <dl> <dt>**ERROR\_NOT\_ENOUGH\_MEMORY**</dt> </dl>   | There is insufficient memory to allocate the handle.<br/>                                                              |



 

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

[**RTM\_IP\_ROUTE**](rtm-ip-route.md)
</dt> <dt>

[**RTM\_IPX\_ROUTE**](rtm-ipx-route.md)
</dt> <dt>

[**RtmCloseEnumerationHandle**](rtmcloseenumerationhandle.md)
</dt> <dt>

[**RtmEnumerateGetNextRoute**](rtmenumerategetnextroute.md)
</dt> </dl>

 

