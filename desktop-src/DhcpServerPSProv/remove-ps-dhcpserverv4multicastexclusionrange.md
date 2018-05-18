---
title: Remove method of the PS\_DhcpServerv4MulticastExclusionRange class
description: Removes a range of addresses previously excluded from a multicast scope.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'f868fd2d-20be-488c-a234-7181019ed6cb'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dhcp-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Remove method", "Remove method, PS_DhcpServerv4MulticastExclusionRange class", "PS_DhcpServerv4MulticastExclusionRange class, Remove method"]
topic_type:
- apiref
api_name:
- PS_DhcpServerv4MulticastExclusionRange.Remove
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
---

# Remove method of the PS\_DhcpServerv4MulticastExclusionRange class

Removes a range of addresses previously excluded from a multicast scope.

## Syntax


```mof
uint32 Remove(
  [in]  string                              ComputerName,
  [in]  string                              EndRange,
  [in]  string                              Name,
  [in]  string                              StartRange,
  [in]  boolean                             PassThru,
  [out] DhcpServerv4MulticastExclusionRange cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

DNS name or IP address of the target computer running the DHCP server service.

</dd> <dt>

*EndRange* \[in\]
</dt> <dd>

End of the range of IP which were previously excluded from the Scope

</dd> <dt>

*Name* \[in\]
</dt> <dd>

Name of the multicast scope from which to remove the IP address exclusion range

</dd> <dt>

*StartRange* \[in\]
</dt> <dd>

Start of the range of IP addresses which were previously excluded from the Scope

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

If this parameter is specified, the cmdlet return the PowerShell objects which are deleted.

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

 

 





