---
title: IVMTask PercentCompleted property
description: The PercentCompleted property contains the completion percentage of the task.
ms.assetid: ea5e8f07-f6de-49d8-a3d9-9019c3780d20
keywords:
- PercentCompleted property Virtual Server
- PercentCompleted property Virtual Server , IVMTask interface
- IVMTask interface Virtual Server , PercentCompleted property
- PercentCompleted property Virtual Server , VMTask interface
- VMTask interface Virtual Server , PercentCompleted property
topic_type:
- apiref
api_name:
- IVMTask.PercentCompleted
- IVMTask.get_PercentCompleted
- VMTask.PercentCompleted
api_location:
- VsComInterfaces.h
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IVMTask::PercentCompleted property

The **PercentCompleted** property contains the completion percentage of the task.

This property is read-only.

## Syntax


```C++
HRESULT get_PercentCompleted(
  [in] long *percentCompleted
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
<td><pre><code>VMTask.PercentCompleted( _
  ByVal percentCompleted _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The current completion percentage of the task. Values range from 0 to 100.

This property value is read-only.

## Error codes



| Name                                                                                           | Meaning                                                  |
|------------------------------------------------------------------------------------------------|----------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>               | The operation was successful.<br/>                 |
| <dl> <dt>E\_POINTER</dt> </dl>          | The *percentCompleted* parameter is **NULL**.<br/> |
| <dl> <dt> DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error occurred.<br/>                 |



## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMTask**](ivmtask.md)
</dt> </dl>

 

 





