---
title: IVMNetworkAdapter VirtualNetwork property
description: The VirtualNetwork property contains the virtual network to which the virtual NIC is attached.
ms.assetid: 9a2cba39-dae1-4955-b10d-9e5d2d5a37ab
keywords:
- VirtualNetwork property Virtual Server
- VirtualNetwork property Virtual Server , IVMNetworkAdapter interface
- IVMNetworkAdapter interface Virtual Server , VirtualNetwork property
- VirtualNetwork property Virtual Server , VMNetworkAdapter interface
- VMNetworkAdapter interface Virtual Server , VirtualNetwork property
topic_type:
- apiref
api_name:
- IVMNetworkAdapter.VirtualNetwork
- IVMNetworkAdapter.get_VirtualNetwork
- VMNetworkAdapter.VirtualNetwork
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

# IVMNetworkAdapter::VirtualNetwork property

The **VirtualNetwork** property contains the virtual network to which the virtual NIC is attached.

This property is read-only.

## Syntax


```C++
HRESULT get_VirtualNetwork(
  [out] IVMVirtualNetwork **virtualNetwork
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
<td><pre><code>VMNetworkAdapter.VirtualNetwork( _
  ByRef virtualNetwork _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The [**VMVirtualNetwork**](ivmvirtualnetwork.md) object which is associated with this virtual NIC.

This property value is read-only.

## Error codes



| Name                                                                                                            | Meaning                                                                                   |
|-----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>                                | The operation was successful.<br/>                                                  |
| <dl> <dt>E\_POINTER</dt> </dl>                           | The parameter *virtualNetwork* was **NULL**.<br/>                                   |
| <dl> <dt>S\_FALSE</dt> </dl>                             | This network interface is unplugged and is not connected to a virtual network.<br/> |
| <dl> <dt>VM\_E\_INVALID\_VIRTUAL\_NETWORK\_ID</dt> </dl> | This interface is connected to a virtual network with an invalid ID.<br/>           |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl>                   | An unexpected error has occurred.<br/>                                              |



## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMNetworkAdapter**](ivmnetworkadapter.md)
</dt> </dl>

 

 





