---
title: IVMAccountant MaximumSystemCapacity property
description: The MaximumSystemCapacity property contains the maximum percentage of system capacity that can be used by this virtual machine.
ms.assetid: '967b30f5-85b4-4478-8667-ed28386c6d70'
keywords: ["MaximumSystemCapacity property Virtual Server", "MaximumSystemCapacity property Virtual Server , IVMAccountant interface", "IVMAccountant interface Virtual Server , MaximumSystemCapacity property", "MaximumSystemCapacity property Virtual Server , VMAccountant interface", "VMAccountant interface Virtual Server , MaximumSystemCapacity property"]
topic_type:
- apiref
api_name:
- IVMAccountant.MaximumSystemCapacity
- IVMAccountant.get_MaximumSystemCapacity
- VMAccountant.MaximumSystemCapacity
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMAccountant::MaximumSystemCapacity property

The **MaximumSystemCapacity** property contains the maximum percentage of system capacity that can be used by this virtual machine.

This property is read-only.

## Syntax


```C++
HRESULT get_MaximumSystemCapacity(
  [out] VARIANT *maximumSystemCapacity
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
<td><pre><code>VMAccountant.MaximumSystemCapacity( _
  ByRef maximumSystemCapacity _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

Retrieves the maximum percentage of system capacity assigned to this virtual machine. The number is returned as a **Double** value.

This property value is read-only.

## Error codes



| Name                                                                                           | Meaning                                         |
|------------------------------------------------------------------------------------------------|-------------------------------------------------|
| <dl> <dt> S\_OK</dt> </dl>              | The operation was successful.<br/>        |
| <dl> <dt> E\_POINTER</dt> </dl>         | *maximumSystemCapacity* is **NULL**.<br/> |
| <dl> <dt>VM\_E\_VM\_UNKNOWN</dt> </dl>  | Unknown virtual machine.<br/>             |
| <dl> <dt> DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error occurred.<br/>        |



## Examples

The following example prints the MaximumSystemCapacity property information for each virtual machine.


```VB
Set objVS = CreateObject("VirtualServer.Application")
set colVMs = objVS.VirtualMachines

For Each objVM in colVMS
    Set colAccountants = objVM.Accountant
        Wscript.Echo "Virtual machine: " & objVM.Name
        Wscript.Echo "Maximum system capacity: " & colAccountants.MaximumSystemCapacity
        Wscript.Echo
Next
```



## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMAccountant**](ivmaccountant.md)
</dt> </dl>

 

 





