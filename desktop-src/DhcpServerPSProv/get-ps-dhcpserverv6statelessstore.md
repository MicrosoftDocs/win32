---
title: Get method of the PS\_DhcpServerv6StatelessStore class
description: Returns the properties of IPv6 stateless store for the specified IPv6 subnet.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 5912f1d3-a271-49bd-8a8b-ca8ec1d12404
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Get method
- Get method, PS_DhcpServerv6StatelessStore class
- PS_DhcpServerv6StatelessStore class, Get method
topic_type:
- apiref
api_name:
- PS_DhcpServerv6StatelessStore.Get
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Get method of the PS\_DhcpServerv6StatelessStore class

Returns the properties of IPv6 stateless store for the specified IPv6 subnet.

## Syntax


```mof
uint32 Get(
  [in]  string                     Prefix[],
  [in]  string                     ComputerName,
  [out] DhcpServerv6StatelessStore cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*Prefix* \[in\]
</dt> <dd>

IPv6 subnet prefixes of the scopes whose stateless store properties are to be returned.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

DNS name or IP address of the target computer running the DHCP server service.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of the [**DhcpServerv6StatelessStore**](dhcpserverv6statelessstore.md) class.

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

[**PS\_DhcpServerv6StatelessStore**](ps-dhcpserverv6statelessstore.md)
</dt> </dl>

 

 





