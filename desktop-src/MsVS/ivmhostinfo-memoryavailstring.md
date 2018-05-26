---
title: IVMHostInfo MemoryAvailString property
description: The MemoryAvailString property contains the total quantity, in megabytes, of available RAM in the host machine.
ms.assetid: b0ef7ce4-0c7b-44da-838c-834ec614aba8
keywords:
- MemoryAvailString property Virtual Server
- MemoryAvailString property Virtual Server , IVMHostInfo interface
- IVMHostInfo interface Virtual Server , MemoryAvailString property
- MemoryAvailString property Virtual Server , VMHostInfo interface
- VMHostInfo interface Virtual Server , MemoryAvailString property
topic_type:
- apiref
api_name:
- IVMHostInfo.MemoryAvailString
- IVMHostInfo.get_MemoryAvailString
- VMHostInfo.MemoryAvailString
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

# IVMHostInfo::MemoryAvailString property

The **MemoryAvailString** property contains the total quantity, in megabytes, of available RAM in the host machine.

This property is read-only.

## Syntax


```C++
HRESULT get_MemoryAvailString(
  [out] BSTR *megabytesOfMemory
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
<td><pre><code>VMHostInfo.MemoryAvailString( _
  ByRef megabytesOfMemory _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The total quantity, in megabytes, of available RAM in the host machine.

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
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMHostInfo**](ivmhostinfo.md)
</dt> </dl>

 

 





