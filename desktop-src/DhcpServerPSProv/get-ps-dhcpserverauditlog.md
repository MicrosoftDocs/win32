---
title: Get method of the PS\_DhcpServerAuditLog class
description: Gets the configuration parameters related to the audit log of the DHCP server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: e7cd83c9-2d8c-4f2a-9c3c-8e899f026f5d
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Get method
- Get method, PS_DhcpServerAuditLog class
- PS_DhcpServerAuditLog class, Get method
topic_type:
- apiref
api_name:
- PS_DhcpServerAuditLog.Get
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Get method of the PS\_DhcpServerAuditLog class

Gets the configuration parameters related to the audit log of the DHCP server.

## Syntax


```mof
uint32 Get(
  [in]  string             ComputerName,
  [out] DhcpServerAuditLog cmdletOutput
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

DNS name or IP address of the target computer running the DHCP server service.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of the [**DhcpServerAuditLog**](dhcpserverauditlog.md) class.

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

[**PS\_DhcpServerAuditLog**](ps-dhcpserverauditlog.md)
</dt> </dl>

 

 





