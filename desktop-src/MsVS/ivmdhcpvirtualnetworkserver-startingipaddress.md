---
title: IVMDHCPVirtualNetworkServer StartingIPAddress property
description: The StartingIPAddress property contains the first TCP/IP address that the server can dynamically assign to a client on the Virtual Network.
ms.assetid: 014a1dfa-112f-4668-a394-4a6b7b1eecca
keywords:
- StartingIPAddress property Virtual Server
- StartingIPAddress property Virtual Server , IVMDHCPVirtualNetworkServer interface
- IVMDHCPVirtualNetworkServer interface Virtual Server , StartingIPAddress property
- StartingIPAddress property Virtual Server , VMDHCPVirtualNetworkServer interface
- VMDHCPVirtualNetworkServer interface Virtual Server , StartingIPAddress property
topic_type:
- apiref
api_name:
- IVMDHCPVirtualNetworkServer.StartingIPAddress
- IVMDHCPVirtualNetworkServer.get_StartingIPAddress
- VMDHCPVirtualNetworkServer.StartingIPAddress
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

# IVMDHCPVirtualNetworkServer::StartingIPAddress property

The **StartingIPAddress** property contains the first TCP/IP address that the server can dynamically assign to a client on the Virtual Network.

This property is read-only.

## Syntax


```C++
HRESULT get_StartingIPAddress(
  [out] BSTR *startingIPAddress
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
<td><pre><code>VMDHCPVirtualNetworkServer.StartingIPAddress( _
  ByRef startingIPAddress _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

Retrieves the TCP/IP address formatted as a string in dotted-decimal notation, such as "10.237.0.16".

This property value is read-only.

## Error codes



| Name                                                                                          | Meaning                                                    |
|-----------------------------------------------------------------------------------------------|------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>                   |
| <dl> <dt> E\_POINTER</dt> </dl>        | The parameter *startingIPAddress* was **NULL**.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error has occurred.<br/>               |



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

 

 





