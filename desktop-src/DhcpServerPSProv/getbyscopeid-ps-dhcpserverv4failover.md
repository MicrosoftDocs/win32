---
title: GetByScopeId method of the PS\_DhcpServerv4Failover class
description: Gets the failover relationships configured on the server for the specific failover relationship name.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 76cecbcc-48eb-4efb-b33e-18a4ae384676
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetByScopeId method
- GetByScopeId method, PS_DhcpServerv4Failover class
- PS_DhcpServerv4Failover class, GetByScopeId method
topic_type:
- apiref
api_name:
- PS_DhcpServerv4Failover.GetByScopeId
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GetByScopeId method of the PS\_DhcpServerv4Failover class

Gets the failover relationships configured on the server for the specific failover relationship name.

## Syntax


```mof
uint32 GetByScopeId(
  [in]  string               ComputerName,
  [in]  string               ScopeId[],
  [out] DhcpServerv4Failover cmdletOutput[]
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

Scope identifier(s) (in IPv4 address format). Properties of the failover relationships on the server to which these scopes are associated are returned.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of a [**DhcpServerv4Failover**](dhcpserverv4failover.md) object.

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

[**PS\_DhcpServerv4Failover**](ps-dhcpserverv4failover.md)
</dt> </dl>

 

 





