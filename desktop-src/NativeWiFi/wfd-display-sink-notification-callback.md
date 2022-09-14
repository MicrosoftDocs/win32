---
description: Defines the callback function&\#8212;which you implement in your app&\#8212;that was specified to the WFDStartDisplaySink function.
ms.assetid: 0D4C00FD-4ED6-4F0F-BB72-0A1FCC05DB37
title: WFD_DISPLAY_SINK_NOTIFICATION_CALLBACK callback function (Wfdsink.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WFD_DISPLAY_SINK_NOTIFICATION_CALLBACK
api_type: 
- UserDefined
api_location: 
- wfdsink.h
---

# WFD\_DISPLAY\_SINK\_NOTIFICATION\_CALLBACK callback function

The **WFD\_DISPLAY\_SINK\_NOTIFICATION\_CALLBACK** function defines the callback function—which you implement in your app—that was specified to the [**WFDStartDisplaySink**](wfdstartdisplaysink.md) function.

## Syntax


```C++
DWORD CALLBACK WFD_DISPLAY_SINK_NOTIFICATION_CALLBACK(
  _In_opt_          PVOID                                 pvContext,
  _In_        const PWFD_DISPLAY_SINK_NOTIFICATION        pNotification,
  _Inout_opt_       PWFD_DISPLAY_SINK_NOTIFICATION_RESULT pNotificationResult
);
```



## Parameters

<dl> <dt>

*pvContext* \[in, optional\]
</dt> <dd>

An optional context pointer passed to the callback function.

</dd> <dt>

*pNotification* \[in\]
</dt> <dd>

A pointer to a struct containing data about the display sink notification.

</dd> <dt>

*pNotificationResult* \[in, out, optional\]
</dt> <dd>

A pointer to a struct containing data that your app can optionally set to indicate the result of processing the display sink notification.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                              |
| Header<br/>                   | <dl> <dt>Wfdsink.h</dt> </dl> |



 

 




