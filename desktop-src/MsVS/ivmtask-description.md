---
title: IVMTask Description property
description: The Description property contains the description of the task.
ms.assetid: fdcd1e44-3162-4abc-89ec-ff747aedeb0b
keywords:
- Description property Virtual Server
- Description property Virtual Server , IVMTask interface
- IVMTask interface Virtual Server , Description property
- Description property Virtual Server , VMTask interface
- VMTask interface Virtual Server , Description property
topic_type:
- apiref
api_name:
- IVMTask.Description
- IVMTask.get_Description
- VMTask.Description
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

# IVMTask::Description property

The **Description** property contains the description of the task.

This property is read-only.

## Syntax


```C++
HRESULT get_Description(
  [in] BSTR *description
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
<td><pre><code>VMTask.Description( _
  ByVal description _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The description of the task.

This property value is read-only.

## Error codes



| Name                                                                                           | Meaning                                             |
|------------------------------------------------------------------------------------------------|-----------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>               | The operation was successful.<br/>            |
| <dl> <dt>E\_POINTER</dt> </dl>          | The *description* parameter is **NULL**.<br/> |
| <dl> <dt> DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error occurred.<br/>            |



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

 

 





