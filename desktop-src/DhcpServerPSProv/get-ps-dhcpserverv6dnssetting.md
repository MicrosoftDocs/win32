---
title: Get method of the PS\_DhcpServerv6DnsSetting class
description: Gets the DNS Update settings configured on the DHCP Server for a specific scope or reservation or server wide.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: c8e19290-0bfb-4c02-b3e3-43424d6bdcd1
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Get method
- Get method, PS_DhcpServerv6DnsSetting class
- PS_DhcpServerv6DnsSetting class, Get method
topic_type:
- apiref
api_name:
- PS_DhcpServerv6DnsSetting.Get
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Get method of the PS\_DhcpServerv6DnsSetting class

Gets the DNS Update settings configured on the DHCP Server for a specific scope or reservation or server wide.

## Syntax


```mof
uint32 Get(
  [in]  string                 ComputerName,
  [in]  string                 Prefix,
  [in]  string                 IPAddress,
  [out] DhcpServerv6DnsSetting cmdletOutput
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

DNS name or IP address of the target computer running the DHCP server service.

</dd> <dt>

*Prefix* \[in\]
</dt> <dd>

Subnet prefix of the IPv6 scope whose DNS update settings are to be retrieved.

</dd> <dt>

*IPAddress* \[in\]
</dt> <dd>

IPv6 address of the reservation for which the DNS update settings are to be retrieved.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of the [**DhcpServerv6DnsSetting**](dhcpserverv6dnssetting.md) class.

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

[**PS\_DhcpServerv6DnsSetting**](ps-dhcpserverv6dnssetting.md)
</dt> </dl>

 

 





