---
title: IVMVirtualServer SuggestedMaximumMemoryPerVM property
description: The SuggestedMaximumMemoryPerVM property contains the suggested maximum allowable quantity, in megabytes, of physical RAM per virtual machine to avoid low memory conditions on the host.
ms.assetid: 'c4a42668-3864-4dc9-9444-e3f63666b0d8'
keywords: ["SuggestedMaximumMemoryPerVM property Virtual Server", "SuggestedMaximumMemoryPerVM property Virtual Server , IVMVirtualServer interface", "IVMVirtualServer interface Virtual Server , SuggestedMaximumMemoryPerVM property", "SuggestedMaximumMemoryPerVM property Virtual Server , VMVirtualServer class", "VMVirtualServer class Virtual Server , SuggestedMaximumMemoryPerVM property"]
topic_type:
- apiref
api_name:
- IVMVirtualServer.SuggestedMaximumMemoryPerVM
- IVMVirtualServer.get_SuggestedMaximumMemoryPerVM
- VMVirtualServer.SuggestedMaximumMemoryPerVM
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMVirtualServer::SuggestedMaximumMemoryPerVM property

The **SuggestedMaximumMemoryPerVM** property contains the suggested maximum allowable quantity, in megabytes, of physical RAM per virtual machine to avoid low memory conditions on the host.

This property is read-only.

## Syntax


```C++
HRESULT get_SuggestedMaximumMemoryPerVM(
  [out] long *megabytesOfMemory
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
<td><pre><code>VMVirtualServer.SuggestedMaximumMemoryPerVM( _
  ByRef megabytesOfMemory _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The suggested maximum allowable quantity, in megabytes, of physical RAM per virtual machine to avoid low memory conditions on the host.

This property value is read-only.

## Error codes



| Name                                                                                          | Meaning                                     |
|-----------------------------------------------------------------------------------------------|---------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>    |
| <dl> <dt>E\_POINTER</dt> </dl>         | *megabytesOfMemory* is **NULL**.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error occurred.<br/>    |



## Examples

The following example displays the **SuggestedMaximumMemoryPerVM** property value of the [**VMVirtualServer**](ivmvirtualserver.md) object.


```VB
Set objVS = CreateObject("VirtualServer.Application")

Wscript.Echo "Name: " & objVS.Name
Wscript.Echo "Suggested maximum memory per VM: " & _
              objVS.SuggestedMaximumMemoryPerVM
```



## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMVirtualServer**](ivmvirtualserver.md)
</dt> </dl>

 

 





