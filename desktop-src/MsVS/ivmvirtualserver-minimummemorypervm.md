---
title: IVMVirtualServer MinimumMemoryPerVM property
description: The MinimumMemoryPerVM property contains the minimum allowable quantity, in megabytes, of physical RAM per virtual machine.
ms.assetid: 8b5d840f-ea8f-4d40-b2a6-88323b8fdd19
keywords:
- MinimumMemoryPerVM property Virtual Server
- MinimumMemoryPerVM property Virtual Server , IVMVirtualServer interface
- IVMVirtualServer interface Virtual Server , MinimumMemoryPerVM property
- MinimumMemoryPerVM property Virtual Server , VMVirtualServer class
- VMVirtualServer class Virtual Server , MinimumMemoryPerVM property
topic_type:
- apiref
api_name:
- IVMVirtualServer.MinimumMemoryPerVM
- IVMVirtualServer.get_MinimumMemoryPerVM
- VMVirtualServer.MinimumMemoryPerVM
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

# IVMVirtualServer::MinimumMemoryPerVM property

The **MinimumMemoryPerVM** property contains the minimum allowable quantity, in megabytes, of physical RAM per virtual machine.

This property is read-only.

## Syntax


```C++
HRESULT get_MinimumMemoryPerVM(
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
<td><pre><code>VMVirtualServer.MinimumMemoryPerVM( _
  ByRef megabytesOfMemory _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The minimum allowable quantity, in megabytes, of physical RAM per virtual machine.

This property value is read-only.

## Error codes



| Name                                                                                          | Meaning                                     |
|-----------------------------------------------------------------------------------------------|---------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>    |
| <dl> <dt>E\_POINTER</dt> </dl>         | *megabytesOfMemory* is **NULL**.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error occurred.<br/>    |



## Examples

The following example displays the **MinimumMemoryPerVM** property value of the [**VMVirtualServer**](ivmvirtualserver.md) object.


```VB
Set objVS = CreateObject("VirtualServer.Application")

Wscript.Echo "Name: " & objVS.Name
Wscript.Echo "Minimum memory per VM: " & objVS.MinimumMemoryPerVM
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

 

 





