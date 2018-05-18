---
title: IVMHostInfo PhysicalProcessorCount property
description: The PhysicalProcessorCount property contains the number of physical processors in the host machine.
ms.assetid: '6f0401a3-d6dd-4ce5-8d8f-d247bea5c6fb'
keywords: ["PhysicalProcessorCount property Virtual Server", "PhysicalProcessorCount property Virtual Server , IVMHostInfo interface", "IVMHostInfo interface Virtual Server , PhysicalProcessorCount property", "PhysicalProcessorCount property Virtual Server , VMHostInfo interface", "VMHostInfo interface Virtual Server , PhysicalProcessorCount property"]
topic_type:
- apiref
api_name:
- IVMHostInfo.PhysicalProcessorCount
- IVMHostInfo.get_PhysicalProcessorCount
- VMHostInfo.PhysicalProcessorCount
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMHostInfo::PhysicalProcessorCount property

The **PhysicalProcessorCount** property contains the number of physical processors in the host machine.

This property is read-only.

## Syntax


```C++
HRESULT get_PhysicalProcessorCount(
  [out] long *processorCount
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
<td><pre><code>VMHostInfo.PhysicalProcessorCount( _
  ByRef processorCount _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The number of physical processors in the host machine.

This property value is read-only.

## Error codes



| Name                                                                                           | Meaning                                        |
|------------------------------------------------------------------------------------------------|------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>               | The operation was successful.<br/>       |
| <dl> <dt> E\_POINTER</dt> </dl>         | The outgoing parameter is **NULL**.<br/> |
| <dl> <dt> DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error occurred.<br/>       |



## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMHostInfo**](ivmhostinfo.md)
</dt> </dl>

 

 





