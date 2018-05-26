---
title: IVMVirtualNetwork PacketsSent property
description: The PacketsSent property contains the current number of packets sent per second by this virtual network.
ms.assetid: 9e9f55ba-d666-411b-b9a9-bbbd6692b5d4
keywords:
- PacketsSent property Virtual Server
- PacketsSent property Virtual Server , IVMVirtualNetwork interface
- IVMVirtualNetwork interface Virtual Server , PacketsSent property
- PacketsSent property Virtual Server , VMVirtualNetwork class
- VMVirtualNetwork class Virtual Server , PacketsSent property
topic_type:
- apiref
api_name:
- IVMVirtualNetwork.PacketsSent
- IVMVirtualNetwork.get_PacketsSent
- VMVirtualNetwork.PacketsSent
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

# IVMVirtualNetwork::PacketsSent property

The **PacketsSent** property contains the current number of packets sent per second by this virtual network.

This property is read-only.

## Syntax


```C++
HRESULT get_PacketsSent(
  [out] long *packetsSent
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
<td><pre><code>VMVirtualNetwork.PacketsSent( _
  ByRef packetsSent _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The current number of packets sent per second by this virtual network.

This property value is read-only.

## Error codes



| Name                                                                                           | Meaning                                             |
|------------------------------------------------------------------------------------------------|-----------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>               | The operation was successful.<br/>            |
| <dl> <dt>E\_POINTER</dt> </dl>          | The *packetsSent* parameter is **NULL**.<br/> |
| <dl> <dt> DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error occurred.<br/>            |



## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMVirtualNetwork**](ivmvirtualnetwork.md)
</dt> </dl>

 

 





