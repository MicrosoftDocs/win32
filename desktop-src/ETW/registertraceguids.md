---
Description: 'The RegisterTraceGuids function registers an event trace provider and the event trace classes that it uses to generate events. This function also specifies the function the provider uses to enable and disable tracing.'
ms.assetid: 'c9158292-281b-4a02-b280-956e340d225c'
title: RegisterTraceGuids function
---

# RegisterTraceGuids function

The **RegisterTraceGuids** function registers an event trace provider and the event trace classes that it uses to generate events. This function also specifies the function the provider uses to enable and disable tracing.

## Syntax


```C++
ULONG RegisterTraceGuids(
  _In_    WMIDPREQUEST             RequestAddress,
  _In_    PVOID                    RequestContext,
  _In_    LPCGUID                  ControlGuid,
  _In_    ULONG                    GuidCount,
  _Inout_ PTRACE_GUID_REGISTRATION TraceGuidReg,
  _In_    LPCTSTR                  MofImagePath,
  _In_    LPCTSTR                  MofResourceName,
  _Out_   PTRACEHANDLE             RegistrationHandle
);
```



## Parameters

<dl> <dt>

*RequestAddress* \[in\]
</dt> <dd>

Pointer to a [**ControlCallback**](controlcallback.md) function that receives notification when the provider is enabled or disabled by an event tracing session. The [**EnableTrace**](enabletrace.md) function calls the callback.

</dd> <dt>

*RequestContext* \[in\]
</dt> <dd>

Pointer to an optional provider-defined context that ETW passes to the function specified by *RequestAddress*.

</dd> <dt>

*ControlGuid* \[in\]
</dt> <dd>

GUID of the registering provider.

</dd> <dt>

*GuidCount* \[in\]
</dt> <dd>

Number of elements in the *TraceGuidReg* array. If *TraceGuidReg* is **NULL**, set this parameter to 0.

</dd> <dt>

*TraceGuidReg* \[in, out\]
</dt> <dd>

Pointer to an array of [**TRACE\_GUID\_REGISTRATION**](trace-guid-registration.md) structures. Each element identifies a category of events that the provider provides.

On input, the **Guid** member of each structure contains an event trace class GUID assigned by the registering provider. The class GUID identifies a category of events that the provider provides. Providers use the same class GUID to set the Guid member of [**EVENT\_TRACE\_HEADER**](event-trace-header.md) when calling the [**TraceEvent**](traceevent.md) function to log the event.

On output, the **RegHandle** member receives a handle to the event's class GUID registration. If the provider calls the [**TraceEventInstance**](traceeventinstance.md) function, use the **RegHandle** member of [**TRACE\_GUID\_REGISTRATION**](trace-guid-registration.md) to set the **RegHandle** member of [**EVENT\_INSTANCE\_HEADER**](event-instance-header.md).

This parameter can be **NULL** if the provider calls only the [**TraceEvent**](traceevent.md) function to log events. If the provider calls the [**TraceEventInstance**](traceeventinstance.md) function to log events, this parameter cannot be **NULL**.

</dd> <dt>

*MofImagePath* \[in\]
</dt> <dd>

This parameter is not supported, set to **NULL**. You should use Mofcomp.exe to register the MOF resource during the setup of your application. For more information see, [Publishing Your Event Schema](publishing-your-event-schema.md).

**Windows XP with SP1, Windows XP and Windows 2000:** Pointer to an optional string that specifies the path of the DLL or executable program that contains the resource specified by *MofResourceName*. This parameter can be **NULL** if the event provider and consumer use another mechanism to share information about the event trace classes used by the provider.

</dd> <dt>

*MofResourceName* \[in\]
</dt> <dd>

This parameter is not supported, set to **NULL**. You should use Mofcomp.exe to register the MOF resource during the setup of your application. For more information see, [Publishing Your Event Schema](publishing-your-event-schema.md).

**Windows XP with SP1, Windows XP and Windows 2000:** Pointer to an optional string that specifies the string resource of *MofImagePath*. The string resource contains the name of the binary MOF file that describes the event trace classes supported by the provider.

</dd> <dt>

*RegistrationHandle* \[out\]
</dt> <dd>

Pointer to the provider's registration handle. Use this handle when you call the [**UnregisterTraceGuids**](unregistertraceguids.md) function.

</dd> </dl>

## Return value

If the function succeeds, the return value is ERROR\_SUCCESS.

If the function fails, the return value is one of the [system error codes](base.system_error_codes). The following table includes some common errors and their causes.

> [!Note]  
> This function can return the return value from [*ControlCallback*](controlcallback.md) if a controller calls [**EnableTrace**](enabletrace.md) to enable the provider and the provider has not yet called **RegisterTraceGuids**. When this occurs, **RegisterTraceGuids** will return the return value of the callback if the registration was successful.

 



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Return code</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><dl> <dt><strong>ERROR_INVALID_PARAMETER</strong></dt> </dl></td>
<td>One of the following is true: <br/>
<ul>
<li><em>RequestAddress</em> is <strong>NULL</strong>.</li>
<li><em>ControlGuid</em> is <strong>NULL</strong>.</li>
<li><em>RegistrationHandle</em> is <strong>NULL</strong>.</li>
</ul>
<strong>Windows XP and Windows 2000:  </strong><em>TraceGuidReg</em> is <strong>NULL</strong> or <em>GuidCount</em> is less than or equal to zero.<br/></td>
</tr>
</tbody>
</table>



 

## Remarks

Providers call this function.

If the provider's *ControlGuid* has been previously registered and enabled, subsequent registrations that reference the same *ControlGuid* are automatically enabled.

A process can register up to 1,024 provider GUIDs; however, you should limit the number of providers that your process registers to one or two. This limit includes those registered using this function and the [**EventRegister**](eventregister-func.md) function.

**Prior to Windows Vista:** There is no limit to the number of providers that a process can register.

## Examples

For an example that uses **RegisterTraceGuids**, see [Writing Classic Events](tracing-events.md).

## Requirements



|                                     |                                                                                                                                                                                                                                                                                                                              |
|-------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps \| UWP apps\]<br/>                                                                                                                                                                                                                                                            |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps \| UWP apps\]<br/>                                                                                                                                                                                                                                                                  |
| Minimum supported phone<br/>  | Windows Phone 8.1<br/>                                                                                                                                                                                                                                                                                                 |
| Header<br/>                   | <dl> <dt>Evntrace.h</dt> </dl>                                                                                                                                                                                                                                        |
| Library<br/>                  | <dl> <dt>Sechost.lib on Windows 8.1 and Windows Server 2012 R2; </dt> <dt>Advapi32.lib on Windows 8, Windows Server 2012, Windows 7, Windows Server 2008 R2, Windows Server 2008, Windows Vista and Windows XP</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Sechost.dll on Windows 8.1 and Windows Server 2012 R2; </dt> <dt>Advapi32.dll on Windows 8, Windows Server 2012, Windows 7, Windows Server 2008 R2, Windows Server 2008, Windows Vista and Windows XP</dt> </dl> |
| Unicode and ANSI names<br/>   | **RegisterTraceGuidsW** (Unicode) and **RegisterTraceGuidsA** (ANSI)<br/>                                                                                                                                                                                                                                              |



## See also

<dl> <dt>

[**EnableTrace**](enabletrace.md)
</dt> <dt>

[**UnregisterTraceGuids**](unregistertraceguids.md)
</dt> </dl>

 

 




