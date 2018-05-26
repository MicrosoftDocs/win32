---
title: Add method of the PS\_DhcpServerv4FailoverScope class
description: Adds the specified scope(s) to the failover relationship.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 3af1c2da-6756-41f6-8151-9accfd3d51e1
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Add method
- Add method, PS_DhcpServerv4FailoverScope class
- PS_DhcpServerv4FailoverScope class, Add method
topic_type:
- apiref
api_name:
- PS_DhcpServerv4FailoverScope.Add
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Add method of the PS\_DhcpServerv4FailoverScope class

Adds the specified scope(s) to the failover relationship.

## Syntax


```mof
uint32 Add(
  [in]  string               Name,
  [in]  string               ScopeId[],
  [in]  string               ComputerName,
  [in]  boolean              PassThru,
  [out] DhcpServerv4Failover cmdletOutput
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

Name of the failover relationship to which the scopes are being added.

</dd> <dt>

*ScopeId* \[in\]
</dt> <dd>

Scope identifiers, in IPv4 address format, which are to be removed from the failover relationship.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

DNS name or IP address of the target computer running the DHCP server service.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

If this parameter is specified, the cmdlet returns the PowerShell object which is added.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of the [**DhcpServerv4Failover**](dhcpserverv4failover.md) class.

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

[**PS\_DhcpServerv4FailoverScope**](ps-dhcpserverv4failoverscope.md)
</dt> </dl>

 

 





