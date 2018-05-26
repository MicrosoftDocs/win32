---
Description: Unsubscribes from service status change notifications.
ms.assetid: 8c04ebf7-4d61-4617-b120-dbe26b2f9ad2
title: UnsubscribeServiceChangeNotifications function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                   |
| Header<br/>                   | <dl> <dt>Winsvcp.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>SecHost.dll</dt> </dl> |



## See also

<dl> <dt>

[**CreateService**](/windows/win32/Winsvc/nf-winsvc-createservicea?branch=master)
</dt> <dt>

[**OpenService**](/windows/win32/Winsvc/nf-winsvc-openservicea?branch=master)
</dt> <dt>

[**OpenSCManager**](/windows/win32/Winsvc/nf-winsvc-openscmanagera?branch=master)
</dt> <dt>

[**SubscribeServiceChangeNotifications**](subscribeservicechangenotifications.md)
</dt> <dt>

[**QueryServiceDynamicInformation**](/windows/win32/Winsvc/nf-winsvc-queryservicedynamicinformation?branch=master)
</dt> </dl>

 

 




