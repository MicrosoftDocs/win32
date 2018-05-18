---
title: Add method of the PS\_DhcpServerv4Reservation class
description: Reserves the specified IPv4 address in the scope for a client.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'd0a35827-80c1-46e4-8f72-365197ff3577'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dhcp-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Add method", "Add method, PS_DhcpServerv4Reservation class", "PS_DhcpServerv4Reservation class, Add method"]
topic_type:
- apiref
api_name:
- PS_DhcpServerv4Reservation.Add
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
---

# Add method of the PS\_DhcpServerv4Reservation class

Reserves the specified IPv4 address in the scope for a client.

## Syntax


```mof
uint32 Add(
  [in]  string                  ComputerName,
  [in]  string                  ScopeId,
  [in]  string                  IPAddress,
  [in]  string                  ClientId,
  [in]  string                  Name,
  [in]  string                  Description,
  [in]  string                  Type,
  [in]  boolean                 PassThru,
  [out] DhcpServerv4Reservation cmdletOutput
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

DNS name or IP address of the target computer running the DHCP server service.

</dd> <dt>

*ScopeId* \[in\]
</dt> <dd>

The identifier of the scope in which the reservation is being created.

</dd> <dt>

*IPAddress* \[in\]
</dt> <dd>

The IPv4 address to be reserved for the client.

</dd> <dt>

*ClientId* \[in\]
</dt> <dd>

The unique identifier for the client. For windows clients, MAC address should be specified.

</dd> <dt>

*Name* \[in\]
</dt> <dd>

Name of the reservation being created. This could be the hostname of the client or a name to be used to identify the reservation on the DHCP server.

</dd> <dt>

*Description* \[in\]
</dt> <dd>

The description for the reservation being created.

</dd> <dt>

*Type* \[in\]
</dt> <dd>

The type of client request for which this IP address is reserved. Valid values are {Dhcp, Bootp, Both}. Default value is Dhcp.

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
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DhcpServerv4Reservation**](ps-dhcpserverv4reservation.md)
</dt> </dl>

 

 





