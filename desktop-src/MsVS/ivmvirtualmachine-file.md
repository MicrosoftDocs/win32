---
title: IVMVirtualMachine File property
description: The File property contains the fully qualified name of the \ 0034;\ .vmc \ 0034; file that describes this virtual machine configuration.
ms.assetid: 'cbd0771d-df2b-4ee4-8a8f-df28622030d7'
keywords: ["File property Virtual Server", "File property Virtual Server , IVMVirtualMachine interface", "IVMVirtualMachine interface Virtual Server , File property", "File property Virtual Server , VMVirtualMachine class", "VMVirtualMachine class Virtual Server , File property"]
topic_type:
- apiref
api_name:
- IVMVirtualMachine.File
- IVMVirtualMachine.get_File
- VMVirtualMachine.File
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMVirtualMachine::File property

The **File** property contains the fully qualified name of the "\*.vmc" file that describes this virtual machine configuration.

This property is read-only.

## Syntax


```C++
HRESULT get_File(
  [out] BSTR *virtualMachineXMLFile
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
<td><pre><code>VMVirtualMachine.File( _
  ByRef virtualMachineXMLFile _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The fully qualified name of the "\*.vmc" file that describes this virtual machine configuration.

This property value is read-only.

## Error codes



| Name                                                                                          | Meaning                                                       |
|-----------------------------------------------------------------------------------------------|---------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>                      |
| <dl> <dt>E\_POINTER</dt> </dl>         | The *virtualMachineXMLFile* parameter is **NULL**.<br/> |
| <dl> <dt>VM\_E\_VM\_UNKNOWN</dt> </dl> | The configuration is unknown.<br/>                      |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error has occurred.<br/>                  |



## Remarks

Virtual machine XML files have the ".vmc" filename extension.

## Examples

The following example displays the **File** property value of a [**VMVirtualMachine**](ivmvirtualmachine.md) object.


```VB
Set objVS = CreateObject("VirtualServer.Application")
Set objVM = objVS.FindVirtualMachine("Windows Server 2003")

Wscript.Echo "VM Name: " & objVM.Name
WScript.Echo "Configuration file: " & objVM.File
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

 

 





