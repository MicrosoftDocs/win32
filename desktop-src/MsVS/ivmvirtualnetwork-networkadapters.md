---
title: IVMVirtualNetwork NetworkAdapters property
description: The NetworkAdapters property contains an enumerable collection of NICs attached to the virtual network.
ms.assetid: 0a40b94a-45dd-44d1-9831-c34670f82824
keywords:
- NetworkAdapters property Virtual Server
- NetworkAdapters property Virtual Server , IVMVirtualNetwork interface
- IVMVirtualNetwork interface Virtual Server , NetworkAdapters property
- NetworkAdapters property Virtual Server , VMVirtualNetwork class
- VMVirtualNetwork class Virtual Server , NetworkAdapters property
topic_type:
- apiref
api_name:
- IVMVirtualNetwork.NetworkAdapters
- IVMVirtualNetwork.get_NetworkAdapters
- VMVirtualNetwork.NetworkAdapters
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

# IVMVirtualNetwork::NetworkAdapters property

The **NetworkAdapters** property contains an enumerable collection of NICs attached to the virtual network.

This property is read-only.

## Syntax


```C++
HRESULT get_NetworkAdapters(
  [out] IVMNetworkAdapterCollection **networkInterfaceCollection
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
<td><pre><code>VMVirtualNetwork.NetworkAdapters( _
  ByRef networkInterfaceCollection _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The [**IVMNetworkAdapterCollection**](ivmnetworkadaptercollection.md) object which holds the virtual NICs attached to this virtual network.

This property value is read-only.

## Error codes



| Name                                                                                          | Meaning                                                            |
|-----------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>                           |
| <dl> <dt>E\_POINTER</dt> </dl>         | The *networkInterfaceCollection* parameter is **NULL**.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error has occurred.<br/>                       |



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

 

 





