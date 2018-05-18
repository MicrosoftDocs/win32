---
title: Get method of the PS\_DhcpServerv4ExclusionRange class
description: Returns the IPv4 address ranges excluded from the specified scope IDs. If scope id is not specified, all IPv4 address ranges excluded on the server are returned.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '1d915737-6000-4dd4-a493-f7a1ee912cbc'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dhcp-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Get method", "Get method, PS_DhcpServerv4ExclusionRange class", "PS_DhcpServerv4ExclusionRange class, Get method"]
topic_type:
- apiref
api_name:
- PS_DhcpServerv4ExclusionRange.Get
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
---

# Get method of the PS\_DhcpServerv4ExclusionRange class

Returns the IPv4 address ranges excluded from the specified scope IDs. If scope id is not specified, all IPv4 address ranges excluded on the server are returned.

## Syntax


```mof
uint32 Get(
  [in]  string                     ComputerName,
  [in]  string                     ScopeId[],
  [out] DhcpServerv4ExclusionRange cmdletOutput[]
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

The scope identifiers (in IPv4 address format) from which the excluded IP address ranges should be returned.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of a [**DhcpServerv4ExclusionRange**](dhcpserverv4exclusionrange.md) object.

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

[**PS\_DhcpServerv4ExclusionRange**](ps-dhcpserverv4exclusionrange.md)
</dt> </dl>

 

 





