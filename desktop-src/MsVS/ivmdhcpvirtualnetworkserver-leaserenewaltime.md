---
title: IVMDHCPVirtualNetworkServer LeaseRenewalTime property
description: The LeaseRenewalTime property contains the time in seconds after which the client virtual machine should renew its TCP/IP address lease.
ms.assetid: b695b666-d4e1-4cfb-9034-138731069f7e
keywords:
- LeaseRenewalTime property Virtual Server
- LeaseRenewalTime property Virtual Server , IVMDHCPVirtualNetworkServer interface
- IVMDHCPVirtualNetworkServer interface Virtual Server , LeaseRenewalTime property
- LeaseRenewalTime property Virtual Server , VMDHCPVirtualNetworkServer interface
- VMDHCPVirtualNetworkServer interface Virtual Server , LeaseRenewalTime property
topic_type:
- apiref
api_name:
- IVMDHCPVirtualNetworkServer.LeaseRenewalTime
- IVMDHCPVirtualNetworkServer.get_LeaseRenewalTime
- VMDHCPVirtualNetworkServer.LeaseRenewalTime
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

# IVMDHCPVirtualNetworkServer::LeaseRenewalTime property

The **LeaseRenewalTime** property contains the time in seconds after which the client virtual machine should renew its TCP/IP address lease.

This property is read-only.

## Syntax


```C++
HRESULT get_LeaseRenewalTime(
  [out] VARIANT *leaseRenewalTime
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
<td><pre><code>VMDHCPVirtualNetworkServer.LeaseRenewalTime( _
  ByRef leaseRenewalTime _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The lease renewal time in seconds. The minimum value for this parameter is 30 seconds. The number is returned as a **Decimal** value.

This property value is read-only.

## Error codes



| Name                                                                                           | Meaning                                                   |
|------------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| <dl> <dt> S\_OK</dt> </dl>              | The operation was successful.<br/>                  |
| <dl> <dt>E\_POINTER</dt> </dl>          | The *leaseRenewalTime* parameter was **NULL**.<br/> |
| <dl> <dt> DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error has occurred.<br/>              |



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

 

 





