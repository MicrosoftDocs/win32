---
Description: The GetTraceEnableFlags function retrieves the enable flags passed by the controller to indicate which category of events to trace.Providers can only call this function from their ControlCallback function.
ms.assetid: e5c0f2bf-34da-4555-9556-4c79ee9a73ab
title: GetTraceEnableFlags function (Evntrace.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- GetTraceEnableFlags
api_type: 
- DllExport
api_location: 
- Advapi32.dll
- API-MS-Win-DownLevel-AdvApi32-l1-1-0.dll
- KernelBase.dll
- API-MS-Win-DownLevel-AdvApi32-l1-1-1.dll
- API-MS-Win-eventing-classicprovider-l1-1-0.dll
---

# GetTraceEnableFlags function

The **GetTraceEnableFlags** function retrieves the enable flags passed by the controller to indicate which category of events to trace.

Providers can only call this function from their [**ControlCallback**](controlcallback.md) function.

## Syntax


```C++
ULONG GetTraceEnableFlags(
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

Returns the value the controller specified in the *EnableFlag* parameter when calling the [**EnableTrace**](enabletrace.md) function.

To determine if the function failed or the controller set the enable flags to 0, follow these steps:

-   Call the [**SetLastError**](https://msdn.microsoft.com/en-us/library/ms680627(v=VS.85).aspx) function to set the last error to **ERROR\_SUCCESS**.
-   Call the **GetTraceEnableFlags** function to retrieve the enable flags.
-   If the enable flags value is 0, call the [**GetLastError**](https://msdn.microsoft.com/en-us/library/ms679360(v=VS.85).aspx) function to retrieve the last known error.
-   If the last known error is **ERROR\_SUCCESS**, the controller set the enable flags to 0; otherwise, the **GetTraceEnableFlags** function failed with the last known error.

## Remarks

Providers can use this value to control which events that it generates. For example, a provider can group events into logical categories of events and use this value to enable or disable their generation.

## Examples

For an example that uses **GetTraceEnableFlags**, see [Retrieving Event Data Using MOF](retrieving-event-data-using-mof.md).

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

[**GetTraceEnableLevel**](gettraceenablelevel.md)
</dt> <dt>

[**GetTraceLoggerHandle**](gettraceloggerhandle.md)
</dt> </dl>

 

 




