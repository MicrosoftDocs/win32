---
title: IVMVirtualNetwork DHCPVirtualNetworkServer property
description: The DHCPVirtualNetworkServer property contains the DHCP virtual network server attached to this virtual network.
ms.assetid: '8bf98efd-13e8-4267-8bb0-b88067a8e6cb'
keywords: ["DHCPVirtualNetworkServer property Virtual Server", "DHCPVirtualNetworkServer property Virtual Server , IVMVirtualNetwork interface", "IVMVirtualNetwork interface Virtual Server , DHCPVirtualNetworkServer property", "DHCPVirtualNetworkServer property Virtual Server , VMVirtualNetwork class", "VMVirtualNetwork class Virtual Server , DHCPVirtualNetworkServer property"]
topic_type:
- apiref
api_name:
- IVMVirtualNetwork.DHCPVirtualNetworkServer
- IVMVirtualNetwork.get_DHCPVirtualNetworkServer
- VMVirtualNetwork.DHCPVirtualNetworkServer
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMVirtualNetwork::DHCPVirtualNetworkServer property

The **DHCPVirtualNetworkServer** property contains the DHCP virtual network server attached to this virtual network.

This property is read-only.

## Syntax


```C++
HRESULT get_DHCPVirtualNetworkServer(
  [out] IVMDHCPVirtualNetworkServer **dhcpVirtualNetworkServer
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
<td><pre><code>VMVirtualNetwork.DHCPVirtualNetworkServer( _
  ByRef dhcpVirtualNetworkServer _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The [**VMDHCPVirtualNetworkServer**](ivmdhcpvirtualnetworkserver.md) object representing the virtual network server attached to this virtual network.

This property value is read-only.

## Error codes



| Name                                                                                   | Meaning                                                          |
|----------------------------------------------------------------------------------------|------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>       | The operation was successful.<br/>                         |
| <dl> <dt> E\_POINTER</dt> </dl> | The *dhcpVirtualNetworkServer* parameter is **NULL**.<br/> |
| <dl> <dt> E\_FAIL</dt> </dl>    | An unexpected error has occurred.<br/>                     |



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

 

 





