---
title: IVMHostInfo MemoryAvail property
description: The MemoryAvail property contains the total quantity, in megabytes, of available RAM in the host machine.
ms.assetid: 'f894dcdb-1fda-4158-b7ee-87e5be797931'
keywords: ["MemoryAvail property Virtual Server", "MemoryAvail property Virtual Server , IVMHostInfo interface", "IVMHostInfo interface Virtual Server , MemoryAvail property", "MemoryAvail property Virtual Server , VMHostInfo interface", "VMHostInfo interface Virtual Server , MemoryAvail property"]
topic_type:
- apiref
api_name:
- IVMHostInfo.MemoryAvail
- IVMHostInfo.get_MemoryAvail
- VMHostInfo.MemoryAvail
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMHostInfo::MemoryAvail property

The **MemoryAvail** property contains the total quantity, in megabytes, of available RAM in the host machine.

This property is read-only.

## Syntax


```C++
HRESULT get_MemoryAvail(
  [out] VARIANT *megabytesOfMemory
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
<td><pre><code>VMHostInfo.MemoryAvail( _
  ByRef megabytesOfMemory _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The total quantity, in megabytes, of available RAM in the host machine. The number is returned as a **Decimal** value.

This property value is read-only.

## Error codes



| Name                                                                                          | Meaning                                        |
|-----------------------------------------------------------------------------------------------|------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>       |
| <dl> <dt> E\_POINTER</dt> </dl>        | The outgoing parameter is **NULL**.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error occurred.<br/>       |



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

 

 





