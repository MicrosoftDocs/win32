---
title: IVMNetworkAdapter VirtualMachine property
description: The VirtualMachine property contains the virtual machine associated with this virtual NIC.
ms.assetid: 'a3d4ccba-def3-4dad-b624-d20f795cbd9e'
keywords: ["VirtualMachine property Virtual Server", "VirtualMachine property Virtual Server , IVMNetworkAdapter interface", "IVMNetworkAdapter interface Virtual Server , VirtualMachine property", "VirtualMachine property Virtual Server , VMNetworkAdapter interface", "VMNetworkAdapter interface Virtual Server , VirtualMachine property"]
topic_type:
- apiref
api_name:
- IVMNetworkAdapter.VirtualMachine
- IVMNetworkAdapter.get_VirtualMachine
- VMNetworkAdapter.VirtualMachine
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMNetworkAdapter::VirtualMachine property

The **VirtualMachine** property contains the virtual machine associated with this virtual NIC.

This property is read-only.

## Syntax


```C++
HRESULT get_VirtualMachine(
  [out] IVMVirtualMachine **virtualMachine
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
<td><pre><code>VMNetworkAdapter.VirtualMachine( _
  ByRef virtualMachine _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The [**VMVirtualMachine**](ivmvirtualmachine.md) object which is associated with this virtual NIC.

This property value is read-only.

## Error codes



| Name                                                                                          | Meaning                                                 |
|-----------------------------------------------------------------------------------------------|---------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>                |
| <dl> <dt>E\_POINTER</dt> </dl>         | The parameter *virtualMachine* was **NULL**.<br/> |
| <dl> <dt>VM\_E\_VM\_UNKNOWN</dt> </dl> | The virtual machine cannot be found.<br/>         |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error has occurred.<br/>            |



## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMNetworkAdapter**](ivmnetworkadapter.md)
</dt> <dt>

[IVMNetwork Properties](ivmnetworkadapter-properties.md)
</dt> </dl>

 

 





