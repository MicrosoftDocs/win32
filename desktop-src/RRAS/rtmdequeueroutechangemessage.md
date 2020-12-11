---
title: RtmDequeueRouteChangeMessage function (Rtm.h)
description: The RtmDequeueRouteChangeMessage function returns the next route-change message in the queue associated with the specified client.
ms.assetid: 44f2116a-3c8d-4ac6-896e-b12930b218a5
keywords:
- RtmDequeueRouteChangeMessage function RAS
topic_type:
- apiref
api_name:
- RtmDequeueRouteChangeMessage
api_location:
- Rtm.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# RtmDequeueRouteChangeMessage function

\[This API has been superseded by the [Routing Table Manager Version 2](about-routing-table-manager-version-2.md) API and will not be available beyond Windows Server 2003. Applications should use the Routing Table Manager Version 2 API.\]

The **RtmDequeueRouteChangeMessage** function returns the next route-change message in the queue associated with the specified client.

## Syntax


```C++
DWORD RtmDequeueRouteChangeMessage(
  _In_  HANDLE ClientHandle,
  _Out_ DWORD  Flags,
  _Out_ PVOID  CurBestRoute,
  _Out_ PVOID  PrevBestRoute
);
```



## Parameters

<dl> <dt>

*ClientHandle* \[in\]
</dt> <dd>

Handle that identifies the client for which the operation is performed. Obtain this handle by calling [**RtmRegisterClient**](rtmregisterclient.md).

</dd> <dt>

*Flags* \[out\]
</dt> <dd>

Pointer to a **DWORD** variable. The value of this variable is set by the routing table manager. The value specifies the type of the change message, and what information was returned in the provided buffers. This parameter is one of the following.



| Flags                                                                                                                                                                      | Meaning                                                                                                                                                                                                                                                                                                           |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="RTM_ROUTE_ADDED"></span><span id="rtm_route_added"></span><dl> <dt>**RTM\_ROUTE\_ADDED**</dt> </dl>       | The first route was added for a particular destination network. The *CurBestRoute* parameter points to the information for the added route.<br/>                                                                                                                                                            |
| <span id="RTM_ROUTE_DELETED"></span><span id="rtm_route_deleted"></span><dl> <dt>**RTM\_ROUTE\_DELETED**</dt> </dl> | The only route available for a particular destination network was deleted. The *PrevBestRoute* parameter points to the information for the deleted route.<br/>                                                                                                                                              |
| <span id="RTM_ROUTE_CHANGED"></span><span id="rtm_route_changed"></span><dl> <dt>**RTM\_ROUTE\_CHANGED**</dt> </dl> | At least one of the significant parameters was changed for a best route to a particular destination network. The significant parameters are: <br/> Protocol identifier<br/> Interface index<br/> Next-hop address<br/> Protocol-family-specific data (including route metrics)<br/> |



 

The *PrevBestRoute* parameter points to the route information as it was before the change. The *CurBestRoute* parameter points to current (that is, after-change) route information.

</dd> <dt>

*CurBestRoute* \[out\]
</dt> <dd>

Pointer to a structure that receives the current best-route information (if any). The type of the structure is specific to the protocol family, for example, IP or IPX.

This parameter is optional. If the caller specifies **NULL** for this parameter, the current best-route information is not returned.

</dd> <dt>

*PrevBestRoute* \[out\]
</dt> <dd>

Pointer to a structure that receives the previous best-route information, if any. The type of the structure is specific to the protocol family, for example, IP or IPX.

This parameter is optional. If the caller specifies **NULL** for this parameter, the previous best-route information is not returned.

</dd> </dl>

## Return value

The return value is one of the following codes.



| Value                                                                                                       | Description                                                                                                                                                                                                                                  |
|-------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**NO\_ERROR**</dt> </dl>                    | This message was the last message in the client's queue. The event object is reset.<br/>                                                                                                                                               |
| <dl> <dt>**ERROR\_INVALID\_HANDLE**</dt> </dl>       | The *ClientHandle* parameter is not a valid handle, or at registration the client did not provide an event object for change message notification (see [**RtmRegisterClient**](rtmregisterclient.md)).<br/>                           |
| <dl> <dt>**ERROR\_MORE\_MESSAGES**</dt> </dl>        | The client's queue contains additional messages. The client should call **RtmDequeueRouteChangeMessage** again as soon as possible to allow the routing table manager to free the resources associated with the pending messages.<br/> |
| <dl> <dt>**ERROR\_NO\_MESSAGES**</dt> </dl>          | The client's queue contains no messages; the call was unsolicited. The event is reset.<br/>                                                                                                                                            |
| <dl> <dt>**ERROR\_NO\_SYSTEM\_RESOURCES**</dt> </dl> | There are insufficient resources to carry out the operation.<br/>                                                                                                                                                                      |



 

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

[**RtmRegisterClient**](rtmregisterclient.md)
</dt> </dl>

 

 





