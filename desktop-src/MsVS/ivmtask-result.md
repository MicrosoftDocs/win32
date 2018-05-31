---
title: IVMTask Result property
description: The Result property contains the result of the task.
ms.assetid: f7522579-22f4-40d4-b5ff-e427d5c8f83c
keywords:
- Result property Virtual Server
- Result property Virtual Server , IVMTask interface
- IVMTask interface Virtual Server , Result property
- Result property Virtual Server , VMTask interface
- VMTask interface Virtual Server , Result property
topic_type:
- apiref
api_name:
- IVMTask.Result
- IVMTask.get_Result
- VMTask.Result
api_location:
- VsComInterfaces.h
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IVMTask::Result property

The **Result** property contains the result of the task.

This property is read-only.

## Syntax


```C++
HRESULT get_Result(
  [in] VMTaskResult *result
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
<td><pre><code>VMTask.Result( _
  ByVal result _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The result of the task.

This property value is read-only.

## Error codes



| Name                                                                                           | Meaning                                        |
|------------------------------------------------------------------------------------------------|------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>               | The operation was successful.<br/>       |
| <dl> <dt>E\_POINTER</dt> </dl>          | The *result* parameter is **NULL**.<br/> |
| <dl> <dt> DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error occurred.<br/>       |



## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMTask**](ivmtask.md)
</dt> <dt>

[**VMTaskResult**](vmtaskresult.md)
</dt> </dl>

 

 





