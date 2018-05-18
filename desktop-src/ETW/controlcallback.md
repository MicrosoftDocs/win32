---
Description: 'Providers implement this function to receive enable or disable notification requests from controllers. The WMIDPREQUEST type defines a pointer to this callback function. ControlCallback is a placeholder for the application-defined function name.'
ms.assetid: 'e9f70ae6-906f-4e55-bca7-4355f1ca6091'
title: WMIDPREQUEST callback function
---

# WMIDPREQUEST callback function

Providers implement this function to receive enable or disable notification requests from controllers.

The **WMIDPREQUEST** type defines a pointer to this callback function. **ControlCallback** is a placeholder for the application-defined function name.

## Syntax


```C++
ULONG WINAPI ControlCallback(
  _In_ WMIDPREQUESTCODE RequestCode,
  _In_ PVOID            Context,
  _In_ ULONG            *Reserved,
  _In_ PVOID            Buffer
);
```



## Parameters

<dl> <dt>

*RequestCode* \[in\]
</dt> <dd>

Request code. Specify one of the following values.



| Value                                                                                                                                                                         | Meaning                           |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------|
| <span id="WMI_ENABLE_EVENTS"></span><span id="wmi_enable_events"></span><dl> <dt>**WMI\_ENABLE\_EVENTS**</dt> </dl>    | Enables the provider.<br/>  |
| <span id="WMI_DISABLE_EVENTS"></span><span id="wmi_disable_events"></span><dl> <dt>**WMI\_DISABLE\_EVENTS**</dt> </dl> | Disables the provider.<br/> |



 

</dd> <dt>

*Context* \[in\]
</dt> <dd>

Provider-defined context. The provider uses the *RequestContext* parameter of [**RegisterTraceGuids**](registertraceguids.md) to specify the context.

</dd> <dt>

*Reserved* \[in\]
</dt> <dd>

Reserved for internal use.

</dd> <dt>

*Buffer* \[in\]
</dt> <dd>

Pointer to a [**WNODE\_HEADER**](wnode-header.md) structure that contains information about the event tracing session for which the provider is being enabled or disabled.

</dd> </dl>

## Return value

You should return ERROR\_SUCCESS if the callback succeeds. Note that ETW ignores the return value for this function except when a controller calls [**EnableTrace**](enabletrace.md) to enable a provider and the provider has not yet called [**RegisterTraceGuids**](registertraceguids.md). When this occurs, **RegisterTraceGuids** will return the return value of this callback if the registration was successful.

## Remarks

This function is specified using the [**RegisterTraceGuids**](registertraceguids.md) function. When the controller calls the [**EnableTrace**](enabletrace.md) function to enable, disable, or change the enable flags or level, ETW calls this callback. The provider enables or disables itself based the *RequestCode* value. Typically, the provider uses this value to set a global flag to indicate its enabled state.

The provider defines its interpretation of being enabled or disabled. Generally, if a provider is enabled, it generates events, but while it is disabled, it does not.

ETW does not pass the enable flags and enable level that the controller passes to the [**EnableTrace**](enabletrace.md) function to this callback. To retrieve this information, call the [**GetTraceEnableFlags**](gettraceenableflags.md) and [**GetTraceEnableLevel**](gettraceenablelevel.md) functions, respectively.

You also need to retrieve the session handle in this callback for future calls. To retrieve the session handle, call the [**GetTraceLoggerHandle**](gettraceloggerhandle.md) function.

Your callback function must not call anything that may incur LoadLibrary (more specifically, anything that requires a loader lock).

## Examples

For an example implementation of a **ControlCallback** function, see [Writing Classic Events](tracing-events.md).

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps \| UWP apps\]<br/>                     |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps \| UWP apps\]<br/>                           |
| Header<br/>                   | <dl> <dt>Evntrace.h</dt> </dl> |



## See also

<dl> <dt>

[**EnableTrace**](enabletrace.md)
</dt> <dt>

[**GetTraceEnableFlags**](gettraceenableflags.md)
</dt> <dt>

[**GetTraceEnableLevel**](gettraceenablelevel.md)
</dt> <dt>

[**GetTraceLoggerHandle**](gettraceloggerhandle.md)
</dt> <dt>

[**RegisterTraceGuids**](registertraceguids.md)
</dt> <dt>

[**WNODE\_HEADER**](wnode-header.md)
</dt> </dl>

 

 




