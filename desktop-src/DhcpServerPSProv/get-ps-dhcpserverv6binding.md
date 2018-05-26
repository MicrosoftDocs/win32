---
title: Get method of the PS\_DhcpServerv6Binding class
description: Returns the IPv6 interfaces to which a DHCP Server is bound.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: ae914219-210b-4e44-bd9b-eaea39ed7979
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Get method
- Get method, PS_DhcpServerv6Binding class
- PS_DhcpServerv6Binding class, Get method
topic_type:
- apiref
api_name:
- PS_DhcpServerv6Binding.Get
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Get method of the PS\_DhcpServerv6Binding class

Returns the IPv6 interfaces to which a DHCP Server is bound.

## Syntax


```mof
uint32 Get(
  [in]  string              ComputerName,
  [out] DhcpServerv6Binding cmdletOutput[]
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

An embedded instance of the [**DhcpServerv6Binding**](dhcpserverv6binding.md) class.

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

[**PS\_DhcpServerv6Binding**](ps-dhcpserverv6binding.md)
</dt> </dl>

 

 





