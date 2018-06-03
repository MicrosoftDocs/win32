---
title: GetByClientId method of the PS\_DhcpServerv4Reservation class
description: Gets the IPv4 reservation(s) for the specified IP addresses or client identifiers. If only a scope identifier is specified, all IPv4 reservations from the specified scope are returned.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: df0bc4ea-6625-4240-a27d-efb9d566a628
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetByClientId method
- GetByClientId method, PS_DhcpServerv4Reservation class
- PS_DhcpServerv4Reservation class, GetByClientId method
topic_type:
- apiref
api_name:
- PS_DhcpServerv4Reservation.GetByClientId
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GetByClientId method of the PS\_DhcpServerv4Reservation class

Gets the IPv4 reservation(s) for the specified IP addresses or client identifiers. If only a scope identifier is specified, all IPv4 reservations from the specified scope are returned.

## Syntax


```mof
uint32 GetByClientId(
  [in]  string                  ComputerName,
  [in]  string                  ClientId[],
  [in]  string                  ScopeId,
  [out] DhcpServerv4Reservation cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

DNS name or IP address of the target computer running the DHCP server service.

</dd> <dt>

*ClientId* \[in\]
</dt> <dd>

The client identifier(s) of the reservations which need to be retrieved. For Windows clients, the MAC address is the client identifier.

</dd> <dt>

*ScopeId* \[in\]
</dt> <dd>

The scope identifier (in IPv4 address format) from which the reservations are to be retrieved.

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

 

 





