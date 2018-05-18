---
title: IVMHardDiskConnection UndoHardDisk property
description: The UndoHardDisk property contains an IVMHardDisk object corresponding to this connection's undo hard disk image.
ms.assetid: '541659aa-006b-4604-a0c1-45038b63a615'
keywords: ["UndoHardDisk property Virtual Server", "UndoHardDisk property Virtual Server , IVMHardDiskConnection interface", "IVMHardDiskConnection interface Virtual Server , UndoHardDisk property", "UndoHardDisk property Virtual Server , VMHardDiskConnection interface", "VMHardDiskConnection interface Virtual Server , UndoHardDisk property"]
topic_type:
- apiref
api_name:
- IVMHardDiskConnection.UndoHardDisk
- IVMHardDiskConnection.get_UndoHardDisk
- VMHardDiskConnection.UndoHardDisk
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMHardDiskConnection::UndoHardDisk property

The **UndoHardDisk** property contains an [**IVMHardDisk**](ivmharddisk.md) object corresponding to this connection's undo hard disk image.

This property is read-only.

## Syntax


```C++
HRESULT get_UndoHardDisk(
  [out] IVMHardDisk **undoHardDisk
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
<td><pre><code>VMHardDiskConnection.UndoHardDisk( _
  ByRef undoHardDisk _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

Contains a [**VMHardDisk**](ivmharddisk.md) object that describes the undo hard disk associated with this connection.

This property value is read-only.

## Error codes



| Name                                                                                                    | Meaning                                                                                                                                     |
|---------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt> S\_OK</dt> </dl>                       | The operation was successful.<br/>                                                                                                    |
| <dl> <dt>E\_POINTER</dt> </dl>                   | The *undoHardDisk* parameter is **NULL** or invalid.<br/>                                                                             |
| <dl> <dt>VM\_E\_VM\_UNKNOWN</dt> </dl>           | The current virtual machine configuration is invalid.<br/>                                                                            |
| <dl> <dt>VM\_E\_DRIVE\_INVALID</dt> </dl>        | The bus location for this connection has not been properly initialized, or the device at this location is not a valid hard disk.<br/> |
| <dl> <dt>VM\_E\_HD\_IMAGE\_NOT\_FOUND</dt> </dl> | The undo hard disk image associated with this connection was not found.<br/>                                                          |
| <dl> <dt> DISP\_E\_EXCEPTION</dt> </dl>          | An unexpected error occurred.<br/>                                                                                                    |



## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMHardDiskConnection**](ivmharddiskconnection.md)
</dt> </dl>

 

 





