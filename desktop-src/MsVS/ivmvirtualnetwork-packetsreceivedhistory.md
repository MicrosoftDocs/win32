---
title: IVMVirtualNetwork PacketsReceivedHistory property
description: The PacketsReceivedHistory property contains the recent number of packets received per second by this virtual network (as an array of number of packets).
ms.assetid: 6eb19043-2c65-42e2-8248-09ce6630d5b8
keywords:
- PacketsReceivedHistory property Virtual Server
- PacketsReceivedHistory property Virtual Server , IVMVirtualNetwork interface
- IVMVirtualNetwork interface Virtual Server , PacketsReceivedHistory property
- PacketsReceivedHistory property Virtual Server , VMVirtualNetwork class
- VMVirtualNetwork class Virtual Server , PacketsReceivedHistory property
topic_type:
- apiref
api_name:
- IVMVirtualNetwork.PacketsReceivedHistory
- IVMVirtualNetwork.get_PacketsReceivedHistory
- VMVirtualNetwork.PacketsReceivedHistory
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

# IVMVirtualNetwork::PacketsReceivedHistory property

The **PacketsReceivedHistory** property contains the recent number of packets received per second by this virtual network (as an array of number of packets).

This property is read-only.

## Syntax


```C++
HRESULT get_PacketsReceivedHistory(
  [out] VARIANT *packetsReceived
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
<td><pre><code>&#39; Data type: Object

VMVirtualNetwork.PacketsReceivedHistory( _
  ByRef packetsReceived _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The recent number of packets received per second by this virtual network as an unsigned **Integer** array of 60 elements, representing the number of packets received at each second over the past minute.

This property value is read-only.

## Error codes



| Name                                                                                          | Meaning                                                 |
|-----------------------------------------------------------------------------------------------|---------------------------------------------------------|
| <dl> <dt> S\_OK</dt> </dl>             | The operation was successful.<br/>                |
| <dl> <dt>E\_POINTER</dt> </dl>         | The *packetsReceived* parameter is **NULL**.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error occurred.<br/>                |



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

 

 





