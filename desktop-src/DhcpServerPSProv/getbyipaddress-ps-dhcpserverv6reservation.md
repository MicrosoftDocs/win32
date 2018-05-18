---
title: GetByIPAddress method of the PS\_DhcpServerv6Reservation class
description: Returns the reserved IPv6 addresses on the server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '466abae9-85f7-4564-beb6-35bcbf2c5d7c'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dhcp-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["GetByIPAddress method", "GetByIPAddress method, PS_DhcpServerv6Reservation class", "PS_DhcpServerv6Reservation class, GetByIPAddress method"]
topic_type:
- apiref
api_name:
- PS_DhcpServerv6Reservation.GetByIPAddress
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
---

# GetByIPAddress method of the PS\_DhcpServerv6Reservation class

Returns the reserved IPv6 addresses on the server.

## Syntax


```mof
uint32 GetByIPAddress(
  [in]  string                  ComputerName,
  [in]  string                  IPAddress[],
  [out] DhcpServerv6Reservation cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

DNS name or IP address of the target computer running the DHCP server service.

</dd> <dt>

*IPAddress* \[in\]
</dt> <dd>

The IPv6 addresses for which the reservation information is requested.

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

 

 





