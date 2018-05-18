---
title: IVMVirtualMachine Notes property
description: The Notes property contains notes about the virtual machine.
ms.assetid: 'c390932c-aa0d-42bb-a90b-48b97329c427'
keywords: ["Notes property Virtual Server", "Notes property Virtual Server , IVMVirtualMachine interface", "IVMVirtualMachine interface Virtual Server , Notes property", "Notes property Virtual Server , VMVirtualMachine class", "VMVirtualMachine class Virtual Server , Notes property"]
topic_type:
- apiref
api_name:
- IVMVirtualMachine.Notes
- IVMVirtualMachine.get_Notes
- IVMVirtualMachine.put_Notes
- VMVirtualMachine.Notes
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMVirtualMachine::Notes property

The **Notes** property contains notes about the virtual machine.

This property is read/write.

## Syntax


```C++
HRESULT put_Notes(
  [in]  BSTR virtualMachineNotes
);

HRESULT get_Notes(
  [out] BSTR *virtualMachineNotes
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
<td><pre><code>VMVirtualMachine.Notes( _
  ByRef virtualMachineNotes, _
  ByVal virtualMachineNotes _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The user-defined notes about the virtual machine. The maximum length of the string is 40,000 characters.

This property value is read/write.

## Error codes



| Name                                                                                          | Meaning                                                                                              |
|-----------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>                                                             |
| <dl> <dt>E\_POINTER</dt> </dl>         | The *virtualMachineNotes* parameter is **NULL**.<br/>                                          |
| <dl> <dt>E\_INVALIDARG</dt> </dl>      | The *virtualMachineNotes* parameter is not valid or contains more than 40,000 characters.<br/> |
| <dl> <dt>VM\_E\_VM\_UNKNOWN</dt> </dl> | The configuration is unknown.<br/>                                                             |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error has occurred.<br/>                                                         |



## Remarks

Pass an empty string to remove any notes.

## Examples

The following example displays the **Notes** property value of a [**VMVirtualMachine**](ivmvirtualmachine.md) object.


```VB
Set objVS = CreateObject("VirtualServer.Application")
Set objVM = objVS. FindVirtualMachine("Windows Server 2003")

Wscript.Echo "VM Name: " & objVM.Name
WScript.Echo "Notes: " & objVM.Notes
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

 

 





