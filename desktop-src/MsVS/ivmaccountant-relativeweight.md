---
title: IVMAccountant RelativeWeight property
description: The RelativeWeight property contains the relative weight assigned to this virtual machine.
ms.assetid: df66fc3d-d3ac-4be7-b36c-1c737d4abd43
keywords:
- RelativeWeight property Virtual Server
- RelativeWeight property Virtual Server , IVMAccountant interface
- IVMAccountant interface Virtual Server , RelativeWeight property
- RelativeWeight property Virtual Server , VMAccountant interface
- VMAccountant interface Virtual Server , RelativeWeight property
topic_type:
- apiref
api_name:
- IVMAccountant.RelativeWeight
- IVMAccountant.get_RelativeWeight
- VMAccountant.RelativeWeight
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

# IVMAccountant::RelativeWeight property

The **RelativeWeight** property contains the relative weight assigned to this virtual machine.

This property is read-only.

## Syntax


```C++
HRESULT get_RelativeWeight(
  [out] long *relativeWeight
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
<td><pre><code>VMAccountant.RelativeWeight( _
  ByRef relativeWeight _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

Retrieves the relative weight assigned to this virtual machine. This is a number between 1 and 10000 representing priority of this virtual machine relative to other virtual machines. A higher number indicates a higher priority.

This property value is read-only.

## Error codes



| Name                                                                                          | Meaning                                  |
|-----------------------------------------------------------------------------------------------|------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/> |
| <dl> <dt> E\_POINTER</dt> </dl>        | *relativeWeight* is **NULL**.<br/> |
| <dl> <dt>VM\_E\_VM\_UNKNOWN</dt> </dl> | Unknown virtual machine.<br/>      |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error occurred.<br/> |



## Examples

The following example prints the RelativeWeight property information for each virtual machine.


```VB
Set objVS = CreateObject("VirtualServer.Application")
set colVMs = objVS.VirtualMachines

For Each objVM in colVMS
    Set colAccountants = objVM.Accountant
        Wscript.Echo "Virtual machine: " & objVM.Name
        Wscript.Echo "Relative weight: " & colAccountants.RelativeWeight
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

 

 





