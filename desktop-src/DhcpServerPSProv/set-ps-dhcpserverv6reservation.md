---
title: Set method of the PS\_DhcpServerv6Reservation class
description: Modifies the properties of the specified IPv6 Reservation.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '6bd0414a-516c-4d3c-aa24-96fa90813a55'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dhcp-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Set method", "Set method, PS_DhcpServerv6Reservation class", "PS_DhcpServerv6Reservation class, Set method"]
topic_type:
- apiref
api_name:
- PS_DhcpServerv6Reservation.Set
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
---

# Set method of the PS\_DhcpServerv6Reservation class

Modifies the properties of the specified IPv6 Reservation.

## Syntax


```mof
uint32 Set(
  [in]  string                  ComputerName,
  [in]  string                  IPAddress,
  [in]  string                  ClientDuid,
  [in]  uint32                  Iaid,
  [in]  string                  Name,
  [in]  string                  Description,
  [in]  boolean                 PassThru,
  [out] DhcpServerv6Reservation cmdletOutput
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

IPv6 address of the reservation being modified.

</dd> <dt>

*ClientDuid* \[in\]
</dt> <dd>

DHCPv6 unique identifier of the client.

</dd> <dt>

*Iaid* \[in\]
</dt> <dd>

DHCPv6 IAID (interface identifier).

</dd> <dt>

*Name* \[in\]
</dt> <dd>

Name to be set for the reservation.

</dd> <dt>

*Description* \[in\]
</dt> <dd>

Description string to be set for the reservation.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

If this parameter is specified, the cmdlet returns the PowerShell object which is modified.

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

 

 





