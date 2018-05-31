---
title: IVMAccountant AllowableReservedSystemCapacity property
description: The AllowableReservedSystemCapacity property contains the currently allowable minimum percentage of system capacity that can be reserved for this virtual machine.
ms.assetid: 7e80baf3-8cec-4be7-b413-9349f6f13ceb
keywords:
- AllowableReservedSystemCapacity property Virtual Server
- AllowableReservedSystemCapacity property Virtual Server , IVMAccountant interface
- IVMAccountant interface Virtual Server , AllowableReservedSystemCapacity property
- AllowableReservedSystemCapacity property Virtual Server , VMAccountant interface
- VMAccountant interface Virtual Server , AllowableReservedSystemCapacity property
topic_type:
- apiref
api_name:
- IVMAccountant.AllowableReservedSystemCapacity
- IVMAccountant.get_AllowableReservedSystemCapacity
- VMAccountant.AllowableReservedSystemCapacity
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

# IVMAccountant::AllowableReservedSystemCapacity property

The **AllowableReservedSystemCapacity** property contains the currently allowable minimum percentage of system capacity that can be reserved for this virtual machine.

This property is read-only.

## Syntax


```C++
HRESULT get_AllowableReservedSystemCapacity(
  [out] VARIANT *allowableReservedSystemCapacity
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
<td><pre><code>VMAccountant.AllowableReservedSystemCapacity( _
  ByRef allowableReservedSystemCapacity _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The currently allowable minimum percentage of system capacity that can be reserved for this virtual machine. This number is returned as a **Double** and may be less than 100 depending on the number of host processors.

This property value is read-only.

## Error codes



| Name                                                                                          | Meaning                                                   |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>                  |
| <dl> <dt>E\_POINTER</dt> </dl>         | *allowableReservedSystemCapacity* is **NULL**.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error occurred.<br/>                  |



## Examples

The following example prints the AllowableReservedSystemCapacity property information for each virtual machine.


```VB
Set objVS = CreateObject("VirtualServer.Application")
set colVMs = objVS.VirtualMachines

For Each objVM in colVMS
    Set colAccountants = objVM.Accountant
        Wscript.Echo "Virtual machine: " & objVM.Name
        Wscript.Echo "Allowable reserved system capacity: " & colAccountants.AllowableReservedSystemCapacity
        Wscript.Echo
Next
```



## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMAccountant**](ivmaccountant.md)
</dt> </dl>

 

 





