---
title: Set method of the PS\_DhcpServerv4Reservation class
description: Modifies/sets the properties of an IPv4 reservation.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 7c0f8787-2cf5-4cdf-8c90-fb27fc9dffb4
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Set method
- Set method, PS_DhcpServerv4Reservation class
- PS_DhcpServerv4Reservation class, Set method
topic_type:
- apiref
api_name:
- PS_DhcpServerv4Reservation.Set
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Set method of the PS\_DhcpServerv4Reservation class

Modifies/sets the properties of an IPv4 reservation.

## Syntax


```mof
uint32 Set(
  [in]  string                  ComputerName,
  [in]  string                  IPAddress,
  [in]  string                  ClientId,
  [in]  string                  Name,
  [in]  string                  Description,
  [in]  string                  Type,
  [in]  boolean                 PassThru,
  [out] DhcpServerv4Reservation cmdletOutput
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

IPv4 address of the reservation whose properties are to be modified or set

</dd> <dt>

*ClientId* \[in\]
</dt> <dd>

Value of client identifier to be set on the reservation. For Windows clients, MAC address is used as a client identifier.

</dd> <dt>

*Name* \[in\]
</dt> <dd>

Name to be set for the reservation

</dd> <dt>

*Description* \[in\]
</dt> <dd>

Description string to be set for the reservation

</dd> <dt>

*Type* \[in\]
</dt> <dd>

Type of client which can be leased the reserved IPv4 address. Valid values are Dhcp, Bootp or Both.

<dt>

<span id="Dhcp"></span><span id="dhcp"></span><span id="DHCP"></span>

**Dhcp** ("Dhcp")


</dt> <dd></dd> <dt>

<span id="Bootp"></span><span id="bootp"></span><span id="BOOTP"></span>

**Bootp** ("Bootp")


</dt> <dd></dd> <dt>

<span id="Both"></span><span id="both"></span><span id="BOTH"></span>

**Both** ("Both")


</dt> <dd></dd> </dl> </dd> <dt>

*PassThru* \[in\]
</dt> <dd>

If this parameter is specified, the cmdlet returns the PowerShell object which is modified.

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

 

 





