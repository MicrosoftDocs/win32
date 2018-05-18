---
title: IVMVirtualMachine Name property
description: The Name property contains the name of the virtual machine configuration.
ms.assetid: 'feb2eff6-cccd-4399-b72d-d4cb414301bb'
keywords: ["Name property Virtual Server", "Name property Virtual Server , IVMVirtualMachine interface", "IVMVirtualMachine interface Virtual Server , Name property", "Name property Virtual Server , VMVirtualMachine class", "VMVirtualMachine class Virtual Server , Name property"]
topic_type:
- apiref
api_name:
- IVMVirtualMachine.Name
- IVMVirtualMachine.get_Name
- IVMVirtualMachine.put_Name
- VMVirtualMachine.Name
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMVirtualMachine::Name property

The **Name** property contains the name of the virtual machine configuration.

This property is read/write.

## Syntax


```C++
HRESULT put_Name(
  [in]  BSTR virtualMachineName
);

HRESULT get_Name(
  [out] BSTR *virtualMachineName
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
<td><pre><code>VMVirtualMachine.Name( _
  ByRef virtualMachineName, _
  ByVal virtualMachineName _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The name of the virtual machine configuration. The total length of the fully qualified path that includes the virtual machine name configuration file cannot be more than 256 characters.

This property value is read/write.

## Error codes



| Name                                                                                                          | Meaning                                                                                                |
|---------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>                              | The operation was successful.<br/>                                                               |
| <dl> <dt>E\_POINTER</dt> </dl>                         | The *virtualMachineName* parameter is **NULL**.<br/>                                             |
| <dl> <dt>E\_INVALIDARG</dt> </dl>                      | The *virtualMachineName* parameter is not valid or is an empty string.<br/>                      |
| <dl> <dt>VM\_E\_VM\_UNKNOWN</dt> </dl>                 | Unknown configuration.<br/>                                                                      |
| <dl> <dt>VM\_E\_CONFIG\_NAME\_TOO\_LONG</dt> </dl>     | *virtualMachineName* contains too many characters.<br/>                                          |
| <dl> <dt>VM\_E\_CONFIG\_NAME\_INVALID\_CHAR</dt> </dl> | *virtualMachineName* contains one of the following invalid characters "\*?:&lt;&gt;/\|\\"".<br/> |
| <dl> <dt>VM\_E\_CONFIG\_DUPLICATE\_NAME</dt> </dl>     | *virtualMachineName* already exists as a name of another virtual machine.<br/>                   |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl>                 | An unexpected error has occurred.<br/>                                                           |



## Remarks

Virtual machine names are case-insensitive, e.g. "MyVM" and "myvm" refer to the same virtual machine. This is the default property for [**IVMVirtualMachine**](ivmvirtualmachine.md).

Due to the method in which links to a ".vmc" configuration file are maintained by Virtual Server, the effective maximum length of a virtual machine name is roughly 150 characters. The actual usable maximum length will vary for each system.

## Examples

The following example displays the **Name** property value of a [**VMVirtualMachine**](ivmvirtualmachine.md) object.


```VB
Set objVS = CreateObject("VirtualServer.Application")
Set objVM = objVS.FindVirtualMachine("Windows Server 2003")

Wscript.Echo "VM Name: " & objVM.Name
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

 

 





