---
title: GetByPrefix method of the PS\_DhcpServerv6Reservation class
description: Returns the reserved IPv6 addresses on the server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'f85cfddf-1b2d-4cc3-a083-24173b3f3981'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dhcp-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["GetByPrefix method", "GetByPrefix method, PS_DhcpServerv6Reservation class", "PS_DhcpServerv6Reservation class, GetByPrefix method"]
topic_type:
- apiref
api_name:
- PS_DhcpServerv6Reservation.GetByPrefix
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
---

# GetByPrefix method of the PS\_DhcpServerv6Reservation class

Returns the reserved IPv6 addresses on the server.

## Syntax


```mof
uint32 GetByPrefix(
  [in]  string                  Prefix,
  [in]  string                  ComputerName,
  [out] DhcpServerv6Reservation cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*Prefix* \[in\]
</dt> <dd>

IPv6 prefix of the DHCP server from which the reservations are requested.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

DNS name or IP address of the target computer running the DHCP server service.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of the [**DhcpServerv6Reservation**](dhcpserverv6reservation.md) class.

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

[**PS\_DhcpServerv6Reservation**](ps-dhcpserverv6reservation.md)
</dt> </dl>

 

 





