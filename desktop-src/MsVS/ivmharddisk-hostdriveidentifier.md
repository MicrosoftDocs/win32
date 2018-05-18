---
title: IVMHardDisk HostDriveIdentifier property
description: The HostDriveIdentifier property contains a string that identifies the host drive linked to by this virtual hard disk image.
ms.assetid: 'bfe17e0d-0b83-46a9-80f5-97da6c61265e'
keywords: ["HostDriveIdentifier property Virtual Server", "HostDriveIdentifier property Virtual Server , IVMHardDisk interface", "IVMHardDisk interface Virtual Server , HostDriveIdentifier property", "HostDriveIdentifier property Virtual Server , VMHardDisk interface", "VMHardDisk interface Virtual Server , HostDriveIdentifier property"]
topic_type:
- apiref
api_name:
- IVMHardDisk.HostDriveIdentifier
- IVMHardDisk.get_HostDriveIdentifier
- VMHardDisk.HostDriveIdentifier
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMHardDisk::HostDriveIdentifier property

The **HostDriveIdentifier** property contains a string that identifies the host drive linked to by this virtual hard disk image.

This property is read-only.

## Syntax


```C++
HRESULT get_HostDriveIdentifier(
  [out] BSTR *hostDriveIdentifier
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
<td><pre><code>VMHardDisk.HostDriveIdentifier( _
  ByRef hostDriveIdentifier _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The host drive identifier.

This property value is read-only.

## Error codes



| Name                                                                                                       | Meaning                                                                                   |
|------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| <dl> <dt> S\_OK</dt> </dl>                          | The operation was successful.<br/>                                                  |
| <dl> <dt> E\_POINTER</dt> </dl>                     | The parameter is **NULL**.<br/>                                                     |
| <dl> <dt>S\_FALSE</dt> </dl>                        | The hard disk image type is invalid for this operation.<br/>                        |
| <dl> <dt>E\_FILE\_NOT\_FOUND</dt> </dl>             | The current virtual hard disk could not be located.<br/>                            |
| <dl> <dt> VM\_E\_HOST\_DRIVE\_NOT\_FOUND</dt> </dl> | The host drive linked to by this virtual hard disk image could not be found.<br/>   |
| <dl> <dt>VM\_E\_HD\_IMAGE\_OPEN\_FAIL</dt> </dl>    | The current hard disk image could not be opened.<br/>                               |
| <dl> <dt>VM\_E\_HD\_IMAGE\_ACCESS</dt> </dl>        | An error occurred while attempting to access the current hard disk image file.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl>              | An unexpected error occurred.<br/>                                                  |



## Remarks

This property should be called only on a host drive virtual hard disk image.

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

 

 





