---
title: IVMHostInfo ParallelPort property
description: The ParallelPort property contains the name of the parallel port on the host computer.
ms.assetid: '9ff6cdb1-c13b-49f6-a630-b2097478ea15'
keywords: ["ParallelPort property Virtual Server", "ParallelPort property Virtual Server , IVMHostInfo interface", "IVMHostInfo interface Virtual Server , ParallelPort property", "ParallelPort property Virtual Server , VMHostInfo interface", "VMHostInfo interface Virtual Server , ParallelPort property"]
topic_type:
- apiref
api_name:
- IVMHostInfo.ParallelPort
- IVMHostInfo.get_ParallelPort
- VMHostInfo.ParallelPort
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMHostInfo::ParallelPort property

The **ParallelPort** property contains the name of the parallel port on the host computer.

This property is read-only.

## Syntax


```C++
HRESULT get_ParallelPort(
  [out] BSTR *parallelPort
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
<td><pre><code>VMHostInfo.ParallelPort( _
  ByRef parallelPort _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The name of the parallel port.

This property value is read-only.

## Error codes



| Name                                                                                          | Meaning                                                      |
|-----------------------------------------------------------------------------------------------|--------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>                     |
| <dl> <dt>E\_POINTER</dt> </dl>         | The *parallelPort* parameter referenced **NULL**.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error occurred.<br/>                     |



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

 

 





