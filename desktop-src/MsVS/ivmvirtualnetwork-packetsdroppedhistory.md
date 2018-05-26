---
title: IVMVirtualNetwork PacketsDroppedHistory property
description: The PacketsDroppedHistory property contains the recent number of packets dropped per second by this virtual network (as an array of number of bytes).
ms.assetid: bee66b3d-ea04-464c-84b2-e11272e66a96
keywords:
- PacketsDroppedHistory property Virtual Server
- PacketsDroppedHistory property Virtual Server , IVMVirtualNetwork interface
- IVMVirtualNetwork interface Virtual Server , PacketsDroppedHistory property
- PacketsDroppedHistory property Virtual Server , VMVirtualNetwork class
- VMVirtualNetwork class Virtual Server , PacketsDroppedHistory property
topic_type:
- apiref
api_name:
- IVMVirtualNetwork.PacketsDroppedHistory
- IVMVirtualNetwork.get_PacketsDroppedHistory
- VMVirtualNetwork.PacketsDroppedHistory
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

# IVMVirtualNetwork::PacketsDroppedHistory property

The **PacketsDroppedHistory** property contains the recent number of packets dropped per second by this virtual network (as an array of number of bytes).

This property is read-only.

## Syntax


```C++
HRESULT get_PacketsDroppedHistory(
  [out] VARIANT *packetsDropped
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
<td><pre><code>VMVirtualNetwork.PacketsDroppedHistory( _
  ByRef packetsDropped _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The recent number of packets dropped by this virtual network as an unsigned **Integer** array of 60 elements, representing the number of packets dropped at each second over the past minute.

This property value is read-only.

## Error codes



| Name                                                                                           | Meaning                                                |
|------------------------------------------------------------------------------------------------|--------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>               | The operation was successful.<br/>               |
| <dl> <dt>E\_POINTER</dt> </dl>          | The *packetsDropped* parameter is **NULL**.<br/> |
| <dl> <dt> DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error occurred.<br/>               |



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

 

 





