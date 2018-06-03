---
title: Set method of the PS\_DhcpServerDnsCredential class
description: Sets DNS credentials to be used by the DHCP server for registering or de-registering client records with DNS server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 51f471a9-1144-4895-8f89-3e05a5561908
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Set method
- Set method, PS_DhcpServerDnsCredential class
- PS_DhcpServerDnsCredential class, Set method
topic_type:
- apiref
api_name:
- PS_DhcpServerDnsCredential.Set
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Set method of the PS\_DhcpServerDnsCredential class

Sets DNS credentials to be used by the DHCP server for registering or de-registering client records with DNS server

## Syntax


```mof
uint32 Set(
  [in]  string                  ComputerName,
  [in]  string                  Credential,
  [in]  boolean                 PassThru,
  [out] DhcpServerDnsCredential cmdletOutput
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

DNS name or IP address of the target computer running the DHCP server service.

</dd> <dt>

*Credential* \[in\]
</dt> <dd>

PSCredential object which contains fully qualified username and password of the account to be used.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

If this parameter is specified, the cmdlet returns the PowerShell object which is added.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of a [**DhcpServerDnsCredential**](dhcpserverdnscredential.md) object.

</dd> </dl>

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                   |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DhcpServerDnsCredential**](ps-dhcpserverdnscredential.md)
</dt> </dl>

 

 





