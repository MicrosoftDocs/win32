---
title: IVMVirtualServer VirtualMachines property
description: The VirtualMachines property contains a collection of IVMVirtualMachine objects.
ms.assetid: 72ae8a70-c4f3-417a-b29f-7a94e087e118
keywords:
- VirtualMachines property Virtual Server
- VirtualMachines property Virtual Server , IVMVirtualServer interface
- IVMVirtualServer interface Virtual Server , VirtualMachines property
- VirtualMachines property Virtual Server , VMVirtualServer class
- VMVirtualServer class Virtual Server , VirtualMachines property
topic_type:
- apiref
api_name:
- IVMVirtualServer.VirtualMachines
- IVMVirtualServer.get_VirtualMachines
- VMVirtualServer.VirtualMachines
api_location:
- VsComInterfaces.h
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IVMVirtualServer::VirtualMachines property

The **VirtualMachines** property contains a collection of [**IVMVirtualMachine**](ivmvirtualmachine.md) objects.

This property is read-only.

## Syntax


```C++
HRESULT get_VirtualMachines(
  [out] IVMVirtualMachineCollection **virtualMachineCollection
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
<td><pre><code>VMVirtualServer.VirtualMachines( _
  ByRef virtualMachineCollection _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The [**IVMVirtualMachineCollection**](ivmvirtualmachinecollection.md) object associated with Virtual Server.

This property value is read-only.

## Error codes



| Name                                                                                          | Meaning                                            |
|-----------------------------------------------------------------------------------------------|----------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>           |
| <dl> <dt>E\_POINTER</dt> </dl>         | *virtualMachineCollection* is **NULL**.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error occurred.<br/>           |



## Examples

The following example displays properties of the **VirtualMachines** object associated with the [**VMVirtualServer**](ivmvirtualserver.md) object.


```VB
Set objVS = CreateObject("VirtualServer.Application")
Wscript.Echo "Name: " & objVS.Name

Set objVMColl = objVS.VirtualMachines
If objVMColl.Count = 0 Then
  Wscript.Echo "    Virtual machines: [none]"
Else
  Wscript.Echo "Virtual machines: " & objVMColl.Count
  For Each objVM in objVMColl
    Wscript.Echo "    Name: " & objVM.Name
  Next
End If
```



## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMVirtualServer**](ivmvirtualserver.md)
</dt> </dl>

 

 





