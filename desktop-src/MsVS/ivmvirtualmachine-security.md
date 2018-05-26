---
title: IVMVirtualMachine Security property
description: The IVMSecurity object associated with this virtual machine.
ms.assetid: 9db25ce3-fad2-4aed-838e-70caefee7e0f
keywords:
- Security property Virtual Server
- Security property Virtual Server , IVMVirtualMachine interface
- IVMVirtualMachine interface Virtual Server , Security property
- Security property Virtual Server , VMVirtualMachine class
- VMVirtualMachine class Virtual Server , Security property
topic_type:
- apiref
api_name:
- IVMVirtualMachine.Security
- IVMVirtualMachine.get_Security
- VMVirtualMachine.Security
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

# IVMVirtualMachine::Security property

The [**IVMSecurity**](ivmsecurity.md) object associated with this virtual machine.

This property is read-only.

## Syntax


```C++
HRESULT get_Security(
  [out] IVMSecurity **outSecurity
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
<td><pre><code>VMVirtualMachine.Security( _
  ByRef outSecurity _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

An [**VMSecurity**](ivmsecurity.md) instance that represents the security attributes of this virtual machine.

This property value is read-only.

## Error codes



| Name                                                                                          | Meaning                                                           |
|-----------------------------------------------------------------------------------------------|-------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>                          |
| <dl> <dt>E\_POINTER</dt> </dl>         | The *outSecurity* parameter is **NULL**.<br/>               |
| <dl> <dt>E\_OUTOFMEMORY</dt> </dl>     | Could not allocate memory for the security descriptor.<br/> |
| <dl> <dt>VM\_E\_VM\_UNKNOWN</dt> </dl> | The configuration is unknown.<br/>                          |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error has occurred.<br/>                      |



## Examples

The following example displays [**VMSecurity**](ivmsecurity.md) properties of a [**VMVirtualMachine**](ivmvirtualmachine.md) object.


```VB
Set objVS = CreateObject("VirtualServer.Application")
Set objVM = objVS.FindVirtualMachine("Windows Server 2003")
Set objSec = objVM.Security

WScript.Echo "VM Name: " & objVM.Name
WScript.Echo "Security principle: "
WScript.Echo "    Owner Name: " & objSec.OwnerName
WScript.Echo "    Owner SID: " & objSec.OwnerSID
WScript.Echo "    Group Name: " & objSec.GroupName
WScript.Echo "    Group SID: " & objSec.GroupSID
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

 

 





