---
title: InvokeByScopeId method of the PS\_DhcpServerv4FailoverReplication class
description: Replicate scope configuration between failover partner servers.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 1744db10-403c-4674-a908-12eb59e5b57e
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- InvokeByScopeId method
- InvokeByScopeId method, PS_DhcpServerv4FailoverReplication class
- PS_DhcpServerv4FailoverReplication class, InvokeByScopeId method
topic_type:
- apiref
api_name:
- PS_DhcpServerv4FailoverReplication.InvokeByScopeId
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# InvokeByScopeId method of the PS\_DhcpServerv4FailoverReplication class

Replicate scope configuration between failover partner servers.

## Syntax


```mof
uint32 InvokeByScopeId(
  [in]  string  ComputerName,
  [in]  boolean Force,
  [in]  string  ScopeId[],
  [out] string  cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

DNS name or IP address of the target computer running the DHCP server service.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

A user confirmation is sought by default by this cmdlet. If -Force is specified, the default confirmation is not sought from the user.

</dd> <dt>

*ScopeId* \[in\]
</dt> <dd>

Scope identifiers, in IPv4 address format, which are to be removed from the failover relationship.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of the [**DhcpServerv4FailoverReplication**](ps-dhcpserverv4failoverreplication.md) class.

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

[**PS\_DhcpServerv4FailoverReplication**](ps-dhcpserverv4failoverreplication.md)
</dt> </dl>

 

 





