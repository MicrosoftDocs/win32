---
title: IVMDHCPVirtualNetworkServer Network property
description: The Network property contains the base TCP/IP address of the range.
ms.assetid: '5f545f80-f291-4b25-98ff-616fa829990e'
keywords: ["Network property Virtual Server", "Network property Virtual Server , IVMDHCPVirtualNetworkServer interface", "IVMDHCPVirtualNetworkServer interface Virtual Server , Network property", "Network property Virtual Server , VMDHCPVirtualNetworkServer interface", "VMDHCPVirtualNetworkServer interface Virtual Server , Network property"]
topic_type:
- apiref
api_name:
- IVMDHCPVirtualNetworkServer.Network
- IVMDHCPVirtualNetworkServer.get_Network
- VMDHCPVirtualNetworkServer.Network
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMDHCPVirtualNetworkServer::Network property

The **Network** property contains the base TCP/IP address of the range.

This property is read-only.

## Syntax


```C++
HRESULT get_Network(
  [out] BSTR *network
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
<td><pre><code>VMDHCPVirtualNetworkServer.Network( _
  ByRef network _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

Retrieves the TCP/IP address formatted as a string in dotted-decimal notation, such as "10.237.0.0".

This property value is read-only.

## Error codes



| Name                                                                                          | Meaning                                          |
|-----------------------------------------------------------------------------------------------|--------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>         |
| <dl> <dt>E\_POINTER</dt> </dl>         | The parameter *network* was **NULL**.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error has occurred.<br/>     |



## Remarks

The **Network** property in conjunction with the [**NetworkMask**](ivmdhcpvirtualnetworkserver-networkmask.md) property define the range of TCP/IP addresses managed by the DHCP server. For example, a **Network** of "192.168.0.0" and a **NetworkMask** of "255.255.255.0" define the range "192.168.0.1" to "192.168.0.254". ("192.168.0.0" is invalid and "192.168.0.255" is a special address used to broadcast to all nodes in this network range.)

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMDHCPVirtualNetworkServer**](ivmdhcpvirtualnetworkserver.md)
</dt> </dl>

 

 





