---
description: Subscribes for service status change notifications using a callback function.
ms.assetid: d67113eb-2141-444c-9f09-eaa772bcad8a
title: SubscribeServiceChangeNotifications function (Winsvcp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SubscribeServiceChangeNotifications
api_type: 
- DllExport
api_location: 
- SecHost.dll
- API-MS-Win-Service-Private-L1-1-0.dll
- API-MS-Win-Service-Private-L1-1-1.dll
- Advapi32.dll
- API-MS-Win-Service-Private-L1-1-2.dll
---

# SubscribeServiceChangeNotifications function

Subscribes for service status change notifications using a callback function.

## Syntax


```C++
DWORD WINAPI SubscribeServiceChangeNotifications(
  _In_     SC_HANDLE                     hService,
  _In_     SC_EVENT_TYPE                 eEventType,
  _In_     PSC_NOTIFICATION_CALLBACK     pCallback,
  _In_opt_ PVOID                         pCallbackContext,
  _Out_    PSC_NOTIFICATION_REGISTRATION *pSubscription
);
```



## Parameters

<dl> <dt>

*hService* \[in\]
</dt> <dd>

A handle to the service or a handle to the service control manager (SCM) to monitor for changes.

Handles to services are returned by the [**OpenService**](/windows/desktop/api/Winsvc/nf-winsvc-openservicea) and [**CreateService**](/windows/desktop/api/Winsvc/nf-winsvc-createservicea) function and must have the **SERVICE\_QUERY\_STATUS** access right. Handles to the service control manager are returned by the [**OpenSCManager**](/windows/desktop/api/Winsvc/nf-winsvc-openscmanagera) function and must have the **SC\_MANAGER\_ENUMERATE\_SERVICE** access right.

</dd> <dt>

*eEventType* \[in\]
</dt> <dd>

Specifies the type of status changes that should be reported. This parameter is set to one of the values specified in [**SC\_EVENT\_TYPE**](sc-event-type.md). The behavior for this function is different depending on the event type as follows.



| Value                                                                                                                                                                                                                                                   | Meaning                                                                                                                |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| <span id="SC_EVENT_DATABASE_CHANGE"></span><span id="sc_event_database_change"></span><dl> <dt>**SC\_EVENT\_DATABASE\_CHANGE**</dt> <dt>0</dt> </dl> | A service has been added or deleted. The *hService* parameter must be a handle to the SCM.<br/>                  |
| <span id="SC_EVENT_PROPERTY_CHANGE"></span><span id="sc_event_property_change"></span><dl> <dt>**SC\_EVENT\_PROPERTY\_CHANGE**</dt> <dt>1</dt> </dl> | One or more service properties have been updated. The *hService* parameter must be a handle to the service.<br/> |
| <span id="SC_EVENT_STATUS_CHANGE"></span><span id="sc_event_status_change"></span><dl> <dt>**SC\_EVENT\_STATUS\_CHANGE**</dt> <dt>2</dt> </dl>       | The status of a service has changed. The *hService* parameter must be a handle to the service.<br/>              |



 

</dd> <dt>

*pCallback* \[in\]
</dt> <dd>

Specifies the callback function. The callback must be defined as having a type of **SC\_NOTIFICATION\_CALLBACK**. For more information, see Remarks.

</dd> <dt>

*pCallbackContext* \[in, optional\]
</dt> <dd>

A pointer representing the context for this notification callback.

</dd> <dt>

*pSubscription* \[out\]
</dt> <dd>

Returns a pointer to the subscription resulting from the notification callback registration. The caller is responsible for calling [**UnsubscribeServiceChangeNotifications**](unsubscribeservicechangenotifications.md) to stop receiving notifications.

</dd> </dl>

## Return value

If the function succeeds, the return value is **ERROR\_SUCCESS**.

If the function fails, the return value is one of the [system error codes](/windows/desktop/Debug/system-error-codes).

## Remarks

The callback function is declared as follows:


```C++
typedef VOID CALLBACK SC_NOTIFICATION_CALLBACK(
    _In_    DWORD                   dwNotify,
    _In_    PVOID                   pCallbackContext
);
typedef SC_NOTIFICATION_CALLBACK* PSC_NOTIFICATION_CALLBACK;
```



The callback function receives a pointer to the context provided by the caller. The callback is invoked as a result of the service status change event. When the callback is invoked, it is provided with a bitmask of **SERVICE\_NOTIFY\_*XXX*** values that indicating the type of service status change. When the callback is provided with zero instead of a valid **SERVICE\_NOTIFY\_*XXX*** value, the application must verify what was changed.

The callback function must not block execution. If you expect the execution of the callback function to take time, offload the work that you perform in the callback function to a separate thread by queuing a work item to a thread in a thread pool. Some types of work that can make the callback function take time include performing file I/O, waiting on an event, and making external remote procedure calls.

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

[**UnsubscribeServiceChangeNotifications**](unsubscribeservicechangenotifications.md)
</dt> <dt>

[**QueryServiceDynamicInformation**](/windows/desktop/api/Winsvc/nf-winsvc-queryservicedynamicinformation)
</dt> </dl>

 

