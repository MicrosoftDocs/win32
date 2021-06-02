---
title: RtmGetNetworkCount function (Rtm.h)
description: The RtmGetNetworkCount function retrieves the number of networks to which the routing table manager has routes.
ms.assetid: d0c04b8d-a6c4-44bf-a3f2-de822d635131
keywords:
- RtmGetNetworkCount function RAS
topic_type:
- apiref
api_name:
- RtmGetNetworkCount
api_location:
- Rtm.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# RtmGetNetworkCount function

\[This API has been superseded by the [Routing Table Manager Version 2](about-routing-table-manager-version-2.md) API and will not be available beyond Windows Server 2003. Applications should use the Routing Table Manager Version 2 API.\]

The **RtmGetNetworkCount** function retrieves the number of networks to which the routing table manager has routes.

## Syntax


```C++
ULONG RtmGetNetworkCount(
  _In_ DWORD ProtocolFamily
);
```



## Parameters

<dl> <dt>

*ProtocolFamily* \[in\]
</dt> <dd>

Specifies for which type of network to obtain route information, for example, IP or IPX.

</dd> </dl>

## Return value

If the function succeeds, the return value is the network count, the number of networks known to the routing protocols of the specified protocol family.

If the return value is zero, either no routes are available, or the operation failed. Call [**GetLastError**](/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror) to obtain more information.



| Value                                                                                                    | Description                                                                                                  |
|----------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**NO\_ERROR**</dt> </dl>                 | The operation succeeded, but no routes are available.<br/>                                             |
| <dl> <dt>**ERROR\_INVALID\_PARAMETER**</dt> </dl> | The value of the *ProtocolFamily* parameter does not correspond to any installed protocol family.<br/> |



 

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

[RTMv1 Protocol Family Identifiers](routing-table-manager-version-1-protocol-family-identifiers.md)
</dt> </dl>

 

