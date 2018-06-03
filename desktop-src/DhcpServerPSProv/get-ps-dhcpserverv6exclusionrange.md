---
title: Get method of the PS\_DhcpServerv6ExclusionRange class
description: Returns the IPv6 address ranges excluded from the specified IPv6 subnet prefix.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: e9e04dde-4494-40d9-a543-7086d970f4f6
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Get method
- Get method, PS_DhcpServerv6ExclusionRange class
- PS_DhcpServerv6ExclusionRange class, Get method
topic_type:
- apiref
api_name:
- PS_DhcpServerv6ExclusionRange.Get
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Get method of the PS\_DhcpServerv6ExclusionRange class

Returns the IPv6 address ranges excluded from the specified IPv6 subnet prefix.

## Syntax


```mof
uint32 Get(
  [in]  string                     ComputerName,
  [in]  string                     Prefix[],
  [out] DhcpServerv6ExclusionRange cmdletOutput[]
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

The IPv6 prefixes of the scopes for which the exclusion ranges are requested.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of the [**DhcpServerv6ExclusionRange**](dhcpserverv6exclusionrange.md) class.

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

[**PS\_DhcpServerv6ExclusionRange**](ps-dhcpserverv6exclusionrange.md)
</dt> </dl>

 

 





