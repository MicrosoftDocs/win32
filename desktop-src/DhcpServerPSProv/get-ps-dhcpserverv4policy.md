---
title: Get method of the PS\_DhcpServerv4Policy class
description: Gets one or more policies at the server level or the scope level.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '4ac0e140-4587-4089-ae24-4995ac2611b5'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dhcp-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Get method", "Get method, PS_DhcpServerv4Policy class", "PS_DhcpServerv4Policy class, Get method"]
topic_type:
- apiref
api_name:
- PS_DhcpServerv4Policy.Get
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
---

# Get method of the PS\_DhcpServerv4Policy class

Gets one or more policies at the server level or the scope level.

## Syntax


```mof
uint32 Get(
  [in]  string             ComputerName,
  [in]  string             Name[],
  [in]  string             ScopeId,
  [out] DhcpServerv4Policy cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

DNS name or IP address of the target computer running the DHCP server service.

</dd> <dt>

*Name* \[in\]
</dt> <dd>

Name(s) of the policy(ies) to be returned

</dd> <dt>

*ScopeId* \[in\]
</dt> <dd>

Scope identifier (in IPv4 address format) from which the policies are to be retrieved. If scope id is not specified, server level policies are retrieved.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of the [**DhcpServerv4Policy**](dhcpserverv4policy.md) class.

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

[**PS\_DhcpServerv4Policy**](ps-dhcpserverv4policy.md)
</dt> </dl>

 

 





