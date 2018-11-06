---
Description: The CloseTrace function closes a trace.
ms.assetid: 25f4c4d3-0b70-40fe-bf03-8f9ffd82fbec
title: CloseTrace function
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CloseTrace
api_type: 
- DllExport
api_location: 
- Sechost.dll
- Advapi32.dll
- API-MS-Win-DownLevel-AdvAPI32-l2-1-1.dll
- API-MS-Win-Eventing-Consumer-l1-1-0.dll
- KernelBase.dll
---

# CloseTrace function

The **CloseTrace** function closes a trace.

## Syntax


```C++
ULONG CloseTrace(
  _In_ TRACEHANDLE TraceHandle
);
```



## Parameters

<dl> <dt>

*TraceHandle* \[in\]
</dt> <dd>

Handle to the trace to close. The [**OpenTrace**](opentrace.md) function returns this handle.

</dd> </dl>

## Return value

If the function succeeds, the return value is ERROR\_SUCCESS.

If the function fails, the return value is one of the [system error codes](https://msdn.microsoft.com/library/windows/desktop/ms681381). The following table includes some common errors and their causes.



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
<td><dl> <dt><strong>ERROR_INVALID_HANDLE</strong></dt> </dl></td>
<td>One of the following is true:<br/>
<ul>
<li><em>TraceHandle</em> is <strong>NULL</strong>.</li>
<li><em>TraceHandle</em> is INVALID_HANDLE_VALUE.</li>
</ul></td>
</tr>
<tr class="even">
<td><dl> <dt><strong>ERROR_BUSY</strong></dt> </dl></td>
<td>Prior to Windows Vista, you cannot close the trace until the <a href="processtrace"><strong>ProcessTrace</strong></a> function completes. <br/></td>
</tr>
<tr class="odd">
<td><dl> <dt><strong>ERROR_CTX_CLOSE_PENDING</strong></dt> </dl></td>
<td>The call was successful. The <a href="processtrace"><strong>ProcessTrace</strong></a> function will stop after it has processed all real-time events in its buffers (it will not receive any new events).<br/></td>
</tr>
</tbody>
</table>



 

## Remarks

Consumers call this function.

If you are processing events from a log file, you call this function only after the [**ProcessTrace**](processtrace.md) function returns. However, if you are processing real-time events, you can call this function before **ProcessTrace** returns. If you call this function before **ProcessTrace** returns, the **CloseTrace** function returns ERROR\_CTX\_CLOSE\_PENDING. The ERROR\_CTX\_CLOSE\_PENDING code indicates that the **CloseTrace** function call was successful; the **ProcessTrace** function will stop processing events after it processes all events in its buffers (**ProcessTrace** will not receive any new events after you call the **CloseTrace** function). You can call the **CloseTrace** function from your [*BufferCallback*](buffercallback.md), [*EventCallback*](eventcallback.md), or [*EventClassCallback*](eventclasscallback.md) callback.

**Prior to Windows Vista:** You can call **CloseTrace** only after [**ProcessTrace**](processtrace.md) returns.

## Examples

For an example that uses **CloseTrace**, see [Retrieving Event Data Using MOF](retrieving-event-data-using-mof.md).

## Requirements



|                                     |                                                                                                                                                                                                                                                                                                                              |
|-------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps \| UWP apps\]<br/>                                                                                                                                                                                                                                                            |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps \| UWP apps\]<br/>                                                                                                                                                                                                                                                                  |
| Header<br/>                   | <dl> <dt>Evntrace.h</dt> </dl>                                                                                                                                                                                                                                        |
| Library<br/>                  | <dl> <dt>Sechost.lib on Windows 8.1 and Windows Server 2012 R2; </dt> <dt>Advapi32.lib on Windows 8, Windows Server 2012, Windows 7, Windows Server 2008 R2, Windows Server 2008, Windows Vista and Windows XP</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Sechost.dll on Windows 8.1 and Windows Server 2012 R2; </dt> <dt>Advapi32.dll on Windows 8, Windows Server 2012, Windows 7, Windows Server 2008 R2, Windows Server 2008, Windows Vista and Windows XP</dt> </dl> |



## See also

<dl> <dt>

[**OpenTrace**](opentrace.md)
</dt> <dt>

[**ProcessTrace**](processtrace.md)
</dt> </dl>

 

 




