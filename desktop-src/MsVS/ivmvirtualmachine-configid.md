---
title: IVMVirtualMachine ConfigID property
description: The ConfigID property contains the unique ID that identifies the virtual machine.
ms.assetid: 7783b8ae-d025-4bd9-86e4-48462415562f
keywords:
- ConfigID property Virtual Server
- ConfigID property Virtual Server , IVMVirtualMachine interface
- IVMVirtualMachine interface Virtual Server , ConfigID property
- ConfigID property Virtual Server , VMVirtualMachine class
- VMVirtualMachine class Virtual Server , ConfigID property
topic_type:
- apiref
api_name:
- IVMVirtualMachine.ConfigID
- IVMVirtualMachine.get_ConfigID
- VMVirtualMachine.ConfigID
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

# IVMVirtualMachine::ConfigID property

The **ConfigID** property contains the unique ID that identifies the virtual machine.

This property is read-only.

## Syntax


```C++
HRESULT get_ConfigID(
  [out] BSTR *virtualMachineConfigID
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
<td><pre><code>VMVirtualMachine.ConfigID( _
  ByRef virtualMachineConfigID _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The unique ID that identifies the virtual machine.

This property value is read-only.

## Error codes



| Name                                                                                          | Meaning                                                        |
|-----------------------------------------------------------------------------------------------|----------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>                       |
| <dl> <dt>E\_POINTER</dt> </dl>         | The *virtualMachineConfigID* parameter is **NULL**.<br/> |
| <dl> <dt>VM\_E\_VM\_UNKNOWN</dt> </dl> | The configuration is unknown.<br/>                       |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error has occurred.<br/>                   |



## Examples

The following example displays the **ConfigID** property value of a [**VMVirtualMachine**](ivmvirtualmachine.md) object.


```VB
Set objVS = CreateObject("VirtualServer.Application")
Set objVM = objVS.FindVirtualMachine("Windows Server 2003")

Wscript.Echo "VM Name: " & objVM.Name
WScript.Echo "Configuration ID: " & objVM.ConfigID
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

 

 





