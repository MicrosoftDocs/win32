---
title: RtmDeleteRoute function (Rtm.h)
description: The RtmDeleteRoute function deletes a route entry.
ms.assetid: a98026e9-40f5-42e9-943c-dfc561feef6d
keywords:
- RtmDeleteRoute function RAS
topic_type:
- apiref
api_name:
- RtmDeleteRoute
api_location:
- Rtm.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# RtmDeleteRoute function

\[This API has been superseded by the [Routing Table Manager Version 2](about-routing-table-manager-version-2.md) API and will not be available beyond Windows Server 2003. Applications should use the Routing Table Manager Version 2 API.\]

The **RtmDeleteRoute** function deletes a route entry.

## Syntax


```C++
DWORD RtmDeleteRoute(
  _In_  HANDLE ClientHandle,
  _In_  PVOID  Route,
  _Out_ DWORD  Flags,
  _Out_ PVOID  CurBestRoute
);
```



## Parameters

<dl> <dt>

*ClientHandle* \[in\]
</dt> <dd>

Handle that identifies the client and therefore the routing protocol of the added or updated route. Obtain this handle by calling [**RtmRegisterClient**](rtmregisterclient.md).

</dd> <dt>

*Route* \[in\]
</dt> <dd>

Pointer to a protocol-family-specific structure that specifies the new or updated route. The following fields are used by the routing table manager to update the routing table:



| Value                                                                                                                                                                                                         | Meaning                                                                               |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| <span id="RR_Network"></span><span id="rr_network"></span><span id="RR_NETWORK"></span><dl> <dt>**RR\_Network**</dt> </dl>                             | Specifies the destination network number. <br/>                                 |
| <span id="RR_InterfaceID"></span><span id="rr_interfaceid"></span><span id="RR_INTERFACEID"></span><dl> <dt>**RR\_InterfaceID**</dt> </dl>             | Specifies the index of the interface through which the route was received.<br/> |
| <span id="RR_NextHopAddress"></span><span id="rr_nexthopaddress"></span><span id="RR_NEXTHOPADDRESS"></span><dl> <dt>**RR\_NextHopAddress**</dt> </dl> | Specifies the network address of the next-hop router.<br/>                      |



 

</dd> <dt>

*Flags* \[out\]
</dt> <dd>

Pointer to a set of flags that indicate the type of the change message, and what information was placed in the provided buffers. This parameter is one of the following values.



| Flags                                                                                                                                                                      | Meaning                                                                                                                                                                                          |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="RTM_NO_CHANGE"></span><span id="rtm_no_change"></span><dl> <dt>**RTM\_NO\_CHANGE**</dt> </dl>             | Deleting the route did not affect the best route to any destination network. In other words, another entry represents a route to the same destination network and has a lower metric.<br/> |
| <span id="RTM_ROUTE_DELETED"></span><span id="rtm_route_deleted"></span><dl> <dt>**RTM\_ROUTE\_DELETED**</dt> </dl> | The route deleted was the only route available for a particular destination network.<br/>                                                                                                  |
| <span id="RTM_ROUTE_CHANGED"></span><span id="rtm_route_changed"></span><dl> <dt>**RTM\_ROUTE\_CHANGED**</dt> </dl> | After this route was deleted, another route became the best route to a particular destination network. *CurBestRoute* points to the information for the new best route.<br/>               |



 

</dd> <dt>

*CurBestRoute* \[out\]
</dt> <dd>

Pointer to a structure that receives the current best-route information, if any. The type of the structure is specific to the protocol family, for example, IP or IPX.

This parameter is optional. If the caller specifies **NULL** for this parameter, the current best-route information is not returned.

</dd> </dl>

## Return value

If the function succeeds, the return value is **NO\_ERROR**.

If the function fails, the return value is one of the following error codes.



| Value                                                                                                       | Description                                                                                            |
|-------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| <dl> <dt>**ERROR\_INVALID\_HANDLE**</dt> </dl>       | The client handle parameter is not a valid handle.<br/>                                          |
| <dl> <dt>**ERROR\_INVALID\_PARAMETER**</dt> </dl>    | The route structure pointed to by the *Route* parameter contains a member value.<br/>            |
| <dl> <dt>**ERROR\_NO\_SUCH\_ROUTE**</dt> </dl>       | There are no entries in the routing table that match the parameters of the specified route.<br/> |
| <dl> <dt>**ERROR\_NO\_SYSTEM\_RESOURCES**</dt> </dl> | There are insufficient resources to perform the operation. <br/>                                 |



 

## Remarks

The function generates a route-change message if the best route to a destination network has changed as the result of the deletion. However, the route-change message is not sent to the client that makes this call. Instead, relevant information is returned by this function directly to that client.

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

[**RtmAddRoute**](rtmaddroute.md)
</dt> <dt>

[**RtmDequeueRouteChangeMessage**](rtmdequeueroutechangemessage.md)
</dt> </dl>

 

 





