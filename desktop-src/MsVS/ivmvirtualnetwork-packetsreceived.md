---
title: IVMVirtualNetwork PacketsReceived property
description: The PacketsReceived property contains the current number of packets received per second by this virtual network.
ms.assetid: 'b6d9be99-a68b-45a7-943e-7d53183e5527'
keywords: ["PacketsReceived property Virtual Server", "PacketsReceived property Virtual Server , IVMVirtualNetwork interface", "IVMVirtualNetwork interface Virtual Server , PacketsReceived property", "PacketsReceived property Virtual Server , VMVirtualNetwork class", "VMVirtualNetwork class Virtual Server , PacketsReceived property"]
topic_type:
- apiref
api_name:
- IVMVirtualNetwork.PacketsReceived
- IVMVirtualNetwork.get_PacketsReceived
- VMVirtualNetwork.PacketsReceived
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMVirtualNetwork::PacketsReceived property

The **PacketsReceived** property contains the current number of packets received per second by this virtual network.

This property is read-only.

## Syntax


```C++
HRESULT get_PacketsReceived(
  [out] long *packetsReceived
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
<td><pre><code>VMVirtualNetwork.PacketsReceived( _
  ByRef packetsReceived _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The current number of packets received per second by this virtual network.

This property value is read-only.

## Error codes



| Name                                                                                          | Meaning                                                 |
|-----------------------------------------------------------------------------------------------|---------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>                |
| <dl> <dt>E\_POINTER</dt> </dl>         | The *packetsReceived* parameter is **NULL**.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error occurred.<br/>                |



## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMVirtualNetwork**](ivmvirtualnetwork.md)
</dt> </dl>

 

 





