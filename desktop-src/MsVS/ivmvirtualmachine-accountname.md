---
title: IVMVirtualMachine AccountName property
description: The AccountName property contains the account name for the context in which this virtual machine will run.
ms.assetid: '38a08dcf-d4a4-48f8-8f5c-e64fe53ca6ad'
keywords: ["AccountName property Virtual Server", "AccountName property Virtual Server , IVMVirtualMachine interface", "IVMVirtualMachine interface Virtual Server , AccountName property", "AccountName property Virtual Server , VMVirtualMachine class", "VMVirtualMachine class Virtual Server , AccountName property"]
topic_type:
- apiref
api_name:
- IVMVirtualMachine.AccountName
- IVMVirtualMachine.get_AccountName
- VMVirtualMachine.AccountName
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMVirtualMachine::AccountName property

The **AccountName** property contains the account name for the context in which this virtual machine will run.

This property is read-only.

## Syntax


```C++
HRESULT get_AccountName(
  [out] BSTR *accountName
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
<td><pre><code>VMVirtualMachine.AccountName( _
  ByRef accountName _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The account name for the context in which this virtual machine will run.

This property value is read-only.

## Error codes



| Name                                                                                          | Meaning                                             |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>            |
| <dl> <dt>E\_POINTER</dt> </dl>         | The *accountName* parameter is **NULL**.<br/> |
| <dl> <dt>VM\_E\_VM\_UNKNOWN</dt> </dl> | The configuration is unknown.<br/>            |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error has occurred. <br/>       |



## Examples

The following example displays the **AccountName** property value of a [**IVMVirtualMachine**](ivmvirtualmachine.md) object.


```VB
Set objVS = CreateObject("VirtualServer.Application")
Set objVM = objVS.FindVirtualMachine("Windows Server 2003")

Wscript.Echo "VM Name: " & objVM.Name
WScript.Echo "Account name: " & objVM.AccountName
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

 

 





