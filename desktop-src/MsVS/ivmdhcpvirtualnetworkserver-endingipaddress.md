---
title: IVMDHCPVirtualNetworkServer EndingIPAddress property
description: The EndingIPAddress property contains the last TCP/IP address that the DHCP server can dynamically assign to a client on the Virtual Network.
ms.assetid: 31ad2349-d8bc-49a3-85f5-f251549de476
keywords:
- EndingIPAddress property Virtual Server
- EndingIPAddress property Virtual Server , IVMDHCPVirtualNetworkServer interface
- IVMDHCPVirtualNetworkServer interface Virtual Server , EndingIPAddress property
- EndingIPAddress property Virtual Server , VMDHCPVirtualNetworkServer interface
- VMDHCPVirtualNetworkServer interface Virtual Server , EndingIPAddress property
topic_type:
- apiref
api_name:
- IVMDHCPVirtualNetworkServer.EndingIPAddress
- IVMDHCPVirtualNetworkServer.get_EndingIPAddress
- VMDHCPVirtualNetworkServer.EndingIPAddress
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

# IVMDHCPVirtualNetworkServer::EndingIPAddress property

The **EndingIPAddress** property contains the last TCP/IP address that the DHCP server can dynamically assign to a client on the Virtual Network.

This property is read-only.

## Syntax


```C++
HRESULT get_EndingIPAddress(
  [out] BSTR *endingIPAddress
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
<td><pre><code>VMDHCPVirtualNetworkServer.EndingIPAddress( _
  ByRef endingIPAddress _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The TCP/IP address formatted as a string in dotted-decimal notation, such as "10.237.255.254".

This property value is read-only.

## Error codes



| Name                                                                                          | Meaning                                                  |
|-----------------------------------------------------------------------------------------------|----------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>                 |
| <dl> <dt>E\_POINTER</dt> </dl>         | The parameter *endingIPAddress* was **NULL**.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error has occurred.<br/>             |



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

 

 





