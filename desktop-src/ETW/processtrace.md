---
Description: The ProcessTrace function delivers events from one or more event tracing sessions to the consumer.
ms.assetid: acc6b1c4-9be1-490d-8b82-7ae8e73bd929
title: ProcessTrace function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ProcessTrace function

The **ProcessTrace** function delivers events from one or more event tracing sessions to the consumer.

## Syntax


```C++
ULONG ProcessTrace(
  _In_ PTRACEHANDLE HandleArray,
  _In_ ULONG        HandleCount,
  _In_ LPFILETIME   StartTime,
  _In_ LPFILETIME   EndTime
);
```



## Parameters

<dl> <dt>

*HandleArray* \[in\]
</dt> <dd>

Pointer to an array of trace handles obtained from earlier calls to the [**OpenTrace**](opentrace.md) function. The number of handles that you can specify is limited to 64.

The array can contain the handles to multiple log files, but only one real-time trace session.

</dd> <dt>

*HandleCount* \[in\]
</dt> <dd>

Number of elements in *HandleArray*.

</dd> <dt>

*StartTime* \[in\]
</dt> <dd>

Pointer to an optional [**FILETIME**](https://msdn.microsoft.com/windows/desktop/9baf8a0e-59e3-4fbd-9616-2ec9161520d1) structure that specifies the beginning time period for which you want to receive events. The function does not deliver events recorded prior to *StartTime*.

</dd> <dt>

*EndTime* \[in\]
</dt> <dd>

Pointer to an optional [**FILETIME**](https://msdn.microsoft.com/windows/desktop/9baf8a0e-59e3-4fbd-9616-2ec9161520d1) structure that specifies the ending time period for which you want to receive events. The function does not deliver events recorded after *EndTime*.

**Windows Server 2003:** This value is ignored for real-time event delivery.

</dd> </dl>

## Return value

If the function succeeds, the return value is ERROR\_SUCCESS.

If the function fails, the return value is one of the [system error codes](https://msdn.microsoft.com/windows/desktop/4a3a8feb-a05f-4614-8f04-1f507da7e5b7). The following table includes some common errors and their causes.



| Return code                                                                                                     | Description                                                                                                                                       |
|-----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**ERROR\_BAD\_LENGTH**</dt> </dl>               | *HandleCount* is not valid or the number of handles is greater than 64.<br/>                                                                |
| <dl> <dt>**ERROR\_INVALID\_HANDLE**</dt> </dl>           | An element of *HandleArray* is not a valid event tracing session handle.<br/>                                                               |
| <dl> <dt>**ERROR\_INVALID\_TIME**</dt> </dl>             | *EndTime* is less than *StartTime*. <br/>                                                                                                   |
| <dl> <dt>**ERROR\_INVALID\_PARAMETER**</dt> </dl>        | *HandleArray* is **NULL**.<br/>                                                                                                             |
| <dl> <dt>**ERROR\_NOACCESS**</dt> </dl>                  | An exception occurred in one of the callback functions that receives the events.<br/>                                                       |
| <dl> <dt>**ERROR\_CANCELLED**</dt> </dl>                 | Indicates the consumer canceled processing by returning **FALSE** in their [*BufferCallback*](buffercallback.md) function.<br/>            |
| <dl> <dt>**ERROR\_WMI\_INSTANCE\_NOT\_FOUND**</dt> </dl> | The session from which you are trying to consume events in real time is not running or does not have the real-time trace mode enabled.<br/> |
| <dl> <dt>**ERROR\_WMI\_ALREADY\_ENABLED**</dt> </dl>     | The *HandleArray* parameter contains the handle to more than one real-time session.<br/>                                                    |



 

## Remarks

Consumers call this function.

You must call the [**OpenTrace**](opentrace.md) function prior to calling **ProcessTrace**.

The **ProcessTrace** function delivers the events to the consumer's [**BufferCallback**](buffercallback.md), [**EventCallback**](eventcallback.md), and [**EventClassCallback**](eventclasscallback.md) callback functions.

The **ProcessTrace** function sorts the events chronologically and delivers all events generated between *StartTime* and *EndTime*. Note that events can appear out of order if the session specifies system time as the clock (low resolution) and the volume of events is high. In this case, it is possible for multiple events to contain the same time stamp. If multiple events contain the same time stamp, ETW cannot guarantee the order of those events.

The **ProcessTrace** function blocks the thread until it delivers all events, the [**BufferCallback**](buffercallback.md) function returns **FALSE**, or you call [**CloseTrace**](closetrace.md). If the consumer is consuming events in real time, the **ProcessTrace** function returns after the controller stops the trace session. (Note that there may be a several-second delay before the function returns.)

**Windows Server 2003:** You can call [**CloseTrace**](closetrace.md) only after **ProcessTrace** returns.

## Examples

For an example that uses **ProcessTrace**, see [Using TdhFormatProperty to Consume Event Data](using-tdhformatproperty-to-consume-event-data.md) or [Retrieving Event Data Using MOF](retrieving-event-data-using-mof.md).

## Requirements



|                                     |                                                                                                                                                                                                                                                                                                                              |
|-------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps \| UWP apps\]<br/>                                                                                                                                                                                                                                                            |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps \| UWP apps\]<br/>                                                                                                                                                                                                                                                                  |
| Header<br/>                   | <dl> <dt>Evntrace.h</dt> </dl>                                                                                                                                                                                                                                        |
| Library<br/>                  | <dl> <dt>Sechost.lib on Windows 8.1 and Windows Server 2012 R2; </dt> <dt>Advapi32.lib on Windows 8, Windows Server 2012, Windows 7, Windows Server 2008 R2, Windows Server 2008, Windows Vista and Windows XP</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Sechost.dll on Windows 8.1 and Windows Server 2012 R2; </dt> <dt>Advapi32.dll on Windows 8, Windows Server 2012, Windows 7, Windows Server 2008 R2, Windows Server 2008, Windows Vista and Windows XP</dt> </dl> |



## See also

<dl> <dt>

[**BufferCallback**](buffercallback.md)
</dt> <dt>

[**EventCallback**](eventcallback.md)
</dt> <dt>

[**EventClassCallback**](eventclasscallback.md)
</dt> <dt>

[**OpenTrace**](opentrace.md)
</dt> <dt>

[**SetTraceCallback**](settracecallback.md)
</dt> </dl>

 

 




