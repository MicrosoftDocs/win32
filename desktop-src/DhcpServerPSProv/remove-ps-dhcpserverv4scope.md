---
title: Remove method of the PS\_DhcpServerv4Scope class
description: Deletes the specified IPv4 scopes from the server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 41df0170-772b-483d-9d58-e205c8272b1a
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Remove method
- Remove method, PS_DhcpServerv4Scope class
- PS_DhcpServerv4Scope class, Remove method
topic_type:
- apiref
api_name:
- PS_DhcpServerv4Scope.Remove
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Remove method of the PS\_DhcpServerv4Scope class

Deletes the specified IPv4 scopes from the server.

## Syntax


```mof
uint32 Remove(
  [in]  string            ScopeId[],
  [in]  boolean           Force,
  [in]  boolean           Passthru,
  [in]  string            ComputerName,
  [out] DhcpServerv4Scope cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*ScopeId* \[in\]
</dt> <dd>

Scope identifier(s) (in IPv4 address format) which are to be deleted.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

If specified, deletes the scope even if there are active leases in the scope.

</dd> <dt>

*Passthru* \[in\]
</dt> <dd>

If this parameter is specified, the cmdlet returns the PowerShell object which is modified.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

DNS name or IP address of the target computer running the DHCP server service.

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

 

 





