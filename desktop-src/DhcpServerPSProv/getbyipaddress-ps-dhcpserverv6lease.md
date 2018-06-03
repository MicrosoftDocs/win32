---
title: GetByIPAddress method of the PS\_DhcpServerv6Lease class
description: Gets one or more IPv6 lease records from the DHCP server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 00a0c100-ab3c-4397-ba05-91833296687e
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetByIPAddress method
- GetByIPAddress method, PS_DhcpServerv6Lease class
- PS_DhcpServerv6Lease class, GetByIPAddress method
topic_type:
- apiref
api_name:
- PS_DhcpServerv6Lease.GetByIPAddress
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GetByIPAddress method of the PS\_DhcpServerv6Lease class

Gets one or more IPv6 lease records from the DHCP server.

## Syntax


```mof
uint32 GetByIPAddress(
  [in]  string            ComputerName,
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

*IPAddress* \[in\]
</dt> <dd>

IPv6 address(es) for which the lease records are to be retrieved.

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

 

 





