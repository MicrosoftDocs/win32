---
title: GetByIPAddress method of the PS\_DhcpServerv4Reservation class
description: Gets the IPv4 reservation(s) for the specified IP addresses or client identifiers. If only a scope identifier is specified, all IPv4 reservations from the specified scope are returned.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '5bce20f6-51b7-4d76-bed4-e678a8a9e0ee'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dhcp-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["GetByIPAddress method", "GetByIPAddress method, PS_DhcpServerv4Reservation class", "PS_DhcpServerv4Reservation class, GetByIPAddress method"]
topic_type:
- apiref
api_name:
- PS_DhcpServerv4Reservation.GetByIPAddress
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
---

# GetByIPAddress method of the PS\_DhcpServerv4Reservation class

Gets the IPv4 reservation(s) for the specified IP addresses or client identifiers. If only a scope identifier is specified, all IPv4 reservations from the specified scope are returned.

## Syntax


```mof
uint32 GetByIPAddress(
  [in]  string                  IPAddress[],
  [in]  string                  ComputerName,
  [out] DhcpServerv4Reservation cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*IPAddress* \[in\]
</dt> <dd>

The IPv4 address(es) of the reservations which are to be retrieved.

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
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DhcpServerv4Reservation**](ps-dhcpserverv4reservation.md)
</dt> </dl>

 

 





