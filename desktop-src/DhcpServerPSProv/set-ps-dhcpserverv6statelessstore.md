---
title: Set method of the PS\_DhcpServerv6StatelessStore class
description: Sets the properties of IPv6 stateless store for the specified IPv6 prefix.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: fc6ba3e3-2468-488c-8182-599c1fd1f83c
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Set method
- Set method, PS_DhcpServerv6StatelessStore class
- PS_DhcpServerv6StatelessStore class, Set method
topic_type:
- apiref
api_name:
- PS_DhcpServerv6StatelessStore.Set
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Set method of the PS\_DhcpServerv6StatelessStore class

Sets the properties of IPv6 stateless store for the specified IPv6 prefix.

## Syntax


```mof
uint32 Set(
  [in]  string                     Prefix,
  [in]  boolean                    Enabled,
  [in]  datetime                   PurgeInterval,
  [in]  string                     ComputerName,
  [in]  boolean                    PassThru,
  [out] DhcpServerv6StatelessStore cmdletOutput
);
```



## Parameters

<dl> <dt>

*Prefix* \[in\]
</dt> <dd>

IPv6 subnet prefix of the scope whose stateless store properties are to be set

</dd> <dt>

*Enabled* \[in\]
</dt> <dd>

Enable or Disable the stateless store. Valid values are True, False.

</dd> <dt>

*PurgeInterval* \[in\]
</dt> <dd>

Purge interval for the stateless store. If a client does not send a DHCPv6 Information Request, request for options, in this interval, the client is assumed to be no longer present on that subnet and the stateless store entry for the client is purged by the server. This value can be configured in dd.hh format. If minutes or seconds are specified, by using the dd.hh:mm:ss format, they will be ignored.

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

An embedded instance of the [**DhcpServerv6StatelessStore**](dhcpserverv6statelessstore.md) class.

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

[**PS\_DhcpServerv6StatelessStore**](ps-dhcpserverv6statelessstore.md)
</dt> </dl>

 

 





