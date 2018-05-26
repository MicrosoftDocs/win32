---
title: IVMHardDisk Type property
description: The Type property contains the type of the current hard disk image.
ms.assetid: be1b3612-d115-4d86-aa1d-ebe48d29037d
keywords:
- Type property Virtual Server
- Type property Virtual Server , IVMHardDisk interface
- IVMHardDisk interface Virtual Server , Type property
- Type property Virtual Server , VMHardDisk interface
- VMHardDisk interface Virtual Server , Type property
topic_type:
- apiref
api_name:
- IVMHardDisk.Type
- IVMHardDisk.get_Type
- VMHardDisk.Type
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

# IVMHardDisk::Type property

The **Type** property contains the type of the current hard disk image.

This property is read-only.

## Syntax


```C++
HRESULT get_Type(
  [out] VMHardDiskType *type
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
<td><pre><code>VMHardDisk.Type( _
  ByRef type _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The type of the current hard disk image.

This property value is read-only.

## Error codes



| Name                                                                                                    | Meaning                                                                                   |
|---------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>                        | The operation was successful.<br/>                                                  |
| <dl> <dt>E\_POINTER</dt> </dl>                   | The parameter is **NULL**.<br/>                                                     |
| <dl> <dt>E\_FILE\_NOT\_FOUND</dt> </dl>          | The current hard disk image file could not be found.<br/>                           |
| <dl> <dt> VM\_E\_PREF\_READ\_ERROR</dt> </dl>    | The preferences for the current hard disk image could not be read.<br/>             |
| <dl> <dt>VM\_E\_DRIVE\_INVALID</dt> </dl>        | The type of the current hard disk image is invalid.<br/>                            |
| <dl> <dt>VM\_E\_HD\_IMAGE\_OPEN\_FAIL</dt> </dl> | An error occurred while attempting to open the current hard disk image file.<br/>   |
| <dl> <dt> VM\_E\_HD\_IMAGE\_ACCESS</dt> </dl>    | An error occurred while attempting to access the current hard disk image file.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl>           | An unexpected error occurred.<br/>                                                  |



## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMHardDisk**](ivmharddisk.md)
</dt> <dt>

[**VMHardDiskType**](vmharddisktype.md)
</dt> </dl>

 

 





