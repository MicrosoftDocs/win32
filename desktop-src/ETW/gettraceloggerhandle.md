---
Description: The GetTraceLoggerHandle function retrieves the handle of the event tracing session. Providers can only call this function from their ControlCallback function.
ms.assetid: 050d3a01-0087-40f1-af35-b9ceeaf47813
title: GetTraceLoggerHandle function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# GetTraceLoggerHandle function

The **GetTraceLoggerHandle** function retrieves the handle of the event tracing session.

Providers can only call this function from their [**ControlCallback**](controlcallback.md) function.

## Syntax


```C++
TRACEHANDLE GetTraceLoggerHandle(
  _In_ PVOID Buffer
);
```



## Parameters

<dl> <dt>

*Buffer* \[in\]
</dt> <dd>

Pointer to a [**WNODE\_HEADER**](wnode-header.md) structure. ETW passes this structure to the provider's [**ControlCallback**](controlcallback.md) function in the *Buffer* parameter.

The **HistoricalContext** member of [**WNODE\_HEADER**](wnode-header.md) contains the session's handle.

</dd> </dl>

## Return value

If the function succeeds, it returns the event tracing session handle.

If the function fails, it returns **INVALID\_HANDLE\_VALUE**. To get extended error information, call the [**GetLastError**](base.getlasterror) function.

## Remarks

You use the handle when calling the [**GetTraceEnableFlags**](gettraceenableflags.md) and [**GetTraceEnableLevel**](gettraceenablelevel.md) functions to retrieve the enable flags and level values passed to the [**EnableTrace**](enabletrace.md) function.

## Examples

For an example that uses **GetTraceLoggerHandle**, see [Retrieving Event Data Using MOF](retrieving-event-data-using-mof.md).

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps \| UWP apps\]<br/>                       |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps \| UWP apps\]<br/>                             |
| Minimum supported phone<br/>  | Windows Phone 8.1<br/>                                                            |
| Header<br/>                   | <dl> <dt>Evntrace.h</dt> </dl>   |
| Library<br/>                  | <dl> <dt>Advapi32.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Advapi32.dll</dt> </dl> |



## See also

<dl> <dt>

[**GetTraceEnableFlags**](gettraceenableflags.md)
</dt> <dt>

[**GetTraceEnableLevel**](gettraceenablelevel.md)
</dt> </dl>

 

 




