---
title: IVMVirtualServer MaximumParallelPortsPerVM property
description: The MaximumParallelPortsPerVM property contains the maximum number of parallel ports per virtual machine.
ms.assetid: 8a29337d-e622-4384-9a39-40bac704f949
keywords:
- MaximumParallelPortsPerVM property Virtual Server
- MaximumParallelPortsPerVM property Virtual Server , IVMVirtualServer interface
- IVMVirtualServer interface Virtual Server , MaximumParallelPortsPerVM property
- MaximumParallelPortsPerVM property Virtual Server , VMVirtualServer class
- VMVirtualServer class Virtual Server , MaximumParallelPortsPerVM property
topic_type:
- apiref
api_name:
- IVMVirtualServer.MaximumParallelPortsPerVM
- IVMVirtualServer.get_MaximumParallelPortsPerVM
- VMVirtualServer.MaximumParallelPortsPerVM
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

# IVMVirtualServer::MaximumParallelPortsPerVM property

The **MaximumParallelPortsPerVM** property contains the maximum number of parallel ports per virtual machine.

This property is read-only.

## Syntax


```C++
HRESULT get_MaximumParallelPortsPerVM(
  [out] long *maxPorts
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
<td><pre><code>VMVirtualServer.MaximumParallelPortsPerVM( _
  ByRef maxPorts _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The maximum number of parallel ports per virtual machine.

This property value is read-only.

## Error codes



| Name                                                                                          | Meaning                                  |
|-----------------------------------------------------------------------------------------------|------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/> |
| <dl> <dt>E\_POINTER</dt> </dl>         | *maxPorts* is **NULL**.<br/>       |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error occurred.<br/> |



## Examples

The following example displays the **MaximumParallelPortsPerVM** property value of the [**VMVirtualServer**](ivmvirtualserver.md) object.


```VB
Set objVS = CreateObject("VirtualServer.Application")

Wscript.Echo "Name: " & objVS.Name
Wscript.Echo "Maximum parallel ports per VM: " & _
              objVS.MaximumParallelPortsPerVM
```



## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMVirtualServer**](ivmvirtualserver.md)
</dt> </dl>

 

 





