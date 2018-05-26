---
title: IVMTask IsComplete property
description: The IsComplete property indicates whether the task has completed.
ms.assetid: 95e84969-8edb-4a84-b9ef-74df0413e8f7
keywords:
- IsComplete property Virtual Server
- IsComplete property Virtual Server , IVMTask interface
- IVMTask interface Virtual Server , IsComplete property
- IsComplete property Virtual Server , VMTask interface
- VMTask interface Virtual Server , IsComplete property
topic_type:
- apiref
api_name:
- IVMTask.IsComplete
- IVMTask.get_IsComplete
- VMTask.IsComplete
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

# IVMTask::IsComplete property

The **IsComplete** property indicates whether the task has completed.

This property is read-only.

## Syntax


```C++
HRESULT get_IsComplete(
  [in] VARIANT_BOOL *isComplete
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
<td><pre><code>VMTask.IsComplete( _
  ByVal isComplete _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

Contains **vbTrue** if the task has completed.

This property value is read-only.

## Error codes



| Name                                                                                           | Meaning                                            |
|------------------------------------------------------------------------------------------------|----------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>               | The operation was successful.<br/>           |
| <dl> <dt>E\_POINTER</dt> </dl>          | The *isComplete* parameter is **NULL**.<br/> |
| <dl> <dt> DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error has occurred.<br/>       |



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

 

 





