---
title: Get method of the PS\_DhcpServerv4FreeIPAddress class
description: Gets free/unassigned IP Address(es) from the specified scope.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: a838ea7a-0cee-4a7d-bd14-604be1924b00
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Get method
- Get method, PS_DhcpServerv4FreeIPAddress class
- PS_DhcpServerv4FreeIPAddress class, Get method
topic_type:
- apiref
api_name:
- PS_DhcpServerv4FreeIPAddress.Get
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Get method of the PS\_DhcpServerv4FreeIPAddress class

Gets free/unassigned IP Address(es) from the specified scope.

## Syntax


```mof
uint32 Get(
  [in]  string ComputerName,
  [in]  string ScopeId,
  [in]  uint32 NumAddress,
  [in]  string StartAddress,
  [in]  string EndAddress,
  [out] string cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

DNS name or IP address of the target computer running the DHCP server service.

</dd> <dt>

*ScopeId* \[in\]
</dt> <dd>

Scope identifier (in IPv4 address format) from which the free IP address(es) are requested

</dd> <dt>

*NumAddress* \[in\]
</dt> <dd>

Number of free IP addresses requested. Default is 1.

</dd> <dt>

*StartAddress* \[in\]
</dt> <dd>

Start IP address of the range from which the free IP addresses are to be returned

</dd> <dt>

*EndAddress* \[in\]
</dt> <dd>

End IP address of the range from which the free IP addresses are to be returned

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An array of IP addresses from the scopes which are unallocated/ not leased.

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

[**PS\_DhcpServerv4FreeIPAddress**](ps-dhcpserverv4freeipaddress.md)
</dt> </dl>

 

 





