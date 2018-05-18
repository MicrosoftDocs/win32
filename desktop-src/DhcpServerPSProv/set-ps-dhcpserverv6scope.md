---
title: Set method of the PS\_DhcpServerv6Scope class
description: Modifies the properties of a IPv6 scope on the server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'b4ba80c4-33f9-42ea-9316-2c4360f290ce'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dhcp-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Set method", "Set method, PS_DhcpServerv6Scope class", "PS_DhcpServerv6Scope class, Set method"]
topic_type:
- apiref
api_name:
- PS_DhcpServerv6Scope.Set
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
---

# Set method of the PS\_DhcpServerv6Scope class

Modifies the properties of a IPv6 scope on the server

## Syntax


```mof
uint32 Set(
  [in]  string            Prefix,
  [in]  string            Name,
  [in]  string            Description,
  [in]  string            State,
  [in]  uint16            Preference,
  [in]  datetime          PreferredLifeTime,
  [in]  datetime          ValidLifeTime,
  [in]  datetime          T1,
  [in]  datetime          T2,
  [in]  string            ComputerName,
  [in]  boolean           PassThru,
  [out] DhcpServerv6Scope cmdletOutput
);
```



## Parameters

<dl> <dt>

*Prefix* \[in\]
</dt> <dd>

IPv6 subnet prefix of the scope whose properties are to be modified

</dd> <dt>

*Name* \[in\]
</dt> <dd>

New name to be set for the scope

</dd> <dt>

*Description* \[in\]
</dt> <dd>

Description string set on the scope

</dd> <dt>

*State* \[in\]
</dt> <dd>

State of the scope (Active or Inactive)

<dt>

<span id="Active"></span><span id="active"></span><span id="ACTIVE"></span>

**Active** ("Active")


</dt> <dd></dd> <dt>

<span id="InActive"></span><span id="inactive"></span><span id="INACTIVE"></span>

**InActive** ("InActive")


</dt> <dd></dd> </dl> </dd> <dt>

*Preference* \[in\]
</dt> <dd>

Preference value of the server. The server with the lowest preference value is selected by the DHCP client in case the client gets responses from more than one DHCP server

</dd> <dt>

*PreferredLifeTime* \[in\]
</dt> <dd>

The preferred life time of the IPv6 addresses leased from the scope

</dd> <dt>

*ValidLifeTime* \[in\]
</dt> <dd>

The valid life time of the IPv6 addresses leased from the scope

</dd> <dt>

*T1* \[in\]
</dt> <dd>

T1 time for the IPv6 addresses lease by the scope. The client is expected to use a unicast message to renew the lease at time T1 from the same DHCP server from which it had initially obtained the lease.

</dd> <dt>

*T2* \[in\]
</dt> <dd>

T2 time for the IPv6 addresses lease by the scope. The client is expected to use a multi cast message to renew the lease at time T2 from any DHCP server.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

DNS name or IP address of the target computer running the DHCP server service.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

If this parameter is specified, the cmdlet returns the PowerShell object which is modified.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of the [**DhcpServerv6Scope**](dhcpserverv6scope.md) class.

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

[**PS\_DhcpServerv6Scope**](ps-dhcpserverv6scope.md)
</dt> </dl>

 

 





