---
title: Remove method of the PS\_DhcpServerv6Scope class
description: Deletes the IPv6 Scopes from the DHCP Server corresponding to the specified prefixes.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 2f27b3c6-1c5d-441d-b229-1eff79f6bd66
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Remove method
- Remove method, PS_DhcpServerv6Scope class
- PS_DhcpServerv6Scope class, Remove method
topic_type:
- apiref
api_name:
- PS_DhcpServerv6Scope.Remove
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Remove method of the PS\_DhcpServerv6Scope class

Deletes the IPv6 Scopes from the DHCP Server corresponding to the specified prefixes

## Syntax


```mof
uint32 Remove(
  [in]  string            Prefix[],
  [in]  boolean           Force,
  [in]  boolean           Passthru,
  [in]  string            ComputerName,
  [out] DhcpServerv6Scope cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*Prefix* \[in\]
</dt> <dd>

IPv6 subnet prefixes of the scopes which are to be deleted.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

If specified, the scope will be deleted even if there are active leases in the scope

</dd> <dt>

*Passthru* \[in\]
</dt> <dd>

If this parameter is specified, the cmdlet return the PowerShell objects which are deleted.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

DNS name or IP address of the target computer running the DHCP server service.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of the [**DhcpServerv6Scope**](dhcpserverv6scope.md) class.

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

[**PS\_DhcpServerv6Scope**](ps-dhcpserverv6scope.md)
</dt> </dl>

 

 





