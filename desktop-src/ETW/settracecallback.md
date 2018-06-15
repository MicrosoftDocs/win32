---
Description: The SetTraceCallback function specifies an EventClassCallback function to process events for the specified event trace class.
ms.assetid: 8663f64f-a203-43e5-94e8-337f2d81c3a0
title: SetTraceCallback function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SetTraceCallback function

\[Do not use this function; it may be unavailable in subsequent versions. Instead, filter for the event trace class in your [*EventRecordCallback*](eventrecordcallback.md) function.\]

The **SetTraceCallback** function specifies an [**EventClassCallback**](eventclasscallback.md) function to process events for the specified event trace class.

## Syntax


```C++
ULONG SetTraceCallback(
  _In_ LPCGUID         pGuid,
  _In_ PEVENT_CALLBACK EventCallback
);
```



## Parameters

<dl> <dt>

*pGuid* \[in\]
</dt> <dd>

Pointer to the class GUID of an event trace class for which you want to receive events. For a list of kernel provider class GUIDs, see [NT Kernel Logger Constants](nt-kernel-logger-constants.md).

</dd> <dt>

*EventCallback* \[in\]
</dt> <dd>

Pointer to an [**EventClassCallback**](eventclasscallback.md) function used to process events belonging to the event trace class.

</dd> </dl>

## Return value

If the function succeeds, the return value is ERROR\_SUCCESS.

If the function fails, the return value is one of the [system error codes](https://msdn.microsoft.com/en-us/library/ms681381(v=VS.85).aspx). The following table includes some common errors and their causes.



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
<td>One of the following is true:<br/>
<ul>
<li><em>pGuid</em> is <strong>NULL</strong>.</li>
<li><em>EventCallback</em> is <strong>NULL</strong>.</li>
</ul></td>
</tr>
</tbody>
</table>



 

## Remarks

Consumers call this function.

You can only specify one callback function for an event trace class. If you specify more than one callback function for the even trace class, the last callback function receives the events for that event trace class.

To stop the callback function from receiving events for the event trace class, call the [**RemoveTraceCallback**](removetracecallback.md) function. The callback automatically stops receiving callbacks when you close the trace.

You can use this function to receive events written using one of the [**TraceEvent**](traceevent.md) functions. You cannot use this function to consume events from a provider that used one of the [**EventWrite**](/windows/desktop/api/Evntprov/nf-evntprov-eventwrite) functions to log events.

## Requirements



|                                     |                                                                                                                                                                                                                                                                                                                              |
|-------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                                                                                                                                                                                                                                   |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                                                                                                                                                                                                                                         |
| Header<br/>                   | <dl> <dt>Evntrace.h</dt> </dl>                                                                                                                                                                                                                                        |
| Library<br/>                  | <dl> <dt>Sechost.lib on Windows 8.1 and Windows Server 2012 R2; </dt> <dt>Advapi32.lib on Windows 8, Windows Server 2012, Windows 7, Windows Server 2008 R2, Windows Server 2008, Windows Vista and Windows XP</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Sechost.dll on Windows 8.1 and Windows Server 2012 R2; </dt> <dt>Advapi32.dll on Windows 8, Windows Server 2012, Windows 7, Windows Server 2008 R2, Windows Server 2008, Windows Vista and Windows XP</dt> </dl> |



## See also

<dl> <dt>

[**EventClassCallback**](eventclasscallback.md)
</dt> <dt>

[**ProcessTrace**](processtrace.md)
</dt> <dt>

[**RemoveTraceCallback**](removetracecallback.md)
</dt> </dl>

 

 




