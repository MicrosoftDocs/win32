---
title: IVMHostInfo LogicalProcessorCount property
description: The LogicalProcessorCount property contains the number of logical processors in the host machine.
ms.assetid: 3ce8d439-ce08-47bc-8704-c3d3bebb3ed2
keywords:
- LogicalProcessorCount property Virtual Server
- LogicalProcessorCount property Virtual Server , IVMHostInfo interface
- IVMHostInfo interface Virtual Server , LogicalProcessorCount property
- LogicalProcessorCount property Virtual Server , VMHostInfo interface
- VMHostInfo interface Virtual Server , LogicalProcessorCount property
topic_type:
- apiref
api_name:
- IVMHostInfo.LogicalProcessorCount
- IVMHostInfo.get_LogicalProcessorCount
- VMHostInfo.LogicalProcessorCount
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

# IVMHostInfo::LogicalProcessorCount property

The **LogicalProcessorCount** property contains the number of logical processors in the host machine.

This property is read-only.

## Syntax


```C++
HRESULT get_LogicalProcessorCount(
  [out] long *processorCount
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
<td><pre><code>VMHostInfo.LogicalProcessorCount( _
  ByRef processorCount _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The number of logical processors in the host machine.

This property value is read-only.

## Error codes



| Name                                                                                          | Meaning                                        |
|-----------------------------------------------------------------------------------------------|------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>       |
| <dl> <dt>E\_POINTER</dt> </dl>         | The outgoing parameter is **NULL**.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error occurred.<br/>       |



## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMHostInfo**](ivmhostinfo.md)
</dt> </dl>

 

 





