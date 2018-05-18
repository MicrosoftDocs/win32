---
title: IVMHardDisk File property
description: The File property contains the full path name of the current hard disk image file.
ms.assetid: 'f2cbbe12-84cf-4a6c-8269-28f88147cc55'
keywords: ["File property Virtual Server", "File property Virtual Server , IVMHardDisk interface", "IVMHardDisk interface Virtual Server , File property", "File property Virtual Server , VMHardDisk interface", "VMHardDisk interface Virtual Server , File property"]
topic_type:
- apiref
api_name:
- IVMHardDisk.File
- IVMHardDisk.get_File
- VMHardDisk.File
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMHardDisk::File property

The **File** property contains the full path name of the current hard disk image file.

This property is read-only.

## Syntax


```C++
HRESULT get_File(
  [out] BSTR *hardDiskName
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
<td><pre><code>VMHardDisk.File( _
  ByRef hardDiskName _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The full path name of the current hard disk image file.

This property value is read-only.

## Error codes



| Name                                                                                           | Meaning                                  |
|------------------------------------------------------------------------------------------------|------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>               | The operation was successful.<br/> |
| <dl> <dt>E\_POINTER</dt> </dl>          | The parameter is **NULL**.<br/>    |
| <dl> <dt> DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error occurred.<br/> |



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

 

 





