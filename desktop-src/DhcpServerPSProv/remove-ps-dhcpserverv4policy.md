---
title: Remove method of the PS\_DhcpServerv4Policy class
description: Deletes the specified IPv4 policy(ies) either at the server level or the specified scope level.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: d072490e-878a-446a-8e22-ecc4722f6fdd
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Remove method
- Remove method, PS_DhcpServerv4Policy class
- PS_DhcpServerv4Policy class, Remove method
topic_type:
- apiref
api_name:
- PS_DhcpServerv4Policy.Remove
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Remove method of the PS\_DhcpServerv4Policy class

Deletes the specified IPv4 policy(ies) either at the server level or the specified scope level.

## Syntax


```mof
uint32 Remove(
  [in]  string             ComputerName,
  [in]  boolean            PassThru,
  [in]  string             Name[],
  [in]  string             ScopeId,
  [out] DhcpServerv4Policy cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

DNS name or IP address of the target computer running the DHCP server service.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

If this parameter is specified, the cmdlet returns the PowerShell object which is modified.

</dd> <dt>

*Name* \[in\]
</dt> <dd>

Name(s) of the policies to be deleted.

</dd> <dt>

*ScopeId* \[in\]
</dt> <dd>

Scope Identifier (in IPv4 address format) from which the policies are to be deleted.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of the [**DhcpServerv4Policy**](dhcpserverv4policy.md) class.

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

[**PS\_DhcpServerv4Policy**](ps-dhcpserverv4policy.md)
</dt> </dl>

 

 





