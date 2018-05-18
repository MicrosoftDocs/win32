---
title: IVMTask ID property
description: The ID property contains the unique ID of the task.
ms.assetid: '20e10ba1-5290-4028-b28e-70fdbb0db15f'
keywords: ["ID property Virtual Server", "ID property Virtual Server , IVMTask interface", "IVMTask interface Virtual Server , ID property", "ID property Virtual Server , VMTask interface", "VMTask interface Virtual Server , ID property"]
topic_type:
- apiref
api_name:
- IVMTask.ID
- IVMTask.get_ID
- VMTask.ID
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMTask::ID property

The **ID** property contains the unique ID of the task.

This property is read-only.

## Syntax


```C++
HRESULT get_ID(
  [in] long *ID
);
```

<span codelanguage="VisualBasic"></span>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>VB</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>VMTask.ID( _
  ByVal ID _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The unique ID of the task.

This property value is read-only.

## Error codes



| Name                                                                                           | Meaning                                    |
|------------------------------------------------------------------------------------------------|--------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>               | The operation was successful.<br/>   |
| <dl> <dt>E\_POINTER</dt> </dl>          | The *ID* parameter is **NULL**.<br/> |
| <dl> <dt> DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error occurred.<br/>   |



## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMTask**](ivmtask.md)
</dt> </dl>

 

 





