---
description: Unsubscribes from service status change notifications.
ms.assetid: 8c04ebf7-4d61-4617-b120-dbe26b2f9ad2
title: UnsubscribeServiceChangeNotifications function (Winsvcp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- UnsubscribeServiceChangeNotifications
api_type: 
- DllExport
api_location: 
- SecHost.dll
- API-MS-Win-Service-Private-L1-1-0.dll
- API-MS-Win-Service-Private-L1-1-1.dll
- Advapi32.dll
- API-MS-Win-Service-Private-L1-1-2.dll
---

# UnsubscribeServiceChangeNotifications function

Unsubscribes from service status change notifications. This function uses subscriptions returned by [**SubscribeServiceChangeNotifications**](subscribeservicechangenotifications.md).

## Syntax


```C++
 VOID WINAPI UnsubscribeServiceChangeNotifications(
  _In_ PSC_NOTIFICATION_REGISTRATION pSubscription
);
```



## Parameters

<dl> <dt>

*pSubscription* \[in\]
</dt> <dd>

A pointer to the subscription to be unsubscribed.

</dd> </dl>

## Return value

This function does not return a value.

## Remarks

**UnsubscribeServiceChangeNotifications** does not return until outstanding in-process callbacks are complete. So, you cannot call **UnsubscribeServiceChangeNotifications** within the callback without causing a deadlock.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                   |
| Header<br/>                   | <dl> <dt>Winsvcp.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>SecHost.dll</dt> </dl> |



## See also

<dl> <dt>

[**CreateService**](/windows/desktop/api/Winsvc/nf-winsvc-createservicea)
</dt> <dt>

[**OpenService**](/windows/desktop/api/Winsvc/nf-winsvc-openservicea)
</dt> <dt>

[**OpenSCManager**](/windows/desktop/api/Winsvc/nf-winsvc-openscmanagera)
</dt> <dt>

[**SubscribeServiceChangeNotifications**](subscribeservicechangenotifications.md)
</dt> <dt>

[**QueryServiceDynamicInformation**](/windows/desktop/api/Winsvc/nf-winsvc-queryservicedynamicinformation)
</dt> </dl>

 

 




