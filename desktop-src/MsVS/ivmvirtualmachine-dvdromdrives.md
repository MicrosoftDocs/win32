---
title: IVMVirtualMachine DVDROMDrives property
description: The DVDROMDrives property contains an enumerable collection of CD/DVD-ROM drives attached to the virtual machine.
ms.assetid: 65f4fd02-5c33-4f1f-b088-278becb4e0b8
keywords:
- DVDROMDrives property Virtual Server
- DVDROMDrives property Virtual Server , IVMVirtualMachine interface
- IVMVirtualMachine interface Virtual Server , DVDROMDrives property
- DVDROMDrives property Virtual Server , VMVirtualMachine class
- VMVirtualMachine class Virtual Server , DVDROMDrives property
topic_type:
- apiref
api_name:
- IVMVirtualMachine.DVDROMDrives
- IVMVirtualMachine.get_DVDROMDrives
- VMVirtualMachine.DVDROMDrives
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

# IVMVirtualMachine::DVDROMDrives property

The **DVDROMDrives** property contains an enumerable collection of CD/DVD-ROM drives attached to the virtual machine.

This property is read-only.

## Syntax


```C++
HRESULT get_DVDROMDrives(
  [out] IVMDVDDriveCollection **dvdROMCollection
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
<td><pre><code>VMVirtualMachine.DVDROMDrives( _
  ByRef dvdROMCollection _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The [**IVMDVDDriveCollection**](ivmdvddrivecollection.md) object associated with this virtual machine.

This property value is read-only.

## Error codes



| Name                                                                                          | Meaning                                                  |
|-----------------------------------------------------------------------------------------------|----------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>                 |
| <dl> <dt>E\_POINTER</dt> </dl>         | The *dvdROMCollection* parameter is **NULL**.<br/> |
| <dl> <dt>VM\_E\_VM\_UNKNOWN</dt> </dl> | The configuration is unknown.<br/>                 |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error has occurred.<br/>             |



## Examples

The following example displays the number of DVD drives attached to a [**VMVirtualMachine**](ivmvirtualmachine.md) object.


```VB
Set objVS = CreateObject("VirtualServer.Application")
Set objVM = objVS.FindVirtualMachine("Windows Server 2003")
Set colDVDs = objVM.DVDROMDrives

Wscript.Echo "VM Name: " & objVM.Name
WScript.Echo "DVD/CDROM disc drives installed: " & colDVDs.Count
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

 

 





