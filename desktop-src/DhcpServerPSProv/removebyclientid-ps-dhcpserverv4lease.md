---
title: RemoveByClientId method of the PS\_DhcpServerv4Lease class
description: Deletes the specified IPv4 address lease record from the DHCP server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: fe6ecb26-980c-410b-b247-d201c378d75d
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- RemoveByClientId method
- RemoveByClientId method, PS_DhcpServerv4Lease class
- PS_DhcpServerv4Lease class, RemoveByClientId method
topic_type:
- apiref
api_name:
- PS_DhcpServerv4Lease.RemoveByClientId
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# RemoveByClientId method of the PS\_DhcpServerv4Lease class

Deletes the specified IPv4 address lease record from the DHCP server.

## Syntax


```mof
uint32 RemoveByClientId(
  [in]  boolean           PassThru,
  [in]  string            ComputerName,
  [in]  string            ClientId[],
  [in]  string            ScopeId,
  [out] DhcpServerv4Lease cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*PassThru* \[in\]
</dt> <dd>

If this parameter is specified, the cmdlet return the PowerShell objects which are deleted.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

DNS name or IP address of the target computer running the DHCP server service.

</dd> <dt>

*ClientId* \[in\]
</dt> <dd>

Client identifier whose IP address lease is to be deleted. Windows clients use the MAC address as the client identifier.

</dd> <dt>

*ScopeId* \[in\]
</dt> <dd>

Scope identifier (in IPv4 address format) from which the IP address leases are to be deleted.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of the [**DhcpServerv4Lease**](dhcpserverv4lease.md) class.

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

[**PS\_DhcpServerv4Lease**](ps-dhcpserverv4lease.md)
</dt> </dl>

 

 





