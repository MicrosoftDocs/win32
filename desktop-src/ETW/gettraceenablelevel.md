---
Description: 'The GetTraceEnableLevel function retrieves the severity level passed by the controller to indicate the level of logging the provider should perform. Providers can only call this function from their ControlCallback function.'
ms.assetid: '22326fd9-c428-4430-8a92-978d005f6705'
title: GetTraceEnableLevel function
---

# GetTraceEnableLevel function

The **GetTraceEnableLevel** function retrieves the severity level passed by the controller to indicate the level of logging the provider should perform.

Providers can only call this function from their [**ControlCallback**](controlcallback.md) function.

## Syntax


```C++
UCHAR GetTraceEnableLevel(
  _In_ TRACEHANDLE SessionHandle
);
```



## Parameters

<dl> <dt>

*SessionHandle* \[in\]
</dt> <dd>

Handle to an event tracing session, obtained by calling the [**GetTraceLoggerHandle**](gettraceloggerhandle.md) function.

</dd> </dl>

## Return value

Returns the value the controller specified in the *EnableLevel* parameter when calling the [**EnableTrace**](enabletrace.md) function.

To determine if the function failed or the controller set the enable flags to 0, follow these steps:

-   Call the [**SetLastError**](base.setlasterror) function to set the last error to **ERROR\_SUCCESS**.
-   Call the **GetTraceEnableLevel** function to retrieve the enable level.
-   If the enable level value is 0, call the [**GetLastError**](base.getlasterror) function to retrieve the last known error.
-   If the last known error is **ERROR\_SUCCESS**, the controller set the enable level to 0; otherwise, the **GetTraceEnableLevel** function failed with the last known error.

## Remarks

Providers use this value to control the severity of events that it generates. For example, providers can use this value to determine if it should generate informational, warning, or error events.

## Examples

For an example that uses **GetTraceEnableLevel**, see [Retrieving Event Data Using MOF](retrieving-event-data-using-mof.md).

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

[**GetTraceLoggerHandle**](gettraceloggerhandle.md)
</dt> </dl>

 

 




