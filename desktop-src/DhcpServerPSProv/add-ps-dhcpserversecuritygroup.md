---
title: Add method of the PS\_DhcpServerSecurityGroup class
description: Adds a specified security group.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 5305df5d-1d52-4169-9163-72dff0fb4175
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Add method
- Add method, PS_DhcpServerSecurityGroup class
- PS_DhcpServerSecurityGroup class, Add method
topic_type:
- apiref
api_name:
- PS_DhcpServerSecurityGroup.Add
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Add method of the PS\_DhcpServerSecurityGroup class

Adds a specified security group.

## Syntax


```mof
uint32 Add(
  [in] string ComputerName
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

DNS name or IP address of the target computer running the DHCP server service.

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

[**PS\_DhcpServerSecurityGroup**](ps-dhcpserversecuritygroup.md)
</dt> </dl>

 

 





