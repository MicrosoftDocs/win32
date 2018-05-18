---
title: Add method of the PS\_DhcpServerv4Superscope class
description: Adds the specified scopes to a superscope.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'bcd0ddb7-16ed-4255-ae82-1c94fc39f492'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dhcp-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Add method", "Add method, PS_DhcpServerv4Superscope class", "PS_DhcpServerv4Superscope class, Add method"]
topic_type:
- apiref
api_name:
- PS_DhcpServerv4Superscope.Add
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
---

# Add method of the PS\_DhcpServerv4Superscope class

Adds the specified scopes to a superscope.

## Syntax


```mof
uint32 Add(
  [in]  string                 SuperscopeName,
  [in]  string                 ScopeId[],
  [in]  boolean                Force,
  [in]  string                 ComputerName,
  [in]  boolean                PassThru,
  [out] DhcpServerv4Superscope cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*SuperscopeName* \[in\]
</dt> <dd>

The name of the superscope to which the scopes will be added.

</dd> <dt>

*ScopeId* \[in\]
</dt> <dd>

The identifiers of the scopes which are to be made part of a superscope. The specified scope should already exist.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

If Force is specified and if a specified scope is already part of a different superscope, the specified scope will be removed from this superscope and added to the specified superscope.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

DNS name or IP address of the target computer running the DHCP server service.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

If this parameter is specified, the cmdlet return the PowerShell objects which are deleted.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of the [**DhcpServerv4Superscope**](dhcpserverv4superscope.md) class.

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

[**PS\_DhcpServerv4Superscope**](ps-dhcpserverv4superscope.md)
</dt> </dl>

 

 





