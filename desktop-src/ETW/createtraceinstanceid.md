---
Description: The CreateTraceInstanceId function creates a unique transaction identifier and maps it to a class GUID registration handle. You then use the transaction identifier when calling the TraceEventInstance function.
ms.assetid: ab890392-f1e4-4b4e-a46c-8c7c2bfd3897
title: CreateTraceInstanceId function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CreateTraceInstanceId function

The **CreateTraceInstanceId** function creates a unique transaction identifier and maps it to a class GUID registration handle. You then use the transaction identifier when calling the [**TraceEventInstance**](traceeventinstance.md) function.

## Syntax


```C++
ULONG CreateTraceInstanceId(
  _In_  HANDLE               RegHandle,
  _Out_ PEVENT_INSTANCE_INFO pInstInfo
);
```



## Parameters

<dl> <dt>

*RegHandle* \[in\]
</dt> <dd>

Handle to a registered event trace class. The [**RegisterTraceGuids**](registertraceguids.md) function returns this handle in the **RegHandle** member of the [**TRACE\_GUID\_REGISTRATION**](trace-guid-registration.md) structure.

</dd> <dt>

*pInstInfo* \[out\]
</dt> <dd>

Pointer to an [**EVENT\_INSTANCE\_INFO**](event-instance-info.md) structure. The **InstanceId** member of this structure contains the transaction identifier.

</dd> </dl>

## Return value

If the function is successful, the return value is ERROR\_SUCCESS.

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
<td><dl> <dt><strong>ERROR_INVALID_PARAMETER</strong></dt> </dl></td>
<td>One of the following is true:<br/>
<ul>
<li><em>RegHandle</em> is <strong>NULL</strong>.</li>
<li><em>pInstInfo</em> is <strong>NULL</strong>.</li>
</ul></td>
</tr>
</tbody>
</table>



 

## Remarks

Providers call this function.

ETW creates the identifier in the user-mode process, thus it can return the same number for different processes. The value starts over at one when **InstanceId** reaches the maximum value for a **ULONG**. Only user-mode providers can call the **CreateTraceInstanceId** function; drivers cannot call this function.

## Examples

For an example that uses **CreateTraceInstanceId**, see [Tracing Event Instances](tracing-event-instances.md).

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                              |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Evntrace.h</dt> </dl>   |
| Library<br/>                  | <dl> <dt>Advapi32.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Advapi32.dll</dt> </dl> |



## See also

<dl> <dt>

[**RegisterTraceGuids**](registertraceguids.md)
</dt> <dt>

[**TraceEventInstance**](traceeventinstance.md)
</dt> </dl>

 

 




