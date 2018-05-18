---
title: Add method of the PS\_DhcpServerv6ExclusionRange class
description: Sets the range of IPv6 addresses to exclude from an IPv6 scope. IP addresses from this range will not be leased out by the DHCP server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'bb418a86-8d1c-4088-b830-2715507a0de8'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dhcp-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Add method", "Add method, PS_DhcpServerv6ExclusionRange class", "PS_DhcpServerv6ExclusionRange class, Add method"]
topic_type:
- apiref
api_name:
- PS_DhcpServerv6ExclusionRange.Add
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
---

# Add method of the PS\_DhcpServerv6ExclusionRange class

Sets the range of IPv6 addresses to exclude from an IPv6 scope. IP addresses from this range will not be leased out by the DHCP server.

## Syntax


```mof
uint32 Add(
  [in]  string                     ComputerName,
  [in]  string                     StartRange,
  [in]  string                     EndRange,
  [in]  string                     Prefix,
  [in]  boolean                    PassThru,
  [out] DhcpServerv6ExclusionRange cmdletOutput
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

DNS name or IP address of the target computer running the DHCP server service.

</dd> <dt>

*StartRange* \[in\]
</dt> <dd>

Starting IP address in exclusion range, string formatted as an IPv6 Address.

</dd> <dt>

*EndRange* \[in\]
</dt> <dd>

Ending IP address in exclusion range, string formatted as an IPv6 Address.

</dd> <dt>

*Prefix* \[in\]
</dt> <dd>

The IPv6 prefix of the scope to which the exclusion range is being added.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

If this parameter is specified, the cmdlet returns the PowerShell object which is added.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of the [**DhcpServerv6ExclusionRange**](dhcpserverv6exclusionrange.md) class.

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

[**PS\_DhcpServerv6ExclusionRange**](ps-dhcpserverv6exclusionrange.md)
</dt> </dl>

 

 





