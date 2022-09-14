---
title: UninitializeNapAgentNotifier function (NapUtil.h)
description: Unsubscribes the calling process from NapAgent state change notifications and quarantine state change notifications.
ms.assetid: b676ee33-caf6-48f0-acf8-5be1b23c62fe
keywords:
- UninitializeNapAgentNotifier function NAP
topic_type:
- apiref
api_name:
- UninitializeNapAgentNotifier
api_location:
- qutil.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# UninitializeNapAgentNotifier function

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **UninitializeNapAgentNotifier** function unsubscribes the calling process from NapAgent state change notifications and quarantine state change notifications. These notifications are provided by the NapAgent service.

## Syntax


```C++
NAPAPI VOID WINAPI UninitializeNapAgentNotifier(
  _In_ NapNotifyType type
);
```



## Parameters

<dl> <dt>

*type* \[in\]
</dt> <dd>

A [**NapNotifyType**](/windows/win32/api/naptypes/ne-naptypes-napnotifytype) value that specifies the type of service notifications to unsubscribe from.

</dd> </dl>

## Return value

This function has no return values.

## Remarks

This function is not thread safe.

Each process subscribed to NapAgent service notifications of the specified *type* must call **UninitializeNapAgentNotifier** to unsubscribe from notifications. If a process is subscribed to more than one type of notification, it must call **UninitializeNapAgentNotifier** once for each type of notification.

This function will fail silently if the process had not previously called [**InitializeNapAgentNotifier**](initializenapagentnotifier.md) for the notification type.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>NapUtil.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Qutil.dll</dt> </dl> |



## See also

<dl> <dt>

[**InitializeNapAgentNotifier**](initializenapagentnotifier.md)
</dt> </dl>

 

 





