---
title: RemoveByIPAddress method of the PS\_DhcpServerv6Reservation class
description: Deletes the IPv6 reservation(s) from the specified scope.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: c011e161-9c48-44e7-9fd4-dd65ede9c534
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- RemoveByIPAddress method
- RemoveByIPAddress method, PS_DhcpServerv6Reservation class
- PS_DhcpServerv6Reservation class, RemoveByIPAddress method
topic_type:
- apiref
api_name:
- PS_DhcpServerv6Reservation.RemoveByIPAddress
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# RemoveByIPAddress method of the PS\_DhcpServerv6Reservation class

Deletes the IPv6 reservation(s) from the specified scope.

## Syntax


```mof
uint32 RemoveByIPAddress(
  [in]  string                  ComputerName,
  [in]  string                  IPAddress[],
  [in]  boolean                 PassThru,
  [out] DhcpServerv6Reservation cmdletOutput[]
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

IPv6 address(es) of the reservation(s) which are to be deleted.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

If this parameter is specified, the cmdlet return the PowerShell objects which are deleted.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of the [**DhcpServerv6Reservation**](dhcpserverv6reservation.md) class.

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

[**PS\_DhcpServerv6Reservation**](ps-dhcpserverv6reservation.md)
</dt> </dl>

 

 





