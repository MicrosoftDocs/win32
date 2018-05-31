---
title: IVMVirtualMachine State property
description: Contains the current state of the virtual machine.
ms.assetid: 897f19d2-c5f0-4004-8bf6-4343a421d5b9
keywords:
- State property Virtual Server
- State property Virtual Server , IVMVirtualMachine interface
- IVMVirtualMachine interface Virtual Server , State property
- State property Virtual Server , VMVirtualMachine class
- VMVirtualMachine class Virtual Server , State property
topic_type:
- apiref
api_name:
- IVMVirtualMachine.State
- IVMVirtualMachine.get_State
- VMVirtualMachine.State
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

# IVMVirtualMachine::State property

The **State** property contains the current state of the virtual machine.

This property is read-only.

## Syntax


```C++
HRESULT get_State(
  [out] VMVMState *virtualMachineState
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
<td><pre><code>VMVirtualMachine.State( _
  ByRef virtualMachineState _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The current state of the virtual machine.

This property value is read-only.

## Error codes



| Name                                                                                          | Meaning                                                     |
|-----------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>                    |
| <dl> <dt>E\_POINTER</dt> </dl>         | The *virtualMachineState* parameter is **NULL**.<br/> |
| <dl> <dt>VM\_E\_VM\_UNKNOWN</dt> </dl> | The configuration is unknown.<br/>                    |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error has occurred.<br/>                |



## Examples

The following example displays the **State** property value of a [**VMVirtualMachine**](ivmvirtualmachine.md) object.


```VB
Set objVS = CreateObject("VirtualServer.Application")
Set objVM = objVS.FindVirtualMachine("Windows Server 2003")

Wscript.Echo "VM Name: " & objVM.Name
WScript.Echo "State: " & objVM.State
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
</dt> <dt>

[**VMVMState**](vmvmstate.md)
</dt> </dl>

 

 





