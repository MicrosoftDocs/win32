---
title: IVMAccountant DiskBytesWritten property
description: The DiskBytesWritten property contains the total number of bytes written by all IDE and SCSI controllers for this virtual machine.
ms.assetid: 1b5a0603-14ac-426e-b55f-945db521171a
keywords:
- DiskBytesWritten property Virtual Server
- DiskBytesWritten property Virtual Server , IVMAccountant interface
- IVMAccountant interface Virtual Server , DiskBytesWritten property
- DiskBytesWritten property Virtual Server , VMAccountant interface
- VMAccountant interface Virtual Server , DiskBytesWritten property
topic_type:
- apiref
api_name:
- IVMAccountant.DiskBytesWritten
- IVMAccountant.get_DiskBytesWritten
- VMAccountant.DiskBytesWritten
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

# IVMAccountant::DiskBytesWritten property

The **DiskBytesWritten** property contains the total number of bytes written by all IDE and SCSI controllers for this virtual machine.

This property is read-only.

## Syntax


```C++
HRESULT get_DiskBytesWritten(
  [out] VARIANT *bytesWritten
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
<td><pre><code>VMAccountant.DiskBytesWritten( _
  ByRef bytesWritten _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The total number of bytes written by all IDE and SCSI controllers for this virtual machine. The number is returned as a **Decimal** value.

This property value is read-only.

## Error codes



| Name                                                                                          | Meaning                                        |
|-----------------------------------------------------------------------------------------------|------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>       |
| <dl> <dt>E\_POINTER</dt> </dl>         | *bytesWritten* is **NULL**.<br/>         |
| <dl> <dt>S\_FALSE</dt> </dl>           | The virtual machine is not running.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error occurred.<br/>       |



## Remarks

Note that disk I/O statistics are reset to zero when a virtual machine is powered up, reset, or restored from saved state.

## Examples

The following example prints the DiskBytesWritten property information for each virtual machine.


```VB
Set objVS = CreateObject("VirtualServer.Application")
set colVMs = objVS.VirtualMachines

For Each objVM in colVMS
    Set colAccountants = objVM.Accountant
        Wscript.Echo "Virtual machine: " & objVM.Name
        Wscript.Echo "Disk bytes written: " & colAccountants.DiskBytesWritten
        Wscript.Echo
Next
```



## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMAccountant**](ivmaccountant.md)
</dt> </dl>

 

 





