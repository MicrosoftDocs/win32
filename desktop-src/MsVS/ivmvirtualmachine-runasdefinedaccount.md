---
title: IVMVirtualMachine RunAsDefinedAccount property
description: The RunAsDefinedAccount property indicates whether this virtual machine should always be run in the same account.
ms.assetid: 4605e724-c445-4a08-898e-5f88766a86ca
keywords:
- RunAsDefinedAccount property Virtual Server
- RunAsDefinedAccount property Virtual Server , IVMVirtualMachine interface
- IVMVirtualMachine interface Virtual Server , RunAsDefinedAccount property
- RunAsDefinedAccount property Virtual Server , VMVirtualMachine class
- VMVirtualMachine class Virtual Server , RunAsDefinedAccount property
topic_type:
- apiref
api_name:
- IVMVirtualMachine.RunAsDefinedAccount
- IVMVirtualMachine.get_RunAsDefinedAccount
- IVMVirtualMachine.put_RunAsDefinedAccount
- VMVirtualMachine.RunAsDefinedAccount
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

# IVMVirtualMachine::RunAsDefinedAccount property

The **RunAsDefinedAccount** property indicates whether this virtual machine should always be run in the same account.

This property is read/write.

## Syntax


```C++
HRESULT put_RunAsDefinedAccount(
  [in]  VARIANT_BOOL runAsDefinedAccountEnabled
);

HRESULT get_RunAsDefinedAccount(
  [out] VARIANT_BOOL *runAsDefinedAccountEnabled
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
<td><pre><code>VMVirtualMachine.RunAsDefinedAccount( _
  ByRef runAsDefinedAccountEnabled, _
  ByVal runAsDefinedAccountEnabled _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

Contains **vbTrue** if this virtual machine should always be run in the same account.

This property value is read/write.

## Error codes



| Name                                                                                          | Meaning                                                            |
|-----------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>                           |
| <dl> <dt>E\_POINTER</dt> </dl>         | The *runAsDefinedAccountEnabled* parameter is **NULL**.<br/> |
| <dl> <dt>VM\_E\_VM\_UNKNOWN</dt> </dl> | The configuration is unknown.<br/>                           |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error has occurred.<br/>                       |



## Examples

The following example displays the **RunAsDefinedAccount** property value of a [**VMVirtualMachine**](ivmvirtualmachine.md) object.


```VB
Set objVS = CreateObject("VirtualServer.Application")
Set objVM = objVS.FindVirtualMachine("Windows Server 2003")

Wscript.Echo "VM Name: " & objVM.Name
WScript.Echo "Run as defined account" & objVM.RunAsDefinedAccount
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

 

 





