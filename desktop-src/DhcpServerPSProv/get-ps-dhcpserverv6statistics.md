---
title: Get method of the PS\_DhcpServerv6Statistics class
description: Gets the DHCP Server statistics for IPv6.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '56df00d0-d07e-4883-b77f-9a0a77e2b01b'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dhcp-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Get method", "Get method, PS_DhcpServerv6Statistics class", "PS_DhcpServerv6Statistics class, Get method"]
topic_type:
- apiref
api_name:
- PS_DhcpServerv6Statistics.Get
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
---

# Get method of the PS\_DhcpServerv6Statistics class

Gets the DHCP Server statistics for IPv6.

## Syntax


```mof
uint32 Get(
  [in]  string                 ComputerName,
  [out] DhcpServerv6Statistics cmdletOutput
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

DNS name or IP address of the target computer running the DHCP server service.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of the [**DhcpServerv6Statistics**](dhcpserverv6statistics.md) class.

</dd> </dl>

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DhcpServerv6Statistics**](ps-dhcpserverv6statistics.md)
</dt> </dl>

 

 





