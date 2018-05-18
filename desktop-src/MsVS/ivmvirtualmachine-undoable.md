---
title: IVMVirtualMachine Undoable property
description: The Undoable property contains TRUE if undo drives are enabled for hard disks connected to the virtual machine.
ms.assetid: 'ebebff02-0248-47c3-8d55-77629ea69d91'
keywords: ["Undoable property Virtual Server", "Undoable property Virtual Server , IVMVirtualMachine interface", "IVMVirtualMachine interface Virtual Server , Undoable property", "Undoable property Virtual Server , VMVirtualMachine class", "VMVirtualMachine class Virtual Server , Undoable property"]
topic_type:
- apiref
api_name:
- IVMVirtualMachine.Undoable
- IVMVirtualMachine.get_Undoable
- IVMVirtualMachine.put_Undoable
- VMVirtualMachine.Undoable
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMVirtualMachine::Undoable property

The **Undoable** property contains **TRUE** if undo drives are enabled for hard disks connected to the virtual machine.

This property is read/write.

## Syntax


```C++
HRESULT put_Undoable(
  [in]  VARIANT_BOOL enableUndo
);

HRESULT get_Undoable(
  [out] VARIANT_BOOL *isUndoable
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
<td><pre><code>VMVirtualMachine.Undoable( _
  ByVal enableUndo, _
  ByRef isUndoable _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

Contains **vbTrue** if undo drives should be enabled for the virtual machine.

This property value is read/write.

## Error codes



| Name                                                                                          | Meaning                                            |
|-----------------------------------------------------------------------------------------------|----------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>           |
| <dl> <dt>E\_POINTER</dt> </dl>         | The *isUndoable* parameter is **NULL**.<br/> |
| <dl> <dt>VM\_E\_VM\_UNKNOWN</dt> </dl> | The configuration is unknown.<br/>           |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error has occurred.<br/>       |



## Remarks

If undo drives are disabled, any existing undo drive files will be deleted.

You cannot set this property if the virtual machine is running or saved.

## Examples

The following example displays the **Undoable** property value of a [**VMVirtualMachine**](ivmvirtualmachine.md) object.


```VB
Set objVS = CreateObject("VirtualServer.Application")
Set objVM = objVS.FindVirtualMachine("Windows Server 2003")

WScript.Echo "VM Name: " & objVM.Name
WScript.Echo "Undoable: " & objVM.Undoable
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

 

 





