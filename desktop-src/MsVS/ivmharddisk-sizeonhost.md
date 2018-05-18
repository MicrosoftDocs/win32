---
title: IVMHardDisk SizeOnHost property
description: The SizeOnHost property contains the size, in bytes, of the hard disk image file on the host computer.
ms.assetid: '2d5ebfe2-79ea-46a9-bdd2-f61381b54e23'
keywords: ["SizeOnHost property Virtual Server", "SizeOnHost property Virtual Server , IVMHardDisk interface", "IVMHardDisk interface Virtual Server , SizeOnHost property", "SizeOnHost property Virtual Server , VMHardDisk interface", "VMHardDisk interface Virtual Server , SizeOnHost property"]
topic_type:
- apiref
api_name:
- IVMHardDisk.SizeOnHost
- IVMHardDisk.get_SizeOnHost
- VMHardDisk.SizeOnHost
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMHardDisk::SizeOnHost property

The **SizeOnHost** property contains the size, in bytes, of the hard disk image file on the host computer.

This property is read-only.

## Syntax


```C++
HRESULT get_SizeOnHost(
  [out] VARIANT *fileSize
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
<td><pre><code>VMHardDisk.SizeOnHost( _
  ByRef fileSize _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The size, in bytes, of the hard disk image file on the host computer. The number is returned as a **Decimal** value.

This property value is read-only.

## Error codes



| Name                                                                                          | Meaning                                  |
|-----------------------------------------------------------------------------------------------|------------------------------------------|
| <dl> <dt> S\_OK</dt> </dl>             | The operation was successful.<br/> |
| <dl> <dt>E\_POINTER</dt> </dl>         | The parameter is **NULL**.<br/>    |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error occurred.<br/> |



## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMHardDisk**](ivmharddisk.md)
</dt> </dl>

 

 





