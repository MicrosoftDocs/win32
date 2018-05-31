---
title: IVMDHCPVirtualNetworkServer NetworkMask property
description: The NetworkMask property contains the mask used to calculate the base TCP/IP address for the given network.
ms.assetid: b8c36cfe-5b76-485b-9894-47c7a2898098
keywords:
- NetworkMask property Virtual Server
- NetworkMask property Virtual Server , IVMDHCPVirtualNetworkServer interface
- IVMDHCPVirtualNetworkServer interface Virtual Server , NetworkMask property
- NetworkMask property Virtual Server , VMDHCPVirtualNetworkServer interface
- VMDHCPVirtualNetworkServer interface Virtual Server , NetworkMask property
topic_type:
- apiref
api_name:
- IVMDHCPVirtualNetworkServer.NetworkMask
- IVMDHCPVirtualNetworkServer.get_NetworkMask
- VMDHCPVirtualNetworkServer.NetworkMask
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

# IVMDHCPVirtualNetworkServer::NetworkMask property

The **NetworkMask** property contains the mask used to calculate the base TCP/IP address for the given network.

This property is read-only.

## Syntax


```C++
HRESULT get_NetworkMask(
  [out] BSTR *networkMask
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
<td><pre><code>VMDHCPVirtualNetworkServer.NetworkMask( _
  ByRef networkMask _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

Retrieves the TCP/IP address formatted as a string in dotted-decimal notation, such as "255.255.0.0".

This property value is read-only.

## Error codes



| Name                                                                                          | Meaning                                              |
|-----------------------------------------------------------------------------------------------|------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>             |
| <dl> <dt>E\_POINTER</dt> </dl>         | The parameter *networkMask* was **NULL**.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error has occurred.<br/>         |



## Remarks

The **NetworkMask** and the [**Network**](ivmdhcpvirtualnetworkserver-network.md) parameter define the range of TCP/IP addresses managed by the DHCP server. For example, a **Network** of "192.168.0.0" and a **NetworkMask** of "255.255.255.0" define the range "192.168.0.1" to "192.168.0.254". ("192.168.0.0" is invalid and "192.168.0.255" is a special address used to broadcast to all nodes in this network range.)

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMDHCPVirtualNetworkServer**](ivmdhcpvirtualnetworkserver.md)
</dt> </dl>

 

 





