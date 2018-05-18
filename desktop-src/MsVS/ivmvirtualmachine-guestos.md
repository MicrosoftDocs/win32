---
title: IVMVirtualMachine GuestOS property
description: The GuestOS property contains the guest operating system for this virtual machine.
ms.assetid: '4f3c2f7b-3919-43bf-ac6b-1ddbc78605aa'
keywords: ["GuestOS property Virtual Server", "GuestOS property Virtual Server , IVMVirtualMachine interface", "IVMVirtualMachine interface Virtual Server , GuestOS property", "GuestOS property Virtual Server , VMVirtualMachine object", "VMVirtualMachine object Virtual Server , GuestOS property"]
topic_type:
- apiref
api_name:
- IVMVirtualMachine.GuestOS
- IVMVirtualMachine.get_GuestOS
- VMVirtualMachine.GuestOS
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMVirtualMachine::GuestOS property

The **GuestOS** property contains the guest operating system for this virtual machine.

This property is read-only.

## Syntax


```C++
HRESULT get_GuestOS(
  [out] IVMGuestOS **guestOS
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
<td><pre><code>VMVirtualMachine.GuestOS( _
  ByRef guestOS _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The [**VMGuestOS**](ivmguestos.md) object associated with this virtual machine.

This property value is read-only.

## Error codes



| Name                                                                                          | Meaning                                         |
|-----------------------------------------------------------------------------------------------|-------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>        |
| <dl> <dt>E\_POINTER</dt> </dl>         | The *guestOS* parameter is **NULL**.<br/> |
| <dl> <dt>VM\_E\_VM\_UNKNOWN</dt> </dl> | The configuration is unknown.<br/>        |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error has occurred.<br/>    |



## Examples

The following example displays the name of the guest operating system installed in a [**VMVirtualMachine**](ivmvirtualmachine.md) object.


```VB
Set objVS = CreateObject("VirtualServer.Application")
Set objVM = objVS.FindVirtualMachine("Windows Server 2003")
Set objGuest = objVM.GuestOS

Wscript.Echo "VM Name: " & objVM.Name
If objGuest.Name = 0 Then
  WScript.Echo "Operating System: [none]"
Else
  WScript.Echo "Operating System: " & objGuest.Name
End If
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

 

 





