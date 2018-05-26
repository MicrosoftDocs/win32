---
title: Add method of the PS\_DhcpServerInDC class
description: Adds the server to the list of authorized DHCP servers in AD. A DHCP server running on a domain joined computer needs to be authorized in AD so that it can start leasing IP addresses on the network.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 35eb71c0-304b-49db-8617-3e4d8a52ba26
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Add method
- Add method, PS_DhcpServerInDC class
- PS_DhcpServerInDC class, Add method
topic_type:
- apiref
api_name:
- PS_DhcpServerInDC.Add
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Add method of the PS\_DhcpServerInDC class

Adds the server to the list of authorized DHCP servers in AD. A DHCP server running on a domain joined computer needs to be authorized in AD so that it can start leasing IP addresses on the network.

## Syntax


```mof
uint32 Add(
  [in]  string         DnsName,
  [in]  string         IPAddress,
  [in]  boolean        PassThru,
  [out] DhcpServerInDC cmdletOutput
);
```



## Parameters

<dl> <dt>

*DnsName* \[in\]
</dt> <dd>

DNS name of the DHCP server to be added to the list of authorized DHCP servers in AD

</dd> <dt>

*IPAddress* \[in\]
</dt> <dd>

IP address of the DHCP server which is to be added to the list of authorized DHCP server in AD

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

If this parameter is specified, the cmdlet returns the PowerShell object which is added.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of a [**DhcpServerInDC**](dhcpserverindc.md) object.

</dd> </dl>

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DhcpServerInDC**](ps-dhcpserverindc.md)
</dt> </dl>

 

 





