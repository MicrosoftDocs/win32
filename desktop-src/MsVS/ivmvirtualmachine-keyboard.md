---
title: IVMVirtualMachine Keyboard property
description: The Keyboard property contains the keyboard device for the virtual machine.
ms.assetid: c856c54d-45ed-442b-b72a-7aaf57631162
keywords:
- Keyboard property Virtual Server
- Keyboard property Virtual Server , IVMVirtualMachine interface
- IVMVirtualMachine interface Virtual Server , Keyboard property
- Keyboard property Virtual Server , VMVirtualMachine class
- VMVirtualMachine class Virtual Server , Keyboard property
topic_type:
- apiref
api_name:
- IVMVirtualMachine.Keyboard
- IVMVirtualMachine.get_Keyboard
- VMVirtualMachine.Keyboard
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

# IVMVirtualMachine::Keyboard property

The **Keyboard** property contains the keyboard device for the virtual machine.

This property is read-only.

## Syntax


```C++
HRESULT get_Keyboard(
  [out] IVMKeyboard **keyboard
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
<td><pre><code>VMVirtualMachine.Keyboard( _
  ByRef keyboard _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The [**VMKeyboard**](ivmkeyboard.md) object associated with this virtual machine.

This property value is read-only.

## Error codes



| Name                                                                                          | Meaning                                          |
|-----------------------------------------------------------------------------------------------|--------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>         |
| <dl> <dt>E\_POINTER</dt> </dl>         | The *keyboard* parameter is **NULL**.<br/> |
| <dl> <dt>VM\_E\_VM\_UNKNOWN</dt> </dl> | The configuration is unknown.<br/>         |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error has occurred.<br/>     |



## Examples

The following example accesses the [**VMKeyboard**](ivmkeyboard.md) object of a [**VMVirtualMachine**](ivmvirtualmachine.md) object and sends a text string to the VM.


```VB
Set objVS = CreateObject("VirtualServer.Application")
Set objVM = objVS.FindVirtualMachine("Windows Server 2003")
Set objKeyboard = objVM.Keyboard

Wscript.Echo "VM Name: " & objVM.Name
Wscript.Echo "  Sending Hello World"
objKeyboard.TypeAsciiText("Hello World")
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

 

 





