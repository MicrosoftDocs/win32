---
title: Remove method of the PS\_DhcpServerv4Superscope class
description: Removes the specified scope(s) from a superscope. Superscope is deleted if there are no scopes left in the superscope.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 023279fb-3b5a-4f10-99f2-04f65a43461c
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Remove method
- Remove method, PS_DhcpServerv4Superscope class
- PS_DhcpServerv4Superscope class, Remove method
topic_type:
- apiref
api_name:
- PS_DhcpServerv4Superscope.Remove
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Remove method of the PS\_DhcpServerv4Superscope class

Removes the specified scope(s) from a superscope. Superscope is deleted if there are no scopes left in the superscope.

## Syntax


```mof
uint32 Remove(
  [in]  string                 ComputerName,
  [in]  string                 SuperscopeName,
  [in]  string                 ScopeId[],
  [in]  boolean                Passthru,
  [out] DhcpServerv4Superscope cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

DNS name or IP address of the target computer running the DHCP server service.

</dd> <dt>

*SuperscopeName* \[in\]
</dt> <dd>

Name of the superscope from which the scopes are to be removed.

</dd> <dt>

*ScopeId* \[in\]
</dt> <dd>

Scope identifier(s) (in IPv4 address format) which need to be removed from a superscope.

</dd> <dt>

*Passthru* \[in\]
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
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DhcpServerv4Superscope**](ps-dhcpserverv4superscope.md)
</dt> </dl>

 

 





