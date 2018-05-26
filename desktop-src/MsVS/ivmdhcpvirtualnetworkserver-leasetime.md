---
title: IVMDHCPVirtualNetworkServer LeaseTime property
description: The LeaseTime property contains the time in seconds after which leases granted by the virtual DHCP server expire.
ms.assetid: 3dedd7f0-bb52-463e-bbff-461670e163c7
keywords:
- LeaseTime property Virtual Server
- LeaseTime property Virtual Server , IVMDHCPVirtualNetworkServer interface
- IVMDHCPVirtualNetworkServer interface Virtual Server , LeaseTime property
- LeaseTime property Virtual Server , VMDHCPVirtualNetworkServer interface
- VMDHCPVirtualNetworkServer interface Virtual Server , LeaseTime property
topic_type:
- apiref
api_name:
- IVMDHCPVirtualNetworkServer.LeaseTime
- IVMDHCPVirtualNetworkServer.get_LeaseTime
- VMDHCPVirtualNetworkServer.LeaseTime
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

# IVMDHCPVirtualNetworkServer::LeaseTime property

The **LeaseTime** property contains the time in seconds after which leases granted by the virtual DHCP server expire.

This property is read-only.

## Syntax


```C++
HRESULT get_LeaseTime(
  [out] VARIANT *leaseTime
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
<td><pre><code>VMDHCPVirtualNetworkServer.LeaseTime( _
  ByRef leaseTime _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The lease time in seconds. The minimum value for this parameter is 60 seconds. The number is returned as a **Decimal** value.

This property value is read-only.

## Error codes



| Name                                                                                          | Meaning                                            |
|-----------------------------------------------------------------------------------------------|----------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>           |
| <dl> <dt>E\_POINTER</dt> </dl>         | The *leaseTime* parameter was **NULL**.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error has occurred.<br/>       |



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

 

 





