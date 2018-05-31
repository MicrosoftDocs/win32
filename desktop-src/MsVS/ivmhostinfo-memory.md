---
title: IVMHostInfo Memory property
description: The Memory property contains the total quantity, in megabytes, of physical RAM in the host machine.
ms.assetid: cefe0366-bf70-4cbd-bdfe-8756324178b3
keywords:
- Memory property Virtual Server
- Memory property Virtual Server , IVMHostInfo interface
- IVMHostInfo interface Virtual Server , Memory property
- Memory property Virtual Server , VMHostInfo interface
- VMHostInfo interface Virtual Server , Memory property
topic_type:
- apiref
api_name:
- IVMHostInfo.Memory
- IVMHostInfo.get_Memory
- VMHostInfo.Memory
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

# IVMHostInfo::Memory property

The **Memory** property contains the total quantity, in megabytes, of physical RAM in the host machine.

This property is read-only.

## Syntax


```C++
HRESULT get_Memory(
  [out] VARIANT *megabytesOfMemory
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
<td><pre><code>VMHostInfo.Memory( _
  ByRef megabytesOfMemory _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The total quantity, in megabytes, of physical RAM in the host machine. The number is returned as a **Decimal** value.

This property value is read-only.

## Error codes



| Name                                                                                          | Meaning                                        |
|-----------------------------------------------------------------------------------------------|------------------------------------------------|
| <dl> <dt> S\_OK</dt> </dl>             | The operation was successful.<br/>       |
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

 

 





