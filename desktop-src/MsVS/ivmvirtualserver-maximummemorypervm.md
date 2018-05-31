---
title: IVMVirtualServer MaximumMemoryPerVM property
description: The MaximumMemoryPerVM property contains the maximum allowable quantity, in megabytes, of physical RAM per virtual machine.
ms.assetid: 69345b81-4c5a-487c-9163-41a2619f16d7
keywords:
- MaximumMemoryPerVM property Virtual Server
- MaximumMemoryPerVM property Virtual Server , IVMVirtualServer interface
- IVMVirtualServer interface Virtual Server , MaximumMemoryPerVM property
- MaximumMemoryPerVM property Virtual Server , VMVirtualServer class
- VMVirtualServer class Virtual Server , MaximumMemoryPerVM property
topic_type:
- apiref
api_name:
- IVMVirtualServer.MaximumMemoryPerVM
- IVMVirtualServer.get_MaximumMemoryPerVM
- VMVirtualServer.MaximumMemoryPerVM
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

# IVMVirtualServer::MaximumMemoryPerVM property

The **MaximumMemoryPerVM** property contains the maximum allowable quantity, in megabytes, of physical RAM per virtual machine.

This property is read-only.

## Syntax


```C++
HRESULT get_MaximumMemoryPerVM(
  [out] long *megabytesOfMemory
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
<td><pre><code>VMVirtualServer.MaximumMemoryPerVM( _
  ByRef megabytesOfMemory _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The maximum allowable quantity, in megabytes, of physical RAM per virtual machine.

This property value is read-only.

## Error codes



| Name                                                                                          | Meaning                                     |
|-----------------------------------------------------------------------------------------------|---------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>    |
| <dl> <dt>E\_POINTER</dt> </dl>         | *megabytesOfMemory* is **NULL**.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error occurred.<br/>    |



## Examples

The following example displays the **MaximumMemoryPerVM** property value of the [**VMVirtualServer**](ivmvirtualserver.md) object.


```VB
Set objVS = CreateObject("VirtualServer.Application")

Wscript.Echo "Name: " & objVS.Name
Wscript.Echo "Maximum memory per VM: " & objVS.MaximumMemoryPerVM
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

 

 





