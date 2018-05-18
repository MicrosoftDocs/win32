---
title: IVMTask IsCancelable property
description: The IsCancelable property indicates whether the task can be canceled before completion.
ms.assetid: '2847c066-1c4b-44ec-91ec-ac5ef78de546'
keywords: ["IsCancelable property Virtual Server", "IsCancelable property Virtual Server , IVMTask interface", "IVMTask interface Virtual Server , IsCancelable property", "IsCancelable property Virtual Server , VMTask interface", "VMTask interface Virtual Server , IsCancelable property"]
topic_type:
- apiref
api_name:
- IVMTask.IsCancelable
- IVMTask.get_IsCancelable
- VMTask.IsCancelable
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMTask::IsCancelable property

The **IsCancelable** property indicates whether the task can be canceled before completion.

This property is read-only.

## Syntax


```C++
HRESULT get_IsCancelable(
  [in] VARIANT_BOOL *isCancelable
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
<td><pre><code>VMTask.IsCancelable( _
  ByVal isCancelable _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

Contains **vbTrue** if the task can be canceled before completion.

This property value is read-only.

## Error codes



| Name                                                                                           | Meaning                                              |
|------------------------------------------------------------------------------------------------|------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>               | The operation was successful.<br/>             |
| <dl> <dt>E\_POINTER</dt> </dl>          | The *isCancelable* parameter is **NULL**.<br/> |
| <dl> <dt> DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error has occurred.<br/>         |



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

 

 





