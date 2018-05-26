---
title: RemoveByIPAddress method of the PS\_DhcpServerv6Lease class
description: Deletes one or more IPv6 lease records from the server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 4b3f7855-6ccc-432a-b8f5-0c50f3acf2b8
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- RemoveByIPAddress method
- RemoveByIPAddress method, PS_DhcpServerv6Lease class
- PS_DhcpServerv6Lease class, RemoveByIPAddress method
topic_type:
- apiref
api_name:
- PS_DhcpServerv6Lease.RemoveByIPAddress
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# RemoveByIPAddress method of the PS\_DhcpServerv6Lease class

Deletes one or more IPv6 lease records from the server.

## Syntax


```mof
uint32 RemoveByIPAddress(
  [in]  string            ComputerName,
  [in]  boolean           PassThru,
  [in]  string            IPAddress[],
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

*IPAddress* \[in\]
</dt> <dd>

IPv6 addresses whose leases records are to be deleted from the server.

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

 

 





