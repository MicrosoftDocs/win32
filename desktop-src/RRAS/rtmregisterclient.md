---
title: RtmRegisterClient function (Rtm.h)
description: The RtmRegisterClient function registers a client as a handler of the specified protocol. It establishes a route change notification mechanism for the client, and sets protocol options.
ms.assetid: 70426601-695d-47ed-b71a-1df3fb8ddf10
keywords:
- RtmRegisterClient function RAS
topic_type:
- apiref
api_name:
- RtmRegisterClient
api_location:
- Rtm.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# RtmRegisterClient function

\[This API has been superseded by the [Routing Table Manager Version 2](about-routing-table-manager-version-2.md) API and will not be available beyond Windows Server 2003. Applications should use the Routing Table Manager Version 2 API.\]

The **RtmRegisterClient** function registers a client as a handler of the specified protocol. It establishes a route change notification mechanism for the client, and sets protocol options.

## Syntax


```C++
HANDLE RtmRegisterClient(
  _In_ DWORD  ProtocolFamily,
  _In_ DWORD  RoutingProtocol,
  _In_ HANDLE ChangeEvent,
  _In_ DWORD  Flags
);
```



## Parameters

<dl> <dt>

*ProtocolFamily* \[in\]
</dt> <dd>

Specifies the protocol family of the routing protocol to register.

</dd> <dt>

*RoutingProtocol* \[in\]
</dt> <dd>

Specifies the routing protocol identifier, the same as that used when registering with the router manager. See [**RegisterProtocol**](/windows/desktop/api/Routprot/nc-routprot-pregister_protocol).

</dd> <dt>

*ChangeEvent* \[in\]
</dt> <dd>

Specifies that a best route to a network in the table has changed. The routing table manager signals this event after a change to the best route to any network in the table. See [**RtmDequeueRouteChangeMessage**](rtmdequeueroutechangemessage.md) for more information about route-change notification.

This parameter is optional. If the caller specifies **NULL** for this parameter, the routing table manager does not notify the client of changes in best route status.

</dd> <dt>

*Flags* \[in\]
</dt> <dd>

Specifies miscellaneous options for special handling of the routing protocol. The following value is currently supported.



| Flags                                                                                                                                                                                               | Meaning                                                                                                                                                                                                                                                 |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="RTM_PROTOCOL_SINGLE_ROUTE"></span><span id="rtm_protocol_single_route"></span><dl> <dt>**RTM\_PROTOCOL\_SINGLE\_ROUTE**</dt> </dl> | The routing table manager keeps only one route per destination network for the routing protocol. In other words, the routing table manager replaces route entries that have the same destination network numbers instead of adding new ones.<br/> |



 

</dd> </dl>

## Return value

On successful return, a **HANDLE** value that identifies the client in subsequent calls to the routing table manager.

A **NULL** handle indicates that the routing table manager was unable to register the client. Call [**GetLastError**](/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror) to obtain the reason for the failure.



| Value                                                                                                         | Description                                                                                     |
|---------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| <dl> <dt>**ERROR\_CLIENT\_ALREADY\_EXISTS**</dt> </dl> | Another client has already registered to handle the specified protocol.<br/>              |
| <dl> <dt>**ERROR\_INVALID\_PARAMETER**</dt> </dl>      | The specified protocol family is not supported, or the *Flags* parameter is invalid.<br/> |
| <dl> <dt>**ERROR\_NO\_SYSTEM\_RESOURCES**</dt> </dl>   | Insufficient resources to carry out the operation.<br/>                                   |
| <dl> <dt>**ERROR\_NOT\_ENOUGH\_MEMORY**</dt> </dl>     | Insufficient memory to allocate data structures for the client.<br/>                      |



 

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

[**RegisterProtocol**](/windows/desktop/api/Routprot/nc-routprot-pregister_protocol)
</dt> <dt>

[RTMv1 Protocol Family Identifiers](routing-table-manager-version-1-protocol-family-identifiers.md)
</dt> <dt>

[**RtmDequeueRouteChangeMessage**](rtmdequeueroutechangemessage.md)
</dt> <dt>

[**RtmDeregisterClient**](rtmderegisterclient.md)
</dt> </dl>

 

