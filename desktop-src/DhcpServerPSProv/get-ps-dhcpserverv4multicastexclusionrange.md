---
title: Get method of the PS\_DhcpServerv4MulticastExclusionRange class
description: Returns the Exclusion range for the specified multicast scopes.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'cdc6c501-76ec-4595-ab1c-ba5e63a3eb1a'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dhcp-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Get method", "Get method, PS_DhcpServerv4MulticastExclusionRange class", "PS_DhcpServerv4MulticastExclusionRange class, Get method"]
topic_type:
- apiref
api_name:
- PS_DhcpServerv4MulticastExclusionRange.Get
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
---

# Get method of the PS\_DhcpServerv4MulticastExclusionRange class

Returns the Exclusion range for the specified multicast scopes

## Syntax


```mof
uint32 Get(
  [in]  string                              ComputerName,
  [in]  string                              Name[],
  [out] DhcpServerv4MulticastExclusionRange cmdletOutput[]
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

Names of multicast scopes from which to get the exclusion range.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of the [**DhcpServerv4MulticastExclusionRange**](dhcpserverv4multicastexclusionrange.md) class.

</dd> </dl>

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                   |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DhcpServerv4MulticastExclusionRange**](ps-dhcpserverv4multicastexclusionrange.md)
</dt> </dl>

 

 





