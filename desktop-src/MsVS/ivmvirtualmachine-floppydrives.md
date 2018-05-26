---
title: IVMVirtualMachine FloppyDrives property
description: The FloppyDrives property contains an enumerable collection of floppy drives attached to the virtual machine.
ms.assetid: 27740f6e-0f6d-4094-a17e-9e4e9846aa2f
keywords:
- FloppyDrives property Virtual Server
- FloppyDrives property Virtual Server , IVMVirtualMachine interface
- IVMVirtualMachine interface Virtual Server , FloppyDrives property
- FloppyDrives property Virtual Server , VMVirtualMachine class
- VMVirtualMachine class Virtual Server , FloppyDrives property
topic_type:
- apiref
api_name:
- IVMVirtualMachine.FloppyDrives
- IVMVirtualMachine.get_FloppyDrives
- VMVirtualMachine.FloppyDrives
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

# IVMVirtualMachine::FloppyDrives property

The **FloppyDrives** property contains an enumerable collection of floppy drives attached to the virtual machine.

This property is read-only.

## Syntax


```C++
HRESULT get_FloppyDrives(
  [out] IVMFloppyDriveCollection **floppyCollection
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
<td><pre><code>VMVirtualMachine.FloppyDrives( _
  ByRef floppyCollection _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The [**IVMFloppyDriveCollection**](ivmfloppydrivecollection.md) object associated with this virtual machine.

This property value is read-only.

## Error codes



| Name                                                                                          | Meaning                                                  |
|-----------------------------------------------------------------------------------------------|----------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>                 |
| <dl> <dt>E\_POINTER</dt> </dl>         | The *floppyCollection* parameter is **NULL**.<br/> |
| <dl> <dt>VM\_E\_VM\_UNKNOWN</dt> </dl> | The configuration is unknown.<br/>                 |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error has occurred.<br/>             |



## Examples

The following example displays the number of floppy disc drives attached to a [**VMVirtualMachine**](ivmvirtualmachine.md) object.


```VB
Set objVS = CreateObject("VirtualServer.Application")
Set objVM = objVS.FindVirtualMachine("Windows Server 2003")
Set colFDs = objVM.FloppyDrives

Wscript.Echo "VM Name: " & objVM.Name
WScript.Echo "Floppy disc drives installed: " & colFDs.Count
```



## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMVirtualMachine**](ivmvirtualmachine.md)
</dt> </dl>

 

 





