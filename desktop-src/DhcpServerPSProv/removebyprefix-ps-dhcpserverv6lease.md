---
title: RemoveByPrefix method of the PS\_DhcpServerv6Lease class
description: Deletes one or more IPv6 lease records from the server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 76964462-c9a0-4f33-9d28-4cf7ff3aae23
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- RemoveByPrefix method
- RemoveByPrefix method, PS_DhcpServerv6Lease class
- PS_DhcpServerv6Lease class, RemoveByPrefix method
topic_type:
- apiref
api_name:
- PS_DhcpServerv6Lease.RemoveByPrefix
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# RemoveByPrefix method of the PS\_DhcpServerv6Lease class

Deletes one or more IPv6 lease records from the server.

## Syntax


```mof
uint32 RemoveByPrefix(
  [in]  string            ComputerName,
  [in]  boolean           PassThru,
  [in]  string            Prefix,
  [out] DhcpServerv6Lease cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

DNS name or IP address of the target computer running the DHCP server service.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

If this parameter is specified, the cmdlet return the PowerShell objects which are deleted.

</dd> <dt>

*Prefix* \[in\]
</dt> <dd>

IPv6 subnet prefix of the scope from which the leases are to be deleted.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of the [**DhcpServerv6Lease**](dhcpserverv6lease.md) class.

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

[**PS\_DhcpServerv6Lease**](ps-dhcpserverv6lease.md)
</dt> </dl>

 

 





