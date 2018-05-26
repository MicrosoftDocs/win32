---
title: Rename method of the PS\_DhcpServerv4Superscope class
description: Renames the superscope with the specified name.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 174D7451-AB3F-44BE-94DD-B5C95E141826
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Rename method
- Rename method, PS_DhcpServerv4Superscope class
- PS_DhcpServerv4Superscope class, Rename method
topic_type:
- apiref
api_name:
- PS_DhcpServerv4Superscope.Rename
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Rename method of the PS\_DhcpServerv4Superscope class

Renames the superscope with the specified name.

## Syntax


```mof
uint32 Rename(
  [in]  string                 ComputerName,
  [in]  string                 Name,
  [in]  string                 NewName,
  [in]  boolean                PassThru,
  [out] DhcpServerv4Superscope cmdletOutput
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

Current Name of the superscope.

</dd> <dt>

*NewName* \[in\]
</dt> <dd>

New name of the superscope.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

If this parameter is specified, the cmdlet returns the PowerShell object which is added.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of a [**DhcpServerv4Superscope**](ps-dhcpserverv4superscope.md) object.

</dd> </dl>

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                   |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DhcpServerv4Superscope**](ps-dhcpserverv4superscope.md)
</dt> </dl>

 

 





