---
title: RtmAddRoute function (Rtm.h)
description: The RtmAddRoute function adds a route entry or updates an existing route entry.
ms.assetid: 09a9b57d-f10b-40b7-a3c1-2e0613f29431
keywords:
- RtmAddRoute function RAS
topic_type:
- apiref
api_name:
- RtmAddRoute
api_location:
- Rtm.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# RtmAddRoute function

\[This API has been superseded by the [Routing Table Manager Version 2](about-routing-table-manager-version-2.md) API and will not be available beyond Windows Server 2003. Applications should use the Routing Table Manager Version 2 API.\]

The **RtmAddRoute** function adds a route entry or updates an existing route entry.

## Syntax


```C++
DWORD RtmAddRoute(
  _In_  HANDLE ClientHandle,
  _In_  PVOID  Route,
  _In_  DWORD  TimeToLive,
  _Out_ DWORD  Flags,
  _Out_ PVOID  CurBestRoute,
  _Out_ PVOID  PrevBestRoute
);
```



## Parameters

<dl> <dt>

*ClientHandle* \[in\]
</dt> <dd>

Handle that identifies the client, and therefore the routing protocol, that added or updated the route. Obtain this handle by calling [**RtmRegisterClient**](rtmregisterclient.md).

</dd> <dt>

*Route* \[in\]
</dt> <dd>

Pointer to a protocol-family-specific structure that specifies the new or updated route. The following fields are used by the routing table manager to update the routing table:



| Value                                                                                                                                                                                                                                 | Meaning                                                                                                                                                                                                                                                                                                                                                                                                   |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="RR_Network"></span><span id="rr_network"></span><span id="RR_NETWORK"></span><dl> <dt>**RR\_Network**</dt> </dl>                                                     | Specifies the destination network number.<br/>                                                                                                                                                                                                                                                                                                                                                      |
| <span id="RR_InterfaceID"></span><span id="rr_interfaceid"></span><span id="RR_INTERFACEID"></span><dl> <dt>**RR\_InterfaceID**</dt> </dl>                                     | Specifies the index of the interface through which the route was received.<br/>                                                                                                                                                                                                                                                                                                                     |
| <span id="RR_NextHopAddress"></span><span id="rr_nexthopaddress"></span><span id="RR_NEXTHOPADDRESS"></span><dl> <dt>**RR\_NextHopAddress**</dt> </dl>                         | Specifies the address of the next-hop router.<br/>                                                                                                                                                                                                                                                                                                                                                  |
| <span id="RR_FamilySpecificData"></span><span id="rr_familyspecificdata"></span><span id="RR_FAMILYSPECIFICDATA"></span><dl> <dt>**RR\_FamilySpecificData**</dt> </dl>         | Specifies data that is specific to the protocol family. Although the data is transparent to the routing table manager, it is considered when comparing routes to determine if route information has changed. The data is also used to set metric values that are independent of the routing protocol. Consequently, this data is used to determine the best route for the destination network.<br/> |
| <span id="RR_ProtocolSpecificData"></span><span id="rr_protocolspecificdata"></span><span id="RR_PROTOCOLSPECIFICDATA"></span><dl> <dt>**RR\_ProtocolSpecificData**</dt> </dl> | Specifies data which is specific to the routing protocol that supplied the route.<br/>                                                                                                                                                                                                                                                                                                              |
| <span id="RR_TimeStamp"></span><span id="rr_timestamp"></span><span id="RR_TIMESTAMP"></span><dl> <dt>**RR\_TimeStamp**</dt> </dl>                                             | Specifies the current system time. This field is set by the routing table manager.<br/>                                                                                                                                                                                                                                                                                                             |



 

</dd> <dt>

*TimeToLive* \[in\]
</dt> <dd>

Specifies the number of seconds the specified route should be kept in the routing table. If this parameter is set to INFINITE, the route is kept until it is explicitly deleted. The current limit for *TimeToLive* is 2147483 sec (24+ days).

</dd> <dt>

*Flags* \[out\]
</dt> <dd>

Pointer to a **DWORD** variable. The value of this variable is set by the routing table manager. The value indicates the type of the change, and what information was returned in the provided buffers. This parameter is one of the following.



| Flags                                                                                                                                                                      | Meaning                                                                                                                                                                                                                                                                                                    |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="RTM_NO_CHANGE"></span><span id="rtm_no_change"></span><dl> <dt>**RTM\_NO\_CHANGE**</dt> </dl>             | The addition or update either did not change any of the significant route parameters, or the route entry affected is not the best route among the entries for the destination network.<br/>                                                                                                          |
| <span id="RTM_ROUTE_ADDED"></span><span id="rtm_route_added"></span><dl> <dt>**RTM\_ROUTE\_ADDED**</dt> </dl>       | The route was added for the destination network. The *CurBestRoute* parameter points to the information for the added route.<br/>                                                                                                                                                                    |
| <span id="RTM_ROUTE_CHANGED"></span><span id="rtm_route_changed"></span><dl> <dt>**RTM\_ROUTE\_CHANGED**</dt> </dl> | At least one of the significant parameters was changed for the best route to the destination network. The significant parameters are: <br/> Protocol identifier<br/> Interface index<br/> Next-hop address<br/> Protocol-family-specific data (including route metrics)<br/> |



 

The *PrevBestRoute* parameter points to the route information as it was before the change. The *CurBestRoute* parameter points to the current (that is, after-change) route information.

</dd> <dt>

*CurBestRoute* \[out\]
</dt> <dd>

Pointer to a structure that receives the current best-route information, if any. The type of the structure is specific to the protocol family, for example, IP or IPX.

This parameter is optional. If the caller specifies **NULL** for this parameter, the current best-route information is not returned.

</dd> <dt>

*PrevBestRoute* \[out\]
</dt> <dd>

Pointer to a structure that receives the previous best-route information, if any. The type of the structure is specific to the protocol family, for example, IP or IPX.

This parameter is optional. If the caller specifies **NULL** for this parameter the previous best-route information is not returned.

</dd> </dl>

## Return value

The return value is one of the following codes.



| Value                                                                                                       | Description                                                             |
|-------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| <dl> <dt>**NO\_ERROR**</dt> </dl>                    | The route was added or updated successfully.<br/>                 |
| <dl> <dt>**ERROR\_INVALID\_HANDLE**</dt> </dl>       | The client handle parameter is not a valid handle.<br/>           |
| <dl> <dt>**ERROR\_INVALID\_PARAMETER**</dt> </dl>    | The route structure contains an invalid parameter.<br/>           |
| <dl> <dt>**ERROR\_NO\_SYSTEM\_RESOURCES**</dt> </dl> | There are insufficient resources to carry out the operation.<br/> |
| <dl> <dt>**ERROR\_NOT\_ENOUGH\_MEMORY**</dt> </dl>   | There is insufficient memory to allocate the route entry.<br/>    |



 

## Remarks

The function generates a route-change message if the best route to a destination network has changed as the result of this operation. However, the route-change message is not sent to the client that makes this call. Instead, relevant information is returned by this function directly to that client through the *Flags*, *CurBestRoute*, and *PrevBestRoute* parameters.

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

[**RtmDeleteRoute**](rtmdeleteroute.md)
</dt> <dt>

[**RtmDequeueRouteChangeMessage**](rtmdequeueroutechangemessage.md)
</dt> </dl>

 

 





