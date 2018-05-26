---
title: GetByScopeId method of the PS\_DhcpServerv4Reservation class
description: Gets the IPv4 reservation(s) for the specified IP addresses or client identifiers. If only a scope identifier is specified, all IPv4 reservations from the specified scope are returned.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 5a86a118-37c9-496d-bc8c-c83abc0a802a
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetByScopeId method
- GetByScopeId method, PS_DhcpServerv4Reservation class
- PS_DhcpServerv4Reservation class, GetByScopeId method
topic_type:
- apiref
api_name:
- PS_DhcpServerv4Reservation.GetByScopeId
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# GetByScopeId method of the PS\_DhcpServerv4Reservation class

Gets the IPv4 reservation(s) for the specified IP addresses or client identifiers. If only a scope identifier is specified, all IPv4 reservations from the specified scope are returned.

## Syntax


```mof
uint32 GetByScopeId(
  [in]  string                  ScopeId,
  [in]  string                  ComputerName,
  [out] DhcpServerv4Reservation cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*ScopeId* \[in\]
</dt> <dd>

The scope identifier (in IPv4 address format) from which the reservations are to be retrieved.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

DNS name or IP address of the target computer running the DHCP server service.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of the [**DhcpServerv4Reservation**](dhcpserverv4reservation.md) class.

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

[**PS\_DhcpServerv4Reservation**](ps-dhcpserverv4reservation.md)
</dt> </dl>

 

 





