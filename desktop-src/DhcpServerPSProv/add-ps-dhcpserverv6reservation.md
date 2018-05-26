---
title: Add method of the PS\_DhcpServerv6Reservation class
description: Add an IPv6 Reservation to an IPv6 Prefix/Scope.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: ab862019-8cef-4135-9a63-d98998eb16c3
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Add method
- Add method, PS_DhcpServerv6Reservation class
- PS_DhcpServerv6Reservation class, Add method
topic_type:
- apiref
api_name:
- PS_DhcpServerv6Reservation.Add
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Add method of the PS\_DhcpServerv6Reservation class

Add an IPv6 Reservation to an IPv6 Prefix/Scope.

## Syntax


```mof
uint32 Add(
  [in]  string                  ComputerName,
  [in]  string                  IPAddress,
  [in]  string                  ClientDuid,
  [in]  uint32                  Iaid,
  [in]  string                  Name,
  [in]  string                  Description,
  [in]  string                  Prefix,
  [in]  boolean                 PassThru,
  [out] DhcpServerv6Reservation cmdletOutput
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

The IPv6 address to be reserved for the client.

</dd> <dt>

*ClientDuid* \[in\]
</dt> <dd>

The DHCPv6 unique identifier of the client.

</dd> <dt>

*Iaid* \[in\]
</dt> <dd>

DHCPv6 unique identifiers of a specific network interface of the client.

</dd> <dt>

*Name* \[in\]
</dt> <dd>

Name of the client. This could be the actual hostname of the client or a name assigned to identify the reserved client on the DHCP server.

</dd> <dt>

*Description* \[in\]
</dt> <dd>

The description string for the IPv6 reservation being created.

</dd> <dt>

*Prefix* \[in\]
</dt> <dd>

The IPv6 prefix which identifies the scope in which the reservation will be created.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

If this parameter is specified, the cmdlet returns the PowerShell object which is added.

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

 

 





