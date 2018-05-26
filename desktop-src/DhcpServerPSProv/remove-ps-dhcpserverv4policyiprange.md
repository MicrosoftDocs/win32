---
title: Remove method of the PS\_DhcpServerv4PolicyIPRange class
description: Deletes an IP range from an existing policy at the scope level.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 072a9b01-3f5e-46df-bfe7-9367f2f6226c
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Remove method
- Remove method, PS_DhcpServerv4PolicyIPRange class
- PS_DhcpServerv4PolicyIPRange class, Remove method
topic_type:
- apiref
api_name:
- PS_DhcpServerv4PolicyIPRange.Remove
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Remove method of the PS\_DhcpServerv4PolicyIPRange class

Deletes an IP range from an existing policy at the scope level.

## Syntax


```mof
uint32 Remove(
  [in]  string                    Name,
  [in]  string                    ScopeId,
  [in]  string                    StartRange,
  [in]  string                    EndRange,
  [in]  boolean                   PassThru,
  [in]  string                    ComputerName,
  [out] DhcpServerv4PolicyIPRange cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

Name of the policy whose associated IP address range(s) are to be deleted

</dd> <dt>

*ScopeId* \[in\]
</dt> <dd>

Scope identifier (in IPv4 address format) which contains the specified policy

</dd> <dt>

*StartRange* \[in\]
</dt> <dd>

Start IP address of the IP address range which is to be deleted from the policy

</dd> <dt>

*EndRange* \[in\]
</dt> <dd>

End IP address of the IP address range which is to be deleted from the policy

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

If this parameter is specified, the cmdlet returns the PowerShell object which is added.

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
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DhcpServerv4PolicyIPRange**](ps-dhcpserverv4policyiprange.md)
</dt> </dl>

 

 





