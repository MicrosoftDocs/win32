---
title: Get method of the PS\_DhcpServerv4Scope class
description: Returns the IPv4 scope configuration of the specified scopes. If scope id is not specified all the scopes configured on the server are returned.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 0e5262e1-a1a8-4fbd-b9d0-578c9297a71b
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Get method
- Get method, PS_DhcpServerv4Scope class
- PS_DhcpServerv4Scope class, Get method
topic_type:
- apiref
api_name:
- PS_DhcpServerv4Scope.Get
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Get method of the PS\_DhcpServerv4Scope class

Returns the IPv4 scope configuration of the specified scopes. If scope id is not specified all the scopes configured on the server are returned.

## Syntax


```mof
uint32 Get(
  [in]  string            ComputerName,
  [in]  string            ScopeId[],
  [out] DhcpServerv4Scope cmdletOutput[]
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

The scope identifier(s) (in IPv4 address format) whose configuration is to be retrieved.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of the [**DhcpServerv4Scope**](dhcpserverv4scope.md) class.

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

[**PS\_DhcpServerv4Scope**](ps-dhcpserverv4scope.md)
</dt> </dl>

 

 





