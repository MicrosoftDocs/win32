---
title: IVMAccountant AllowableMaximumSystemCapacity property
description: The AllowableMaximumSystemCapacity property contains the currently allowable maximum percentage of system capacity that can be assigned to this virtual machine.
ms.assetid: be0d8cdf-6463-4f7c-a10b-9eabecfaf335
keywords:
- AllowableMaximumSystemCapacity property Virtual Server
- AllowableMaximumSystemCapacity property Virtual Server , IVMAccountant interface
- IVMAccountant interface Virtual Server , AllowableMaximumSystemCapacity property
- AllowableMaximumSystemCapacity property Virtual Server , VMAccountant interface
- VMAccountant interface Virtual Server , AllowableMaximumSystemCapacity property
topic_type:
- apiref
api_name:
- IVMAccountant.AllowableMaximumSystemCapacity
- IVMAccountant.get_AllowableMaximumSystemCapacity
- VMAccountant.AllowableMaximumSystemCapacity
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

# IVMAccountant::AllowableMaximumSystemCapacity property

The **AllowableMaximumSystemCapacity** property contains the currently allowable maximum percentage of system capacity that can be assigned to this virtual machine.

This property is read-only.

## Syntax


```C++
HRESULT get_AllowableMaximumSystemCapacity(
  [out] VARIANT *allowableMaximumSystemCapacity
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
<td><pre><code>VMAccountant.AllowableMaximumSystemCapacity( _
  ByRef allowableMaximumSystemCapacity _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The currently allowable maximum percentage of system capacity that can be assigned to this virtual machine. This number is returned as a **Double** and may be less than 100 depending on the number of host processors.

This property value is read-only.

## Error codes



| Name                                                                                          | Meaning                                                  |
|-----------------------------------------------------------------------------------------------|----------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>                 |
| <dl> <dt>E\_POINTER</dt> </dl>         | *allowableMaximumSystemCapacity* is **NULL**.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error occurred.<br/>                 |



## Examples

The following example prints the AllowableMaximumSystemCapacity property information for each virtual machine.


```VB
Set objVS = CreateObject("VirtualServer.Application")
set colVMs = objVS.VirtualMachines

For Each objVM in colVMS
    Set colAccountants = objVM.Accountant
        Wscript.Echo "Virtual machine: " & objVM.Name
        Wscript.Echo "Allowable maximum system capacity: " & colAccountants.AllowableMaximumSystemCapacity
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

 

 





