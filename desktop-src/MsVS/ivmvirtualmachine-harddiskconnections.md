---
title: IVMVirtualMachine HardDiskConnections property
description: The HardDiskConnections property contains an enumerable collection of hard disk connections.
ms.assetid: bb82e59c-ec29-4240-8d9f-4ce4e18a5489
keywords:
- HardDiskConnections property Virtual Server
- HardDiskConnections property Virtual Server , IVMVirtualMachine interface
- IVMVirtualMachine interface Virtual Server , HardDiskConnections property
- HardDiskConnections property Virtual Server , VMVirtualMachine class
- VMVirtualMachine class Virtual Server , HardDiskConnections property
topic_type:
- apiref
api_name:
- IVMVirtualMachine.HardDiskConnections
- IVMVirtualMachine.get_HardDiskConnections
- VMVirtualMachine.HardDiskConnections
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

# IVMVirtualMachine::HardDiskConnections property

The **HardDiskConnections** property contains an enumerable collection of hard disk connections.

This property is read-only.

## Syntax


```C++
HRESULT get_HardDiskConnections(
  [out] IVMHardDiskConnectionCollection **hardDiskConnectionCollection
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
<td><pre><code>VMVirtualMachine.HardDiskConnections( _
  ByRef hardDiskConnectionCollection _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The [**IVMHardDiskConnectionCollection**](ivmharddiskconnectioncollection.md) object associated with this virtual machine.

This property value is read-only.

## Error codes



| Name                                                                                          | Meaning                                                              |
|-----------------------------------------------------------------------------------------------|----------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>                             |
| <dl> <dt>E\_POINTER</dt> </dl>         | The *hardDiskConnectionCollection* parameter is **NULL**.<br/> |
| <dl> <dt>VM\_E\_VM\_UNKNOWN</dt> </dl> | The configuration is unknown.<br/>                             |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error has occurred.<br/>                         |



## Examples

The following example displays the number of hard disk connections attached to a [**VMVirtualMachine**](ivmvirtualmachine.md) object.


```VB
Set objVS = CreateObject("VirtualServer.Application")
Set objVM = objVS.FindVirtualMachine("Windows Server 2003")
Set colHDs = objVM.HardDiskConnections

Wscript.Echo "VM Name: " & objVM.Name
WScript.Echo "Hard disc connections: " & colHDs.Count
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

 

 





