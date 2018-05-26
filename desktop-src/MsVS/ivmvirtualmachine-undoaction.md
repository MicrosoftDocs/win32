---
title: IVMVirtualMachine UndoAction property
description: The UndoAction property contains the default action to be performed on all undo drives when the virtual machine is shut down from within the guest operating system.
ms.assetid: b8cef869-fb3b-4d71-b49e-6e5d19075779
keywords:
- UndoAction property Virtual Server
- UndoAction property Virtual Server , IVMVirtualMachine interface
- IVMVirtualMachine interface Virtual Server , UndoAction property
- UndoAction property Virtual Server , VMVirtualMachine class
- VMVirtualMachine class Virtual Server , UndoAction property
topic_type:
- apiref
api_name:
- IVMVirtualMachine.UndoAction
- IVMVirtualMachine.get_UndoAction
- IVMVirtualMachine.put_UndoAction
- VMVirtualMachine.UndoAction
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

# IVMVirtualMachine::UndoAction property

The **UndoAction** property contains the default action to be performed on all undo drives when the virtual machine is shut down from within the guest operating system.

This property is read/write.

## Syntax


```C++
HRESULT put_UndoAction(
  [in]  VMUndoAction undoAction
);

HRESULT get_UndoAction(
  [out] VMUndoAction *undoAction
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
<td><pre><code>VMVirtualMachine.UndoAction( _
  ByRef undoAction, _
  ByVal undoAction _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The default action to be performed on all undo drives when the virtual machine is shut down from within the guest operating system.

This property value is read/write.

## Error codes



| Name                                                                                          | Meaning                                             |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>            |
| <dl> <dt>E\_POINTER</dt> </dl>         | The *undoAction* parameter is **NULL**.<br/>  |
| <dl> <dt>E\_INVALIDARG</dt> </dl>      | The *undoAction* parameter is not valid.<br/> |
| <dl> <dt>VM\_E\_VM\_UNKNOWN</dt> </dl> | The configuration is unknown.<br/>            |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error has occurred.<br/>        |



## Remarks

See the [**VMUndoAction**](vmundoaction.md) enumeration for descriptions of the allowable *undoAction* values.

## Examples

The following example displays the **UndoAction** property value of a [**VMVirtualMachine**](ivmvirtualmachine.md) object.


```VB
Set objVS = CreateObject("VirtualServer.Application")
Set objVM = objVS.FindVirtualMachine("Windows Server 2003")

WScript.Echo "VM Name: " & objVM.Name
WScript.Echo "Undo action: " & objVM.UndoAction
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

[**VMUndoAction**](vmundoaction.md)
</dt> </dl>

 

 





