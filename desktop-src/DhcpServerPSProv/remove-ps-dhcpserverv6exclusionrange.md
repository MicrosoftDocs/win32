---
title: Remove method of the PS\_DhcpServerv6ExclusionRange class
description: Deletes a range of IP addresses previously excluded from an IPv4 Scope.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: e097be1c-f529-46cf-a297-445e9536353b
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Remove method
- Remove method, PS_DhcpServerv6ExclusionRange class
- PS_DhcpServerv6ExclusionRange class, Remove method
topic_type:
- apiref
api_name:
- PS_DhcpServerv6ExclusionRange.Remove
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Remove method of the PS\_DhcpServerv6ExclusionRange class

Deletes a range of IP addresses previously excluded from an IPv4 Scope.

## Syntax


```mof
uint32 Remove(
  [in]  string                     ComputerName,
  [in]  string                     Prefix,
  [in]  string                     StartRange,
  [in]  string                     EndRange,
  [in]  boolean                    Passthru,
  [out] DhcpServerv6ExclusionRange cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

DNS name or IP address of the target computer running the DHCP server service.

</dd> <dt>

*Prefix* \[in\]
</dt> <dd>

The IPv6 subnet prefix of the scope from which the excluded IP ranges are to be deleted.

</dd> <dt>

*StartRange* \[in\]
</dt> <dd>

The start IPv6 address of the excluded IP range which is to be deleted

</dd> <dt>

*EndRange* \[in\]
</dt> <dd>

The end IPv6 address of the excluded IP range which is to be deleted.

</dd> <dt>

*Passthru* \[in\]
</dt> <dd>

If this parameter is specified, the cmdlet return the PowerShell objects which are deleted.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of the [**DhcpServerv6ExclusionRange**](dhcpserverv6exclusionrange.md) class.

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

[**PS\_DhcpServerv6ExclusionRange**](ps-dhcpserverv6exclusionrange.md)
</dt> </dl>

 

 





