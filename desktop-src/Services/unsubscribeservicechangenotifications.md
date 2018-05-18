---
Description: 'Unsubscribes from service status change notifications.'
ms.assetid: '8c04ebf7-4d61-4617-b120-dbe26b2f9ad2'
title: UnsubscribeServiceChangeNotifications function
---

# UnsubscribeServiceChangeNotifications function

Unsubscribes from service status change notifications. This function uses subscriptions returned by [**SubscribeServiceChangeNotifications**](subscribeservicechangenotifications.md).

## Syntax


```C++
 VOID WINAPI UnsubscribeServiceChangeNotifications(
  _In_ PSC_NOTIFICATION_REGISTRATION pSubscription
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



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                   |
| Header<br/>                   | <dl> <dt>Winsvcp.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>SecHost.dll</dt> </dl> |



## See also

<dl> <dt>

[**CreateService**](createservice.md)
</dt> <dt>

[**OpenService**](openservice.md)
</dt> <dt>

[**OpenSCManager**](openscmanager.md)
</dt> <dt>

[**SubscribeServiceChangeNotifications**](subscribeservicechangenotifications.md)
</dt> <dt>

[**QueryServiceDynamicInformation**](queryservicedynamicinformation.md)
</dt> </dl>

 

 




