---
title: IVMVirtualMachine SCSIControllers property
description: The SCSIControllers property contains an enumerable collection of SCSI controllers attached to the virtual machine.
ms.assetid: 'f9830608-8418-4910-8a48-d93dba56235e'
keywords: ["SCSIControllers property Virtual Server", "SCSIControllers property Virtual Server , IVMVirtualMachine interface", "IVMVirtualMachine interface Virtual Server , SCSIControllers property", "SCSIControllers property Virtual Server , VMVirtualMachine class", "VMVirtualMachine class Virtual Server , SCSIControllers property"]
topic_type:
- apiref
api_name:
- IVMVirtualMachine.SCSIControllers
- IVMVirtualMachine.get_SCSIControllers
- VMVirtualMachine.SCSIControllers
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMVirtualMachine::SCSIControllers property

The **SCSIControllers** property contains an enumerable collection of SCSI controllers attached to the virtual machine.

This property is read-only.

## Syntax


```C++
HRESULT get_SCSIControllers(
  [out] IVMSCSIControllerCollection **scsiControllerCollection
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
<td><pre><code>VMVirtualMachine.SCSIControllers( _
  ByRef scsiControllerCollection _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The [**IVMSCSIControllerCollection**](ivmscsicontrollercollection.md) object associated with this virtual machine.

This property value is read-only.

## Error codes



| Name                                                                                          | Meaning                                                          |
|-----------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>                         |
| <dl> <dt>E\_POINTER</dt> </dl>         | The *scsiControllerCollection* parameter is **NULL**.<br/> |
| <dl> <dt>VM\_E\_VM\_UNKNOWN</dt> </dl> | The configuration is unknown.<br/>                         |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error has occurred.<br/>                     |



## Examples

The following example displays the number of SCSI controllers attached to a [**VMVirtualMachine**](ivmvirtualmachine.md) object.


```VB
Set objVS = CreateObject("VirtualServer.Application")
Set objVM = objVS.FindVirtualMachine("Windows Server 2003")
Set colSCSIs = objVM.SCSIControllers

Wscript.Echo "VM Name: " & objVM.Name
WScript.Echo "SCSI controllers: " & colSCSIs.Count
```



## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMVirtualMachine**](ivmvirtualmachine.md)
</dt> </dl>

 

 





