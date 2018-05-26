---
title: IVMVirtualMachine SavedStateFilePath property
description: The SavedStateFilePath property contains the path to the saved state file.
ms.assetid: 72e1e803-f8bb-430b-b9aa-21008cdcd830
keywords:
- SavedStateFilePath property Virtual Server
- SavedStateFilePath property Virtual Server , IVMVirtualMachine interface
- IVMVirtualMachine interface Virtual Server , SavedStateFilePath property
- SavedStateFilePath property Virtual Server , VMVirtualMachine class
- VMVirtualMachine class Virtual Server , SavedStateFilePath property
topic_type:
- apiref
api_name:
- IVMVirtualMachine.SavedStateFilePath
- IVMVirtualMachine.get_SavedStateFilePath
- VMVirtualMachine.SavedStateFilePath
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

# IVMVirtualMachine::SavedStateFilePath property

The **SavedStateFilePath** property contains the path to the saved state file.

This property is read-only.

## Syntax


```C++
HRESULT get_SavedStateFilePath(
  [out] BSTR *savedStateFilePath
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
<td><pre><code>VMVirtualMachine.SavedStateFilePath( _
  ByRef savedStateFilePath _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The fully qualified path to the virtual machine's saved state file.

This property value is read-only.

## Error codes



| Name                                                                                                   | Meaning                                                            |
|--------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>                       | The operation was successful.<br/>                           |
| <dl> <dt>E\_POINTER</dt> </dl>                  | The *savedStateFilePath* parameter is **NULL**.<br/>         |
| <dl> <dt>VM\_E\_VM\_UNKNOWN</dt> </dl>          | The configuration is unknown.<br/>                           |
| <dl> <dt>VM\_E\_VM\_NO\_SAVED\_STATE</dt> </dl> | The virtual machine has no associated saved state file.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl>          | An unexpected error has occurred.<br/>                       |



## Examples

The following example displays the SavedStateFilePath property value of a [**VMVirtualMachine**](ivmvirtualmachine.md) object.


```VB
Set objVS = CreateObject("VirtualServer.Application")
Set objVM = objVS.FindVirtualMachine("Windows Server 2003")

WScript.Echo "VM Name: " & objVM.Name
If objVM.SavedStateFilePath = 0 Then
  WScript.Echo "Saved state file path: [null]"
Else
  WScript.Echo "Saved state file path" & objVM.SavedStateFilePath
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

[**IVMVirtualMachine**](ivmvirtualmachine.md)
</dt> </dl>

 

 





