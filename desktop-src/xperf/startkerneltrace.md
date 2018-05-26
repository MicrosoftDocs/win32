---
title: StartKernelTrace function
description: The StartKernelTrace function registers and starts a kernel event tracing session. Also, you can enable stack walking for certain kernel events using StartKernelTrace.
ms.assetid: 29fd8307-9ebe-40f1-8668-b62575b6c185
keywords:
- StartKernelTrace function Windows Performance Analyzer
topic_type:
- apiref
api_name:
- StartKernelTrace
api_location:
- KernelTraceControl.dll
- KernelTraceControl.dll.dll
api_type:
- LibDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# StartKernelTrace function

The **StartKernelTrace** function registers and starts a kernel event tracing session. Also, you can enable stack walking for certain kernel events using **StartKernelTrace**.

## Syntax


```C++
ULONG
WINAPI StartKernelTrace(
  _Out_   PTRACEHANDLE            TraceHandle,
  _Inout_ PEVENT_TRACE_PROPERTIES Properties,
  _In_    STACK_TRACING_EVENT_ID  StackTracingEventIds[],
  _In_    ULONG                   cStackTracingEventIds
);
```



## Parameters

<dl> <dt>

*TraceHandle* \[out\]
</dt> <dd>

Stores a handle to an event tracing session. *TraceHandle* is set to zero if the handle is not valid. *TraceHandle* should not be compared to **INVALID\_HANDLE\_VALUE**. Do not use this handle if the function fails.

</dd> <dt>

*Properties* \[in, out\]
</dt> <dd>

Stores a pointer to an [EVENT\_TRACE\_PROPERTIES](http://go.microsoft.com/fwlink/p/?linkid=141500) structure. **EVENT\_TRACE\_PROPERTIES** configures certain aspects of session behavior.

For more information about the format of this parameter, see [Formatting the Properties Parameter](formatting-the-properties-parameter.md).

</dd> <dt>

*StackTracingEventIds* \[in\]
</dt> <dd>

An array of [**STACK\_TRACING\_EVENT\_ID**](stack-tracing-event-id.md) entries, where each entry specifies the type of events on which to enable stack walking.

For more information about the format of this parameter, see [Formatting the StackTracingEventIds Parameter](formatting-the-stacktracingeventids-parameter.md).

</dd> <dt>

*cStackTracingEventIds* \[in\]
</dt> <dd>

The number of [**STACK\_TRACING\_EVENT\_ID**](stack-tracing-event-id.md) entries in the *StackTracingEventIds* parameter.

</dd> </dl>

## Return value

**StartKernelTrace** returns **ERROR\_SUCCESS** if the call was successful.

Possible error return values include:



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
<td><dl> <dt> <strong>ERROR_INVALID_PARAMETER</strong> </dt> </dl></td>
<td>Possibly indicates that <em>Wnode.Guid</em> does not correspond to <strong>SystemTraceControlGuid</strong> or <strong>KernelRundownGuid</strong>. Also, this error return value possibly indicates the number of cStackTracingEventIds is greater than 256.<br/>
<blockquote>
[!Note]<br />
Starting with Windows Vista, kernel-mode WPT/ETW only supports 16 stack tracing event IDs. In the case where there are more than 16 stack tracing event IDs, the error for too many stack tracing event IDs is detected and returned by [StartTrace](http://go.microsoft.com/fwlink/p/?linkid=141509) rather than <strong>StartKernelTrace</strong>.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td><dl> <dt> <strong>ERROR_INVALID_FLAGS</strong> </dt> </dl></td>
<td>Possibly indicates that there are invalid trace flags in <em>Properties.EnableFlags</em>.<br/></td>
</tr>
<tr class="odd">
<td><dl> <dt> <strong>ERROR_OUT_OF_MEMORY</strong> </dt> </dl></td>
<td>Possibly indicates failure to allocate memory for <strong>EVENT_TRACE_PROPERTIES</strong>. <br/></td>
</tr>
<tr class="even">
<td><dl> <dt> <strong>ERROR_ALREADY_EXISTS</strong> </dt> </dl></td>
<td>Only a single instance of Kernel logger runs on the system. If <strong>StartKernelTrace</strong> attempts to start after another component has started kernel logging, this error is possibly returned.<br/></td>
</tr>
</tbody>
</table>



 

If the function fails for a reason other than those listed, a system error code is returned. For more information about system error codes, see [System Error Codes](http://go.microsoft.com/fwlink/p/?linkid=141506).

## Remarks

For more information about how to configure symbol decoding, see [Symbol Support](http://go.microsoft.com/fwlink/p/?linkid=141507).

## Requirements



|                    |                                                                                                                                                               |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Available in Windows Vista and later versions of the Windows operating system. This function is distributed with the Windows Performance Analyzer.<br/> |
| Header<br/>  | <dl> <dt>KernelTraceControl.h (include KernelTraceControl.h or Evntrace.h)</dt> </dl>                  |
| Library<br/> | <dl> <dt>KernelTraceControl.dll</dt> </dl>                                                             |



## See also

<dl> <dt>

[StartTrace](http://go.microsoft.com/fwlink/p/?linkid=141509)
</dt> <dt>

[EVENT\_TRACE\_PROPERTIES](http://go.microsoft.com/fwlink/p/?linkid=141500)
</dt> <dt>

[**STACK\_TRACING\_EVENT\_ID**](stack-tracing-event-id.md)
</dt> </dl>

 

 





