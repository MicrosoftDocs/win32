---
title: InitializeNapAgentNotifier function (NapUtil.h)
description: Subscribes the calling process to NapAgent state change notifications and quarantine state change notifications.
ms.assetid: 24180194-50d7-4f54-845d-25402af9cf9a
keywords:
- InitializeNapAgentNotifier function NAP
topic_type:
- apiref
api_name:
- InitializeNapAgentNotifier
api_location:
- qutil.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# InitializeNapAgentNotifier function

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **InitializeNapAgentNotifier** function subscribes the calling process to NapAgent state change notifications and quarantine state change notifications. These notifications are provided by the NapAgent service.

## Syntax


```C++
NAPAPI HRESULT WINAPI InitializeNapAgentNotifier(
  _In_ NapNotifyType type,
  _In_ HANDLE        hNotifyEvent
);
```



## Parameters

<dl> <dt>

*type* \[in\]
</dt> <dd>

A [**NapNotifyType**](/windows/win32/api/naptypes/ne-naptypes-napnotifytype) value that specifies the type of service notifications to receive.

</dd> <dt>

*hNotifyEvent* \[in\]
</dt> <dd>

An event handle used for notification. The caller must pass an open handle to the *hNotifyEvent* parameter. The caller must also close the event handle when it is no longer needed.

</dd> </dl>

## Return value



| Return code                                                                                                | Description                                                                                               |
|------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                       | Initialization completed successfully.<br/>                                                         |
| <dl> <dt>**E\_FAIL**</dt> </dl>                     | Initialization failed.<br/>                                                                         |
| <dl> <dt>**ERROR\_ALREADY\_INITIALIZED**</dt> </dl> | The process has already subscribed to NapAgent service notifications of the *type* specified. <br/> |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>               | An invalid argument was passed. <br/>                                                               |



 

## Remarks

This function is not thread safe.

Each process that requires a subscription to NapAgent service notifications of the specified *type* must call **InitializeNapAgentNotifier** to subscribe to notifications. If a process must subscribe to more than one type of notification, it must call **InitializeNapAgentNotifier** once for each type of notification.

Once a process does not require further notifications, the process must call [**UninitializeNapAgentNotifier**](uninitializenapagentnotifier.md) for the specified *type*.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>NapUtil.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Qutil.dll</dt> </dl> |



## See also

<dl> <dt>

[**UninitializeNapAgentNotifier**](uninitializenapagentnotifier.md)
</dt> </dl>

 

 





