---
title: IVMDHCPVirtualNetworkServer WINSServers property
description: The WINSServers property contains a comma-separated list of the TCP/IP address representing WINS servers. The list of WINS servers is returned to the DHCP client as part of the servers response.
ms.assetid: b6f16470-eb84-4756-8c02-cbc5f347783d
keywords:
- WINSServers property Virtual Server
- WINSServers property Virtual Server , IVMDHCPVirtualNetworkServer interface
- IVMDHCPVirtualNetworkServer interface Virtual Server , WINSServers property
- WINSServers property Virtual Server , VMDHCPVirtualNetworkServer interface
- VMDHCPVirtualNetworkServer interface Virtual Server , WINSServers property
topic_type:
- apiref
api_name:
- IVMDHCPVirtualNetworkServer.WINSServers
- IVMDHCPVirtualNetworkServer.get_WINSServers
- IVMDHCPVirtualNetworkServer.put_WINSServers
- VMDHCPVirtualNetworkServer.WINSServers
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

# IVMDHCPVirtualNetworkServer::WINSServers property

The **WINSServers** property contains a comma-separated list of the TCP/IP address representing WINS servers. The list of WINS servers is returned to the DHCP client as part of the server's response.

This property is read/write.

## Syntax


```C++
HRESULT put_WINSServers(
  [in]  BSTR winsServers
);

HRESULT get_WINSServers(
  [out] BSTR *winsServers
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
<td><pre><code>VMDHCPVirtualNetworkServer.WINSServers( _
  ByRef winsServers, _
  ByVal winsServers _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

Contains a comma-separated list of TCP/IP addresses formatted as a string in dotted-decimal notation. For example, 10.237.0.3,10.237.0.4.

This property value is read/write.

## Error codes



| Name                                                                                                   | Meaning                                                                 |
|--------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>                       | The operation was successful.<br/>                                |
| <dl> <dt>E\_POINTER</dt> </dl>                  | The *winsServers* parameter was **NULL**.<br/>                    |
| <dl> <dt>E\_INVALIDARG</dt> </dl>               | The *winsServers* parameter was an empty string.<br/>             |
| <dl> <dt>VM\_E\_INVALID\_IP\_ADDRESS</dt> </dl> | The *winsServers* parameter contained an invalid IP address.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl>          | An unexpected error has occurred.<br/>                            |



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

 

 





