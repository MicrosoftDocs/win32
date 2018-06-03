---
title: InvokeByName method of the PS\_DhcpServerv4FailoverReplication class
description: Replicate scope configuration between failover partner servers.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: de2d02fd-80c4-4829-8c66-cefbaa61f708
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- InvokeByName method
- InvokeByName method, PS_DhcpServerv4FailoverReplication class
- PS_DhcpServerv4FailoverReplication class, InvokeByName method
topic_type:
- apiref
api_name:
- PS_DhcpServerv4FailoverReplication.InvokeByName
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# InvokeByName method of the PS\_DhcpServerv4FailoverReplication class

Replicate scope configuration between failover partner servers.

## Syntax


```mof
uint32 InvokeByName(
  [in]  string  ComputerName,
  [in]  boolean Force,
  [in]  string  Name[],
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

*Name* \[in\]
</dt> <dd>

Name of the failover relationship. All scopes of the specified relationship(s) are replicated to the partner server.

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

 

 





