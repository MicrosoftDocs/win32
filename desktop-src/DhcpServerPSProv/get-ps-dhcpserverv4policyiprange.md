---
title: Get method of the PS\_DhcpServerv4PolicyIPRange class
description: Gets an IP range(s) from a policy in the specified scope.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'd2c752bb-30fd-417d-a5da-c28779f681ff'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dhcp-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Get method", "Get method, PS_DhcpServerv4PolicyIPRange class", "PS_DhcpServerv4PolicyIPRange class, Get method"]
topic_type:
- apiref
api_name:
- PS_DhcpServerv4PolicyIPRange.Get
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
---

# Get method of the PS\_DhcpServerv4PolicyIPRange class

Gets an IP range(s) from a policy in the specified scope.

## Syntax


```mof
uint32 Get(
  [in]  string                    Name[],
  [in]  string                    ScopeId,
  [in]  string                    ComputerName,
  [out] DhcpServerv4PolicyIPRange cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

Name of the policy whose associated IP ranges are to be returned

</dd> <dt>

*ScopeId* \[in\]
</dt> <dd>

Scope identifier (in IPv4 address format) which contains the specified policy

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

DNS name or IP address of the target computer running the DHCP server service.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of the [**DhcpServerv4PolicyIPRange**](dhcpserverv4policyiprange.md) class.

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

[**PS\_DhcpServerv4PolicyIPRange**](ps-dhcpserverv4policyiprange.md)
</dt> </dl>

 

 





