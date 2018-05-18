---
title: Add method of the PS\_DhcpServerv4PolicyIPRange class
description: Adds an IP range to an existing policy at the scope level.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '07dd51a9-319c-45fd-9fd3-769fd91458a5'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dhcp-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Add method", "Add method, PS_DhcpServerv4PolicyIPRange class", "PS_DhcpServerv4PolicyIPRange class, Add method"]
topic_type:
- apiref
api_name:
- PS_DhcpServerv4PolicyIPRange.Add
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
---

# Add method of the PS\_DhcpServerv4PolicyIPRange class

Adds an IP range to an existing policy at the scope level.

## Syntax


```mof
uint32 Add(
  [in]  string                    ComputerName,
  [in]  string                    Name,
  [in]  string                    ScopeId,
  [in]  string                    StartRange,
  [in]  string                    EndRange,
  [in]  boolean                   PassThru,
  [out] DhcpServerv4PolicyIPRange cmdletOutput
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

Name of the policy to which IP address ranges are to be added

</dd> <dt>

*ScopeId* \[in\]
</dt> <dd>

Scope identifier, in IPv4 address format, which contains the specified policy

</dd> <dt>

*StartRange* \[in\]
</dt> <dd>

Start IP address of the range being added to the policy

</dd> <dt>

*EndRange* \[in\]
</dt> <dd>

End IP address of the range being added to the policy

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

If this parameter is specified, the cmdlet returns the PowerShell object which is added.

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

 

 





