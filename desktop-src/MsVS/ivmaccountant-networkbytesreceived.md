---
title: IVMAccountant NetworkBytesReceived property
description: The NetworkBytesReceived property contains the total number of bytes received by all virtual network interface cards for this virtual machine.
ms.assetid: d22d7196-224f-42c1-b24c-4a739c68d7cf
keywords:
- NetworkBytesReceived property Virtual Server
- NetworkBytesReceived property Virtual Server , IVMAccountant interface
- IVMAccountant interface Virtual Server , NetworkBytesReceived property
- NetworkBytesReceived property Virtual Server , VMAccountant interface
- VMAccountant interface Virtual Server , NetworkBytesReceived property
topic_type:
- apiref
api_name:
- IVMAccountant.NetworkBytesReceived
- IVMAccountant.get_NetworkBytesReceived
- VMAccountant.NetworkBytesReceived
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

# IVMAccountant::NetworkBytesReceived property

The **NetworkBytesReceived** property contains the total number of bytes received by all virtual network interface cards for this virtual machine.

This property is read-only.

## Syntax


```C++
HRESULT get_NetworkBytesReceived(
  [out] VARIANT *bytesReceived
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
<td><pre><code>VMAccountant.NetworkBytesReceived( _
  ByRef bytesReceived _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The total number of bytes received by all virtual network interface cards for this virtual machine. The number is returned as a **Decimal** value.

This property value is read-only.

## Error codes



| Name                                                                                          | Meaning                                        |
|-----------------------------------------------------------------------------------------------|------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>       |
| <dl> <dt>E\_POINTER</dt> </dl>         | *bytesReceived* is **NULL**.<br/>        |
| <dl> <dt>S\_FALSE</dt> </dl>           | The virtual machine is not running.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error occurred.<br/>       |



## Remarks

Note that network I/O statistics are reset to zero when a virtual machine is powered up, reset, or restored from saved state.

## Examples

The following example prints the NetworkBytesReceived property information for each virtual machine.


```VB
Set objVS = CreateObject("VirtualServer.Application")
set colVMs = objVS.VirtualMachines

For Each objVM in colVMS
    Set colAccountants = objVM.Accountant
        Wscript.Echo "Virtual machine: " & objVM.Name
        Wscript.Echo "Network bytes received: " & colAccountants.NetworkBytesReceived
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

 

 





